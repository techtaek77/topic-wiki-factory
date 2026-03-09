# Wiki Memory — Harness

> 에이전트 간 공유 지식 저장소.
> initializer가 빈 구조 생성 → researcher가 첫 내용 채움 → writer/reviewer가 계속 추가.

---

## 확정 용어
<!-- researcher가 채움. writer는 매 문서 작성 시 이 목록 참조. -->

| 용어 | 정의 | 첫 등장 문서 |
|------|------|------------|
| Pipeline | 코드 변경이 테스트를 거쳐 배포까지 자동으로 가는 흐름 | pipeline.md |
| Stage | Pipeline 안의 개별 실행 단계. CI Stage / CD Stage로 나뉨 | stage.md |
| Step | Stage 안의 가장 작은 실행 단위 (명령어 1개) | step.md |
| Trigger | Pipeline을 자동 실행하는 조건 (push, PR, 스케줄 등) | trigger.md |
| Service | 배포 대상 애플리케이션 정의 | service-environment.md |

---

## 스타일 결정사항
<!-- writer 첫 실행 후 확정. 이후 모든 문서에 일관 적용. -->

- 한 줄 요약: "~이다"로 끝내기
- 예시: 실행 가능한 YAML 코드 블록 사용
- 자주 하는 실수: 최소 2개
- 비유: 공장/컨베이어 벨트 계열 비유 사용 (Harness 특성상)
- 독자 호칭: "개발자", "여러분" 사용. "사용자" 금지.

---

## 문서 간 참조 맵
<!-- writer가 문서 생성할 때마다 추가. updater가 파급 분석에 사용. -->

| 문서 | 참조하는 문서들 |
|------|--------------|
| pipeline.md | stage, trigger, cicd-basics |
| stage.md | pipeline, step |
| step.md | stage |
| trigger.md | pipeline |
| first-pipeline.md | pipeline, stage, step, trigger |
| approval-stage.md | stage |
| rolling-deployment.md | stage, service-environment |

---

## 수정 이유 로그
<!-- reviewer가 REVISE 판정 시 추가. writer가 재작성 전 반드시 읽음. -->

| 문서 | 판정 | 이유 | 시도 횟수 |
|------|------|------|---------|
| stage.md | REVISE | 자주 하는 실수 1개뿐 → 최소 2개로 보강 | 1회 |
