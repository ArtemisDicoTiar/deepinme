# translations/ko/ — 한국어 번역본

`data/`의 영어 문항 데이터셋을 **자연스러운 한국어로 충실 번역(faithful translation)**한 버전. 원본 폴더 구조(bigfive/hexaco/enneagram/mbti/misc)를 그대로 미러링한다.

- 📊 **15개 데이터셋 · 976문항** (원본 영어 15종 전체)
- 파일명: `items.<원본id>.ko.json`
- 각 파일은 원본과 **동일한 [item-bank 스키마](../../reference/schema/README.md)**를 따른다(검증 통과). 문항에 `text`(한국어) + `text_en`(원문 병기), `language: "ko"`.

## 무엇을 보존했나

번역은 **문항 순서 · 채점 방향(`keyed`) · `factor`/`facet`/`dimension`을 원본과 100% 동일하게** 유지한다. 즉 원본 검사의 채점 로직을 그대로 쓸 수 있다.
- 역채점(reverse-keyed) 문항은 **뒤집지 않고 원문 그대로** 번역 (채점키 유효성 유지).
- 양극형 문항(OEJTS·OEPS v2)은 `A ↔ B` 형식과 ` ↔ ` 구분자를 유지 (예: `목록을 작성한다 ↔ 기억에 의존한다`).

## ⚠️ 중요 — 이건 "검증된 한국어 표준검사"가 아니다

- **LLM 충실 번역**이다(2026-07 deepinme 번역 워크플로우). 각 번역은 2차 에이전트 QA를 거쳤고 **전 데이터셋 fidelity=high · naturalness=natural · 카운트 일치**로 나왔지만, 학술적으로 타당화(validated)된 한국어 검사와는 다르다.
- 실제 서비스 투입 전 **사람 재검수** 권장. 각 파일 `_meta.translation.qa.issues`에 QA가 짚은 경미한 다듬기 포인트가 들어 있다(데이터셋당 1~5개, 주로 뉘앙스).
- **번역 ≠ 쉬운말 리라이팅.** 이건 뜻·난이도를 보존한 번역이고, deepinme의 핵심인 "번역투 → 쉬운 일상어" 변환은 이 번역본을 원본 삼아 이뤄진다. 작성 원칙은 [`../../raw/korean/plain-language-examples.json`](../../raw/korean/plain-language-examples.json) 참고.

## 한국어 친화 리라이팅 — `text_ko_friendly` (진행 중)

일부 문항에는 `text`(충실 번역)에 더해 **`text_ko_friendly`** 필드가 붙어 있다. 번역투를 걷어낸 **자연스러운 한국어**(검사 문항 말투 `나는 ~다` 유지, 측정 구성개념·채점 방향 불변)다. 예: `리더로 떠오르는 편이다`(번역) → `리더가 되는 편이다`(친화).

- 규칙·도구: [`../../reference/rewriting/README.md`](../../reference/rewriting/README.md) (+ `review.py` before/after 검토기).
- 현재 **샘플 2종**(TIPI-10, OEPS v2)에만 적용 — 말투/톤 검수 후 전 데이터셋으로 확장 예정.
- 완전 구어체(해요체) "쉬운 일상어"는 별도 후속 단(tier 3).

## 라이선스 (파생물)

번역은 원본의 **파생물(derivative)**이라 원본 라이선스를 그대로 따른다(각 파일 `_meta` 참조).
- 퍼블릭 도메인(IPIP 계열): 번역도 자유(상업 포함).
- 연구용 무료(BFI/HEXACO/TIPI) · CC-NC(OEJTS/OEPS): **비상업 한정**. 상업 전환 시 제거/허가 필요.
- 1단계(비상업)에서는 전부 사용 가능.

## 이미 한국어인 데이터셋 (여기 없음)

다음 2종은 원래 한국어라 번역 대상이 아니었다 (원위치 유지):
- `data/raw/korean/items.ipip-ko.json` (IPIP 마커 한국어 역번역, 32)
- `data/raw/korean/items.ipip-markers-ko.json` (IPIP 마커 한국어, 100)

## 목록

| 파일 | 문항 | 원본 |
|---|--:|---|
| `bigfive/items.bfi-2-60.ko.json` | 60 | BFI-2 |
| `bigfive/items.bfi-44.ko.json` | 44 | BFI-44 |
| `bigfive/items.ipip-bfas-100.ko.json` | 100 | BFAS |
| `bigfive/items.ipip-big-five-markers-100.ko.json` | 100 | IPIP 마커 100 |
| `bigfive/items.ipip-neo-120.ko.json` | 120 | IPIP-NEO-120 |
| `bigfive/items.mini-ipip-20.ko.json` | 20 | Mini-IPIP |
| `bigfive/items.saucier-mini-markers-40.ko.json` | 40 | Saucier Mini-Markers |
| `bigfive/items.tipi-10.ko.json` | 10 | TIPI |
| `hexaco/items.hexaco-60.ko.json` | 60 | HEXACO-60 |
| `hexaco/items.ipip-hexaco.ko.json` | 240 | IPIP-HEXACO |
| `enneagram/items.oeps.ko.json` | 36 | OEPS v1 |
| `enneagram/items.oeps-v2-bipolar.ko.json` | 54 | OEPS v2 |
| `mbti/items.ipip-bffm.ko.json` | 40 | IPIP-BFFM |
| `mbti/items.oejts.ko.json` | 32 | OEJTS |
| `misc/items.open-hemispheric-brain-dominance.ko.json` | 20 | OHBDS |
