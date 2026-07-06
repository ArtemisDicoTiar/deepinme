# 진행 기록 — 기획·데이터 기반 구축

**기간**: 2026-07-04 ~ 07-06 · **단계**: 프로젝트 인셉션 (코드 이전, 기획·데이터)

deepinme(애니어그램·MBTI 등 심리테스트 웹 플랫폼)의 초기 기획과 검사 데이터 기반을 구축했다. 아직 애플리케이션 코드는 없으며, 기획 문서 + 벤치마킹 조사 + 검사 문항/이론 데이터 + 스키마가 산출물이다.

---

## 1. 프로젝트 설정
- `CLAUDE.md` — 저장소 가이드(초기: 언어 미정, 이후 방향 반영).
- `.claude/` — 프로젝트 설정(`settings.json` 권한 허용목록), `commands/`·`agents/` 스캐폴드. `.gitignore`에 `.claude/settings.local.json` 제외 추가.

## 2. 벤치마킹 조사 — `.claude-research/`
- `benchmark-psychology-test-sites.md` — 글로벌(16Personalities·Truity·Enneagram Institute·Crystal)과 한국(푸망·테스트잇·테몬 등) 대표 사이트의 제품구조·UX·수익모델 정리.
- 결론: **평가형 신뢰 + 바이럴형 공유성**을 결합한 하이브리드 포지셔닝.

## 3. 기획 보고서 — `.claude-plan/`
- `00-기획보고서.md` — 미션(어려운 번역투 문항을 쉬운 말로 → 정확한 자기이해)/비전/핵심가치(친절·정확·자기수용·관계이해·성장가능성)/서비스 컨셉/차별점/로드맵.
- `01~05` — 프로젝트 계획(Phase 1 평가형 → 2 엔터테인먼트 → 3 심화·케어), 분업(3인: 기술·데이터/심리학/마케팅·UIUX·브랜딩, RACI), 조사 계획, 제품·UX·데이터, 심리학 근거(에니어그램 화살표·발달수준, 검사 타당도, 케어 윤리).
- `06-branding-naming.md` — 브랜드 후보 8종 비교. **가제 확정: deepinme(디핀미)**.
- 핵심 결정: 결과 일부 무료공개+공유카드(캐릭터 매칭), 유형별 SEO, 화살표·발달수준으로 "심리 건강 상태" 검토, 행동데이터(반응시간·수정) 수집은 인프라만 먼저, "단계별 추정치"는 오염 우려로 보류.

## 4. 검사 데이터 — `data/` (3층 구조)
2회 멀티에이전트 워크플로우로 수집·검증, 이후 한국어 번역·재구조화.

- **`data/raw/`** — 수집 원본 (문항 + 이론/용어), 검사군별
  - **문항 1,108개 · 17검사 파일**: bigfive(494) · hexaco(300) · mbti(72) · enneagram(90) · korean(132) · misc(20).
  - 라이선스 신호등: 🟢퍼블릭도메인(IPIP 계열, 상업까지 안전) · 🔴연구용무료(BFI/HEXACO/TIPI)·CC-NC(OEJTS/OEPS, 비상업 한정) · ⛔독점 미수록(공식MBTI·16P·RHETI·NEO-PI-R).
  - 이론: MBTI 16유형·인지기능, 에니어그램 9유형(EI 저작권 회피 위해 **원저작 쉬운말**)·센터·화살표(검증)·발달수준, 한국어 용어 + 쉬운말 예시.
- **`data/translations/ko/`** — raw 영어 15종의 **한국어 충실 번역 976문항**(`text_en` 원문 병기, 채점방향·factor 보존). LLM 번역이라 검증된 표준검사는 아님(각 파일 QA 이슈 기록).
- **`data/reference/`** — 메타: `inventory.md`(마스터 카탈로그, 언어 컬럼), `licensing.json`(검사별 저작권 지도), `sources.md`(출처), `schema/`(item-bank JSON Schema + `validate.py`).

### 데이터 품질
- 전 검사 조작위험 none/low, 라이선스 검증 완료(예: OEJTS는 PD 아님→CC BY-NC-SA로 정정).
- 전 파일 `_meta` 표준화(license_class·safe_for_(non)commercial_reuse·source_url·verification·sources).
- **스키마 검증: 32파일 · 2,084문항(EN 976 + KO 1108) 전부 통과** (`python3 data/reference/schema/validate.py`).

---

## 현재 상태 요약
| 영역 | 산출물 |
|---|---|
| 기획 | `.claude-plan/` (보고서 + 01~06) |
| 조사 | `.claude-research/` (벤치마킹) |
| 데이터 | `data/raw` 1,108 + `data/translations/ko` 976, 스키마·인벤토리·라이선스 |
| 브랜드 | 가제 deepinme(디핀미) |
| 코드 | 없음 (다음 단계) |

## 다음 단계 후보
1. IPIP(PD) 문항 → deepinme 톤 "쉬운 일상어" 리라이팅 샘플 (핵심 차별점 실증).
2. Phase 1 대표 검사 선정(에니어그램 vs MBTI) — 심리학 담당.
3. 기술 스택 선정 + 앱 스캐폴드.
4. 도메인·인스타 핸들·상표 가용성 확인(네이밍 확정 전).
