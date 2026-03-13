# Spec: Topic Wiki Factory
version: 1.1.1
updated: 2026-03-10

## Goal

특정 주제에 대한 지식을 `플레이북형 위키 사이트`로 빠르게 생성할 수 있는 템플릿 앱과 에이전트 워크플로우를 설계한다.

핵심 차별점: 단순 문서 자동화가 아니라, **파인만 학습 원칙을 적용한 교육형 위키**다.
독자가 처음 봤을 때 "이게 뭔지"부터 이해하고, "왜 필요한지", "뭘 먼저 알아야 하는지", "어떻게 쓰는지"까지 자연스럽게 따라갈 수 있어야 한다.

## Problem

- 좋은 자료가 있어도 `학습 가능한 구조`로 바꾸는 데 시간이 많이 든다.
- 공식 문서, 블로그, GitHub, 릴리즈 노트가 흩어져 있어 학습 흐름이 끊긴다.
- 매 주제마다 구조를 새로 설계하니 재사용성이 낮다.
- 기존 문서 사이트는 "설치 → 기능 나열" 구조라 맥락 없이 던져지는 느낌이다.

## Users

- 새로운 툴/플랫폼을 빠르게 공부하고 정리하고 싶은 1인 운영자
- 특정 도메인 지식을 팀용 위키로 바꾸고 싶은 실무자
- AI 에이전트를 붙여 문서 생성/유지보수를 자동화하고 싶은 빌더

## Domain Types

두 가지 성격의 주제를 같은 구조로 커버한다.

| 유형 | 예시 | 특징 |
|------|------|------|
| `tool` | Harness, Claude Code, n8n | 공식 URL + GitHub 있음, 버전/릴리즈 추적 필요 |
| `knowledge` | 체스, 알고리즘, 투자 전략 | 공식 URL 없거나 약함, 개념/전략 중심, 거의 정적 |

MVP에서 두 유형 모두 지원한다. 입력 스키마에서 `domain_type`으로 분기한다.

## Learning Methodology: Feynman Structure

모든 문서는 아래 5단계 구조를 따른다.
이 구조가 툴 위키와 지식 도메인 위키를 통일하는 핵심이다.

```
1. 한 줄 설명     — 처음 보는 사람도 이해하는 언어로
2. 왜 필요한가    — 맥락과 존재 이유
3. 선수 지식      — 이걸 이해하려면 먼저 알아야 할 것 (링크 포함)
4. 어떻게 쓰는가  — 구현/적용 예시 (tool: 코드, knowledge: 예제/패턴)
5. 더 깊이 가려면 — 다음 읽을 문서 링크
```

예시 — Harness "Pipeline":
```
1. Pipeline은 코드 변경이 배포까지 가는 자동화 흐름이다.
2. 수동 배포는 실수가 잦고 느리다. Pipeline이 이걸 없애준다.
3. 먼저 알아야 할 것: CI/CD 개념 → YAML 기본 문법
4. 구현: pipeline.yaml 작성 → stage 정의 → trigger 설정
5. 다음: Approval Stage → Rolling Deployment
```

예시 — 체스 "룩(Rook)":
```
1. 룩은 가로/세로 방향으로 원하는 만큼 이동할 수 있는 기물이다.
2. 오픈 파일 장악과 킹사이드 공격의 핵심 기물이다.
3. 먼저 알아야 할 것: 기물 기본 이동 규칙 → 체스판 좌표 표기법
4. 실전 패턴: 룩 연결 → 오픈 파일 배치 → 7th rank 장악
5. 다음: 루크 엔드게임 → 캐슬링
```

## Desired Outcome

`topic-wiki-factory`가 새 주제를 입력받아 아래를 생성한다.

- 위키 홈 (주제 개요 + 학습 로드맵)
- 사이드바 구조
- 빠른 시작 문서
- 핵심 개념 문서 (각각 Feynman 5단계 구조)
- 실전 가이드 문서
- FAQ
- 용어집 (glossary)
- 선수 지식 맵 (prerequisite map)
- 업데이트/릴리즈 추적 문서 (tool 유형만)

## Content Quality Standard

발행 가능 수준의 기준:

- [ ] 각 문서에 "한 줄 설명" 있음 (초보자 언어)
- [ ] 선수 지식이 명시되고 링크됨
- [ ] 실전 예시 1개 이상 있음
- [ ] 다음 읽을 문서 링크 있음
- [ ] 전문 용어는 glossary에 연결됨
- [ ] 과장 표현 없음 ("완벽한", "최고의" 등 금지)

## Non-goals

- 첫 버전에서 완전 자동 사실 검증까지 보장하지 않는다.
- 첫 버전에서 CMS, 로그인, 협업 권한 관리까지 만들지 않는다.
- 첫 버전에서 다국어 번역 자동화까지 포함하지 않는다.
- 첫 버전에서 모든 주제에 완벽히 맞는 정보구조를 보장하지 않는다.
- 폼 UI는 MVP에서 만들지 않는다 (CLI로 충분).

## Constraints

- `주제만 바꾸면 재사용` 가능한 구조여야 한다.
- 위키는 정적 사이트 기반으로 시작해 유지보수 복잡도를 낮춘다.
- 에이전트 출력은 사람이 검수 가능한 단위로 나와야 한다.
- 문서 품질보다 `구조화 속도 + 재사용성`을 먼저 잡는다.
- 모든 문서는 Feynman 5단계 구조를 따른다.

## Assumptions

- MVP 발행 대상은 **GitHub Markdown** 이다.
  - 이유: 별도 빌드 없이 바로 검수/공유 가능하고 `output_path` 경로 독립성을 유지하기 쉽다
- GitHub Wiki의 `Home.md`는 `.wiki.git` 대상에 배포할 때만 예외적으로 필요하다.
- tool/knowledge 두 유형 모두 Feynman 5단계 구조로 커버 가능하다.
- AI 에이전트는 초안 작성에 강하지만, 사실성은 후검수가 필요하다.

## MVP Scope

### Inputs

| 필드 | 필수 | 예시 |
|------|------|------|
| `topic_name` | Y | "Harness", "체스" |
| `domain_type` | Y | `tool` / `knowledge` |
| `official_url` | tool만 | https://harness.io |
| `github_url` | tool만 | https://github.com/harness |
| `reference_url` | knowledge만 | 교재/규칙서/위키 URL |
| `target_audience` | Y | "DevOps 입문자", "체스 완전 초보" |
| `depth_level` | Y | `intro` / `practical` / `advanced` |
| `output_path` | Y | `./output/harness` / `03.Resources/하네스` |

`output_path`는 사용자 환경에 따라 자유롭게 지정한다.
- 내 Obsidian 볼트 안: `03.Resources/하네스/`
- 독립 폴더: `./output/harness/`
- 어디든 상관없음. 에이전트는 이 경로만 보고 작동한다.

### Outputs

- `wiki-config.yaml` — 주제 메타데이터 (initializer가 생성)
- `wiki-state.json` — 진행 상태 (orchestrator가 관리)
- `{output_path}/` 폴더 — 실제 위키 산출물 위치
  - `index.md` (홈 + 학습 로드맵)
  - `prerequisite-map.md`
  - `glossary.md`
  - `faq.md`
  - `sources.md`
  - `wiki-memory.md`
  - `changelog.md` (tool 유형만)
  - `docs/concepts/*.md`
  - `docs/guides/*.md`
- GitHub repo push 완료

### User Flow

```
git clone template-repo
  ↓
@wiki-initializer  → AskUserQuestion 마법사 → wiki-config.yaml 저장
  ↓
@wiki-researcher  → 소스 수집 → {output_path}/sources.md 저장
  @wiki-orchestrator → scope 확인 (사람 승인)
  @wiki-orchestrator → IA 확인 (사람 승인)
  @wiki-writer      → 문서 1개 작성 → docs_planned.path에 저장 (orchestrator가 루프)
  @wiki-orchestrator → 다음 단계
  @wiki-reviewer    → 전체 검토 → 수정 필요 항목 state에 기록
  @wiki-orchestrator → 재작성 필요면 writer 재호출, 완료면 다음
  @wiki-publish-preflight → GitHub Markdown repo / GitHub Wiki 대상 점검
  @wiki-publisher   → git push → GitHub
```

사람이 개입하는 지점: `@wiki-orchestrator` 호출 (반자동). 완전 자동 루프는 MVP 범위 밖.

### Agent Roles

**생성 파이프라인**

| 에이전트 | 담당 | 입력 | 출력 |
|---------|------|------|------|
| `wiki-initializer` | 초기 설정 마법사 | AskUserQuestion 답변 | `wiki-config.yaml` |
| `wiki-orchestrator` | 상태 관리 + 단계 결정 | `wiki-state.json` | 다음 에이전트 호출 + state 업데이트 |
| `wiki-researcher` | 소스 수집 + 의미 해석 초안 | `wiki-config.yaml` + 로컬 참고 자료 | `{output_path}/sources.md` |
| `wiki-writer` | 문서 1개 작성 | 소스 + Feynman 템플릿 + 문서 메타데이터 | `docs_planned.path` 위치의 문서 |
| `wiki-reviewer` | 전체 품질 검토 | `docs_planned` 전체 | 수정 목록 → `wiki-state.json` 반영 |
| `wiki-publish-preflight` | 배포 직전 점검 | `wiki-config.yaml` + `{output_path}/` + 원격 repo | READY / REVISE + 수정 포인트 |
| `wiki-publisher` | GitHub 발행 | `{output_path}/` 산출물 전체 | git push |

**변경 대응**

| 에이전트 | 담당 | 입력 | 출력 |
|---------|------|------|------|
| `wiki-updater` | 변경 파급 효과 분석 | 변경 요청 (문서명 + 변경 내용) | 영향받은 파일 목록 → `wiki-state.json`의 `docs_to_revise`에 추가 후 orchestrator 호출 |

**주기 점검 (Proactive)**

| 에이전트 | 담당 | 입력 | 출력 |
|---------|------|------|------|
| `wiki-auditor` | 구조 건강도 점검 | `{output_path}/` 전체 문서 | 끊긴 링크 / 고아 문서 / Feynman 구조 미준수 / glossary 누락 링크 목록 |
| `wiki-freshness` | 최신성 점검 (tool 전용) | `wiki-config.yaml` + 공식 사이트 | 업데이트 필요 문서 목록 + 버전 차이 요약 |
| `wiki-gap-finder` | 지식 공백 탐지 | `{output_path}/` 문서 + `prerequisite-map.md` | 언급됐지만 문서 없는 개념 / 학습 로드맵 빈 구간 목록 |

에이전트 패키징: `.claude/agents/wiki-*.md` (Claude Code 자동 실행) + `prompts/wiki-*.md` (다른 런타임 수동 참조)

**런타임별 사용 방식**

| 런타임 | 에이전트 실행 방식 | 모델 설정 |
|--------|------------------|----------|
| Claude Code | `@wiki-writer` 자동 실행 | frontmatter + wiki-config.yaml |
| Cursor | `prompts/wiki-*.md` 복사 → `.cursor/rules/` | Cursor 설정에서 직접 선택 |
| Codex / GPT | `prompts/wiki-*.md` 열고 붙여넣기 | 런타임 기본값 사용 |
| 기타 AI | `prompts/wiki-*.md` 참조 | 런타임 기본값 사용 |

`wiki-config.yaml`의 `models:` 섹션은 Claude Code에서 적용되고, 다른 런타임에서는 권장값 참고용으로만 쓰인다.

### 운영 루프

```
생성:  initializer → researcher → orchestrator(scope) → orchestrator(IA) → writer(×N) → reviewer → publish-preflight → publisher
변경:  updater → orchestrator(scope 재확인 필요 시) → orchestrator(IA) → writer(영향 파일만) → reviewer → publish-preflight → publisher
점검:  auditor / freshness / gap-finder → 이슈 목록 출력 → 필요시 updater 호출
```

점검은 주기적으로 직접 호출. freshness는 tool 유형 위키에만 해당.

### State File Schema

```yaml
# wiki-state.json
phase: init | researching | scoping | planning | writing | reviewing | publishing | done
output_path: "03.Resources/하네스"    # wiki-config에서 복사
docs_planned:
  - slug: "index"
    title: "Harness"
    kind: "fixed"
    path: "index.md"
    priority: 100
    depends_on: []
  - slug: "quick-start"
    title: "처음 30분 가이드"
    kind: "guide"
    path: "docs/guides/quick-start.md"
    priority: 90
    depends_on: ["index"]
docs_written:
  - slug: "index"
    title: "Harness"
    kind: "fixed"
    path: "index.md"
docs_to_revise: ["quick-start"]
docs_done:
  - slug: "index"
    title: "Harness"
    kind: "fixed"
    path: "index.md"
current_doc:
  slug: "quick-start"
  title: "처음 30분 가이드"
  kind: "guide"
  path: "docs/guides/quick-start.md"
last_updated:   "2026-03-09T10:00:00"
```

orchestrator는 이 파일을 읽고 `docs_planned.slug - docs_done.slug`가 0이 될 때까지 writer를 호출한다.
기본 선택 규칙은 `docs_to_revise 우선 -> depends_on 충족 -> priority 높은 순 -> docs_planned 원래 순서`다.
중단 후 재실행해도 완료된 문서는 건너뛰고 이어서 진행한다.
updater / auditor / freshness가 이슈를 발견하면 `docs_to_revise`에 추가하고 orchestrator를 호출한다.

호환성 규칙:
- `docs_written`, `docs_done`의 정식 저장 형식은 `{slug,title,kind,path}` 객체 배열이다.
- 예전 샘플처럼 문자열 배열이 들어오면 orchestrator / reviewer는 `docs_planned`를 기준으로 같은 `slug` 객체로 먼저 정규화한다.
- `docs_planned` 객체에는 필요하면 `priority`, `depends_on`를 함께 둘 수 있다.
  - `priority`: 0~100 정수 권장, 기본값 50
  - `depends_on`: 먼저 끝나야 할 문서 slug 배열, 기본값 `[]`

### Publish Target

- **GitHub Markdown** (MVP): `docs/` 폴더를 GitHub repo에 push. GitHub이 MD를 네이티브 렌더링.
- VitePress/GitHub Pages는 선택적 후속 단계. MVP에서 필수 아님.

## Success Criteria

- 새 주제 하나에 대해 30분 이내로 위키 초안 생성 가능
- 최소 8개 이상의 연결된 문서 생성
- 홈/사이드바/문서 제목 체계가 일관됨
- 모든 문서가 Feynman 5단계 구조를 따름
- 선수 지식 링크가 끊기지 않음
- 사람이 검수 후 바로 발행 가능한 수준의 초안 확보

## Error Handling

### Retry / Loop 방지
reviewer가 계속 REVISE 판정을 내리면 무한 루프가 발생한다. 아래 규칙으로 방지한다.

```json
"revision_attempts": { "stage": 2 }
```

- 문서당 최대 재시도 3회
- 3회 초과 시 `docs_blocked`로 이동 + 사용자에게 수동 검토 요청 출력
- orchestrator가 blocked 항목은 건너뛰고 나머지 진행

### 에이전트별 실패 대응

| 에이전트 | 실패 상황 | 대응 |
|---------|---------|------|
| researcher | 소스 부족 (3개 미만) | 경고 출력 후 계속 진행. sources.md에 "소스 부족" 메모. |
| writer | 파일 저장 실패 | 에러 출력 + state 업데이트 안 함 → 재실행 시 재시도 |
| publisher | git push 실패 | 에러 메시지 + 수동 push 명령어 출력 |
| orchestrator | state 파일 손상 | `wiki-state-init` 명령으로 state 초기화 후 재시작 |

## Naming Rules

모든 파일명은 kebab-case 소문자. 링크 일관성을 위해 writer/reviewer/updater 모두 이 규칙을 강제한다.

```
# 개념/실전 문서
pipeline.md
rook.md
cicd-basics.md

# 공통 고정 파일 (모든 위키)
index.md
glossary.md
faq.md
prerequisite-map.md

# tool 전용
changelog.md
```

wiki-writer는 문서명을 받을 때 자동으로 kebab-case로 변환 후 저장한다.

## Initializer Question List

wiki-initializer가 순서대로 묻는 질문 목록. 답변이 wiki-config.yaml에 저장된다.

```
Q1. 어떤 주제의 위키를 만들 건가요? (topic_name)
    예: Harness, 체스, n8n

Q2. 이 주제는 tool인가요, knowledge인가요? (domain_type)
    - tool: 소프트웨어/플랫폼/프레임워크
    - knowledge: 개념/전략/도메인 지식

Q3. [tool만] 공식 사이트 URL을 알려주세요. (official_url)
    모르면 Enter로 건너뛰기

Q4. [tool만] GitHub URL을 알려주세요. (github_url)
    모르면 Enter로 건너뛰기

Q5. [knowledge만] 참고할 자료 URL이 있나요? (reference_url)
    책, 규칙서, 위키 등. 모르면 Enter로 건너뛰기

Q6. 누가 읽을 건가요? (target_audience)
    예: DevOps 입문자, 체스 완전 초보, 투자 초보자

Q7. 얼마나 깊이 다룰 건가요? (depth_level)
    - intro: 개념 중심, 실전 최소
    - practical: 바로 쓸 수 있는 수준
    - advanced: 내부 구조 + 엣지 케이스까지

Q8. 결과물을 어디에 저장할까요? (output_path)
    기본값: ./output/{topic_name_kebab}
    Obsidian 볼트라면: 03.Resources/{topic_name}
```

총 8개 질문 (tool: 8개, knowledge: 7개). 필수 필드 미입력 시 재질문.

## wiki-memory.md 초기화 주체

- **initializer**가 wiki-config.yaml 저장 직후 빈 wiki-memory.md를 생성한다.
- 섹션 헤더만 있는 빈 구조로 시작한다.
- researcher가 첫 번째로 내용을 채운다 (핵심 용어 + 사실).

```markdown
## 확정 용어
(researcher가 채움)

## 스타일 결정사항
(writer 첫 실행 후 채움)

## 문서 간 참조 맵
(writer가 문서 생성할 때마다 추가)

## 수정 이유 로그
(reviewer가 채움)
```

## Risks

- 주제에 따라 정보량이 너무 적거나 많을 수 있음
- AI가 경쟁 제품 비교나 최신 기능에서 과장/오류를 낼 수 있음
- knowledge 유형은 공식 소스가 약해 Researcher 수집 품질이 낮을 수 있음
- 선수 지식 맵이 너무 깊어지면 진입 장벽이 오히려 높아질 수 있음

## Model Selection

`wiki-config.yaml`에서 에이전트별 모델을 지정한다. Claude Code에서는 자동 적용, 다른 런타임에서는 참고용.

```yaml
models:
  writer:       claude-opus-4-6          # 문서 품질이 전체 가치의 80% → opus
  researcher:   claude-sonnet-4-6        # 웹 판단 필요
  reviewer:     claude-sonnet-4-6        # 품질 판단 필요
  updater:      claude-sonnet-4-6        # 의존성 분석
  freshness:    claude-sonnet-4-6        # 웹 비교
  gap_finder:   claude-sonnet-4-6        # 공백 분석
  orchestrator: claude-haiku-4-5-20251001 # 단순 라우팅
  initializer:  claude-haiku-4-5-20251001 # 질문/저장만
  publisher:    claude-haiku-4-5-20251001 # git 명령만
  auditor:      claude-haiku-4-5-20251001 # 링크/구조 체크
```

**선택 기준**
- `opus` — writer만. 문서 품질이 핵심 가치
- `sonnet` — 판단/분석/웹 검색이 필요한 에이전트
- `claude-haiku-4-5-20251001` — 라우팅, 저장, 명령 실행처럼 판단 없이 처리하는 에이전트

## Memory Architecture

에이전트 간 공유 지식과 상태를 관리하는 파일 레이어.

```
wiki-config.yaml    — 설정 (영구, 변경 안 됨)
wiki-state.json     — 진행 상태 + 수정 이유 (orchestrator가 관리)
wiki-memory.md      — 에이전트 공유 지식 (용어/스타일/참조맵/수정로그)
sources.md          — researcher 원본 수집 결과
docs/{slug}.md      — writer 출력물
```

### wiki-memory.md 구조

```markdown
## 확정 용어 (writer가 매 문서 작성 시 참조)
- Pipeline: 코드 변경이 배포까지 가는 자동화 흐름

## 스타일 결정사항
- 예시는 실행 가능한 형태로 통일
- 한 줄 요약은 "~이다"로 끝내기

## 문서 간 참조 맵 (updater 파급 분석용)
- pipeline.md → [stage, trigger, cicd-basics]
- stage.md → [pipeline, step]

## 수정 이유 로그 (reviewer → writer 전달)
- stage.md: "자주 하는 실수 1개뿐 → 2개로 보강 필요"
```

### wiki-state.json 추가 필드

```json
{
  "docs_to_revise": ["stage"],
  "revision_reasons": {
    "stage": "자주 하는 실수 1개뿐 → 2개로 보강 필요"
  }
}
```

### 에이전트별 읽기/쓰기

| 에이전트 | wiki-memory.md | wiki-state.json |
|---------|---------------|----------------|
| researcher | write (용어/사실 추가) | read |
| writer | read (용어/스타일 참조) | read |
| reviewer | write (수정 이유 추가) | write (revision_reasons) |
| orchestrator | read | read/write |
| updater | read+write (참조 맵/변경 로그) | write |
| auditor / gap-finder | read | write |

### 스토리지 결정

- **MVP**: 전부 MD + JSON. 규모(8~15개 문서)와 순차 실행 구조에서 충분.
- **Phase 2 선택사항**: 참조 맵이 커지면 `wiki-links.db` (SQLite, 파일 기반) 도입 고려.
- **원격 DB 불가**: "clone → 실행" 원칙을 깨므로 MVP + Phase 2 모두 해당 없음.

## Decisions (Closed)

| 질문 | 결정 | 이유 |
|------|------|------|
| 입력 방식 | **AskUserQuestion → wiki-config.yaml** | 어떤 AI 런타임에서도 작동 |
| 에이전트 패키징 | **`.claude/agents/wiki-*.md`** | 주제 무관 공용, template repo에 포함 |
| domain_type | **tool + knowledge 통합** | Feynman 구조로 통일 커버 가능 |
| 자동화 수준 | **반자동** (orchestrator 수동 호출) | 위키 생성 작업에 완전 자동 루프 불필요 |
| 발행 방식 | **GitHub Markdown** (MVP) | 별도 호스팅 없이 GitHub 네이티브 렌더링 |
| VitePress | **Phase 2 선택사항** | MVP에서 필수 아님 |
| state 관리 | **wiki-state.json** | 중단 후 재실행 시 이어서 진행 가능 |
| output_path | **wiki-config.yaml에서 지정** | 볼트 안/독립 폴더 모두 지원, 배포 대상 무관 |
| 모델 설정 | **wiki-config.yaml `models:` 섹션** | Claude Code 자동 적용, 다른 런타임 참고용 |
| 다중 런타임 지원 | **`.claude/agents/` + `prompts/` 이중 제공** | Claude Code 자동 / 나머지 수동 참조 |
| 메모리 스토리지 | **MD + JSON (MVP)** | 규모/순차 실행에 충분, clone → 실행 원칙 유지 |
| 참조 맵 DB | **Phase 2 선택사항 SQLite** | 문서 수 증가 시만 도입, 원격 DB 불가 |
