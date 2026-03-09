# wiki-publisher

완료된 위키 산출물을 GitHub에 push하는 프롬프트.

> 이 파일을 Cursor / Codex / 다른 AI에 붙여넣고 실행하세요.
> Claude Code 사용자는 `@wiki-publisher`로 바로 실행 가능합니다.

---

## 역할

당신은 발행 담당자입니다. `wiki-config.yaml`의 publish 설정을 읽고 GitHub에 push하세요.

발행 전에 가능하면 먼저 `wiki-publish-preflight`를 실행해 배포 준비 상태를 확인하세요.

## 실행 순서

**1. 설정 확인**: `wiki-config.yaml` → `publish.enabled`, `publish.repo_url`

`publish.enabled: false` → 발행 스킵, 파일 목록만 출력 후 종료.
`publish.repo_url` 비어있음 → 사용자에게 입력 요청 후 중단.

브랜치 확인 규칙:
- `publish.branch` 값을 그대로 사용
- 단, GitHub Wiki 저장소(`.wiki.git`)는 기본 브랜치가 `master`인 경우가 많다
- 사용자가 `.wiki.git`에 발행하는데 `publish.branch: main`이면, 먼저 원격 기본 브랜치를 확인하고 필요하면 `master` 사용을 권장하거나 그대로 push 가능한지 확인한다

**2. 발행 대상 확인**: `{output_path}/` 전체 파일 목록 확인

GitHub Wiki 원격(`.wiki.git`)이면:
- `Home.md` 가 없으면 생성 권장 또는 생성 후 진행
- 원격 기본 브랜치가 `master` 일 가능성을 먼저 확인

일반 GitHub Markdown repo면:
- `index.md`를 홈 문서로 간주하고 `Home.md`는 만들지 않는다

**2.5. .gitignore 생성** (`{output_path}/.gitignore` 없으면):
```
# 에이전트 내부 파일
wiki-memory.md
sources.md
reviewer-check.md
```

**3. git 발행**

```bash
cd {output_path}
git init  # repo 없는 경우
git remote add origin {repo_url}  # remote 없는 경우
git add .
git commit -m "{commit_message_prefix} {topic_name} — {날짜}"
git push origin {branch}
```

GitHub Wiki 원격에 이미 첫 페이지가 있어 non-fast-forward가 나면:
- 먼저 원격 브랜치를 fetch
- `--allow-unrelated-histories`로 병합
- 자동 생성된 기본 `Home.md`와 로컬 `Home.md`가 충돌하면 로컬 문서 버전을 유지
- 그 다음 다시 push

push 실패 시 → 에러 메시지 + 수동 명령어 출력:
```bash
cd {output_path} && git push origin {branch}
```

**4. wiki-state.json 업데이트**: 성공 시 `"phase": "done"` 저장

## 주의사항

- force push 절대 금지
- git 미설치 환경이면 에러 안내 후 종료
