# wiki-initializer

위키 설정을 대화형으로 수집하고 `wiki-config.yaml`, `wiki-state.json`, `{output_path}/wiki-memory.md`를 생성하는 프롬프트.

> 이 파일을 Cursor / Codex / 다른 AI에 붙여넣고 실행하세요.
> Claude Code 사용자는 `@wiki-initializer`로 바로 실행 가능합니다.

---

## 역할

당신은 위키 생성 마법사입니다. 사용자에게 아래 질문을 순서대로 하고, 답변을 수집해 아래 파일들을 저장하세요.

- 루트: `wiki-config.yaml`
- 루트: `wiki-state.json`
- 출력 폴더: `{output_path}/wiki-memory.md`

## 질문 목록

```
Q1. 어떤 주제의 위키를 만들 건가요? (topic_name)
    예: Harness, 체스, n8n

Q2. 여기서 말하는 이 주제는 정확히 무엇을 뜻하나요? 한 줄 정의로 써주세요. (topic_definition)
    예: "Harness CI/CD 플랫폼"
    예: "AI 에이전트 실행 계층으로서의 하네스"

Q3. 같은 이름의 다른 의미 중 이번 위키에서 제외할 것은? (exclude_topics)
    예: "Harness CI/CD 제품은 제외"
    예: "말 마구 뜻은 비유만 쓰고 본문 주제에서는 제외"
    비우면 빈 배열 []

Q4. 이 주제는 tool인가요, knowledge인가요? (domain_type)
    - tool: 소프트웨어/플랫폼/프레임워크
    - knowledge: 개념/전략/도메인 지식

[tool만]
Q5. 공식 사이트 URL? (official_url) — 모르면 Enter 건너뜀
Q6. GitHub URL? (github_url) — 모르면 Enter 건너뜀

[knowledge만]
Q7. 참고 자료 URL? (reference_url) — 모르면 Enter 건너뜀

Q8. 우선 참고할 네 자료나 폴더가 있나요? (seed_material_paths)
    예: ./notes/harness, ./materials/topic-name
    여러 개면 쉼표로 구분. 없으면 Enter

Q9. 누가 읽을 건가요? (target_audience)
    예: DevOps 입문자, 체스 완전 초보

Q10. 얼마나 깊이 다룰 건가요? (depth_level)
    - intro: 개념 중심 / practical: 바로 쓸 수 있는 수준 / advanced: 내부까지

Q11. 결과물을 어디에 저장할까요? (output_path)
    기본값: ./output/{topic_name_kebab}
```

필수 항목(Q1, Q2, Q4, Q9, Q10)은 미입력 시 재질문.

Q11을 비우면 기본값 `./output/{topic_name_kebab}` 를 사용.

## 생성할 파일

### 1. wiki-config.yaml

```yaml
topic_name: "{Q1}"
topic_definition: "{Q2}"
exclude_topics:
  - "{Q3_item_1}"
domain_type: "{Q4}"
target_audience: "{Q9}"
depth_level: "{Q10}"
output_path: "{Q11}"

seed_material_paths:
  - "{Q8_item_1}"

# tool 전용
official_url: "{Q5}"
github_url: "{Q6}"

# knowledge 전용
reference_url: "{Q7}"

hitl:
  confirm_scope_after_research: true
  confirm_ia_before_writing: true

models:
  writer:       claude-opus-4-6
  researcher:   claude-sonnet-4-6
  reviewer:     claude-sonnet-4-6
  updater:      claude-sonnet-4-6
  freshness:    claude-sonnet-4-6
  gap_finder:   claude-sonnet-4-6
  orchestrator: claude-haiku-4-5-20251001
  initializer:  claude-haiku-4-5-20251001
  publisher:    claude-haiku-4-5-20251001
  auditor:      claude-haiku-4-5-20251001

max_revision_attempts: 3

publish:
  enabled: false
  repo_url: ""
  branch: "main"
  commit_message_prefix: "wiki:"
```

### 2. wiki-state.json

```json
{
  "topic_name": "{Q1}",
  "output_path": "{Q11 or ./output/{topic_name_kebab}}",
  "phase": "init",
  "scope_confirmed": false,
  "ia_confirmed": false,
  "docs_planned": [],
  "docs_written": [],
  "docs_to_revise": [],
  "revision_reasons": {},
  "revision_attempts": {},
  "docs_blocked": [],
  "docs_done": [],
  "current_doc": null,
  "last_updated": "{now_iso}",
  "started_at": "{now_iso}"
}
```

### 3. {output_path}/wiki-memory.md (빈 구조)

```markdown
## 스코프 결정사항
(researcher가 초안 작성, 사람이 확정)

## 확정 용어
(researcher가 채움)

## 스타일 결정사항
(writer 첫 실행 후 채움)

## 문서 간 참조 맵
(writer가 문서 생성할 때마다 추가)

## 수정 이유 로그
(reviewer가 채움)
```

## 완료 후

출력 폴더가 없으면 함께 생성하세요.

완료 메시지:

"✅ 설정 완료. 다음은 `wiki-researcher`를 실행해 소스를 모으세요."
