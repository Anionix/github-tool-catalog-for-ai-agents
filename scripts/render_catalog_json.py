#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

from catalog_common import CATALOG_JSON_PATH, CATALOG_JSON_SCHEMA_PATH, CATALOG_PATH, load_catalog, slugify


def render_tool(tool: dict[str, Any], category_ids: dict[str, str]) -> dict[str, Any]:
    return {
        "id": tool["id"],
        "name": tool["name"],
        "repo": tool["repo"],
        "url": tool["url"],
        "kind": tool["kind"],
        "category_id": category_ids[tool["category"]],
        "category": tool["category"],
        "summary": tool["summary"],
        "ratings": {
            "agent": tool["agent_usefulness"],
            "human": tool["human_usefulness"],
            "risk": tool["risk"],
            "status": tool["recommended_status"],
        },
        "install": {
            "display": tool["install"],
            "methods": tool["install_methods"],
        },
        "practical": tool["practical"],
        "notes": tool.get("notes", ""),
        "evidence": tool["evidence"],
    }


def render_catalog_json() -> str:
    catalog = load_catalog()
    category_ids = {name: slugify(name) for name in catalog["categories"]}
    source_bytes = CATALOG_PATH.read_bytes()

    payload = {
        "schema_version": catalog["schema_version"],
        "source": {
            "path": str(CATALOG_PATH.relative_to(CATALOG_PATH.parents[1])),
            "sha256": hashlib.sha256(source_bytes).hexdigest(),
            "schema": str(CATALOG_JSON_SCHEMA_PATH.relative_to(CATALOG_JSON_SCHEMA_PATH.parents[1])),
        },
        "categories": [
            {"id": category_ids[name], "name": name, "order": index + 1}
            for index, name in enumerate(catalog["categories"])
        ],
        "tools": [render_tool(tool, category_ids) for tool in catalog["tools"]],
        "starter_kits": catalog["starter_kits"],
        "evaluation_kits": catalog["evaluation_kits"],
    }
    return json.dumps(payload, indent=2, ensure_ascii=True) + "\n"


def validate_rendered_catalog_json(rendered: str) -> int:
    payload = json.loads(rendered)
    schema = json.loads(CATALOG_JSON_SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(payload), key=lambda error: list(error.path))
    if not errors:
        return 0
    for error in errors:
        path = ".".join(str(part) for part in error.path) or "<root>"
        print(f"catalog JSON schema error at {path}: {error.message}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if dist/catalog.v2.json is not up to date")
    args = parser.parse_args()

    rendered = render_catalog_json()
    schema_status = validate_rendered_catalog_json(rendered)
    if schema_status:
        return schema_status
    if args.check:
        current = CATALOG_JSON_PATH.read_text(encoding="utf-8") if CATALOG_JSON_PATH.exists() else ""
        if current != rendered:
            print("dist/catalog.v2.json is out of date. Run: python scripts/render_catalog_json.py", file=sys.stderr)
            return 1
        print("dist/catalog.v2.json is up to date")
        return 0

    CATALOG_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_JSON_PATH.write_text(rendered, encoding="utf-8")
    print(f"wrote {CATALOG_JSON_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
