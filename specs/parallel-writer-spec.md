# Spec: Parallel Writer Extension
version: 0.1.0
updated: 2026-03-10

## 왜 이 문서가 필요한가

현재 `wiki-orchestrator`는 `wiki-state.json`을 기준으로 다음 단계를 자동으로 넘겨주는 상태 기계다.
`hitl` 설정을 끄면 사람 확인 없이 진행할 수 있지만, 기본 작성 모델은 여전히 `문서 1개 선택 -> writer 실행 -> state 갱신`의 순차 루프다.

이 문서는 "자동 진행"과 "병렬 writer 실행"을 구분하고, 병렬 확장을 안전하게 도입하기 위한 설계를 정의한다.

## 문제 정의

- 사용자는 `hitl=false`면 전체 문서가 한 번에 병렬 작성될 것이라고 기대하기 쉽다.
- 하지만 현재 state 스키마는 단일 `current_doc` 중심이라 동시 실행 추적이 어렵다.
- reviewer 이전에 writer 여러 개가 동시에 돌면 링크, glossary, prerequisite map, 중복 개념 같은 충돌이 생길 수 있다.
- 실패한 문서만 재시도해야 하는데, 현재 구조는 순차 루프에 더 잘 맞는다.

## 목표

- `hitl=false`일 때도 orchestrator가 사람 질문 없이 끝까지 자동 진행되게 한다.
- 선택적으로 여러 writer를 동시에 실행할 수 있게 한다.
- 병렬 실행 중에도 `wiki-state.json`이 단일 진실원으로 유지되게 한다.
- 실패, 재시도, 충돌, 재검토 루프를 추적 가능하게 만든다.

## 비목표

- 첫 버전에서 모든 런타임에 동일한 병렬 실행 기능을 강제하지 않는다.
- writer들이 같은 파일을 동시에 수정하는 협업 편집까지 지원하지 않는다.
- reviewer까지 완전 병렬 분산 처리하는 것은 이번 범위에 넣지 않는다.

## 용어

- `sequential mode`: 현재 기본 방식. 문서 1개씩 선택해 작성
- `parallel mode`: 여러 문서를 동시에 writer에 할당
- `dispatch batch`: 한 번에 병렬로 내보낸 문서 묶음
- `ready docs`: 선수 지식/선행 문서 조건을 만족해 지금 작성 가능한 문서

## 제안

기본값은 그대로 순차 모드로 둔다.
병렬 실행은 opt-in 설정으로 추가한다.

```yaml
execution:
  mode: sequential   # sequential | parallel
  max_parallel_writers: 3
  batch_strategy: ready-first   # ready-first | guides-last
```

## 상태 스키마 변경

현재의 단일 `current_doc`만으로는 병렬 추적이 안 된다.
아래 필드를 추가한다.

```json
{
  "current_doc": null,
  "active_docs": [
    {
      "slug": "quick-start",
      "path": "docs/guides/quick-start.md",
      "status": "writing",
      "assigned_at": "2026-03-10T10:00:00+09:00",
      "attempt": 1,
      "batch_id": "batch-001"
    }
  ],
  "dispatch_queue": [
    "specification",
    "planning"
  ],
  "completed_batches": [
    {
      "batch_id": "batch-001",
      "doc_slugs": ["quick-start", "specification"],
      "finished_at": "2026-03-10T10:08:00+09:00"
    }
  ]
}
```

규칙:

- `current_doc`는 하위 호환용으로 유지하되, parallel 모드에서는 `null` 허용
- 병렬 모드의 실행 중 문서는 `active_docs`가 진실원
- 아직 시작 안 한 문서는 `dispatch_queue`에 둔다
- batch 단위 완료 기록은 디버깅과 재시도 분석용으로 남긴다

## 문서 의존성 규칙

병렬 writer를 막 돌리면 문서끼리 서로 없는 링크를 걸 수 있다.
그래서 먼저 `docs_planned`에서 의존성을 계산한다.

기본 규칙:

- `index`, `prerequisite-map`, `glossary`, `faq`는 먼저 작성 가능
- `quick-start`는 바로 작성 가능
- guide 문서는 관련 concept가 최소 1개 이상 준비되면 작성 가능
- concept 간 강한 선후관계가 있으면 `sources.md` 또는 `wiki-memory.md`에 의존성을 기록

간단한 예:

```json
"doc_dependencies": {
  "turn-a-spec-into-a-plan": ["specification", "planning"],
  "run-sdd-with-an-agent-team": ["planning", "tasks-and-acceptance-criteria"]
}
```

## 오케스트레이터 동작

### 1. planning 단계

- `docs_planned` 설계
- `doc_dependencies` 계산
- `execution.mode=parallel`이면 `dispatch_queue` 초기화

### 2. writing 단계

순차 모드:

- 기존처럼 문서 1개 선택

병렬 모드:

- `docs_to_revise`가 있으면 재작성 대상을 우선 배치
- `active_docs.length < max_parallel_writers` 동안 `ready docs`를 꺼내 배치
- 같은 batch 안에는 서로 직접 의존하는 문서를 같이 넣지 않음
- writer 실행 후 결과를 기다리고 state를 갱신

### 3. reviewing 단계

- 모든 `active_docs`가 비어 있을 때만 진입
- reviewer는 전체 문서를 보고 수정 목록을 반환
- 수정 필요 문서는 다시 `dispatch_queue`로 넣되, 같은 batch에 묶지 않아도 됨

## 충돌 방지 규칙

- writer는 자신에게 할당된 `path`만 수정한다
- 공용 파일인 `index.md`, `glossary.md`, `prerequisite-map.md`, `wiki-memory.md`는 batch 종료 후 orchestrator가 통합 갱신한다
- writer가 공용 파일 변경 제안이 필요하면 `proposed_shared_updates` 형태로 state에 남긴다

예시:

```json
{
  "slug": "specification",
  "proposed_shared_updates": {
    "glossary_terms": ["spec", "constraint"],
    "index_links": ["docs/concepts/specification.md"]
  }
}
```

## 실패와 재시도

- writer 실패 시 해당 slug만 `docs_to_revise` 또는 `docs_blocked`로 이동
- 다른 active 문서는 계속 진행 가능
- `revision_attempts[slug]`는 문서별로 독립 증가
- 같은 문서가 `max_revision_attempts`를 넘기면 batch 전체를 막지 않고 그 문서만 차단

## HITL 규칙

- `hitl.confirm_scope_after_research=false`면 scope 질문 없이 planning으로 진행
- `hitl.confirm_ia_before_writing=false`면 IA 질문 없이 writing으로 진행
- 병렬 여부는 `hitl`이 아니라 `execution.mode`가 결정

즉:

- `hitl=false + sequential` = 사람 질문 없는 순차 자동 진행
- `hitl=false + parallel` = 사람 질문 없는 병렬 자동 진행

이 둘은 다른 모드다. 여기서 많이 헷갈린다. 범인은 이름이 아니라 기대치였다.

## 롤아웃 순서

1. 문서와 프롬프트에 `hitl`과 `execution.mode` 차이를 명시
2. state 스키마에 `active_docs`, `dispatch_queue`, `doc_dependencies` 추가
3. orchestrator가 `ready docs` 계산하도록 수정
4. writer 결과를 batch 단위로 집계
5. reviewer 이후 재시도 루프 검증
6. 마지막에만 기본값 변경 여부 검토

## 성공 기준

- `execution.mode=sequential`일 때 기존 동작이 깨지지 않음
- `execution.mode=parallel`일 때 최소 2개 문서를 동시에 안정적으로 처리
- 공용 파일 충돌 없이 reviewer까지 완료
- 실패한 문서 1개가 나와도 다른 문서 진행이 막히지 않음

## 열린 질문

- 런타임별 병렬 실행 방식 차이를 어디까지 흡수할 것인가
- 병렬 writer가 공통 용어를 서로 다르게 정의할 때 어느 단계에서 합칠 것인가
- concept 선행 조건을 수동 설계할지, researcher가 초안으로 뽑아줄지

## 현재 결론

지금 저장소의 기본값은 계속 `sequential`이 맞다.
먼저 "HITL이 꺼지면 질문 없이 자동 진행"을 분명히 하고, 그 다음 별도 opt-in 기능으로 병렬 writer를 넣는 게 가장 안전하다.
