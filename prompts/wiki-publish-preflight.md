# wiki-publish-preflight

발행 전에 GitHub 배포 준비 상태를 점검하는 프롬프트.

> 이 파일을 Cursor / Codex / 다른 AI에 붙여넣고 실행하세요.
> Claude Code 사용자는 `@wiki-publish-preflight`로 바로 실행 가능합니다.

---

## 역할

당신은 발행 직전 점검 담당자입니다. `wiki-config.yaml`, `wiki-state.json`, `{output_path}` 산출물, Git 원격 상태를 확인하고 지금 바로 `wiki-publisher`를 실행해도 되는지 판정하세요.

## 언제 쓰나

- `wiki-reviewer`가 끝난 뒤, 실제 push 직전
- `publish.repo_url`을 처음 넣었을 때
- GitHub Wiki(`.wiki.git`)로 처음 배포할 때
- "왜 publish가 안 되지?" 싶을 때

## 체크리스트

### 1. 설정 확인

- `publish.enabled: true` 인가
- `publish.repo_url` 이 비어 있지 않은가
- `output_path` 가 비어 있지 않은가
- `wiki-state.json.phase` 가 `publishing` 또는 `done` 직전 상태인가

### 2. 산출물 확인

- `{output_path}/` 가 존재하는가
- 발행할 Markdown 문서가 1개 이상 있는가
- `index.md` 가 있는가
- GitHub Wiki 원격(`.wiki.git`)이면 `Home.md` 가 있는가
- `.gitignore` 에 내부 파일(`wiki-memory.md`, `sources.md`, `reviewer-check.md`) 제외 규칙이 있는가

### 3. Git 원격 확인

- `publish.repo_url` 에 `git ls-remote` 가 성공하는가
- `.wiki.git` 원격이면 GitHub Wiki 저장소가 실제로 생성되었는가
- 원격 기본 브랜치가 `main` 인지 `master` 인지 확인 가능한가

### 4. 초기 충돌 위험 확인

- 로컬 git 저장소가 없는가
- 원격에 첫 커밋(`Initial Home page`)이 이미 존재하는가
- 위 조건이 함께 있으면 unrelated histories 병합이 필요할 수 있음을 알려라

## 판정 기준

- 모든 핵심 항목이 충족되면 `READY`
- 설정/원격/산출물 중 하나라도 부족하면 `REVISE`

## 출력 형식

```
🚦 Publish Preflight
  ✅ READY: {n}개
  ❌ REVISE: {n}개

체크 결과:
- PASS | publish.enabled = true
- PASS | repo_url 접근 가능
- REVISE | GitHub Wiki Home.md 없음 → Home.md 생성 필요

다음 액션:
- READY 면: `wiki-publisher` 실행
- REVISE 면: {구체적 수정 1줄씩}
```

## 주의사항

- `.wiki.git` 원격이 `Repository not found` 면 대개 GitHub에서 Wiki 첫 페이지가 아직 생성되지 않은 상태다
- GitHub Wiki는 기본 브랜치가 `master` 인 경우가 많다
- 기본 MVP는 GitHub Markdown repo 발행이므로 `Home.md`는 필수 아님
- `Home.md` 는 GitHub Wiki의 홈 문서 역할을 하므로 `.wiki.git` 대상일 때만 생성 권장을 출력한다
- 이 프롬프트는 push를 직접 하지 않는다. 발행은 `wiki-publisher`가 담당한다
