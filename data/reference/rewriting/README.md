# rewriting/ — 한국어 친화 리라이팅 (`text_ko_friendly`)

deepinme의 핵심 차별점은 **"번역투 심리검사 문항을 자연스러운 한국어로 다시 쓰는 것"**이다.
이 폴더는 그 작업의 **규칙(spec)과 도구**다. 실제 리라이팅 문장은 `data/translations/ko/**/items.*.ko.json`의 각 문항에 **`text_ko_friendly` 필드**로 붙는다.

## 한국어 텍스트의 3단(tier)

한 문항에 대해 한국어 표현이 세 층위로 존재한다. `text_ko_friendly`는 **2단**이다.

| 단 | 필드 | 성격 | 예 (`I naturally emerge as a leader.`) |
|---|---|---|---|
| 0 | `text_en` | 영어 원문 | I naturally emerge as a leader. |
| 1 | `text` | **충실 번역** — 뜻·난이도 보존, 다소 번역투 가능 | 나는 자연스럽게 리더로 떠오르는 편이다. |
| **2** | **`text_ko_friendly`** | **자연스러운 한국어** — 번역투만 제거, 검사 문항 말투 유지 | **나는 자연스럽게 리더가 되는 편이다.** |
| 3 | (미정, 후속) | **쉬운 일상어(해요체)** — 완전 구어체 리라이팅 | 저는 어쩌다 보면 제가 리더를 맡고 있더라고요. |

- **1단(`text`)은 그대로 둔다.** `text_ko_friendly`는 병기되는 **추가** 필드다(원본 대조·롤백 가능).
- **3단(해요체 쉬운말)은 이 파일의 범위가 아니다.** 그건 별도 후속 단계이고, 원칙은 [`../../raw/korean/plain-language-examples.json`](../../raw/korean/plain-language-examples.json) 참고.

## `text_ko_friendly` 작성 규칙

### 지켜야 할 것 (register)
- **1인칭 자기보고 말투 유지**: `나는 ~다`, `나는 ~하는 편이다`, 형용사형(`~ㄴ/~는`). 해요체(`~해요`)로 내려가지 않는다.
- **번역투 걷어내기**: 영어 구조를 그대로 옮긴 명사구·수동태·calque를 자연스러운 동사·구문으로 푼다.
  - `리더로 떠오르는`(emerge의 직역) → `리더가 되는`
  - `사회적 상호작용을 통해 에너지를 획득` → `사람들과 어울리면 기운이 나는`
  - `~에 대한 민감성이 높다` → `~을 금방 알아채는`
- **어색한 외래어/한자어 → 일상어**: `과업 수행` → `일할 때`, `정서적 동요` → `마음이 흔들림`.

### 절대 바꾸면 안 되는 것 (measurement invariants)
1. **측정 구성개념(construct) 동일** — 같은 특성을 재야 한다. 뜻을 넓히거나 좁히지 않는다.
2. **채점 방향(`keyed`) 불변** — 역채점 문항을 **뒤집지 않는다**. 긍정/부정 어조를 유지한다.
3. **응답 난이도 동일** — 더 동의하기 쉽/어렵게 만들지 않는다(예: 단정 `~다`를 완화 `~편이다`로 바꿔 문턱을 낮추지 않기 — 원문 강도를 따른다).
4. **양극형(bipolar)** — `A ↔ B` 형식과 ` ↔ ` 구분자를 유지한다. 양극 단어만 자연스럽게 다듬는다.
5. **한 문항 = 한 내용** — 원문이 이중질문이면 그대로 둔다(임의로 쪼개지 않는다).
6. `num`·`factor`·`facet`·`keyed`·`text`·`text_en`은 **건드리지 않는다**. `text_ko_friendly`만 추가.

### 이미 자연스러운 문항
`text`가 이미 자연스러우면 `text_ko_friendly`를 **`text`와 동일하게** 채운다(모든 문항이 이 필드를 갖도록 — 다운스트림이 항상 `text_ko_friendly`만 읽으면 되게).

### 기존 QA 이슈 반영
각 번역 파일 `_meta.translation.qa.issues`에 2차 QA가 짚은 다듬기 포인트가 있다(예: OEPS v2 Q8 `리더로 떠오르는`, Q33 `충직하다`→`의리가 있다`). 리라이팅 때 **우선 반영**한다.

## 도구 — `review.py`

리라이팅 결과를 검토·검증하는 스크립트.

```bash
# 특정 파일들의 before→after 표 출력
python3 data/reference/rewriting/review.py data/translations/ko/bigfive/items.tipi-10.ko.json

# text_ko_friendly가 있는 모든 파일을 훑어 표 + 린트 (인자 없이)
python3 data/reference/rewriting/review.py
```

출력: 문항별 `text_en → text → text_ko_friendly` 3열 비교표(변경된 문항만 ▲ 표시) + 린트 결과.
린트가 잡는 것: 빈 `text_ko_friendly`, 양극형인데 ` ↔ ` 유실, 필드 커버리지(몇/몇 문항). 스키마 검증은 기존 [`../schema/validate.py`](../schema/validate.py)가 담당.

## 작업 절차

1. 대상 `items.*.ko.json`을 열어 각 문항에 `text_ko_friendly`를 추가(위 규칙 준수).
2. `python3 data/reference/schema/validate.py` — 스키마 통과 확인.
3. `python3 data/reference/rewriting/review.py <파일>` — before/after + 린트 확인, 사람이 검토.
4. 파일 `_meta.translation`에 `friendly_rewrite` 상태를 기록(선택).
