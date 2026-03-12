# Topic Wiki Factory

[English](README.en.md)

어떤 주제든 처음 배우는 사람이 책처럼 따라 읽을 수 있는 입문형 위키를 30분 안에 만드는 AI 에이전트 템플릿이다.

> "이게 뭔지" -> "왜 중요한지" -> "무엇부터 알아야 하는지" -> "어떻게 쓰는지"
> 순서로 읽히게 해서, 처음 보는 사람도 길을 잃지 않게 만든다.

결과물은 검색용 문서 묶음보다 "허브형 입문 위키"에 가깝다.
`index.md`가 홈이 되어 큰 그림, 5분 요약, 읽기 순서, 규칙 요약, 외부 자료를 한 번에 안내한다.

## 이 템플릿이 만드는 것

- 어디부터 읽어야 할지 바로 보이는 허브형 홈 문서
- "왜 이걸 알아야 하는지"부터 잡아 주는 초보자용 입문 문서
- `sources.md`, SVG 설명 자료, 업데이트 포인트까지 포함한 살아 있는 학습 위키

잘 맞는 주제:
- `Harness` 같은 제품/플랫폼
- `체스` 같은 개념/규칙
- `n8n` 같은 도구/자동화

![Example output preview](assets/readme-preview.svg)

## 예시 보기

[examples/README.md](examples/README.md)에서 실제 결과물을 바로 볼 수 있다.
지금은 `examples/chess-intro/`, `examples/codex-101/`, `examples/hitl-intro/` 세 개가 들어 있다.

`examples/chess-intro/`는 이런 흐름을 보여 준다.

- 허브형 홈 문서
- 초보자 입문 가이드
- 캐슬링 / 앙파상 / 프로모션 같은 특수 규칙의 SVG 설명
- `sources.md` 기반 자료 모음 + 업데이트 감시 포인트

`examples/hitl-intro/`는 사람 확인 단계가 왜 필요한지, 어떤 체크포인트가 좋은지 같은 개념형 샘플을 보여 준다.

## 시작하기

빠른 시작은 이렇다.

1. `wiki-initializer`로 주제와 출력 경로를 잡는다.
2. `wiki-orchestrator`로 조사, 작성, 검토를 진행한다.
3. 필요할 때 `wiki-updater`, `wiki-auditor`, `wiki-publisher`를 돌린다.

### 방법 1. GitHub 템플릿으로 시작

1. GitHub에서 `Use this template`를 눌러 새 저장소를 만든다.
2. 새 저장소를 로컬에 클론한다.
3. Claude Code 또는 원하는 AI 런타임에서 아래 흐름을 실행한다.

### 방법 2. 직접 클론

```bash
git clone https://github.com/techtaek77/topic-wiki-factory my-wiki
cd my-wiki
```

### 1. 초기화

Claude Code 사용 시:

```text
@wiki-initializer
```

Cursor / Codex / 기타 사용 시:
- `prompts/wiki-initializer.md`를 열어 그대로 붙여넣는다.

initializer는 11개 질문으로 주제, 제외 범위, 로컬 자료, 출력 경로를 정하고 `wiki-config.yaml`, `wiki-state.json`, `{output_path}/wiki-memory.md`를 초기화한다.

### 2. 위키 생성

```text
@wiki-orchestrator
```

orchestrator는 `wiki-state.json`을 읽고 다음 작업을 정한다.
중간에 멈췄다가 다시 실행해도 이미 끝난 문서는 다시 쓰지 않는다.
기본값은 병렬 writer가 아니라 순차 자동 진행이다.
문서형 작업은 속도보다 상태 안정성이 중요해서다.

사람 확인을 줄이고 자동으로 더 빨리 돌리고 싶다면 `hitl.confirm_scope_after_research`, `hitl.confirm_ia_before_writing`을 둘 다 `false`로 두면 된다.

```yaml
hitl:
  confirm_scope_after_research: false
  confirm_ia_before_writing: false
```

`hitl` 확인을 켜 둔 수동 흐름의 기본 순서는 아래와 같다.

1. `wiki-initializer`
2. `wiki-researcher`
3. `wiki-orchestrator` -> scope 확인
4. `wiki-orchestrator` -> IA 확인
5. `wiki-writer {slug}` 반복
6. `wiki-reviewer`

## 결과물 원칙

- knowledge 위키: 들어가면 길이 보이는 허브형 입문 위키
- tool 위키: 빠른 시작과 changelog까지 포함한 실전 문서 허브
- 특수 규칙 / 예외 / 공간 설명 문서: 텍스트만 버티지 말고 SVG 같은 시각 자료 우선
- `sources.md`: 단순 출처 메모가 아니라 자료 모음 + 필수 학습 축 + 업데이트 감시 포인트

## 운영과 업데이트

이 프로젝트는 "한 번 만들고 끝"보다 "살아 있는 위키"에 가깝게 쓰는 편이 좋다.
사람도 한 번 배우고 멈추면 굳듯이, 위키도 업데이트 루프가 없으면 금방 낡는다.

추천 유지보수 루프:

1. 외부 기준이나 추천 자료가 바뀐 것 같으면 `wiki-researcher`
2. 특정 문서 내용이 바뀌면 `wiki-updater {slug} "{변경 내용}"`
3. 빈 구간이 생겼는지 보면 `wiki-gap-finder`
4. 링크, 허브 문서, 자료 모음 상태를 보면 `wiki-auditor`
5. 수정 대상이 잡히면 `wiki-orchestrator`

특히 knowledge 위키는 초보자용 입문 허브 가이드(`basics`)와 `sources.md`의 자료 모음 / 업데이트 감시 포인트를 같이 유지하는 흐름을 기본으로 잡는다.
보드 배치, 규칙 예외, 상태 변화처럼 글만 읽어선 잘 안 보이는 내용은 SVG 같은 시각 자료까지 함께 관리하는 쪽을 권장한다.

### 완료 후 발행

`wiki-config.yaml`에서 `publish.enabled: true`로 바꾼 뒤:

```text
@wiki-publish-preflight
@wiki-publisher
```

`wiki-publish-preflight`는 `repo_url` 누락, `.wiki.git` 대상의 `Home.md` 필요 여부, 내부 파일 ignore 규칙까지 먼저 점검한다.

### 빠른 검증

PR 전에 아래 acceptance harness를 돌리면 orchestrator 기본 흐름 12개 시나리오를 한 번에 확인할 수 있다.

```bash
python3 scripts/orchestrator_harness.py
```

## 같은 이름, 다른 의미 처리

`Harness`처럼 같은 이름이 제품명일 수도 있고 일반 개념일 수도 있는 주제는 researcher가 먼저 해석 후보를 비교한다.
그다음 확인 단계는 `hitl` 설정에 따라 달라진다.

1. researcher가 해석 후보를 비교한다.
2. `hitl.confirm_scope_after_research=true`면 orchestrator가 research 이후 범위를 사람에게 다시 확인받는다.
3. `hitl.confirm_ia_before_writing=true`면 글쓰기 전에 IA를 한 번 더 확인한다.
4. 둘 중 하나라도 `false`면 해당 단계는 사람 확인 없이 자동 진행된다.

덕분에 "말은 하네스인데 갑자기 CI/CD 문서가 튀어나오는 사고"를 줄일 수 있다.

## 폴더 구조

```text
/
├── .claude/agents/       <- Claude Code 에이전트
├── assets/               <- README용 정적 자산
├── examples/             <- 보여주기용 샘플 위키
├── prompts/              <- 타 런타임용 프롬프트
├── specs/                <- 단계별 설계 제안서
├── templates/            <- 문서 템플릿과 스키마 예시
├── CONTRIBUTING.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── README.md
├── plan.md
├── spec.md
├── wiki-config.yaml
└── wiki-state.json
```

루트의 `wiki-config.yaml`과 `wiki-state.json`은 의도적으로 빈 시작 상태로 들어 있다.
검증용 산출물은 공개 저장소에 넣지 않고, 보여주기용 예제만 `examples/` 아래에 포함한다. 실제 문서와 `docs/`, `sources.md`, `wiki-memory.md`는 첫 실행 뒤 `output_path` 아래 생성된다.

```yaml
output_path: "./output/harness"        # 독립 폴더
output_path: "03.Resources/하네스"     # Obsidian 볼트 안
output_path: "../my-chess-wiki/docs"   # 다른 repo
```

## 런타임별 실행법

| 런타임 | 실행 방법 |
|--------|---------|
| Claude Code | `@wiki-initializer` -> `@wiki-orchestrator` 반복 |
| Cursor | `prompts/wiki-*.md`를 그대로 열어 Agent/Chat 입력창에 붙여넣어 사용 |
| Codex / GPT | `prompts/wiki-*.md`를 열고 AI에 붙여넣기 |

## 에이전트 목록

| 에이전트 | 역할 | 실행 시점 |
|---------|------|---------|
| `wiki-initializer` | 설정 마법사 | 최초 1회 |
| `wiki-orchestrator` | 진행 관리 | 단계마다 반복 |
| `wiki-researcher` | 소스 수집 | orchestrator가 호출 |
| `wiki-writer` | 문서 작성 | orchestrator가 호출 |
| `wiki-reviewer` | 품질 검토 | orchestrator가 호출 |
| `wiki-publish-preflight` | 배포 전 점검 | 발행 직전 |
| `wiki-publisher` | GitHub 발행 | 완료 후 1회 |
| `wiki-updater` | 변경 파급 분석 | 내용 수정 시 |
| `wiki-auditor` | 구조 점검 | 주기적으로 |
| `wiki-freshness` | 최신성 점검 | tool 위키만 |
| `wiki-gap-finder` | 빈 구간 탐지 | 주기적으로 |

## Known Limitations

- 사실 검증을 완전 자동으로 끝내 주지는 않는다. 최종 검수는 사람이 해야 한다.
- 첫 버전은 GitHub Markdown 기준으로 설계돼 있다.
- 모든 주제에서 완벽한 IA를 자동 보장하지 않는다.
- 다국어 번역, CMS, 협업 권한 관리까지는 아직 범위 밖이다.
- 지식형 주제는 공식 소스가 약할 수 있어 research 품질 차이가 더 크다.

## 기여

기여 전에 [CONTRIBUTING.md](CONTRIBUTING.md)를 먼저 보면 편하다.
프롬프트를 바꿀 때는 `.claude/agents/`와 `prompts/`를 같이 맞춰 주는 게 핵심이다.

## 참고

- `EXPERIMENTS.md` -> 메인 / validation / narrative / agent-simplify 실험 정리
- `templates/` -> 문서 구조 예시와 스키마 상세
- `spec.md` -> 설계 문서
- `specs/parallel-writer-spec.md` -> 병렬 writer 확장 설계 (Phase 2, 아직 미구현)
- `tests/README.md` -> orchestrator acceptance harness 설명
- `plan.md` -> 개발 계획
