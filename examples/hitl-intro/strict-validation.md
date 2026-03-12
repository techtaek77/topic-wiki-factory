# HITL Strict Validation

검증일: 2026-03-13
대상: `hitl-intro`

## 1. Scope 검증

- 주제가 `AI 워크플로우의 human-in-the-loop 설계`로 고정되어 있다.
- 군사용 target tracking 문맥은 `exclude_topics`로 제외됐다.
- `topic_definition`, `exclude_topics`, `scope_confirmed`, `ia_confirmed`가 모두 반영되어 있다.

판정: PASS

## 2. Sources 검증

- 공개 샘플이라 출처 목록을 길게 싣진 않았지만 `sources.md`에 학습 축과 업데이트 감시 포인트가 정리돼 있다.
- 이 주제는 공식 문서 1개로 끝나기보다 workflow / approval UX / safety 운영 사례를 함께 보는 편이 더 맞다.
- 개념 위키 특성상 "정의 + 반패턴 + 운영 포인트"가 writer 입력으로 보일 정도는 확보됐다.

판정: PASS

## 3. IA 검증

- intro 기준 9문서로 범위가 과하지 않다.
- fixed 5 + guide 1 + concept 3 구조라 입문자가 길을 잃지 않는다.
- 문서 순서가 `개념 -> 체크포인트 -> 승인 UX -> 자동화 경계`로 자연스럽다.

판정: PASS

## 4. Fixed 문서 검증

### index.md
- 한 줄 소개 있음
- 왜 배우는지 설명 있음
- 읽는 순서 있음
- 다음 문서 링크 있음

판정: PASS

### prerequisite-map.md
- 먼저 볼 순서가 있다
- 막히는 지점이 드러난다

판정: PASS

### glossary.md
- 핵심 용어가 한 줄씩 정리돼 있다
- 초보자가 낯설어할 단어가 빠지지 않았다

판정: PASS

### faq.md
- 질문 4개
- 초보자가 실제로 묻는 질문 중심

판정: PASS

## 5. concept / guide 문서 검증

확인 문서:
- `hitl-basics`
- `checkpoint-design`
- `approval-ux`
- `automation-boundary`

공통 확인 결과:
- 한 줄 설명이 있다
- 실무형 예시가 있다
- 초보자가 자주 하는 오해나 반패턴이 있다
- 다음에 읽을 연결 문서가 보인다

판정: PASS

## 6. 남은 리스크

- 공개 샘플이라 실제 사례 링크가 더 구체적이면 더 좋다.
- 승인 UI 스크린샷이나 다이어그램이 있으면 기억에는 더 잘 남을 수 있다.
- 향후 확장판에서는 의료 / 배포 / 콘텐츠 moderation 같은 도메인별 HITL 예시를 분기해도 좋다.

## 최종 판정

PASS

