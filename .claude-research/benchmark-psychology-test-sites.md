# 심리 테스트 웹페이지 벤치마킹 조사

> **프로젝트**: deepinme — 애니어그램·MBTI 등 심리 테스트 운영 웹페이지
> **조사일**: 2026-07-05
> **목적**: 글로벌 / 한국 대표 사이트의 제품 구조·UX·수익 모델을 벤치마킹하여 초기 설계 방향 도출

---

## 1. 두 갈래의 시장 포지셔닝

심리 테스트 사이트는 크게 두 갈래로 나뉜다. **어느 쪽을 지향하는지 먼저 정해야** 설계·톤·수익 모델이 갈린다.

| 축 | A. 진지형 (Assessment) | B. 바이럴형 (Entertainment) |
|---|---|---|
| 대표 | 16Personalities, Truity, Enneagram Institute | 푸망, 테스트몽, 테스트잇, 테몬 |
| 테스트 길이 | 10~15분, 60문항+ | 2~3분, 10문항 내외 |
| 결과물 | 심층 리포트·커리어·관계 분석 | 짧고 공유하기 좋은 캐릭터/이미지 카드 |
| 재방문 동기 | 자기이해·커리어·연간 재검사 | 신규 테스트 계속 출시 |
| 수익 | 프리미엄 리포트 결제 (freemium) | 광고·기업 제휴(브랜디드 테스트) |
| 이탈 리스크 | 길어서 중도 이탈 | 얕아서 리텐션 약함 |

> **deepinme 시사점**: 애니어그램·MBTI를 "진지하게" 다룬다는 점에서 A에 가깝지만, 한국 유저의 바이럴 공유 습관(카톡)을 고려하면 **A의 신뢰도 + B의 공유성**을 결합하는 하이브리드가 가장 유효.

---

## 2. 글로벌 벤치마크

### 2.1 16Personalities ⭐ 최우선 벤치마크
- **URL**: https://www.16personalities.com/
- **규모**: 45개국어 · 누적 10억 회+ 응시. 사실상 이 카테고리의 표준.
- **테스트 구조**: 약 60문항, 5~7점 리커트(양극 선택) 슬라이더, 약 12분.
- **핵심 강점**:
  - **결과 무페이월**: 기본 유형 결과는 전부 무료로 공개 → 공유·재방문 유도. 결제는 그 위에 얹는다.
  - **캐릭터화**: 16유형마다 일러스트·별명(예: 옹호자, 논리술사)을 부여해 "나를 표현"하고 싶게 만듦 → 공유 동력의 핵심.
  - **심층 콘텐츠**: 유형별 커리어·성장·연애·우정 등 방대한 프로필 페이지 (SEO 자산이자 체류시간 확보).
- **수익 모델**: **Premium Career Suite** — 직무 강점, 커리어 경로 추천, 역할별 설명 등 유료 리포트.
- **가져올 것**: 슬라이더 문항 UX / 결과 무료 공개 후 프리미엄 얹기 / 유형별 랜딩페이지 SEO 전략.

### 2.2 Truity
- **URL**: https://www.truity.com/
- **규모**: 5,000만+ 사용자. Enneagram 테스트는 미국에서 가장 인기(1,000만+ 응시).
- **강점**: MBTI(TypeFinder)·에니어그램·DISC·Holland Code(직업흥미) 등 **다양한 프레임워크를 한 사이트에** 모아 포트폴리오화. 커리어 자산진단에 특화.
- **가져올 것**: 하나의 유형 테스트만이 아니라 **여러 검사를 묶은 "테스트 허브"** 전략. 결과 요약 무료 + 상세 PDF 리포트 유료.

### 2.3 The Enneagram Institute
- **URL**: https://www.enneagraminstitute.com/
- **포지션**: 에니어그램 학술 권위의 원천(리소-허드슨, **RHETI** 공식 검사). 신뢰도·정통성 브랜딩의 교과서.
- **가져올 것**: 에니어그램 콘텐츠를 다룰 때 **이론적 출처를 명확히 인용**하는 신뢰 확보 방식(한국 유저도 "정확도"를 중시).

### 2.4 Crystal (Crystal Knows)
- **URL**: https://www.crystalknows.com/
- **포지션**: B2B/영업·팀 협업용 성격 예측. 무료 테스트를 리드 확보 깔때기로 사용.
- **가져올 것**: 무료 테스트를 **리드 제너레이션 훅**으로 쓰는 B2B 확장 가능성.

### 2.5 IDRlabs / Humanmetrics (참고)
- 간결한 문항 + 즉시 결과 + 그래프 시각화. 군더더기 없는 **저비용 MVP 레퍼런스**.

---

## 3. 한국 벤치마크

### 3.1 푸망 (Poomang) ⭐ 바이럴형 최우선 벤치마크
- **URL**: https://poomang.com/
- **운영**: (주)푸른망아지, 2020.7 설립. MZ·잘파세대 타깃.
- **핵심 수치**: 콘텐츠 평균 **35만 플레이**, '연애고자 테스트' **169만 플레이**(최대 기록).
- **구조적 강점**:
  - **심테공방**: 유저가 직접 테스트를 만드는 UGC 시스템 → 콘텐츠 무한 공급·리텐션.
  - **시리즈화**: 연애심리·성격유형·퍼스널컬러·아우라·공감능력 등 테마 다양화로 계속 신규 유입.
  - **카톡/SNS 공유 최적화**: 결과 카드가 공유 자체를 목적으로 디자인됨 → 무료 바이럴.
- **수익 모델**: **브랜디드 테스트** — 기업 광고를 배너가 아닌 "참여형 테스트"로 제작(MZ 참여율↑). 배너 대비 효과적이라는 것이 세일즈 포인트.
- **가져올 것**: 결과 카드의 공유 UX / 브랜디드 테스트라는 광고 수익 모델 / 시리즈로 신규 테스트 지속 출시하는 콘텐츠 파이프라인.

### 3.2 테스트잇 (Test It!)
- **URL**: https://test-it.co.kr/
- MBTI·성격·연애·얼굴인식 테스트 등 **재미 위주 종합 테스트 포털**. 가입 없이 즉시 플레이.

### 3.3 테몬 (Temon)
- **URL**: https://temon.kr/
- 무료 테스트 모음, 주제별(MBTI·성격·취향) 분류. **가입 없이 2~3분** 컷 → 낮은 진입장벽이 강점.

### 3.4 한국MBTI심리연구소
- **URL**: https://kmbti.co.kr/
- 공식성·정통성 강조. MBTI 검사·궁합 등. **신뢰도 브랜딩** 참고.

### 3.5 에니어그램해라 / 테스트하로
- **URL**: https://testharo.com/, 에니어그램해라 연구소(리소-허드슨 공식 자격)
- 한국어 에니어그램 정통 검사 레퍼런스. 다국어(en) 대응도 참고.

---

## 4. 공통 UX·기능 패턴 (설계 체크리스트)

문항 흐름과 결과 페이지는 아래 검증된 패턴을 따르는 것이 안전하다.

**A. 응답 흐름**
- [ ] **진행률 바(progress bar)**: 다단계 폼의 이탈 방지 필수 요소. 남은 문항 수를 항상 노출.
- [ ] **점진적 노출(progressive disclosure)**: 한 번에 1~소수 문항만 → 인지 부담↓, 완주율↑.
- [ ] 리커트/슬라이더 vs 양자택일: 진지형은 슬라이더(정밀), 바이럴형은 2지선다(속도).
- [ ] 중간 저장/재개(긴 테스트일 경우), 가입 없이 응시 가능.

**B. 결과 페이지 (제품의 핵심)**
- [ ] **유형 캐릭터화**: 별명·일러스트·컬러 → "나를 표현" 욕구 자극(16P의 핵심 성공 요인).
- [ ] **무료로 충분히 공개** 후, 심층 분석만 프리미엄. 결과를 가두면 공유 동력이 죽는다.
- [ ] **공유 카드**: 카톡/인스타 스토리 규격에 맞춘 이미지 자동 생성(OG 태그·동적 이미지).
- [ ] 궁합/관계 기능: "친구와 비교", "우리 궁합" → 재공유·재유입 루프.

**C. 리텐션 / 그로스**
- [ ] 유형별 SEO 랜딩페이지(16P·Truity의 최대 트래픽 자산).
- [ ] 신규 테스트 정기 출시(푸망식 시리즈 전략).
- [ ] 결과 저장·계정으로 재검사 히스토리(연간 재검사 동기).

---

## 5. 수익 모델 옵션

| 모델 | 방식 | 참고 사이트 | deepinme 적합도 |
|---|---|---|---|
| **Freemium 리포트** | 기본 무료 + 심층 PDF/커리어 리포트 유료 | 16P, Truity | 진지형 지향 시 ◎ |
| **브랜디드 테스트** | 기업 광고를 참여형 테스트로 제작 | 푸망 | 트래픽 확보 후 ◎ |
| **광고(디스플레이)** | 결과/문항 사이 광고 노출 | 테스트잇, 테몬 | 초기 손쉬움, 단가 낮음 |
| **B2B 리드** | 무료 테스트 → 팀/영업 유료 전환 | Crystal | 장기 확장 옵션 |

> **권장 초기 전략**: 결과 무료 공개 + 공유 카드로 **바이럴 유입** 먼저 확보 → 트래픽 위에 프리미엄 리포트(freemium) 얹기. 광고는 트래픽이 붙은 뒤 브랜디드로 전환.

---

## 6. deepinme를 위한 핵심 제언 (Top 5)

1. **하이브리드 포지션**: 16Personalities의 신뢰도·심층 콘텐츠 + 푸망의 공유성·시리즈 전략을 결합.
2. **결과를 가두지 말 것**: 무료 결과 → 공유 → 유입 루프가 이 카테고리의 성장 엔진. 프리미엄은 그 "위에" 얹는다.
3. **공유 카드 = 1순위 기능**: 카톡·인스타 규격 동적 결과 이미지 + OG 태그를 초기부터 설계.
4. **유형별 랜딩페이지 SEO**: 애니어그램 9유형 × MBTI 16유형 각각 독립 페이지 → 장기 검색 트래픽 자산.
5. **정통성 인용**: 에니어그램(리소-허드슨/RHETI)·MBTI 이론 출처를 명시해 "정확도" 신뢰 확보. README의 철학("나를 더 잘 설명")과도 정합.

---

## 출처 (Sources)

**글로벌**
- [16Personalities](https://www.16personalities.com/) · [Free test](https://www.16personalities.com/free-personality-test) · [Premium Career Suite](https://www.16personalities.com/premium/premium-report)
- [Truity](https://www.truity.com/) · [Enneagram Test](https://www.truity.com/test/enneagram-personality-test) · [TypeFinder](https://www.truity.com/test/type-finder-personality-test-new)
- [The Enneagram Institute](https://www.enneagraminstitute.com/)
- [Crystal Knows — 성격 테스트 비교](https://www.crystalknows.com/best-personality-test) · [Enneagram Test](https://www.crystalknows.com/enneagram-test)
- [IDRlabs Enneagram](https://www.idrlabs.com/enneagram/test.php)

**한국**
- [푸망 Poomang](https://poomang.com/) · [심테공방](https://poomang.com/gongbang/tests) · [제휴 문의](https://poomang.com/collaboration) · [나무위키](https://namu.wiki/w/%ED%91%B8%EB%A7%9D) · [MZ세대 심리테스트 기사(다음)](https://v.daum.net/v/20210610070001110)
- [테스트잇](https://test-it.co.kr/) · [테몬](https://temon.kr/) · [한국MBTI심리연구소](https://kmbti.co.kr/) · [테스트하로](https://testharo.com/)

**UX 패턴**
- [Progress Bar UX (Page Flows)](https://pageflows.com/resources/progress-bar-ux/) · [UX Design Patterns (Page Flows)](https://pageflows.com/resources/ux-design-patterns-the-complete-guide/)
