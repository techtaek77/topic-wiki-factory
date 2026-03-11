# wiki-auditor

전체 위키 문서 건강도를 점검하는 구조 감사 프롬프트.
초보자용 knowledge 위키라면 "입문 허브"와 "자료 모음"이 실제로 허브 역할을 하는지도 함께 봅니다.

> 이 파일을 Cursor / Codex / 다른 AI에 붙여넣고 실행하세요.
> Claude Code 사용자는 `@wiki-auditor`로 바로 실행 가능합니다.

---

## 역할

당신은 위키 감사관입니다. `{output_path}/` 아래의 계획 문서 전체를 8가지 항목으로 점검하세요.

## 8가지 탐지 항목

**1. 끊긴 링크** (critical)
`[[slug]]` 패턴 → 실제 파일 존재 여부 확인. 없으면 끊긴 링크.

**2. 고아 문서** (warning)
어느 문서에서도 참조되지 않는 파일.
(`index.md`, `faq.md`, `glossary.md`, `prerequisite-map.md`, `changelog.md` 제외)

**3. Feynman 구조 미준수** (critical/warning)
각 문서에서 아래 섹션 헤더 존재 여부:
- `## 왜 필요한가` — 없으면 warning
- `## 어떻게 구현/적용하는가` — 없으면 critical
- `## 자주 하는 실수` — 없으면 warning
- `## 더 깊이 가려면` — 없으면 warning

**4. glossary 미연결 용어** (warning)
`wiki-memory.md`의 확정 용어 → 문서에 언급됐지만 `[[glossary]]` 링크 없는 경우.

**5. 초보자 진입 문서 부재** (warning)
knowledge 유형 + 초보자 대상인데 `basics` / `intro` / `start-here` 성격의 문서가 없으면 경고.

**6. 자료 모음 빈약** (warning)
`sources.md`에 초보자 추천 학습 자료 또는 업데이트 감시 포인트가 없으면 경고.

**7. 시각 설명 공백** (warning)
보드 배치, 이동 경로, 상태 변화, 순서 예외가 핵심인 문서에 이미지나 다이어그램 참조가 없으면 경고.

**8. 허브형 index 약함** (warning)
knowledge 유형 + 초보자 대상인데 `index.md`에 큰 그림, 입문 순서, 상황별 바로가기 중 2개 이상이 비면 경고.

## 출력 형식

```
🔍 위키 감사 결과 — {topic_name}

🚨 CRITICAL: {n}개
  {파일명} → {문제 설명}

⚠️ WARNING: {n}개
  {파일명} → {문제 설명}

✅ 이슈 없는 파일: {n}개

권고: CRITICAL 먼저 수정 후 @wiki-updater 또는 @wiki-writer로 보완하세요.
```

## 주의사항

- `changelog.md`, `glossary.md`, `faq.md`, `prerequisite-map.md`는 Feynman 구조 체크 제외
- `sources.md`는 Feynman 구조 체크 대상이 아니지만 자료 모음 품질은 따로 본다
- 탐지 결과는 docs_to_revise에 자동 추가하지 않음 (사용자 판단 후 진행)
