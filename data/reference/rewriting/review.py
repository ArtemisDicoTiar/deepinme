#!/usr/bin/env python3
"""리라이팅 검토 도구 — `text_ko_friendly`의 before→after 비교표 + 린트.

사용법:
    python3 data/reference/rewriting/review.py [파일 ...]

인자로 파일을 주면 그 파일들만, 안 주면 data/translations/ 아래
`text_ko_friendly`를 가진 모든 items.*.json을 훑는다.

출력: 문항별 (text_en → text → text_ko_friendly) 표. text와 다르게 리라이팅된
문항은 ▲로 표시. 이어서 린트(빈 필드/양극형 ↔ 유실/커버리지)를 요약한다.
스키마 검증은 별도(reference/schema/validate.py).
"""
from __future__ import annotations

import glob
import json
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def find_files(args: list[str]) -> list[str]:
    if args:
        return args
    pat = os.path.join(REPO_ROOT, "data", "translations", "**", "items.*.json")
    hits = []
    for path in sorted(glob.glob(pat, recursive=True)):
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        if any("text_ko_friendly" in it for it in data.get("items", [])):
            hits.append(path)
    return hits


def is_bipolar(text: str) -> bool:
    return " ↔ " in text


def review_file(path: str) -> tuple[int, int, list[str]]:
    """반환: (리라이팅된 문항 수, 전체 문항 수, 린트 경고 목록)."""
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    items = data.get("items", [])
    rel = os.path.relpath(path, REPO_ROOT)
    warnings: list[str] = []
    changed = covered = 0

    print(f"\n\033[1m{rel}\033[0m  ({data.get('_meta', {}).get('instrument', '?')})")
    print("─" * 80)
    for it in items:
        num = it.get("num", "")
        text = it.get("text", "")
        friendly = it.get("text_ko_friendly")
        en = it.get("text_en", "")
        if friendly is None:
            continue
        covered += 1
        if not friendly.strip():
            warnings.append(f"  [{num}] text_ko_friendly가 비어 있음")
            continue
        if is_bipolar(text) and not is_bipolar(friendly):
            warnings.append(f"  [{num}] 원문은 양극형(↔)인데 리라이팅에 ' ↔ ' 없음")
        mark = " "
        if friendly != text:
            changed += 1
            mark = "\033[33m▲\033[0m"
        print(f"{mark} [{num}] {en}")
        print(f"    번역   : {text}")
        if friendly != text:
            print(f"    친화   : \033[32m{friendly}\033[0m")

    total = len(items)
    print("─" * 80)
    print(f"  리라이팅 {changed}개 변경 · {covered}/{total} 문항 커버 · "
          f"미커버 {total - covered}개")
    return changed, covered, warnings


def main() -> int:
    files = find_files(sys.argv[1:])
    if not files:
        print("text_ko_friendly를 가진 파일이 없습니다.")
        return 0

    all_warnings: list[str] = []
    for path in files:
        _, _, warns = review_file(path)
        all_warnings.extend(f"{os.path.relpath(path, REPO_ROOT)}{w}" for w in warns)

    print("\n" + "=" * 80)
    if all_warnings:
        print(f"\033[31m린트 경고 {len(all_warnings)}건:\033[0m")
        for w in all_warnings:
            print(w)
        return 1
    print("\033[32m린트 통과 — 경고 없음.\033[0m")
    return 0


if __name__ == "__main__":
    sys.exit(main())
