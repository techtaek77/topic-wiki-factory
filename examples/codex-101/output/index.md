# Codex 101

> 처음 Codex를 켰을 때 "그래서 뭘 먼저 해야 하지?"에서 멈추지 않도록, 첫 작업 루프를 손에 익게 돕는 입문 위키다.

## 왜 보나

처음 Codex를 쓰는 사람은 보통 비슷한 장면을 겪는다.
터미널은 열려 있고, 저장소도 보이는데, 첫 말을 어떻게 걸어야 할지 잠깐 멈춘다.
"무슨 폴더에서 시작하지?", "main에서 바로 해도 되나?", "뭘 어떻게 요청하지?", "결과는 어디서 확인하지?"

이 위키는 그 얼어붙는 첫 10분을 줄이려고 만들었다.
처음부터 거창한 자동화를 하는 게 아니라, `작은 작업 하나를 안전하게 맡기고 확인하는 루프`를 몸에 익히는 데 초점을 둔다.

한 문장으로 기억하면 이렇다.
`Codex 첫 성공은 대단한 기능 구현보다, 작은 요청을 또렷하게 던지고 diff를 읽는 데서 나온다.`

## 먼저 할 일

1. 작업할 저장소 폴더를 연다.
2. `git status`로 현재 상태를 본다.
3. 작은 feature branch를 만든다.
4. Codex에게 아주 작은 작업 하나를 맡긴다.
5. diff, 테스트, commit/push 순서로 확인한다.

## 먼저 보면 좋은 것

- [quick-start](docs/guides/quick-start.md) - 첫 10분 루프를 그대로 따라 하며 감을 잡는다.
- [prerequisite-map](prerequisite-map.md) - 어떤 감각이 있으면 덜 막히는지 먼저 정리해 둔다.

## 이 위키를 보는 순서

1. [quick-start](docs/guides/quick-start.md)부터 읽고 그대로 한 번 따라 한다.
2. [agents-and-context](docs/concepts/agents-and-context.md)로 요청을 어떻게 써야 하는지 감을 잡는다.
3. [review-vs-implementation](docs/concepts/review-vs-implementation.md)로 언제 구현/리뷰를 나눌지 본다.
4. [faq](faq.md)에서 처음 쓰며 드는 질문을 정리한다.
5. [questions](questions.md)에서 아직 막히는 질문을 적고 다음 보강 포인트를 본다.

## 다음에 읽을 문서

- [quick-start](docs/guides/quick-start.md) - 지금 바로 따라 하기 좋다.
- [faq](faq.md) - 폴더, 브랜치, 커밋 같은 기본 질문을 바로 해결한다.
- [questions](questions.md) - 읽었는데도 막히는 질문을 모아 두는 곳이다.
- [glossary](glossary.md) - 낯선 용어가 보이면 짧게 정리해 둔 곳이다.
- [changelog](changelog.md) - 이 샘플이 어떤 흐름으로 보강됐는지 확인한다.
