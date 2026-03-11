# Wiki IA Structure (Information Architecture)

> wiki-architect(orchestrator)가 새 주제를 받았을 때 사이드바와 문서 목록을 설계하는 기준.
> tool / knowledge 두 유형의 공통 뼈대와 분기 규칙을 정의한다.

---

## 공통 구조 (tool + knowledge 모두)

```
{topic}/
├── index.md              — 홈: 한 줄 소개 + 왜 배우나 + 학습 로드맵
├── prerequisite-map.md   — 선수 지식 맵: 시작 전 알아야 할 것들
├── glossary.md           — 용어집: 핵심 용어 한 줄 정의 + 링크
├── faq.md                — 자주 하는 질문
├── questions.md          — 아직 헷갈리는 질문 / 에이전트 보강 메모
├── sources.md            — researcher가 수집한 소스 + 추천 학습 자료 + 업데이트 감시 포인트
├── wiki-memory.md        — 에이전트 공유 메모 + 스코프/업데이트 메모
└── docs/
    ├── concepts/         — 핵심 개념 (What / Why 중심)
    └── guides/           — 실전 가이드 (How 중심)
```

**tool 전용 추가**
```
└── changelog.md          — 버전별 주요 변경사항 추적
```

---

## 허브형 정보구조 원칙

- 초보자용 knowledge 위키는 `index.md`가 단순 홈이 아니라 "길 안내판"이어야 한다.
- 문서는 "요약 → 어디부터 읽나 → 지금 필요한 규칙 → 더 깊게" 순으로 점프 가능해야 한다.
- 초보자가 자주 찾는 규칙/예외는 허브 문서에서 한 번에 보이게 연결한다.
- 글만으로 이해가 안 되는 규칙은 concept 문서에서 SVG/다이어그램으로 먼저 보여 준다.
- 그래도 막히는 질문은 `questions.md`에 모아 두고, 반복되면 FAQ나 개별 문서로 승격한다.

---

## 사이드바 구조

### tool 유형 사이드바

```
📖 시작하기
  - 홈 (index.md)
  - 이걸 배우기 전에 (prerequisite-map.md)
  - 빠른 시작 (docs/guides/quick-start.md)

🧠 핵심 개념
  - [개념 1]
  - [개념 2]
  - [개념 3]
  ...

🛠 실전 가이드
  - [가이드 1]
  - [가이드 2]
  ...

📚 참고
  - 용어집 (glossary.md)
  - FAQ (faq.md)
  - 변경 이력 (changelog.md)
```

### knowledge 유형 사이드바

```
📖 시작하기
  - 홈 (index.md)
  - 이걸 배우기 전에 (prerequisite-map.md)
  - 기초 이해하기 (입문 허브 guide)
  - 핵심만 빠르게 (docs/guides/quick-start.md)

🧠 기초 개념
  - [개념 1]
  - [개념 2]
  ...

⚡ 실전 패턴
  - [패턴 1]
  - [패턴 2]
  ...

📚 참고
  - 용어집 (glossary.md)
  - FAQ (faq.md)
  - 아직 헷갈리는 질문 (questions.md)
  - 자료 모음 (sources.md)
```

---

## 문서 카테고리 기준

### concepts/ — 핵심 개념 (What / Why)

| 기준 | 내용 |
|------|------|
| 목적 | "이게 뭔지" 이해 |
| 분량 | 150~250줄 |
| 예시 형태 | tool: 간단한 코드 / knowledge: 비유 + 다이어그램 |
| 개수 | 4~8개 |
| 선정 기준 | 이게 없으면 실전 가이드를 이해 못 하는 것 |

### guides/ — 실전 가이드 (How)

| 기준 | 내용 |
|------|------|
| 목적 | "이걸 어떻게 쓰는지" 실행 |
| 분량 | 200~300줄 |
| 예시 형태 | tool: 실행 가능한 코드 / knowledge: 구체적 상황 + 패턴 |
| 개수 | 3~6개 |
| 선정 기준 | 실제로 자주 하는 작업 또는 패턴 |

---

## 고정 문서 구조

### index.md

```markdown
# {topic_name}

> {한 줄 소개}

## {topic_name}가 뭐냐면
{큰 그림 2~4문장}

## 이 위키에 들어 있는 것
- {무엇을 배울 수 있는지}

## 5분 요약
1. {가장 먼저 기억할 핵심}
2. {헷갈리기 쉬운 핵심}
3. {처음 행동}

## 처음이면 여기부터 보면 된다
- [[{intro_guide_slug}]] — 큰 그림 먼저
- [[prerequisite-map]] — 선수 지식 확인
- [[quick-start]] — 가장 빠른 첫 경험

## 학습 로드맵
1. prerequisite-map → 선수 지식 확인
2. quick-start → 30분 안에 첫 경험
3. concepts/ → 핵심 개념 이해
4. guides/ → 실전 적용

## 이런 상황이면 여기부터
- 규칙부터 알고 싶다 → [[{intro_guide_slug}]]
- 바로 손으로 해 보고 싶다 → [[quick-start]]
- 자주 헷갈리는 예외를 보고 싶다 → [[{대표 concept}]]

## 자주 찾는 문서
- [[glossary]]
- [[faq]]
- [[questions]]
- [[{대표 concept}]]
- [[sources]]
```

### prerequisite-map.md

```markdown
# 시작 전에 알아야 할 것

이 위키를 보기 전에 아래 개념을 알고 있으면 훨씬 빠르게 이해할 수 있습니다.

## 필수 (모르면 막힘)
| 개념 | 한 줄 설명 | 추천 자료 |
|------|-----------|---------|
| {prereq_1} | ... | {link} |

## 권장 (알면 더 빠름)
| 개념 | 한 줄 설명 | 추천 자료 |
|------|-----------|---------|
| {prereq_2} | ... | {link} |

## 몰라도 됨
이 위키를 보면서 자연스럽게 익힐 수 있는 것들:
- {concept_a}
- {concept_b}

## 가장 짧은 학습 경로
1. {doc_a}
2. {doc_b}
3. {doc_c}
```

### glossary.md

```markdown
# 용어집

<!-- 표 형식 또는 heading 나열 형식 중 하나를 일관되게 사용 -->
| 용어 | 한 줄 정의 | 관련 문서 |
|------|-----------|---------|
| {term} | {definition} | [[{slug}]] |
```

### faq.md

```markdown
# 자주 하는 질문

## Q. {question_1}
{answer_1}

## Q. {question_2}
{answer_2}
```

### questions.md

```markdown
# 아직 헷갈리는 질문

이 문서는 "읽었는데도 아직 막히는 질문"을 모으는 곳이다.
개인 위키라면 여기 적어 두고 에이전트에게 다시 물으면 된다.

## 이렇게 물어보면 좋다

- 어디 문서를 읽다가 막혔는지
- 어떤 문장이 특히 이해가 안 갔는지
- 글보다 그림이 필요한지
- 답을 들으면 FAQ로 올릴 만한 질문인지

## 지금 답이 있는 질문

| 질문 | 먼저 볼 문서 | 메모 |
|------|-------------|------|
| {question_1} | [[faq]] | 짧은 답이 이미 있으면 여기서 연결 |

## 문서 보강 후보 질문

| 질문 | 막힌 문서 | 왜 막히는가 | 다음 액션 |
|------|----------|-------------|----------|
| {question_2} | [[{doc_slug}]] | {혼동 이유} | FAQ 추가 / SVG 보강 / 새 문서 검토 |
```

### sources.md

```markdown
# 자료 모음

## 공식 소스
| URL | 유형 | 신뢰도 | 핵심 내용 요약 |

## 보조 소스
| URL | 유형 | 신뢰도 | 핵심 내용 요약 |

## 초보자 추천 학습 자료
| 유형 | 이름 | 추천 이유 | 링크 |

## 필수 학습 축
| 축 | 왜 필요한가 | 대표 개념/문서 후보 |

## 업데이트 감시 포인트
- {무엇이 바뀌면 어느 문서를 다시 봐야 하는지}
```

### changelog.md (tool 전용)

```markdown
# 변경 이력

## {version} — {date}
- {change_1}
- {change_2}

## {version} — {date}
...
```

---

## 문서 수 기준

| depth_level | concepts | guides | 총 문서 수 |
|-------------|----------|--------|----------|
| `intro` | 4~5개 | 2~3개 | 8~10개 |
| `practical` | 5~7개 | 4~5개 | 11~14개 |
| `advanced` | 7~8개 | 5~6개 | 14~16개 |

공통 고정 문서(index, prerequisite-map, glossary, faq, questions) 5개 + tool이면 changelog 1개는 항상 포함.

`quick-start`는 guides 개수에 포함되지만 사이드바에서는 시작하기 섹션에 올려도 된다.

---

## 검증 (tool: Harness / knowledge: 체스)

### Harness 사이드바 예시

```
📖 시작하기
  - 홈
  - 이걸 배우기 전에 (CI/CD, YAML, Git)
  - 빠른 시작

🧠 핵심 개념
  - Pipeline
  - Stage
  - Step
  - Trigger
  - Service & Environment

🛠 실전 가이드
  - 첫 Pipeline 만들기
  - Approval Stage 추가하기
  - Rolling Deployment 설정하기

📚 참고
  - 용어집 / FAQ / 변경 이력
```

### 체스 사이드바 예시

```
📖 시작하기
  - 홈
  - 이걸 배우기 전에 (체스판 읽기, 기물 이름)
  - 체스는 어떻게 돌아가나
  - 핵심만 빠르게

🧠 기초 개념
  - 기물별 이동 규칙 (폰/나이트/비숍/룩/퀸/킹)
  - 체크와 체크메이트
  - 캐슬링 / 앙파상

⚡ 실전 패턴
  - 오프닝 원칙 3가지
  - 미들게임 전략
  - 기본 엔드게임 패턴

📚 참고
  - 용어집 / FAQ / 자료 모음
```

두 유형 모두 사이드바가 자연스럽다. ✅

---

## wiki-architect 사용 지침

orchestrator가 researcher 결과(sources.md)를 받은 후 아래 순서로 IA를 확정한다.

1. domain_type 확인 → tool / knowledge 분기
2. depth_level 확인 → 문서 수 범위 결정
3. sources.md에서 핵심 개념 추출 → concepts/ 문서 목록 결정
4. 자주 하는 작업/패턴 추출 → guides/ 문서 목록 결정
5. 고정 문서(index, prerequisite-map, glossary, faq, questions) + tool이면 changelog 추가
6. `quick-start`를 guides의 첫 문서로 추가
7. knowledge + 초보자 주제라면 `index`에서 바로 점프할 "입문 허브 / 빠른 시작 / 자주 찾는 예외 규칙 / 질문 보관함 / 자료 모음" 묶음 확보
8. 전체 문서 목록을 wiki-state.json의 docs_planned에 `{slug,title,kind,path}` 형식으로 저장
9. 각 문서명을 kebab-case로 변환

IA 확정 후 wiki-writer 호출 시작.
