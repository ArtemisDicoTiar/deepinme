# 문항 리라이팅 어노테이터

`data/translations/ko/`(원문·번역이 나란히 있는 15개 데이터셋, 976문항) 전체를 브라우저에서 열어
**원문(text_en) / 번역(text) / 친화(text_ko_friendly)**를 비교하고, 문항마다 최종 한국어 문구를
고르거나 직접 입력해 확정하는 로컬 도구다. 외부 의존성 없이 파이썬 표준 라이브러리만 쓴다.

## 실행

```bash
python3 tools/annotator/server.py            # 기본 포트 8420
# 다른 포트를 쓰려면: python3 tools/annotator/server.py --port 8500
```

브라우저에서 `http://localhost:8420` 열기. `Ctrl+C`로 종료.

## 사용법

1. 왼쪽에서 데이터셋을 고른다(진행률 = 검토 완료 문항 수 / 전체).
2. 문항마다 라디오로 고른다:
   - **친화(추천)** — `text_ko_friendly` 제안값(있는 경우). 없으면 비활성화.
   - **번역 사용** — `text` 값 그대로.
   - **직접 입력** — 자유롭게 새로 쓴다.
3. 아래 텍스트 박스에서 골라진 문구를 그대로 두거나 손으로 다듬는다.
4. **저장**을 누르면 그 문항의 `text_ko_friendly`(+ 선택 근거 `text_ko_friendly_source`,
   검토 여부 `text_ko_friendly_reviewed: true`)가 **원본 JSON 파일에 즉시 기록**된다.
5. 기본은 "미검토만 보기" — 저장한 문항은 목록에서 사라진다. 전체를 다시 보려면 상단 토글 해제.

⚠ 양극형 문항(`A ↔ B`)은 저장 전에 ` ↔ ` 구분자가 빠지면 경고가 뜬다(저장은 막지 않음 — 최종 판단은 어노테이터 몫).

## 무엇을 지켜야 하는지 (리라이팅 원칙)

문구를 고치기 전에 [`../../data/reference/rewriting/README.md`](../../data/reference/rewriting/README.md)를 참고한다.
핵심: 번역투는 걷어내되 **측정 구성개념·채점 방향(`keyed`)·난이도·양극형 형식은 그대로** 유지.

## 저장 후 확인

```bash
python3 data/reference/schema/validate.py          # 스키마 통과 확인
python3 data/reference/rewriting/review.py <파일>   # before/after 표로 재검토
```

## 구조

```
tools/annotator/
├── server.py        # stdlib HTTP 서버 + API (GET /api/files, /api/file, POST /api/item)
├── static/
│   ├── index.html
│   ├── app.js        # 상태·렌더링·저장 로직 (프레임워크 없음)
│   └── style.css      # 라이트/다크 모드 대응
└── README.md
```

`POST /api/item`은 파일을 읽어 해당 `num` 항목만 갱신하고 원자적으로 다시 쓴다
(`os.replace`로 임시 파일 교체). `file_id`는 `data/translations/ko/` 밖으로 못 나가도록
검증한다(경로 탈출 방지). 범위는 `translations/ko/`로 고정되어 있다 —
`raw/`(원본, 대조 언어 쌍 없음)나 다른 언어는 대상이 아니다.
