# codex-101

`Codex 101`은 OpenAI Codex 같은 코딩 에이전트를 처음 써보는 사람이
"폴더를 열고 -> 브랜치를 따고 -> 첫 요청을 넣고 -> diff를 보고 -> 커밋/푸시하는 흐름"
을 감 잡도록 만든 tool 유형 샘플 위키다.

## What this example shows

- `wiki-config.yaml` - 어떤 입력으로 시작했는지
- `wiki-state.json` - 어떤 문서들이 planned/written/done 상태로 관리되는지
- `output/` - 실제 생성 결과가 어떤 모양과 톤으로 나오는지
- `output/changelog.md` - tool 유형 위키에서 변경 이력을 어떻게 보여주는지
- `output/questions.md` - 읽다가 막힌 질문을 어떻게 다시 위키 보강으로 연결하는지

## Notes

- 이 예시는 `intro` 깊이의 작은 샘플이라 핵심 문서만 넣었다.
- 제품 세부 UI보다 작업 흐름과 협업 기본기에 더 초점을 맞췄다.
- 실제 개인 위키를 만들 때는 `output_path`만 바꿔 바로 다른 폴더로 내보낼 수 있다.
