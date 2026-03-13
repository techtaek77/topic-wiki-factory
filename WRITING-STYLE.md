# Writing Style

이 프로젝트는 "정보를 빠짐없이 넣는 글"보다
"처음 읽는 사람이 한 번에 이해하고, 나중에도 떠올릴 수 있는 글"을 지향한다.

아래 원칙은 메인 문서, 샘플, 에이전트 프롬프트에 공통으로 적용한다.

## 핵심 원칙

### 1. 독자가 궁금한 것부터 먼저 말한다

- 문서 초반에 결론, 큰 그림, 다음 행동을 먼저 둔다.
- 배경 설명은 필요할 때만 뒤로 민다.
- "이 문서를 읽고 나면 무엇을 알게 되는가"가 초반 20초 안에 보여야 한다.

### 2. 짧고 분명하게 쓴다

- 짧은 문장, 짧은 문단, 짧은 섹션을 우선한다.
- 한 문단에는 한 생각만 넣는다.
- 가능하면 능동태와 현재형을 쓴다.
- 불필요한 수식어와 과장 표현은 지운다.

### 3. 익숙한 말로 쓰고, 전문 용어는 현장에서 푼다

- 독자가 실제로 쓸 법한 단어를 우선한다.
- 전문 용어가 필요하면 처음 등장한 자리에서 바로 풀어쓴다.
- "아는 사람끼리만 통하는 말"보다 "처음 보는 사람도 추측 가능한 말"을 고른다.

### 4. 스캔되게 구성한다

- 소제목은 재치보다 설명을 우선한다.
- 중요한 내용은 리스트나 짧은 표로 드러낸다.
- 문단 첫 문장만 읽어도 흐름이 보이게 쓴다.
- 링크 텍스트는 "click here" 같은 말 대신, 눌렀을 때 얻는 정보를 드러낸다.

### 5. 기억이 중요하면 장면으로 연다

- 개념이 추상적이거나, 판단 감각이 중요한 문서는 짧은 장면으로 시작한다.
- 좋은 장면은 보통 아래 네 가지를 포함한다.
  - 누가 겪는가
  - 무엇을 하려는가
  - 어디서 헷갈리거나 틀리는가
  - 그 결과 왜 중요한가
- 장면은 짧고 plausible 해야 한다.
- 억지 감동, 과장된 드라마, 소설 톤은 금지한다.

### 6. 원칙은 장면의 해설처럼 붙인다

- 장면을 던지고 끝내지 않는다.
- "그래서 무엇을 배워야 하나?"를 바로 이어서 설명한다.
- 가능하면 마지막에 기억용 한 문장이나 비유를 남긴다.

### 7. 구조가 중요하면 그림으로 압축한다

- 단계 흐름, 분기, 의존성, 상태 변화는 차트가 글보다 빠를 수 있다.
- 텍스트 3문단이 필요한 구조라면 mermaid나 SVG를 검토한다.
- 차트는 장식이 아니라 이해 속도를 높이는 압축 도구여야 한다.

## 문서 유형별 기본 적용

### `index.md`

- 큰 그림과 읽는 순서를 먼저 준다.
- 초보자가 "지금 어디부터 읽어야 하지?"를 고민하지 않게 만든다.
- 필요하면 짧은 장면으로 왜 이 주제가 중요한지 감을 준다.

### `guide`

- 따라 읽는 흐름이 핵심이다.
- 장면 -> 원칙 -> 예시 -> 다음 문서 순서가 잘 맞는다.

### `concept`

- 정의만 던지지 말고, 언제 필요한 개념인지 먼저 보여 준다.
- 기억이 중요한 개념은 짧은 상황 묘사로 여는 편이 좋다.

### `faq`, `questions`

- 실제로 묻는 말투를 유지한다.
- 질문 문장만 읽어도 초보자의 막힘이 보여야 한다.

## 이 프로젝트에서 특히 금지하는 것

- 과장 형용사로 밀어붙이는 글
- 정의를 3문단 깔고 나서야 왜 중요한지 말하는 글
- 소제목이 멋있기만 하고 무슨 내용인지 안 보이는 글
- 한 문단에 설명, 예외, 단서, 비교를 다 우겨 넣는 글
- 장면을 넣되 실제로는 원칙과 연결되지 않는 글

## 차트 원칙

- 흐름/분기 설명은 `mermaid flowchart`를 우선 검토한다.
- 선수지식/문서 의존성은 `mermaid graph`를 우선 검토한다.
- 공간 배치/이동 경로/보드 상태는 SVG나 정적 이미지를 우선 검토한다.
- 차트가 있다면 앞뒤에 "이 그림이 뭘 보여 주는지"와 "어떻게 읽으면 되는지"를 짧게 붙인다.
- 자세한 기준은 `DIAGRAM-GUIDELINES.md`를 따른다.

## 참고한 기준

- [Digital.gov: Writing for understanding](https://digital.gov/guides/plain-language/writing)
- [Digital.gov: Organize the information](https://digital.gov/guides/plain-language/principles/organize)
- [Digital.gov: Plain Language Web Writing Tips](https://digital.gov/resources/plain-language-web-writing-tips)
- [Digital.gov: Clear and short](https://digital.gov/guides/plain-language/writing/clear-short)
- [NN/g: How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/)
- [PubMed: Memory and comprehension of narrative versus expository texts](https://pubmed.ncbi.nlm.nih.gov/33410100/)
- [PMC: Stories in Action](https://pmc.ncbi.nlm.nih.gov/articles/PMC10173355/)
