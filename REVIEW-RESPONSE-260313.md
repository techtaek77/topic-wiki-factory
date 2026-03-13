# REVIEW-260313 대응 메모

> 기준 날짜: 2026-03-13
> 대상 리뷰: [REVIEW-260313.md](REVIEW-260313.md)

이 문서는 외부 리뷰를 읽고, 무엇을 수용하고 무엇을 보류하거나 반박할지 정리한 작업 메모다.
목표는 리뷰를 감상으로 끝내지 않고, 제품 판단과 문서 수정으로 연결하는 것이다.

## 한 줄 결론

리뷰의 큰 방향은 맞다.
특히 `30분 약속 대비 진입 장벽`, `원커맨드 실행 부재`, `Cross-runtime UX`, `사실 검증 리스크` 지적은 실제 제품 위험으로 본다.

다만 모든 지적을 그대로 수용하지는 않는다.
현재의 다중 에이전트 구조는 아직 실험 대상이 아니라 메인 설계의 일부이므로, 바로 4-agent로 줄이지는 않는다.

## 판정표

| 항목 | 판정 | 이유 | 바로 반영한 것 |
|------|------|------|----------------|
| 30분 약속이 과하다 | 수용 | 첫 초안 30분과 완성 30분은 다르다 | README 문구를 `첫 초안` 기준으로 수정 |
| 시작 UX가 무겁다 | 수용 | 빠른 시작은 3단계지만 아래 설명이 다시 무거워진다 | README에 primary path와 현재 한계를 더 명확히 표시 |
| 원커맨드 실행기가 없다 | 수용 | 실제로 아직 없다 | README / tests에 acceptance harness와 runner를 구분해 명시 |
| 에이전트 11개는 과하다 | 부분 수용 | visible complexity는 문제지만 내부 역할 분해 자체는 아직 유지 가치가 있다 | README에서 advanced 섹션으로 내리고 “처음엔 다 외울 필요 없다” 추가 |
| Cross-runtime 경험이 약하다 | 수용 | Cursor / Codex는 현재 paste workflow다 | README에 Claude Code primary, others best-effort 명시 |
| 사실 검증 부재가 위험하다 | 수용 | 교육형 위키에서는 실제 제품 리스크다 | 대응 필요 항목으로 남기고 roadmap 성격으로 표시 |
| LICENSE 파일이 없다 | 반박 | 저장소에 LICENSE가 실제로 있다 | 별도 수정 없음 |
| 하네스가 곧 실행기처럼 보인다 | 수용 | 이름 때문에 기대치 혼동이 생길 수 있다 | tests/README에 acceptance checker 성격 명시 |

## 이번에 반영한 수정

### 1. README 기대치 조정

- "30분 안에 위키를 만든다"를 "30분 안에 첫 초안을 잡도록 돕는다"로 조정
- 현재 가장 매끄러운 런타임이 Claude Code라는 점 명시
- Cursor / Codex / GPT 경로는 best-effort paste workflow라고 명시
- 원커맨드 실행기가 아직 없다는 점을 숨기지 않고 적음

### 2. orchestrator 설명 보정

- orchestrator를 "완성까지 한 번에 도는 실행기"보다 "상태를 읽고 다음 단계를 정하는 컨트롤러"로 설명
- acceptance harness는 상태 전이 규칙 checker이지 end-to-end runner가 아니라는 점을 분리

### 3. visible complexity 완화

- 에이전트 목록을 `Advanced` 섹션으로 내림
- 처음에는 `wiki-initializer`, `wiki-orchestrator`, 필요 시 `wiki-publisher`만 보면 된다고 가이드

### 4. 실험 / 후속 작업 추적

- `EXPERIMENTS.md`의 "당장 반영할 것"을 체크리스트에 가깝게 보강
- 아직 미해결인 항목:
  - 원커맨드 실행기 또는 auto-runner
  - agent-simplify 방향 확정
  - 사실 검증 최소 장치

## 아직 안 한 것

### 원커맨드 실행기

이건 문구 수정으로 해결되는 문제가 아니라 실제 실행 모델 추가가 필요하다.
예:

```bash
./wiki create --topic "체스" --type knowledge
```

또는:

```text
@wiki-orchestrator --auto
```

이건 다음 설계/구현 단계에서 다뤄야 한다.

### 사실 검증 최소 장치

후보는 아래 둘이다.

1. reviewer가 `sources.md`의 핵심 링크를 다시 확인하고 충돌 여부를 표시
2. 자동 검증이 안 된 문장에 주석 또는 경고 블록을 남김

현재는 Known Limitation으로 남아 있고, 제품적으로는 P1~P2 급 개선 후보로 본다.

### agent-simplify 채택 여부

리뷰가 지적한 방향 자체는 타당하다.
하지만 지금 당장 11개 에이전트를 4~6개로 줄이는 건 문서 수정이 아니라 제품 구조 변경이라, RFC 없이 바로 병합하진 않는다.

## 다음 우선순위

1. 원커맨드 실행기 / auto-runner 방향을 spec 수준에서 먼저 확정
2. README 첫 화면을 더 "한 줄 명령 + 결과 예시" 중심으로 줄일지 결정
3. 사실 검증 최소 장치를 reviewer/spec에 설계
4. agent-simplify를 v2 실험으로 계속 둘지, 메인 로드맵에 편입할지 판단

## 메모

이 리뷰는 세게 썼지만, 프로젝트를 엉뚱한 방향으로 끌고 간 리뷰는 아니다.
오히려 "지금 이게 혼자 쓰는 강한 도구인지, 남도 쓰는 제품인지"를 구분하게 해 준 점에서 유효했다.
