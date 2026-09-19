#!/usr/bin/env python3
"""Tiny dashboard: serves index.html and runs widget commands on demand."""
import json
import subprocess
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).parent
WIDGETS = json.loads((ROOT / "widgets.json").read_text())


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/widgets":
            return self.reply(200, json.dumps(WIDGETS).encode(), "application/json")
        if url.path == "/run":
            return self.run_widget(parse_qs(url.query).get("name", [""])[0])
        if url.path in ("/", "/index.html"):
            return self.reply(200, (ROOT / "index.html").read_bytes(), "text/html; charset=utf-8")
        self.reply(404, b"not found", "text/plain")

    def run_widget(self, name):
        widget = next((w for w in WIDGETS if w["name"] == name), None)
        if not widget:
            return self.reply(404, b'{"error":"unknown widget"}', "application/json")
        start = time.time()
        try:
            done = subprocess.run(
                widget["command"], shell=True, capture_output=True, text=True,
                timeout=widget.get("timeout", 30), cwd=widget.get("cwd") or ROOT,
            )
            output, code = done.stdout + done.stderr, done.returncode
        except subprocess.TimeoutExpired:
            output, code = "timed out", 124
        body = json.dumps({"output": output.rstrip(), "code": code,
                           "ms": int((time.time() - start) * 1000)}).encode()
        self.reply(200, body, "application/json")

    def reply(self, code, body, ctype):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Serve the local dashboard.")
    ap.add_argument("-p", "--port", type=int, default=8787)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    print(f"dashboard: http://{args.host}:{args.port}")
    ThreadingHTTPServer((args.host, args.port), Handler).serve_forever()