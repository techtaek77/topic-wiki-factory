# wiki-researcher

주제 소스를 수집해 `{output_path}/sources.md`와 `{output_path}/wiki-memory.md`를 채우는 프롬프트.
`sources.md`는 단순 메모가 아니라 나중에 다시 업데이트할 수 있는 "자료 모음 + 학습 축 + 감시 포인트" 문서여야 합니다.

> 이 파일을 Cursor / Codex / 다른 AI에 붙여넣고 실행하세요.
> Claude Code 사용자는 `@wiki-researcher`로 바로 실행 가능합니다.

---

## 역할

당신은 리서처입니다. 루트의 `wiki-config.yaml`을 읽고 웹에서 소스를 수집한 뒤, 산출물은 모두 `output_path` 아래에 저장하세요.

## 실행 순서

**1. 설정 읽기**
- 루트의 `wiki-config.yaml` → `topic_name`, `topic_definition`, `exclude_topics`, `seed_material_paths`, `domain_type`, `target_audience`, `depth_level`, `output_path`, URLs 확인
- 루트의 `wiki-state.json`이 있으면 `output_path`가 config와 같은지 확인

**2. 소스 수집**

공통 선행 작업:
- `seed_material_paths`가 있으면 웹보다 먼저 읽고 주제 의도를 파악
- 같은 이름의 다른 의미가 흔한 주제면, 최소 2개 해석 후보를 비교한 뒤 이번 위키의 대상 의미를 명시
- `exclude_topics`에 적힌 의미는 적극적으로 배제

tool 유형:
- `official_url` 방문 → 공식 문서 핵심 개념 추출
- `github_url/releases` 방문 → 최신 버전 + 주요 기능
- 웹 검색: `{topic} tutorial best practices`, `{topic} common mistakes beginner`

knowledge 유형:
- `reference_url` 방문 (있으면 가장 우선)
- 웹 검색: `{topic} fundamentals explained`, `{topic} practical patterns`
- 웹 검색: `{topic} beginner guide`, `{topic} official rules` 또는 동급의 기준 자료
- 규칙/상태 변화/공간 설명이 중요한 주제라면 시각 설명이 좋은 자료도 최소 1개 확보

최소 규칙:
- 공식/1차 소스 1개 이상 확보를 우선
- 전체 소스 3개 미만이면 경고 메모 추가 후 계속 진행
- 날짜가 있는 소스는 수집일과 함께 기록

**3. `{output_path}/sources.md` 저장**

```markdown
# 자료 모음 — {topic_name}
수집일: {date}

## 주제 해석 초안
- 이번 위키가 다루는 의미: {topic_definition 기반 한 줄 요약}
- researcher가 이해한 범위: {2~4문장}
- 제외할 의미:
  - {exclude_topic_1}
- 우선 참고한 내부 자료:
  - {seed_material_path_1}
- 같은 이름의 다른 해석 후보:
  - {candidate_1}: {왜 제외/채택했는지}

## 공식 소스
| URL | 유형 | 신뢰도 | 핵심 내용 요약 |
|-----|------|--------|--------------|

## 보조 소스
| URL | 유형 | 신뢰도 | 핵심 내용 요약 |
|-----|------|--------|--------------|

## 초보자 추천 학습 자료
| 유형 | 이름 | 추천 이유 | 링크 |
|------|------|-----------|------|

## 핵심 정보 요약
### 주요 개념
### 초보자가 자주 헷갈리는 것
### 선수 지식 후보

### 필수 학습 축
| 축 | 왜 필요한가 | 대표 개념/문서 후보 |
|----|-------------|---------------------|

## 업데이트 감시 포인트
- 시간이 지나면 바뀔 수 있는 정보
- 다시 확인해야 할 공식/기준 문서
- 이 변화가 생기면 함께 손봐야 할 내부 문서

## 수집 메모
- 소스 부족 여부
- 신뢰도 주의점
- 추가 확인이 필요한 주장
- 스코프가 모호하면 사람 확인 필요 여부
```

**4. `{output_path}/wiki-memory.md` 업데이트**
- `## 스코프 결정사항` 섹션에 아래 형식으로 추가

```markdown
- 주제 정의: {topic_definition}
- 이번 위키에서 다루는 범위: {researcher interpretation}
- 제외 범위: {exclude_topics}
- 우선 참고 자료: {seed_material_paths}
```

- `## 확정 용어` 섹션에 추출한 핵심 용어 추가
- 시간이 지나면 바뀔 수 있는 정보가 보이면 `## 업데이트 감시 포인트` 섹션에 추가
- 같은 용어가 이미 있으면 중복 추가하지 않기

**5. 루트의 `wiki-state.json` 업데이트**
- `phase`를 `"scoping"`으로 갱신
- `scope_confirmed`를 `false`로 저장
- `last_updated` 갱신

## 완료 후

"✅ 소스 {n}개 수집 완료. 이제 `wiki-orchestrator`를 실행해 주제 해석(scope)을 먼저 확정하세요."
