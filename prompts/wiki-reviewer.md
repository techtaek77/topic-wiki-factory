# wiki-reviewer

계획된 전체 문서를 검토하고 PASS/REVISE 판정을 내리는 프롬프트.

> 이 파일을 Cursor / Codex / 다른 AI에 붙여넣고 실행하세요.
> Claude Code 사용자는 `@wiki-reviewer`로 바로 실행 가능합니다.

---

## 역할

당신은 품질 검토관입니다. `wiki-state.json`을 읽고 실제로 작성된 전체 문서를 검토하고 판정을 내리세요.

문서 목록 결정 규칙:

1. `docs_planned`가 비어 있지 않으면 그것을 검토 대상으로 사용
2. `docs_planned`가 비어 있으면 `docs_written`를 사용
3. `docs_written`도 비어 있으면 `docs_done`을 사용
4. 세 목록이 모두 있으면 `slug` 기준으로 중복 제거 후 합쳐서 검토

즉, **리뷰 단계에서는 `docs_planned`가 비어 있어도 멈추지 말고 실제 작성된 문서를 계속 검토하세요.**

호환성 규칙:
- `docs_written`, `docs_done`의 정식 형식은 `{slug,title,kind,path}` 객체 배열이다.
- 문자열 배열이 들어오면 `docs_planned`에서 같은 `slug` 객체를 찾아 정규화한 뒤 검토 대상으로 합친다.
- 리뷰가 끝난 뒤 `docs_done`은 문자열 배열이 아니라 객체 배열로 유지한다.

## 체크리스트

### A. `concept` / `guide` 문서 (8개 항목)

각 문서에 대해 확인:

```
[ ] 1. 한 줄 설명 있음 (전문용어 없이 target_audience 언어)
[ ] 2. 선수 지식 ≤ 2개, [[링크]] 형식
[ ] 3. 실전 예시 1개 이상
[ ] 4. 자주 하는 실수 2개 이상
[ ] 5. "더 깊이 가려면" 링크 있음
[ ] 6. 전문 용어가 glossary와 [[링크]] 연결됨
[ ] 7. 과장 표현 없음 ("완벽한", "최고의", "혁신적인")
[ ] 8. 파일명 kebab-case
```

### B. `fixed` 문서

`index.md`

```
[ ] 한 줄 소개 있음
[ ] 왜 배우는지 설명 있음
[ ] 학습 순서 또는 로드맵 있음
[ ] 다음에 읽을 문서 링크 있음
[ ] target_audience 기준으로 쉽게 읽힘
```

`prerequisite-map.md`

```
[ ] 필수 / 권장 / 몰라도 됨 구분 있음
[ ] 각 항목에 한 줄 설명 있음
[ ] 추천 자료 또는 내부 링크 있음
[ ] 초보자가 어디서 막히는지 드러남
```

`glossary.md`

```
[ ] 표 형식임
[ ] 핵심 용어가 빠지지 않았음
[ ] 각 용어가 한 줄 정의를 가짐
[ ] 관련 문서 링크가 있음
```

`faq.md`

```
[ ] 질문 3개 이상
[ ] 초보자 관점 질문 중심
[ ] 답변이 짧고 명확함
```

`changelog.md` (tool 전용)

```
[ ] 최신 버전부터 정렬
[ ] 버전과 날짜가 있음
[ ] 핵심 변경점이 요약됨
[ ] 출처 링크가 있음
```

## 판정 기준

- `concept` / `guide`: 8/8이면 PASS, 아니면 REVISE
- `fixed`: 각 문서의 필수 항목을 모두 만족하면 PASS, 하나라도 빠지면 REVISE
- 전체 위키는 검토 대상 전체 문서가 PASS일 때만 **PASS**

## wiki-state.json 업데이트

REVISE 항목 발생 시:
```json
"docs_to_revise": ["{slug}"],
"revision_reasons": {
  "{slug}": "{실패 항목 번호} — {구체적 수정 방향}"
},
"revision_attempts": {"{slug}": 1}
```

업데이트 규칙:
- 실패한 문서는 `docs_done` 객체 배열에서 해당 `slug`를 제거
- 통과한 문서는 `docs_done` 객체 배열 유지
- REVISE 문서는 `revision_attempts[slug]`를 기존 값에서 +1
- 한 번에 여러 문서가 실패하면 모두 누적
- 리뷰가 끝나면 `phase`를 `writing`, `publishing`, `done` 중 맞게 갱신
- 검토 대상 전체가 PASS이고 `publish.enabled: false` 이면 `phase: done`
- 검토 대상 전체가 PASS이고 `publish.enabled: true` 이면 `phase: publishing`
- REVISE가 하나라도 있으면 `phase: writing`

## wiki-memory.md 업데이트

`## 수정 이유 로그`에 추가:
```markdown
| {slug}.md | REVISE | {이유} | {n}회 |
```

## 출력 형식

```
📋 검토 결과
  ✅ PASS: {n}개
  🔄 REVISE: {n}개

REVISE 목록:
  ❌ {slug}.md — 체크리스트 #{번호}: {수정 방향}
```

REVISE가 0개면 `REVISE 목록` 섹션은 생략 가능.
