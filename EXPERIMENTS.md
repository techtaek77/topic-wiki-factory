# Experiments

메인 프로젝트는 `topic-wiki-factory/`다.
이 문서는 옆에 생긴 실험용 작업 폴더들이 무엇을 시험했고, 메인에 어떤 상태로 반영할지 정리한다.

## 현재 기준

| 폴더 | 목적 | 현재 판단 | 메인 반영 방식 |
|------|------|----------|----------------|
| `topic-wiki-factory` | 메인 제품 | source of truth | 여기서 계속 발전 |
| `topic-wiki-factory-validation` | 샘플 출력 검수 / 체크리스트 | validation workspace | 필요한 체크리스트와 샘플만 메인으로 이동 |
| `topic-wiki-factory-narrative-layer` | 내러티브 강화 아이디어 실험 | idea branch | 좋은 문장 규칙만 메인 문서/템플릿에 선별 반영 |
| `topic-wiki-factory-agent-simplify` | 4-agent 운영 모델 실험 | RFC 수준 실험 | 별도 의사결정 전까지 메인에 비병합 |

## 왜 이렇게 본다

### validation

- 샘플 출력과 체크리스트를 모아 둔 검수 작업장이다.
- 제품 구조를 갈아엎는 브랜치가 아니라 결과물 품질을 확인하는 용도다.
- 메인에는 `examples/`, `tests/`, 체크리스트 문서 형태로 필요한 부분만 흡수한다.

### narrative-layer

- "책처럼 읽히는 위키"라는 방향을 더 강하게 밀어 보려던 실험이다.
- 다만 README나 spec 일부 조정 외에는 메인을 대체할 만큼 구조가 정리되진 않았다.
- 메인에는 서사적 설명 원칙, 기억에 남는 예시 방식, onboarding 문구만 선별 반영한다.

### agent-simplify

- `initializer / builder / maintainer / publisher` 4개 역할로 줄이는 큰 구조 변경안이다.
- README만 바뀐 게 아니라 spec, prompts, state 운용 방식이 같이 달라진다.
- 이건 "조금씩 섞기"보다 v2 의사결정이 필요한 실험이다.
- 메인 구조와 섞어 쓰면 README와 실제 워크플로우가 서로 충돌할 가능성이 크다.

## 메인에 반영할 원칙

1. 메인 repo는 현재의 다중 에이전트 구조를 유지한다.
2. 실험 브랜치의 아이디어는 "문장", "템플릿", "샘플", "체크리스트"처럼 좁은 단위로만 반영한다.
3. `agent-simplify`는 별도 RFC 문서 없이 메인에 병합하지 않는다.
4. 새 샘플은 메인 `examples/`에 추가해서 제품 방향을 설명하는 데 직접 쓰도록 한다.

## 당장 반영할 것

- README를 내러티브 중심으로 더 선명하게 다듬기
- `examples/`에 새 샘플 추가
- validation에서 얻은 검수 관점을 공개 저장소용 예시에 반영하기

