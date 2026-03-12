# hitl-intro

사람 확인이 필요한 AI 워크플로우를 처음 설계하는 사람을 위한 knowledge 유형 샘플 위키다.
자동화만 밀어붙이다가 사고 나는 지점과, 어디서 사람 확인을 끼워야 하는지 감을 잡는 데 초점을 둔다.

## What this example shows

- `wiki-config.yaml` - 어떤 입력으로 시작했는지
- `wiki-state.json` - 어떤 문서가 planned / written / done 상태인지
- `output/` - HITL 입문 위키가 실제로 어떤 형태로 나오는지
- `output/docs/` - 체크포인트 설계, 승인 UX, 자동화 경계 같은 개념 문서가 어떻게 연결되는지
- `reviewer-check.md` - 공개 예시 기준으로 어떤 점을 PASS로 봤는지
- `strict-validation.md` - 범위, IA, 고정 문서, 일반 문서를 어떻게 검수했는지

## Notes

- 이 예시는 `intro` 깊이의 knowledge 샘플이다.
- 제품 문서가 아니라 개념 위키 예시라서 changelog 대신 핵심 개념 연결을 더 강조했다.
- 현재 메인 README에 나오는 `hitl.confirm_*` 설정과 연결해서 읽기 좋다.
