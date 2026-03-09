# Pipeline (Harness)

> 코드 변경이 테스트를 거쳐 배포까지 자동으로 가는 흐름이다.

---

## 왜 필요한가

개발자가 코드를 수정할 때마다 직접 테스트하고 서버에 올리면 실수가 생기고 시간이 든다.
Pipeline은 이 과정을 자동화해서 사람이 신경 쓸 일을 없애준다.

- 없으면: 배포할 때마다 수동으로 빌드 → 테스트 → 업로드. 실수 1번이 장애로 이어진다
- 있으면: 코드 push 하나로 전체 흐름이 자동 실행된다
- 비유: 공장 컨베이어 벨트. 재료(코드)를 넣으면 완성품(배포)이 나온다

---

## 먼저 알아야 할 것

| 개념 | 한 줄 설명 | 링크 |
|------|-----------|------|
| CI/CD | 코드 통합과 배포를 자동화하는 개념 | [[cicd-basics]] |
| YAML | Pipeline 설정 파일을 작성하는 언어 | [[yaml-basics]] |

---

## 어떻게 구현하는가

Harness에서 Pipeline은 YAML 파일로 정의한다.
크게 3가지를 설정하면 된다: 언제 실행할지(trigger), 무엇을 할지(stage), 어디에 배포할지(service).

### 예시

```yaml
pipeline:
  name: my-first-pipeline
  identifier: myFirstPipeline
  stages:
    - stage:
        name: Build
        type: CI
        spec:
          execution:
            steps:
              - step:
                  type: Run
                  name: Run Tests
                  spec:
                    command: npm test
    - stage:
        name: Deploy
        type: CD
        spec:
          serviceConfig:
            serviceRef: my-service
          infrastructure:
            environmentRef: production
```

### 핵심 포인트

- Stage는 순서대로 실행된다. 앞 Stage가 실패하면 다음으로 넘어가지 않는다
- `identifier`는 영어+숫자만. 나중에 API로 참조할 때 쓰인다
- CI Stage(빌드/테스트)와 CD Stage(배포)는 역할이 다르다

### 자주 하는 실수

- Stage 이름에 한글/특수문자 → `identifier`는 영문만 허용. `name`은 자유롭게 써도 됨
- trigger 없이 저장 → 수동 실행만 가능. 자동 실행하려면 trigger 설정 필수

---

## 더 깊이 가려면

| 문서 | 이유 |
|------|------|
| [[stage]] | Pipeline 안의 각 단계를 상세히 설정하는 방법 |
| [[trigger]] | 코드 push, PR, 스케줄 등 자동 실행 조건 설정 |

---

*관련 용어: [[glossary#stage]] · [[glossary#trigger]] · [[glossary#identifier]]*
