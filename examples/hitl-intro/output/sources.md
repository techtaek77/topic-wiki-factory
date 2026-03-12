# Sources

## 기본 이해용

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
  - AI 시스템을 위험 관리 관점에서 다루는 기본 프레임이다.
  - HITL를 "사람이 마지막에 본다"가 아니라, 신뢰성과 책임성을 위한 운영 설계로 보게 도와준다.
- [NIST AI Risk Management Framework FAQs](https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-faqs)
  - 신뢰성, 안전성, 설명 가능성 같은 기준을 어떤 생애주기에서 봐야 하는지 빠르게 잡기 좋다.
- [Human-in-the-Loop Workflows | Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop)
  - 워크플로우를 멈추고 사람 입력을 받은 뒤 다시 실행하는 패턴을 제품 관점에서 보여 준다.

## 제품 / 워크플로우 구현 참고

- [Using Amazon Augmented AI for Human Review](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html)
  - low-confidence 예측이나 지속 감사 같은 상황에서 human review loop를 어떻게 거는지 보여 준다.
- [Create Custom Worker Task Templates | Amazon SageMaker AI](https://docs.aws.amazon.com/en_us/sagemaker/latest/dg/a2i-custom-templates.html)
  - 승인 화면에 어떤 정보와 선택지를 넣을지 생각할 때 참고하기 좋다.
- [Human-in-the-Loop Overview | Google Cloud Document AI](https://docs.cloud.google.com/document-ai/docs/hitl)
  - Document AI의 HITL 개요 문서다.
  - 다만 이 기능은 2025년 1월 16일 이후 더 이상 제공되지 않는다고 문서에 명시돼 있어, "벤더 기능에만 설계를 묶어 두면 위험하다"는 반면교사로도 볼 수 있다.

## 이 샘플에서 특히 중요하게 보는 포인트

- 승인 지점이 너무 많거나 너무 적을 때 어떤 문제가 생기는가
- 승인 요청에 근거, 대안, 예상 결과가 함께 제공되는가
- 사람 검토 결과가 다음 자동화 기준 개선으로 이어지는가
- low-confidence 하나만으로 사람 확인 여부를 결정하지 않는가

## 업데이트 감시 포인트

- AI workflow product에서 approval UX 사례가 새로 정리되는지
- policy / compliance 흐름에서 human review 기준이 어떻게 바뀌는지
- 특정 벤더의 HITL 기능이 deprecated 되거나 범위가 바뀌는지
- "confidence score만 믿고 승인 생략" 같은 반패턴이 반복되는지
