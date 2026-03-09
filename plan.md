# Plan: Topic Wiki Factory MVP
version: 1.2.1
updated: 2026-03-10

## Spec 요약
- Goal: 주제별 Feynman 구조 위키를 빠르게 생성하는 템플릿 repo + 에이전트 시스템
- Domain Types: `tool` / `knowledge` 통합 구조
- 자동화 수준: 반자동 (orchestrator 수동 호출)
- 발행: GitHub Markdown (MVP)
- 런타임: Claude Code 주, prompts/ 폴더로 타 런타임 지원

---

## Phase 1. Design (설계)

### 1. Feynman 문서 템플릿 정의 ✅
- Input: 파인만 5단계 구조
- Output: `templates/feynman-doc-template.md`
- DoD: tool(Harness Pipeline) + knowledge(체스 룩) 두 예시 검증 통과
- Status: **완료**

### 2. 위키 공통 IA 정의 ✅
- Input: domain_type (tool / knowledge), Feynman 템플릿
- Output: `templates/ia-structure.md`
- DoD: 홈 / prerequisite-map / 개념 / 실전 / FAQ / glossary 구조가 두 유형 모두 명시. tool은 changelog 추가.
- Tests: Harness / 체스 두 주제에 대입해도 사이드바가 자연스럽다 ✅
- Status: **완료**

### 3. wiki-config.yaml 스키마 확정 ✅
- Input: spec의 Inputs 섹션, models 섹션
- Output: `templates/wiki-config.example.yaml` — 채워야 할 모든 필드와 예시값
- DoD: topic_name / domain_type / output_path / models 필드 포함. Harness / 체스 두 예시 손으로 채울 수 있다.
- Tests: 필수 필드 목록이 명확하고 선택 필드는 기본값이 있다
- Risk: 필드가 많아지면 초기 진입 장벽 상승 → 필수는 5개 이하로 제한
- Estimate: 30m

### 4. wiki-state.json + wiki-memory.md 스키마 확정 ✅
- Input: orchestrator 재개 로직 + 에이전트 메모리 요구사항
- Output:
  - `templates/wiki-state.example.json` — phase / docs_planned / docs_written / docs_to_revise / docs_done / revision_reasons
  - `templates/wiki-memory.example.md` — 확정 용어 / 스타일 결정사항 / 참조 맵 / 수정 로그 섹션
- DoD: 중단 후 재실행 시나리오를 글로 설명 가능. 에이전트별 read/write 권한이 명확하다.
- Tests: revision_reasons에 이유가 있어야 docs_to_revise 항목이 생성된다
- Estimate: 30m

---

## Phase 2. Template Repo (템플릿 구조 구축)

### 5. Repo 폴더 구조 확정 및 생성 ✅
- Input: Phase 1 결과물 전체
- Output: template repo 폴더 골격 생성
- DoD: 아래 구조가 실제로 존재한다
  ```
  /
  ├── .claude/agents/wiki-*.md     ← Claude Code용
  ├── prompts/wiki-*.md            ← 타 런타임용
  ├── templates/
  │   ├── feynman-doc-template.md
  │   ├── ia-structure.md
  │   ├── wiki-config.example.yaml
  │   └── wiki-state.example.json
  ├── docs/                        ← 생성된 위키 파일 출력 위치
  ├── wiki-config.yaml             ← 사용자가 채우는 파일 (빈 상태)
  ├── wiki-state.json              ← orchestrator가 관리 (초기 빈 상태)
  └── README.md
  ```
- Tests: git clone 후 README만 읽고 첫 실행까지 가능하다
- Estimate: 45m

### 6. README.md 작성
- Input: 전체 user flow
- Output: `README.md`
- DoD: clone → initializer 실행 → orchestrator 반복 → publish 흐름이 5단계 이내로 설명된다. Claude Code / Cursor / Codex 각 런타임 실행법 안내 포함.
- Tests: 처음 보는 사람이 README만 읽고 시작할 수 있다
- Estimate: 45m

---

## Phase 3. Agents (에이전트 구현)

> 모든 에이전트는 `.claude/agents/wiki-*.md` + `prompts/wiki-*.md` 이중으로 작성한다.
> 형식: `.claude/docs/agents/agent-structure.md` 준수, 50~100줄 범위.

### 7. wiki-initializer ✅
- 담당: AskUserQuestion 마법사 → wiki-config.yaml 저장
- Input: 사용자 답변
- Output: wiki-config.yaml (output_path, models 포함)
- DoD: 필수 5개 질문 후 yaml 저장. 누락 시 재질문. 완료 후 "이제 @wiki-orchestrator를 실행하세요" 안내.
- Tests: Harness / 체스 두 시나리오로 실행 시 wiki-config.yaml이 올바르게 생성된다
- Estimate: 60m

### 8. wiki-orchestrator ✅
- 담당: wiki-state.json 읽고 다음 단계 결정 + 서브 에이전트 호출
- Input: wiki-state.json
- Output: 단계별 서브 에이전트 호출 + state 업데이트
- DoD: phase별 분기 (init→researching→writing→reviewing→publishing→done). docs_to_revise 있으면 writer 재호출. 완료 문서는 건너뜀.
- Tests: 중간에 중단 후 재실행 시 완료된 문서를 다시 쓰지 않는다
- Risk: state 파일 손상 시 복구 방법 필요 → state 초기화 명령 추가
- Estimate: 90m

### 9. wiki-researcher ✅
- 담당: 소스 수집 → sources.md 저장
- Input: wiki-config.yaml (topic, domain_type, urls)
- Output: `sources.md` — 출처 목록 + 핵심 정보 요약
- DoD: tool은 공식 docs + GitHub, knowledge는 reference_url + 웹 검색 결과 포함. 출처별 신뢰도 메모 포함.
- Tests: sources.md만 보고 writer가 문서 작성을 시작할 수 있다
- Model: sonnet
- Estimate: 60m

### 10. wiki-writer ✅
- 담당: 문서 1개 작성 (Feynman 5단계 필수)
- Input: sources.md + feynman-doc-template.md + 문서명
- Output: `{output_path}/docs/{slug}.md`
- DoD: 5섹션 모두 존재. 선수 지식 ≤ 2개. 예시 1개 이상. 과장 표현 없음.
- Tests: 검증 체크리스트 8개 항목 통과
- Model: opus
- Risk: opus 비용 → 문서 1개씩 호출하는 구조로 비용 통제
- Estimate: 60m

### 11. wiki-reviewer ✅
- 담당: docs/ 전체 품질 검토
- Input: `{output_path}/docs/` 전체
- Output: 검토 리포트 + docs_to_revise → wiki-state.json 반영
- DoD: 체크리스트 8개 항목 기준. PASS / REVISE 판정. REVISE면 이유와 수정 방향 명시.
- Tests: REVISE 판정된 문서가 writer 재실행 후 PASS로 바뀐다
- Model: sonnet
- Estimate: 60m

### 12. wiki-publisher ✅
- 담당: git push → GitHub
- Input: `{output_path}/docs/` 완료 파일
- Output: GitHub repo push 완료
- DoD: git add → commit (주제명 + 날짜) → push. 실패 시 에러 메시지 출력.
- Tests: push 후 GitHub에서 MD 파일이 렌더링된다
- Model: haiku
- Estimate: 30m

### 13. wiki-updater ✅
- 담당: 변경 파급 효과 분석 → docs_to_revise 업데이트
- Input: 변경 요청 (변경된 문서명 + 변경 내용)
- Output: 영향받은 파일 목록 → wiki-state.json의 docs_to_revise에 추가
- DoD: 변경 문서를 참조하는 모든 문서 탐지. prerequisite-map / index / glossary 변경 필요 여부 판단. orchestrator 호출로 마무리.
- Tests: pipeline.md 변경 시 stage.md(참조 문서)가 docs_to_revise에 들어간다
- Model: sonnet
- Estimate: 60m

### 14. wiki-auditor ✅
- 담당: 주기 점검 — 끊긴 링크 / 고아 문서 / Feynman 구조 미준수 / glossary 누락
- Input: `{output_path}/docs/` 전체
- Output: 이슈 목록 (종류별 분류) + 심각도 (critical / warning)
- DoD: 끊긴 링크 / 고아 문서 / 5섹션 미준수 / glossary 미연결 4가지 탐지. critical은 즉시 수정 권고.
- Tests: 의도적으로 끊긴 링크를 만들면 auditor가 탐지한다
- Model: haiku
- Estimate: 45m

### 15. wiki-freshness ✅
- 담당: tool 위키 최신성 점검 (tool 전용)
- Input: wiki-config.yaml (official_url, github_url)
- Output: 업데이트 필요 문서 목록 + 버전 차이 요약
- DoD: 공식 사이트 / GitHub 릴리즈 최신 내용과 현재 docs 비교. 버전 차이 있으면 해당 문서를 docs_to_revise 후보로 출력.
- Tests: Harness 새 릴리즈가 있을 때 관련 문서가 탐지된다
- Model: sonnet
- Estimate: 60m

### 16. wiki-gap-finder ✅
- 담당: 지식 공백 탐지 — 언급됐지만 문서 없는 개념
- Input: `{output_path}/docs/` 전체 + prerequisite-map.md
- Output: 미작성 개념 목록 + 학습 로드맵 빈 구간
- DoD: [[링크]]가 있지만 실제 파일이 없는 것 모두 탐지. 우선순위(많이 참조된 순) 포함.
- Tests: [[castling]] 링크가 있는데 castling.md가 없으면 탐지된다
- Model: sonnet
- Estimate: 45m

---

## Phase 4. Validation (End-to-End 검증)

### 17. 샘플 주제 end-to-end 실행
- Input: tool 1개 (Harness) + knowledge 1개 (체스)
- Output: 각각 완성된 docs/ 폴더 + GitHub push
- DoD: initializer → orchestrator 반복 → publisher 전 과정이 막힘 없이 실행된다. 각 주제에서 최소 8개 문서 생성.
- Tests: Content Quality Standard 체크리스트 통과율 90% 이상
- Estimate: 120m

### 18. 타 런타임 검증 (Cursor / Codex)
- Input: prompts/wiki-*.md
- Output: 타 런타임에서 동일한 결과물 생성 확인
- DoD: prompts/ 파일만으로 Cursor에서 같은 흐름 실행 가능하다
- Estimate: 60m

---

## Execution Order

```
Phase 1 (설계)
  1 ✅ Feynman 템플릿
  2   공통 IA
  3   wiki-config 스키마
  4   wiki-state 스키마

Phase 2 (구조)
  5   Repo 폴더 골격 생성
  6   README.md

Phase 3 (에이전트) — 생성 파이프라인 먼저, 관리 에이전트 나중
  7   wiki-initializer
  8   wiki-orchestrator     ← 가장 복잡. 충분히 시간 확보.
  9   wiki-researcher
  10  wiki-writer
  11  wiki-reviewer
  12  wiki-publisher
  13  wiki-updater
  14  wiki-auditor
  15  wiki-freshness
  16  wiki-gap-finder

Phase 4 (검증)
  17  end-to-end 실행
  18  타 런타임 검증
```

**총 예상 시간**: 약 14~16시간 (설계 3h / 구조 2h / 에이전트 8h / 검증 3h)

---

## Current Status

| Phase | 상태 |
|-------|------|
| Phase 1 | ✅ 완료 (Task 1~4 모두 완료) |
| Phase 2 | ✅ 완료 (Task 5~6 + prompts/ 완료) |
| Phase 3 | ✅ 완료 (Task 7~16, 에이전트 11개 + prompts 11개) |
| Phase 4 | ✅ 완료 (validation 3케이스 정리 + schema 정합성 확인) |

**Next**: 템플릿 공개 후 실사용 주제 1개로 GitHub Markdown publish dry run
