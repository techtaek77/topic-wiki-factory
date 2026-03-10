# Tests

`topic-wiki-factory`는 실행 코드보다 프롬프트/에이전트 문서가 핵심 로직에 가깝다.
그래서 테스트도 "런타임 독립적으로 지켜야 할 상태 전이 규칙"을 fixture로 검증하는 방식으로 둔다.

## Orchestrator Harness

아래 스크립트는 두 가지를 검사한다.

1. `.claude/agents/wiki-orchestrator.md`와 `prompts/wiki-orchestrator.md`에 핵심 규칙 문구가 빠지지 않았는지
2. 대표 시나리오에서 기대하는 다음 phase / next action이 일관되는지

실행:

```bash
python3 scripts/orchestrator_harness.py
```

현재 포함된 시나리오:

- `init`에서 `sources.md`가 없으면 `wiki-researcher`로 가는지
- `HITL=false`일 때 `scoping`과 `planning`이 자동 진행되는지
- `docs_to_revise`가 일반 문서보다 우선되는지
- revision limit 초과 시 `docs_blocked`로 빠지는지
- `reviewing` 이후 `publishing` / `done` 분기가 맞는지

이 하네스는 "모든 런타임에서 실제 LLM이 정확히 똑같이 행동한다"를 증명하지는 않는다.
대신 최소한 저장소가 약속한 규칙이 문서에서 빠지거나 서로 어긋나는 건 빨리 잡아낸다.
