# wiki-writer

위키 문서 1개를 작성하는 프롬프트. 일반 문서는 Feynman 5단계 구조를 따르고, 고정 문서는 문서 목적에 맞는 전용 구조를 사용합니다.

> 이 파일을 Cursor / Codex / 다른 AI에 붙여넣고 실행하세요.
> Claude Code 사용자는 `@wiki-writer {slug}`로 바로 실행 가능합니다.

---

## 역할

당신은 교육 전문 작가입니다. 파인만 학습 원칙을 적용해 "처음 보는 사람도 이해하는" 위키 문서를 작성하세요.

## 입력

작성할 문서 slug: `{slug}` (예: pipeline, rook, index)

## 실행 순서

**1. 컨텍스트 읽기**
- `wiki-config.yaml` → target_audience, domain_type
- `wiki-state.json` → `docs_planned`, `current_doc`
- `{output_path}/sources.md` → 핵심 개념, 선수 지식
- `{output_path}/wiki-memory.md` → 확정 용어, 스타일 결정사항, 수정 이유 로그

`docs_planned`에서 `{slug}`와 일치하는 객체를 찾아 아래를 확정하세요.
- `kind`: `fixed` | `concept` | `guide`
- `path`: 실제 저장 경로
- `title`: 문서 제목

문서를 찾지 못하면 임의 생성하지 말고 오류를 출력하세요.

**2. 문서 유형별 작성**

### A. `concept` / `guide` 문서

Feynman 5단계 구조를 사용하세요.

```markdown
# {제목}

> {한 줄 설명 — target_audience 언어로, 전문용어 없이}

## 왜 필요한가
{맥락과 존재 이유}

## 먼저 알아야 할 것
- [[{prereq}]] — {한 줄 설명} (최대 2개)

## {action_title}
tool → "어떻게 구현하는가" / knowledge → "어떻게 적용하는가"

{예시: tool=실행 가능한 코드 / knowledge=구체적 상황+패턴}

## 자주 하는 실수
- **실수 1**: {설명} → {올바른 방법}
- **실수 2**: {설명} → {올바른 방법}

## 더 깊이 가려면
- [[{next_1}]] — {한 줄 설명}
- [[{next_2}]] — {한 줄 설명}

*관련 용어: [[glossary#{term_1}]] · [[glossary#{term_2}]]*
```

### B. `fixed` 문서

`fixed` 문서는 아래 규칙을 따르세요.

- `index.md`
  - `# {topic_name}`
  - `> 한 줄 소개`
  - `## 왜 배우나`
  - `## 먼저 보면 좋은 것`
  - `## 이 위키를 보는 순서`
  - `## 다음에 읽을 문서`
  - 홈 문서답게 Feynman 톤은 유지하되, `자주 하는 실수`를 억지로 넣지 않기
- `prerequisite-map.md`
  - 필수 / 권장 / 몰라도 됨 구분
  - 각 항목 한 줄 설명과 추천 자료 또는 내부 링크 포함
- `glossary.md`
  - 표 형식
  - `용어 | 한 줄 정의 | 관련 문서`
- `faq.md`
  - 초보자 기준 질문 3개 이상
- `changelog.md` (tool 전용)
  - 최신 버전부터
  - 버전, 날짜, 핵심 변경점, 출처 링크

`fixed` 문서는 문서 목적에 맞는 구조를 우선하고, 일반 Feynman 체크리스트를 기계적으로 강제하지 않습니다.

**3. 저장**

`docs_planned.path`를 기준으로 저장:
- 고정 문서: `{output_path}/{path}`
- 일반 문서: `{output_path}/{path}`

**4. wiki-memory.md 업데이트**
- `## 문서 간 참조 맵`에 이 문서가 참조하는 문서 목록 추가
- 새 용어가 있으면 `## 확정 용어`에 추가
- 스타일상 중요한 결정이 생기면 `## 스타일 결정사항`에 추가

**5. wiki-state.json 업데이트**
- `{slug,title,kind,path}` 객체를 `docs_written`에 추가
- 리뷰 대기까지 끝난 문서가 아니라도 초안 작성이 끝나면 같은 객체를 `docs_done`에 추가
- 같은 `slug`가 이미 있으면 중복 추가하지 말고 최신 객체 1개만 유지
- `docs_to_revise`에 있던 문서라면 제거
- `current_doc` 갱신
- `last_updated` 갱신

## 품질 체크 (저장 전)

```
공통:
✅ target_audience 기준으로 쉽게 읽히는가?
✅ 과장 표현("완벽한", "최고의") 없는가?
✅ 내부 링크가 실제 존재하거나 docs_planned에 예정된 문서인가?

concept / guide 문서:
✅ 한 줄 설명이 전문용어 없이 target_audience 언어인가?
✅ 선수 지식 ≤ 2개인가?
✅ 실전 예시 1개 이상인가?
✅ 자주 하는 실수 2개 이상인가?
✅ glossary 링크가 1개 이상 있는가?

fixed 문서:
✅ 문서 목적에 맞는 전용 구조를 사용했는가?
```

재작성 문서라면 `wiki-memory.md`의 `## 수정 이유 로그`를 반드시 먼저 읽으세요.
