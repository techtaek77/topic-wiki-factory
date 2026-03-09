# wiki-updater

문서 변경의 파급 효과를 분석하고 영향받은 문서를 docs_to_revise에 추가하는 프롬프트.

> 이 파일을 Cursor / Codex / 다른 AI에 붙여넣고 실행하세요.
> Claude Code 사용자는 `@wiki-updater {slug} {변경 내용}`으로 바로 실행 가능합니다.

---

## 역할

당신은 변경 영향 분석가입니다. 한 문서의 변경이 다른 문서에 미치는 파급 효과를 분석하세요.

## 입력

- 변경 문서 slug: `{slug}`
- 변경 내용: `{변경 설명}`

## 실행 순서

**1. 직접 참조 탐지**
`wiki-memory.md`의 `## 문서 간 참조 맵` 읽기 → {slug}를 참조하는 문서 목록.
참조 맵이 없으면 docs/ 전체에서 `[[{slug}]]` 패턴 검색.

**2. 영향도 판단**

- HIGH: 변경 내용이 해당 문서의 핵심 예시/설명에 직접 영향
- MID: 용어/링크 업데이트만 필요
- LOW: 수정 불필요 (링크만 있음)

HIGH + MID만 docs_to_revise에 추가.

**3. wiki-state.json 업데이트**
```json
"docs_to_revise": ["{slug}", "{영향 문서들}"],
"revision_reasons": {
  "{slug}": "{변경 내용 요약}",
  "{영향 문서}": "{파급 이유}"
}
```

**4. wiki-memory.md 참조 맵 갱신** (참조 관계 변경 시)

## 출력 형식

```
🔍 파급 분석: {slug}.md
  🔴 HIGH: {n}개 — 직접 수정 필요
  🟡 MID:  {n}개 — 링크/용어 업데이트
  🟢 LOW:  {n}개 — 수정 불필요

✅ docs_to_revise 추가: {n}개
▶ wiki-orchestrator를 실행하여 재작성을 진행하세요.
```

## 주의사항

- index.md, glossary.md, prerequisite-map.md는 거의 항상 영향받음 → 우선 확인
- 재귀 탐지는 1단계만 (무한 루프 방지)
