---
name: wiki-freshness
description: >
  tool 유형 위키 전용. 공식 사이트와 GitHub 릴리즈를 현재 문서와 비교해
  업데이트 필요 문서 목록과 버전 차이 요약을 출력한다.
tools: Read, Write, WebFetch, WebSearch
model: sonnet
---

# wiki-freshness

tool 위키의 최신성을 주기적으로 점검한다. knowledge 유형 위키에는 실행하지 않는다.

## 트리거

- "@wiki-freshness" 호출
- "최신 버전 확인해줘", "릴리즈 확인", "freshness check"

## STEP 1: 설정 확인

`wiki-config.yaml` 읽기.
`domain_type != "tool"` → 종료.

## STEP 2: 최신 버전 정보 수집

- `official_url` 방문 → 최신 버전 / 릴리즈 날짜
- `{github_url}/releases` 방문 → 최신 릴리즈 태그 + 주요 변경사항
- 실패 시 웹 검색: `{topic_name} latest release changelog`

## STEP 3: 현재 문서와 비교

`{output_path}/changelog.md` 읽기 → 마지막 기록 버전과 최신 버전 비교.

영향도:
- HIGH: 기존 docs의 핵심 동작/API가 바뀐 경우
- MID: 새 기능 추가로 보완 필요
- LOW: 마이너 업데이트

## STEP 4: 업데이트 후보 출력

docs_to_revise에 자동 추가하지 않고 후보만 출력한다.

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
