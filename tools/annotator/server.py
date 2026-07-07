#!/usr/bin/env python3
"""deepinme 문항 리라이팅 어노테이터 — 로컬 웹 서버.

data/translations/ko/**/items.*.ko.json (원문·번역이 나란히 있는 "번역" 데이터셋)을
브라우저에서 열어, 문항마다 원문(text_en)/번역(text)/친화(text_ko_friendly)를
비교하고 최종 한국어 문구를 고르거나 직접 입력해 저장하는 도구.

실행:
    python3 tools/annotator/server.py [--port 8420]
    브라우저에서 http://localhost:8420 열기

외부 의존성 없음 (표준 라이브러리만 사용).
"""
from __future__ import annotations

import argparse
import glob
import json
import mimetypes
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCOPE_DIR = os.path.join(REPO_ROOT, "data", "translations", "ko")
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

VALID_SOURCES = {"friendly", "translation", "custom"}

_write_lock = threading.Lock()


def list_dataset_files() -> list[str]:
    pat = os.path.join(SCOPE_DIR, "**", "items.*.json")
    return sorted(glob.glob(pat, recursive=True))


def file_id_for(path: str) -> str:
    return os.path.relpath(path, SCOPE_DIR).replace(os.sep, "/")


def resolve_file_id(file_id: str) -> str:
    """Resolve a file_id back to an absolute path, refusing to escape SCOPE_DIR."""
    if not file_id or ".." in file_id.split("/"):
        raise ValueError("invalid file id")
    path = os.path.abspath(os.path.join(SCOPE_DIR, file_id))
    if not (path == SCOPE_DIR or path.startswith(SCOPE_DIR + os.sep)):
        raise ValueError("path escapes scope")
    if not os.path.isfile(path):
        raise FileNotFoundError(file_id)
    return path


def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: str, data: dict) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.replace(tmp, path)


def file_summary(path: str) -> dict:
    data = load_json(path)
    items = data.get("items", [])
    reviewed = sum(1 for it in items if it.get("text_ko_friendly_reviewed"))
    friendly = sum(1 for it in items if it.get("text_ko_friendly"))
    return {
        "id": file_id_for(path),
        "instrument": data.get("_meta", {}).get("instrument", file_id_for(path)),
        "count": len(items),
        "reviewed": reviewed,
        "friendly_suggested": friendly,
    }


def insert_after(item: dict, anchor_keys: list[str], new_key: str, value) -> dict:
    """Return a copy of item with new_key=value inserted right after the first
    anchor key present (or appended at the end if none are present), preserving
    key order. If new_key already exists, just update its value in place."""
    if new_key in item:
        out = dict(item)
        out[new_key] = value
        return out
    out: dict = {}
    inserted = False
    for k, v in item.items():
        out[k] = v
        if not inserted and k in anchor_keys:
            out[new_key] = value
            inserted = True
    if not inserted:
        out[new_key] = value
    return out


def apply_annotation(item: dict, text: str, source: str) -> dict:
    item = insert_after(item, ["text_en", "text"], "text_ko_friendly", text)
    item = insert_after(item, ["text_ko_friendly"], "text_ko_friendly_source", source)
    item = insert_after(item, ["text_ko_friendly_source"], "text_ko_friendly_reviewed", True)
    return item


class Handler(BaseHTTPRequestHandler):
    server_version = "deepinme-annotator/1"

    def log_message(self, fmt, *args):  # quieter default logging
        pass

    def _send_json(self, status: int, payload) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_error_json(self, status: int, message: str) -> None:
        self._send_json(status, {"error": message})

    def _serve_static(self, url_path: str) -> None:
        rel = url_path.lstrip("/") or "index.html"
        path = os.path.abspath(os.path.join(STATIC_DIR, rel))
        if not (path == STATIC_DIR or path.startswith(STATIC_DIR + os.sep)) or not os.path.isfile(path):
            self._send_error_json(404, "not found")
            return
        ctype = mimetypes.guess_type(path)[0] or "application/octet-stream"
        with open(path, "rb") as fh:
            body = fh.read()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/files":
            files = [file_summary(p) for p in list_dataset_files()]
            self._send_json(200, {"files": files})
            return
        if parsed.path == "/api/file":
            qs = parse_qs(parsed.query)
            file_id = unquote((qs.get("id") or [""])[0])
            try:
                path = resolve_file_id(file_id)
            except (ValueError, FileNotFoundError) as exc:
                self._send_error_json(400, str(exc))
                return
            data = load_json(path)
            self._send_json(200, {"id": file_id, "meta": data.get("_meta", {}), "items": data.get("items", [])})
            return
        self._serve_static(parsed.path)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/api/item":
            self._send_error_json(404, "not found")
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            self._send_error_json(400, "invalid json body")
            return

        file_id = body.get("id", "")
        num = body.get("num")
        text = (body.get("text") or "").strip()
        source = body.get("source")

        if source not in VALID_SOURCES:
            self._send_error_json(400, f"source must be one of {sorted(VALID_SOURCES)}")
            return
        if not text:
            self._send_error_json(400, "text must not be empty")
            return
        if num is None:
            self._send_error_json(400, "num is required")
            return

        try:
            path = resolve_file_id(file_id)
        except (ValueError, FileNotFoundError) as exc:
            self._send_error_json(400, str(exc))
            return

        with _write_lock:
            data = load_json(path)
            items = data.get("items", [])
            idx = next((i for i, it in enumerate(items) if it.get("num") == num), None)
            if idx is None:
                self._send_error_json(404, f"item num={num!r} not found in {file_id}")
                return
            items[idx] = apply_annotation(items[idx], text, source)
            data["items"] = items
            save_json(path, data)

        self._send_json(200, {"ok": True, "item": items[idx], "summary": file_summary(path)})


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8420)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()

    n_files = len(list_dataset_files())
    print(f"deepinme annotator — {n_files}개 데이터셋 (data/translations/ko/)")
    print(f"http://{args.host}:{args.port} 에서 열기 (Ctrl+C 종료)")
    ThreadingHTTPServer((args.host, args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
