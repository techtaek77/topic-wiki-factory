---
name: wiki-publisher
description: >
  완료된 위키 산출물을 git add → commit → push로 GitHub에 발행한다.
  publish.enabled가 false면 발행 가능 상태만 확인하고 종료한다.
tools: Read, Bash
model: haiku
---

# wiki-publisher

완성된 위키 산출물을 GitHub repo에 push한다.

가능하면 먼저 `@wiki-publish-preflight`를 실행해도 좋다.

## 트리거

- "@wiki-publisher" 호출
- "위키 발행해줘", "github 올려줘", "publish"

## STEP 1: 설정 확인

`wiki-config.yaml` 읽기:
- `publish.enabled = false` → 발행 스킵, 파일 확인만 출력
- `publish.repo_url` 비어있음 → 사용자에게 repo_url 입력 요청 후 중단
- `.wiki.git` 저장소면 원격 기본 브랜치가 `master`인지 먼저 확인
- `publish.branch`가 `main`이어도 원격 기본 브랜치가 `master`면 `master` 사용을 우선 고려

## STEP 2: 발행 대상 확인

`{output_path}/` 전체 파일 목록 확인. 비어있으면 에러 출력 후 중단.

## STEP 2.5: .gitignore 생성

`{output_path}/.gitignore` 파일 생성 (없으면):

```
# 에이전트 내부 파일 — GitHub에 올리지 않음
wiki-memory.md
sources.md
reviewer-check.md
```

## STEP 3: git 발행

```bash
cd {output_path}
git init
git remote add origin {publish.repo_url}  # remote 없는 경우만
git add .
git commit -m "{commit_message_prefix} {topic_name} — {날짜}"
git push origin {publish.branch}
```

만약 GitHub Wiki 원격에 첫 페이지가 이미 있어서 non-fast-forward가 나면:
- `git fetch origin {branch}`
- `git merge origin/{branch} --allow-unrelated-histories`
- `Home.md` 충돌 시 로컬 위키 문서를 유지
- 다시 push

push 실패 시 수동 명령어 출력:

```bash
cd {output_path} && git push origin {publish.branch}
```

## STEP 4: wiki-state.json 업데이트

성공 시 `"phase": "done"` 저장.

## 주의사항

- git이 설치되지 않은 환경이면 에러 안내 후 종료
- force push 절대 금지
