#!/usr/bin/env python3
from __future__ import annotations

import sys
import time
import urllib.error
import urllib.request
from argparse import ArgumentParser
from urllib.parse import urlparse

from catalog_common import load_catalog


def check_url(url: str) -> tuple[bool, str]:
    headers = {"User-Agent": "Anionix-awesome-github-tools-link-check/1.0"}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                if 200 <= response.status < 400:
                    return True, str(response.status)
                return False, str(response.status)
        except urllib.error.HTTPError as error:
            if method == "HEAD" and error.code in {403, 405}:
                continue
            return False, str(error.code)
        except urllib.error.URLError as error:
            last = str(error.reason)
            time.sleep(1)
    return False, last if "last" in locals() else "unknown error"


def check_syntax(url: str) -> tuple[bool, str]:
    parsed = urlparse(url)
    if parsed.scheme != "https":
        return False, "scheme must be https"
    if not parsed.netloc:
        return False, "missing host"
    return True, "syntax"


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--live", action="store_true", help="perform network checks")
    args = parser.parse_args()

    catalog = load_catalog()
    urls = sorted({tool["url"] for tool in catalog["tools"]})
    failed: list[tuple[str, str]] = []

    for url in urls:
        ok, detail = check_url(url) if args.live else check_syntax(url)
        status = "ok" if ok else "fail"
        print(f"{status}: {url} ({detail})")
        if not ok:
            failed.append((url, detail))

    if failed:
        print("\nfailed links:", file=sys.stderr)
        for url, detail in failed:
            print(f"- {url}: {detail}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
