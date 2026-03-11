# Wiki Memory

## 확정 용어

| 용어 | 정의 | 첫 등장 문서 |
|------|------|--------------|
| King | 체크메이트를 당하면 게임이 끝나는 핵심 기물 | [chess-basics](docs/guides/chess-basics.md) |
| Queen | 가장 강한 기물 | [chess-basics](docs/guides/chess-basics.md) |
| Rook | 가로와 세로 방향으로 움직이는 기물 | [rook](docs/concepts/rook.md) |
| Open File | 룩이 힘을 쓰기 좋은 빈 세로줄 | [rook](docs/concepts/rook.md) |
| Checkmate | 체크를 막을 수 없는 상태 | [chess-basics](docs/guides/chess-basics.md) |
| Stalemate | 둘 수 있는 수가 없지만 체크는 아닌 상태 | [chess-basics](docs/guides/chess-basics.md) |
| Castle | 킹과 룩을 동시에 움직이는 특수 규칙 | [castle](docs/concepts/castle.md) |
| En Passant | 상대 폰의 두 칸 전진 직후에만 가능한 특수 잡기 | [en-passant](docs/concepts/en-passant.md) |
| Promotion | 폰이 끝줄에 도착했을 때 다른 기물로 승격하는 규칙 | [promotion](docs/concepts/promotion.md) |

## 업데이트 감시 포인트

- 체스처럼 규칙이 비교적 안정적인 주제도 입문 설명 방식과 추천 자료는 계속 개선 여지가 있다.
- 턴 순서 예외나 상태 변화 문서는 시각 자료 품질이 이해도에 큰 영향을 준다.
- `sources.md`의 필수 학습 축에 빈칸이 생기면 reviewing 전에 docs_planned를 다시 보강한다.

## 반복 질문 메모

| 질문 | 막힌 문서 | 다음 액션 |
|------|----------|---------|
| 앙파상은 왜 바로 다음 턴에만 되는가 | [en-passant](docs/concepts/en-passant.md) | FAQ와 questions에 반복 질문으로 유지 |
| 캐슬링은 왜 체크를 지나가면 안 되는가 | [castle](docs/concepts/castle.md) | SVG 주석 또는 FAQ 보강 후보 |

## 스타일 결정사항

- 첫 문장은 가능한 한 쉬운 비유 없이도 이해되게 쓴다.
- 규칙 설명은 짧게, 학습 순서는 명확하게 쓴다.
- 초보자용 문서는 "이게 뭔가 -> 어떻게 하는가 -> 어디서 더 배우나" 순서를 유지한다.
- 허브 문서는 "큰 그림 -> 5분 요약 -> 어디부터 읽나 -> 상황별 바로가기" 흐름을 우선한다.
- 질문 보관함은 "이미 답이 있는 질문"과 "문서 보강 후보 질문"을 나눠 적는다.
- 특수 규칙 문서는 가능하면 텍스트보다 먼저 SVG로 전후 상태를 보여 준다.

## 문서 간 참조 맵

| 문서 | 참조하는 문서들 |
|------|------------------|
| [index](index.md) | [chess-basics](docs/guides/chess-basics.md), [quick-start](docs/guides/quick-start.md), [castle](docs/concepts/castle.md), [en-passant](docs/concepts/en-passant.md), [promotion](docs/concepts/promotion.md), [rook](docs/concepts/rook.md), [faq](faq.md), [questions](questions.md), [sources](sources.md) |
| [chess-basics](docs/guides/chess-basics.md) | [quick-start](docs/guides/quick-start.md), [castle](docs/concepts/castle.md), [en-passant](docs/concepts/en-passant.md), [promotion](docs/concepts/promotion.md), [glossary](glossary.md), [faq](faq.md), [sources](sources.md) |
| [quick-start](docs/guides/quick-start.md) | [chess-basics](docs/guides/chess-basics.md), [castle](docs/concepts/castle.md), [prerequisite-map](prerequisite-map.md), [faq](faq.md) |
| [rook](docs/concepts/rook.md) | [glossary](glossary.md), [quick-start](docs/guides/quick-start.md) |
| [castle](docs/concepts/castle.md) | [quick-start](docs/guides/quick-start.md), [glossary](glossary.md), [faq](faq.md) |
| [en-passant](docs/concepts/en-passant.md) | [glossary](glossary.md), [faq](faq.md), [promotion](docs/concepts/promotion.md) |
| [promotion](docs/concepts/promotion.md) | [glossary](glossary.md), [faq](faq.md) |
| [questions](questions.md) | [faq](faq.md), [en-passant](docs/concepts/en-passant.md), [castle](docs/concepts/castle.md), [chess-basics](docs/guides/chess-basics.md) |

## 수정 이유 로그

| 문서 | 판정 | 이유 | 시도 횟수 |
|------|------|------|-----------|
| [chess-basics](docs/guides/chess-basics.md) | PASS | 초보자가 묻는 "체스가 뭔가, 어떻게 이기나, 말은 어떻게 움직이나"를 한 문서에서 먼저 해결함 | 1 |
| [castle](docs/concepts/castle.md) | PASS | 텍스트로 헷갈리는 특수 규칙을 전후 상태 SVG로 보여 줌 | 1 |
| [en-passant](docs/concepts/en-passant.md) | PASS | 가장 헷갈리는 규칙을 시각 자료 중심으로 설명함 | 1 |
| [promotion](docs/concepts/promotion.md) | PASS | 폰 승격 순간과 결과를 그림으로 보여 줌 | 1 |
| [sources](sources.md) | PASS | 공식 규칙, 사이트, 유튜브 채널을 함께 보여 줘 입문용 허브 역할을 강화함 | 1 |
| [rook](docs/concepts/rook.md) | PASS | 예시와 다음 문서 링크가 모두 있음 | 1 |
