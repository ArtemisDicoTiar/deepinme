# 데이터 스키마 (item bank schema)

`data/**/items*.json`(심리테스트 **문항** 파일) 형식을 고정하는 JSON Schema.
새 문항 세트를 추가할 때 이 형식을 지키면 데이터가 흐트러지지 않는다.

- **스키마**: [`item-bank.schema.json`](item-bank.schema.json) (JSON Schema Draft 2020-12)
- **검증기**: [`validate.py`](validate.py)

## 검증 방법

```bash
pip install jsonschema        # 최초 1회
python3 data/reference/schema/validate.py
```

`data/**/items*.json` 전체를 스키마에 대조하고, `count == items.length`도 확인한다.
종료코드 0 = 전부 통과. (현재: 17개 파일 · 1,108문항 전부 통과 ✔)

## 파일 형식 (한눈에)

```jsonc
{
  "_meta": {
    "instrument":  "TIPI-10",                      // 필수: 짧은 검사 id
    "full_name":   "Ten-Item Personality Inventory (Gosling et al. 2003)", // 필수
    "source_url":  "https://gosling.psy.utexas.edu/...",  // 필수: 문항을 가져온 원출처
    "license":     "Free to use for research ...",  // 필수: 사람이 읽는 라이선스 문구
    "license_class": "free_research_noncommercial", // 필수: 아래 5개 중 하나
    "safe_for_noncommercial_reuse": true,           // 필수(불리언)
    "safe_for_commercial_reuse":    false,          // 필수(불리언)
    "attribution": "Gosling, Rentfrow & Swann (2003) ...", // 필수
    "verification": { "summary": "...", "fabrication_risk": "none" }, // 필수
    "sources": [ { "title": "...", "url": "..." } ],  // 필수(1개 이상)

    // 선택: reuse_notes, scoring_notes, scoring_key, mbti_mapping,
    //       cautions, corrections_applied
  },
  "count": 10,                                       // 필수: items 길이와 일치해야 함
  "items": [
    {
      "text": "Extraverted, enthusiastic.",         // 필수: 문항(질문) 원문
      "language": "en",                              // 필수: 'en' | 'ko' | ...
      // 선택: num, factor, facet, dimension, keyed, instrument, source, license
      "num": "1", "factor": "E", "keyed": "+"
    }
  ]
}
```

### `license_class` 값 (문항 파일 전용, 필터용)

| 값 | 의미 | 비상업 | 상업 |
|---|---|:--:|:--:|
| `public_domain` | 퍼블릭 도메인(IPIP 등) | ✅ | ✅ |
| `cc` | 크리에이티브 커먼즈(대개 NC/SA) | ✅ | ❌ |
| `free_research_noncommercial` | 연구용 무료(저작권 있음) | ✅ | ❌ |
| `proprietary` | 독점(복제 금지) | ❌ | ❌ |
| `unknown` | 미상 | ⚠️ | ⚠️ |

## 범위 주의

- 이 스키마는 **문항 파일(`items*.json`)만** 강제한다.
- **이론·용어 파일**(`types.json`, `dichotomies.json`, `arrows.json`, `terminology-*.json`, `plain-language-examples.json` 등)은 내용마다 구조가 달라 별도 스키마 없이 **`_meta` 관례만 공유**한다(모두 `_meta` 보유).
- **인덱스/지도 파일**(`reference/inventory.json`, `reference/licensing.json`)도 스키마 대상 아님.

## 새 문항 추가 절차

1. `data/raw/<family>/items.<id>.json`(번역본은 `data/translations/ko/<family>/items.<id>.ko.json`)을 위 형식으로 작성.
2. `_meta`의 라이선스·출처·검증을 정확히 채움(추정이면 `verification.summary`에 명시).
3. `python3 data/reference/schema/validate.py` 실행 → 통과 확인.
4. 필요하면 `reference/inventory.md`를 재생성(문항 스캔).
