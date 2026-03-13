# Examples

공개 저장소에는 내부 검증용 `validation/` 산출물을 넣지 않는다.
대신 여기에는 처음 보는 사람이 결과물 형태를 빠르게 이해할 수 있도록 가벼운 샘플만 둔다.

## Included examples

- [chess-intro/](chess-intro/) - knowledge 유형 입문형 위키 예시 (허브형 홈 문서, 입문 가이드, 특수 규칙 SVG, 장면형 서사 도입 포함)
- [codex-101/](codex-101/) - tool 유형 입문형 위키 예시 ([changelog.md](codex-101/output/changelog.md) 포함)
- [hitl-intro/](hitl-intro/) - knowledge 유형 개념 위키 예시 (사람 확인 체크포인트, 승인 설계, 자동화 경계 설명)

각 예시는 아래를 함께 보여준다.

- 입력 설정 `wiki-config.yaml`
- 진행 상태 `wiki-state.json`
- 생성 결과 `output/`

예를 들면:

- [chess-intro/wiki-config.yaml](chess-intro/wiki-config.yaml)
- [chess-intro/wiki-state.json](chess-intro/wiki-state.json)
- [chess-intro/output/index.md](chess-intro/output/index.md)
- [codex-101/wiki-config.yaml](codex-101/wiki-config.yaml)
- [codex-101/wiki-state.json](codex-101/wiki-state.json)
- [codex-101/output/index.md](codex-101/output/index.md)
- [hitl-intro/wiki-config.yaml](hitl-intro/wiki-config.yaml)
- [hitl-intro/wiki-state.json](hitl-intro/wiki-state.json)
- [hitl-intro/output/index.md](hitl-intro/output/index.md)
- [hitl-intro/reviewer-check.md](hitl-intro/reviewer-check.md)
- [hitl-intro/strict-validation.md](hitl-intro/strict-validation.md)

즉, "무슨 파일이 생기지?"와 "완성되면 어느 정도 길이와 톤이 나오지?"를 한 번에 볼 수 있다.
최근 샘플은 `그냥 정리된 문서`보다 `책 첫 장처럼 술술 읽히는 문체`도 함께 실험하고 있다.
