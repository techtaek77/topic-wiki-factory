#!/usr/bin/env python3
"""Deterministic acceptance harness for the documented orchestrator behavior."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS_PATH = ROOT / "tests" / "orchestrator_scenarios.json"
CLAUDE_AGENT_PATH = ROOT / ".claude" / "agents" / "wiki-orchestrator.md"
PROMPT_PATH = ROOT / "prompts" / "wiki-orchestrator.md"


REQUIRED_SNIPPETS = {
    CLAUDE_AGENT_PATH: [
        'hitl.confirm_scope_after_research = false 이면 scope_confirmed = true, phase = "planning"',
        'hitl.confirm_ia_before_writing = false 이면 ia_confirmed = true, phase = "writing"',
        'docs_to_revise 먼저 처리',
        'docs_blocked 항목은 작성 대상에서 제외',
        '병렬 writer 실행은 현재 기본 전제가 아니다.',
    ],
    PROMPT_PATH: [
        'false면 자동으로 `scope_confirmed=true`, phase를 `"planning"`으로',
        '`hitl.confirm_ia_before_writing=false` 이면 사용자 확인 없이 `ia_confirmed=true`, `phase="writing"`으로',
        '`docs_to_revise`에 있는 문서를 최우선',
        '`docs_blocked`에 추가',
        '기본 모델은 "문서 1개씩 선택하는 순차 자동 진행"이다.',
    ],
}


def load_json(path: Path):
    return json.loads(path.read_text())


def normalize_doc_list(items, docs_planned):
    if not items:
        return []
    by_slug = {doc["slug"]: deepcopy(doc) for doc in docs_planned}
    normalized = []
    for item in items:
        if isinstance(item, str):
            normalized.append(deepcopy(by_slug[item]))
        else:
            normalized.append(deepcopy(item))
    return normalized


def doc_slugs(items):
    return [item["slug"] if isinstance(item, dict) else item for item in items]


def first_unfinished_doc(state):
    done = set(doc_slugs(state["docs_done"]))
    blocked = set(doc_slugs(state["docs_blocked"]))
    for doc in state["docs_planned"]:
        if doc["slug"] not in done and doc["slug"] not in blocked:
            return deepcopy(doc)
    return None


def doc_is_dependency_ready(doc, done_slugs):
    dependencies = doc.get("depends_on", [])
    return all(slug in done_slugs for slug in dependencies)


def choose_priority_doc(state):
    done = set(doc_slugs(state["docs_done"]))
    blocked = set(doc_slugs(state["docs_blocked"]))
    eligible = []

    for index, doc in enumerate(state["docs_planned"]):
        slug = doc["slug"]
        if slug in done or slug in blocked:
            continue
        if not doc_is_dependency_ready(doc, done):
            continue
        priority = doc.get("priority", 50)
        eligible.append((-priority, index, doc))

    if eligible:
        eligible.sort(key=lambda item: (item[0], item[1]))
        return deepcopy(eligible[0][2])

    return first_unfinished_doc(state)


def choose_next_action_for_writing(state):
    next_doc = state["docs_to_revise"][0] if state["docs_to_revise"] else choose_priority_doc(state)
    if next_doc is None:
        state["phase"] = "reviewing"
        state["current_doc"] = None
        return "wiki-reviewer"
    state["phase"] = "writing"
    state["current_doc"] = next_doc
    return f'wiki-writer:{next_doc["slug"]}'


def promote_blocked_docs(state, max_revision_attempts):
    remaining = []
    for doc in state["docs_to_revise"]:
        slug = doc["slug"]
        attempts = state["revision_attempts"].get(slug, 0)
        if attempts >= max_revision_attempts:
            state["docs_blocked"].append(deepcopy(doc))
        else:
            remaining.append(doc)
    state["docs_to_revise"] = remaining


def handle_planning(state, hitl):
    state["phase"] = "planning"
    if not state["docs_planned"]:
        state["current_doc"] = None
        return "plan-docs"
    if state["ia_confirmed"]:
        return choose_next_action_for_writing(state)
    if hitl.get("confirm_ia_before_writing", True):
        state["current_doc"] = None
        return "request-ia-confirmation"
    state["ia_confirmed"] = True
    return choose_next_action_for_writing(state)


def handle_scoping(state, hitl):
    state["phase"] = "scoping"
    if state["scope_confirmed"]:
        return handle_planning(state, hitl)
    if hitl.get("confirm_scope_after_research", True):
        state["current_doc"] = None
        return "request-scope-confirmation"
    state["scope_confirmed"] = True
    return handle_planning(state, hitl)


def evaluate(config, state, context):
    state = deepcopy(state)
    planned_docs = normalize_doc_list(state.get("docs_planned"), state.get("docs_planned", []))
    state["docs_planned"] = planned_docs
    state["docs_written"] = normalize_doc_list(state.get("docs_written"), planned_docs)
    state["docs_to_revise"] = normalize_doc_list(state.get("docs_to_revise"), planned_docs)
    state["docs_blocked"] = normalize_doc_list(state.get("docs_blocked"), planned_docs)
    state["docs_done"] = normalize_doc_list(state.get("docs_done"), planned_docs)
    state["current_doc"] = deepcopy(state.get("current_doc"))

    hitl = config.get("hitl", {})
    publish = config.get("publish", {})
    max_revision_attempts = config.get("max_revision_attempts", 3)
    sources_exists = context.get("sources_exists", False)
    publish_preflight_ready = context.get("publish_preflight_ready", False)
    publish_succeeded = context.get("publish_succeeded", False)

    promote_blocked_docs(state, max_revision_attempts)

    phase = state["phase"]
    action = None

    if phase == "init":
        if sources_exists:
            action = handle_scoping(state, hitl)
        else:
            state["phase"] = "researching"
            action = "wiki-researcher"

    elif phase == "researching":
        if sources_exists:
            action = handle_scoping(state, hitl)
        else:
            action = "wiki-researcher"

    elif phase == "scoping":
        action = handle_scoping(state, hitl)

    elif phase == "planning":
        action = handle_planning(state, hitl)

    elif phase == "writing":
        action = choose_next_action_for_writing(state)

    elif phase == "reviewing":
        if state["docs_to_revise"]:
            state["phase"] = "writing"
            next_doc = state["docs_to_revise"][0]
            state["current_doc"] = next_doc
            action = f'wiki-writer:{next_doc["slug"]}'
        elif publish.get("enabled", False):
            state["phase"] = "publishing"
            state["current_doc"] = None
            action = "wiki-publish-preflight"
        else:
            state["phase"] = "done"
            state["current_doc"] = None
            action = "complete"

    elif phase == "publishing":
        if publish_succeeded:
            state["phase"] = "done"
            state["current_doc"] = None
            action = "complete"
        elif publish_preflight_ready:
            action = "wiki-publisher"
        else:
            action = "wiki-publish-preflight"

    elif phase == "done":
        action = "complete"

    else:
        raise ValueError(f"Unsupported phase: {phase}")

    return {
        "phase": state["phase"],
        "action": action,
        "scope_confirmed": state["scope_confirmed"],
        "ia_confirmed": state["ia_confirmed"],
        "current_doc": None if state["current_doc"] is None else state["current_doc"]["slug"],
        "blocked_docs": doc_slugs(state["docs_blocked"]),
    }


def check_required_snippets():
    failures = []
    for path, snippets in REQUIRED_SNIPPETS.items():
        content = path.read_text()
        label = path.relative_to(ROOT).as_posix()
        for snippet in snippets:
            if snippet not in content:
                failures.append(f"{label}: missing snippet -> {snippet}")
    return failures


def main() -> int:
    scenarios = load_json(SCENARIOS_PATH)
    failures = []

    failures.extend(check_required_snippets())

    for scenario in scenarios:
        actual = evaluate(scenario["config"], scenario["state"], scenario["context"])
        expected = scenario["expected"]
        for key, expected_value in expected.items():
            actual_value = actual.get(key)
            if actual_value != expected_value:
                failures.append(
                    f'{scenario["name"]}: expected {key}={expected_value!r}, got {actual_value!r}'
                )

    if failures:
        print("orchestrator harness FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"orchestrator harness OK ({len(scenarios)} scenarios)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
