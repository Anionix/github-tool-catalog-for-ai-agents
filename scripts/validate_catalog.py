#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter
from urllib.parse import urlparse

from jsonschema import Draft202012Validator, FormatChecker

from catalog_common import SCHEMA_PATH, load_catalog


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    catalog = load_catalog()
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(catalog), key=lambda error: list(error.path))
    if errors:
        for error in errors:
            path = ".".join(str(part) for part in error.path) or "<root>"
            print(f"schema error at {path}: {error.message}", file=sys.stderr)
        return 1

    categories = set(catalog["categories"])
    tools = catalog["tools"]

    names = Counter(tool["name"] for tool in tools)
    repos = Counter(tool["repo"].lower() for tool in tools)
    urls = Counter(tool["url"].rstrip("/") for tool in tools)

    duplicates = [name for name, count in names.items() if count > 1]
    if duplicates:
        fail(f"duplicate tool names: {', '.join(sorted(duplicates))}")

    duplicate_repos = [repo for repo, count in repos.items() if count > 1]
    if duplicate_repos:
        fail(f"duplicate repos: {', '.join(sorted(duplicate_repos))}")

    duplicate_urls = [url for url, count in urls.items() if count > 1]
    if duplicate_urls:
        fail(f"duplicate URLs: {', '.join(sorted(duplicate_urls))}")

    for tool in tools:
        if tool["category"] not in categories:
            fail(f"{tool['name']} uses unknown category {tool['category']!r}")

        parsed = urlparse(tool["url"])
        if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
            fail(f"{tool['name']} must use a https://github.com URL")

        expected_prefix = f"https://github.com/{tool['repo']}".lower()
        if not tool["url"].lower().rstrip("/").startswith(expected_prefix):
            fail(f"{tool['name']} url does not match repo {tool['repo']}")

    print(f"catalog ok: {len(tools)} tools, {len(categories)} categories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
