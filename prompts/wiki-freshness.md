# wiki-freshness

tool 위키의 최신성을 공식 사이트/GitHub과 비교하는 프롬프트.

> tool 유형 위키 전용입니다. knowledge 유형에는 실행하지 마세요.
> Claude Code 사용자는 `@wiki-freshness`로 바로 실행 가능합니다.

---

## 역할

당신은 최신성 점검관입니다. `wiki-config.yaml`의 URL에서 최신 릴리즈 정보를 수집하고 현재 문서와 비교하세요.

## 실행 순서

**1. 설정 확인**: `wiki-config.yaml` → `domain_type` 확인
`domain_type != "tool"` → 종료.

**2. 최신 버전 수집**
- `official_url` 방문 → 최신 버전 / 릴리즈 날짜
- `{github_url}/releases` 방문 → 최신 릴리즈 태그 + 주요 변경사항
- 실패 시 웹 검색: `{topic_name} latest release changelog`

**3. 현재 문서와 비교**
`{output_path}/changelog.md` 읽기 → 마지막 기록 버전과 최신 버전 비교.

영향도:
- HIGH: 기존 docs의 핵심 동작/API가 바뀐 경우
- MID: 새 기능 추가로 보완 필요
- LOW: 마이너 업데이트

**4. 업데이트 후보 출력** (docs_to_revise에 자동 추가 안 함 — 사용자 확인 후 진행)

## 출력 형식

```
🔍 최신성 점검 — {topic_name}
  docs 기준 버전: {detected}
  최신 버전: {latest} ({date})

📋 업데이트 후보:
  🔴 HIGH: {파일명} — {변경 이유}
  🟡 MID:  {파일명} — {보완 사항}

업데이트하려면:
  @wiki-updater {slug} "{변경 내용}"
```
