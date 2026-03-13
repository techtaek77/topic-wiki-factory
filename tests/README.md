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

이건 실행 하네스라기보다 acceptance checker에 가깝다.
즉, 위키를 처음부터 끝까지 생성하는 러너가 아니라, 저장소가 약속한 orchestrator 규칙이 문서와 fixture에서 일관되는지 확인하는 스크립트다.

현재 포함된 시나리오:

- `init`에서 `sources.md`가 없으면 `wiki-researcher`로 가는지
- `scope_confirmed=true`, `ia_confirmed=true` 상태로 재실행해도 확인 루프에 안 갇히는지
- `planning`에서 `docs_planned`가 비어 있으면 writer로 건너뛰지 않고 IA 설계를 먼저 요구하는지
- `HITL=false`일 때 `scoping`과 `planning`이 자동 진행되는지
- `docs_to_revise`가 일반 문서보다 우선되는지
- 예전 샘플처럼 문자열 배열 state도 객체 배열로 정규화되는지
- revision limit 초과 시 `docs_blocked`로 빠지는지
- `reviewing` 이후 `publishing` / `done` 분기가 맞는지

이 checker는 "모든 런타임에서 실제 LLM이 정확히 똑같이 행동한다"를 증명하지는 않는다.
대신 최소한 저장소가 약속한 규칙이 문서에서 빠지거나 서로 어긋나는 건 빨리 잡아낸다.
