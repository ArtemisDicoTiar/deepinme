# data/ — 심리검사 문항·이론 데이터 모음

MBTI·에니어그램 및 인접 성격검사(Big Five·HEXACO)의 **문항(질문)**과 **이론 레퍼런스**를 영어·한국어로 수집·검증한 모음.
deepinme의 1단계(**비상업**) 목적에 맞춰, 오픈/무료 배포된 문항을 최대한 넓게 모으고 각 파일에 라이선스·검증 상태를 기록했다.

- 📊 **원본 문항 1,108개 · 17개 검사(`raw/`)** + 한국어 번역 976개(`translations/ko/`) = 총 2,084 · 32파일. + 이론/용어 레퍼런스
- 🗂 **마스터 카탈로그: [`reference/inventory.md`](reference/inventory.md)** (검사별 문항수·라이선스 한눈에)
- 📐 **문항 파일 스키마: [`reference/schema/`](reference/schema/README.md)** — 형식 고정 + 검증기(`python3 data/reference/schema/validate.py`, 현재 32파일 전부 통과 ✔)
- 🇰🇷 **한국어 번역본: [`translations/ko/`](translations/ko/README.md)** — 영어 15종(976문항)의 충실 번역(`text_en` 원문 병기, 채점방향 보존). LLM 번역이라 미검증 표준검사 아님.
- 수집 방식: 2회의 멀티에이전트 워크플로우(총 38 에이전트). 각 검사는 **실제 문항을 원출처에서 fetch → 별도 검증 에이전트가 조작 여부(문항수 대조·원문 스팟체크)와 라이선스 정확성을 재확인**. 전 검사 조작위험 none/low.

## ⚠️ 라이선스 신호등

각 JSON 파일 상단 `_meta`에 `license_class`, `safe_for_noncommercial_reuse`, `safe_for_commercial_reuse`가 있다.

> **1단계(비상업)에서는 이 폴더의 모든 문항을 사용할 수 있다** (비상업 열 전부 🟢). 아래 표는 **나중에 상업 전환할 때**를 위한 구분이다.

| 라이선스 유형 | 예시 | 비상업(1단계) | 상업(추후) |
|---|---|:--:|:--:|
| 퍼블릭 도메인 | IPIP 계열(NEO-120, BFAS, Mini-IPIP, 마커, HEXACO, 한국어 마커) | 🟢 | 🟢 |
| 연구용 무료 | BFI-44, BFI-2, TIPI, Saucier, HEXACO-60 | 🟢 | 🔴 (저자 허가 필요) |
| CC BY-NC-SA | OEJTS, OEPS v1·v2, OHBDS | 🟢 | 🔴 (비상업 한정) |
| 독점(복제금지) | 공식 MBTI·16Personalities·RHETI·NEO-PI-R | ⛔ **문항 미수록** | ⛔ |

독점 상용 검사는 비상업이라도 "복제 금지"가 명시돼 문항을 넣지 않았다(구조만 `reference/licensing.json`에 기록).

## 디렉토리 구조

3층 구조: **raw**(수집 원본) · **translations**(파생 번역) · **reference**(메타).

```
data/
├── raw/              # 수집·정리한 원본 데이터 (문항 + 이론/용어)
│   ├── mbti/         #   융/유형론: 4지표·16유형·8인지기능 + OEJTS 32, IPIP-BFFM 40
│   ├── bigfive/      #   5요인(가장 실증적): NEO-120·BFAS-100·Mini-IPIP-20·마커-100·
│   │                 #     BFI-44·BFI-2-60·TIPI-10·Saucier-40  (총 494)
│   ├── hexaco/       #   6요인: HEXACO-60, IPIP-HEXACO-240  (총 300)
│   ├── enneagram/    #   9유형·센터·화살표·발달수준 + OEPS v1(36)·v2(54)
│   ├── korean/       #   한국어 용어(MBTI/에니어) + 쉬운말 예시 + 한국어 IPIP 문항(32,100)
│   └── misc/         #   인접 오픈 척도(OHBDS 좌우뇌 지배성 20) — 참고
├── translations/     # 언어별 파생 번역본
│   └── ko/           #   raw 영어 15종의 한국어 충실 번역 (976문항, text_en 병기)
└── reference/        # 메타: inventory(카탈로그) · licensing(저작권 지도) · schema · sources
```

## 왜 Big Five·HEXACO까지?

MBTI 4지표는 Big Five에서 파생·매핑되고(외향성↔E/I, 개방성↔S/N, 우호성↔T/F, 성실성↔J/P), **Big Five/HEXACO는 학술적으로 가장 검증된 성격 모델**이다. 퍼블릭 도메인(IPIP) 문항이 풍부해 **쉬운말 리라이팅의 안전한 원본**이 된다. MBTI 유형 결과는 이 축들 위에 얹으면 된다.

## 활용 가이드 (deepinme 관점)

1. **문항 리라이팅 원본** — 상업까지 안전한 **퍼블릭 도메인 IPIP 계열**(`raw/bigfive/`, `raw/mbti/items.ipip-bffm.json`, `raw/korean/items.ipip-markers-ko.json`)을 1순위 원본으로 삼아, `raw/korean/plain-language-examples.json` 원칙대로 쉬운 일상어로 다시 쓴다. 한국어부터 시작하려면 `translations/ko/`의 번역본을 원본 삼아 다듬어도 된다.
2. **검사 길이 선택** — 짧게(TIPI-10, Mini-IPIP-20) vs 정밀하게(IPIP-NEO-120, HEXACO-240). Phase 1은 짧은 셋으로 완주율 확보 권장.
3. **유형 결과 콘텐츠** — `raw/mbti/types.json`, `raw/enneagram/types.json`(원저작 쉬운말).
4. **"현재 심리 건강 상태"** — `raw/enneagram/arrows.json` + `raw/enneagram/levels.json`. (발달수준 명칭은 EI 저작이라 UI 문구는 의역)
5. **저작권·상표** — `reference/licensing.json`. 'MBTI'·'RHETI'는 상표; 'Enneagram' 단어 자체는 자유.

## 중요 주의

- **에니어그램·MBTI는 실증 검증이 부족한 전통**이다(Big Five/HEXACO와 달리). 진단이 아닌 **자기성찰 도구**로 제시할 것.
- **연구용 무료 / CC-NC** 문항은 상업 전환 시 제거하거나 저자 허가가 필요하다. 파일 `_meta`로 언제든 필터링 가능.
- 라이선스 요약은 **법률 자문이 아니다.** 상업 배포 전 확인.
