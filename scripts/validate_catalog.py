#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from urllib.parse import urlparse

from jsonschema import Draft202012Validator, FormatChecker

from catalog_common import SCHEMA_PATH, load_catalog, slugify


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9_]+"),
    re.compile(r"github_pat_[A-Za-z0-9_]+"),
    re.compile(r"sk-[A-Za-z0-9_\\-]+"),
    re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
]


def validate_command(tool_name: str, command: str) -> None:
    if "|" in command:
        fail(f"{tool_name} install command must not contain shell pipes")
    lowered = command.lower()
    if "curl " in lowered and " sh" in lowered:
        fail(f"{tool_name} install command must not use curl-to-shell patterns")
    for pattern in SECRET_PATTERNS:
        if pattern.search(command):
            fail(f"{tool_name} install command appears to contain a literal secret")


def kit_tools(kit: dict[str, object]) -> list[str]:
    return [*kit["core_tools"], *kit["optional_tools"]]


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
    starter_kits = catalog["starter_kits"]
    evaluation_kits = catalog["evaluation_kits"]

    ids = Counter(tool["id"] for tool in tools)
    names = Counter(tool["name"] for tool in tools)
    repos = Counter(tool["repo"].lower() for tool in tools)
    urls = Counter(tool["url"].rstrip("/") for tool in tools)

    duplicate_ids = [tool_id for tool_id, count in ids.items() if count > 1]
    if duplicate_ids:
        fail(f"duplicate tool ids: {', '.join(sorted(duplicate_ids))}")

    duplicates = [name for name, count in names.items() if count > 1]
    if duplicates:
        fail(f"duplicate tool names: {', '.join(sorted(duplicates))}")

    duplicate_repos = [repo for repo, count in repos.items() if count > 1]
    if duplicate_repos:
        fail(f"duplicate repos: {', '.join(sorted(duplicate_repos))}")

    duplicate_urls = [url for url, count in urls.items() if count > 1]
    if duplicate_urls:
        fail(f"duplicate URLs: {', '.join(sorted(duplicate_urls))}")

    category_ids = Counter(slugify(category) for category in catalog["categories"])
    duplicate_category_ids = [category_id for category_id, count in category_ids.items() if count > 1]
    if duplicate_category_ids:
        fail(f"duplicate generated category ids: {', '.join(sorted(duplicate_category_ids))}")

    tools_by_id = {tool["id"]: tool for tool in tools}
    used_categories = set()

    for tool in tools:
        if tool["category"] not in categories:
            fail(f"{tool['name']} uses unknown category {tool['category']!r}")
        used_categories.add(tool["category"])

        parsed = urlparse(tool["url"])
        if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
            fail(f"{tool['name']} must use a https://github.com URL")

        expected_url = f"https://github.com/{tool['repo']}".lower()
        if tool["url"].lower().rstrip("/") != expected_url:
            fail(f"{tool['name']} url does not match repo {tool['repo']}")

        if tool["install_methods"][0]["command"] != tool["install"]:
            fail(f"{tool['name']} install must match install_methods[0].command")
        validate_command(tool["name"], tool["install"])
        for method in tool["install_methods"]:
            validate_command(tool["name"], method["command"])

        status = tool["recommended_status"]
        daily_use = tool["practical"]["daily_use"]
        guardrails = set(tool["practical"]["guardrails"])
        if status in {"watch", "avoid"} and daily_use == "routine":
            fail(f"{tool['name']} cannot be routine when status is {status}")
        if status == "avoid" and daily_use != "not_default":
            fail(f"{tool['name']} must be not_default when status is avoid")
        if status == "recommended" and tool["risk"] == "high" and not guardrails:
            fail(f"{tool['name']} is high-risk recommended and needs guardrails")
        if tool["risk"] == "high" and not tool["practical"]["cautious_start"]:
            fail(f"{tool['name']} is high-risk and needs cautious_start")

        for pair in tool["practical"]["pairs_with"]:
            other_id = pair["tool_id"]
            if other_id == tool["id"]:
                fail(f"{tool['name']} cannot pair with itself")
            if other_id not in tools_by_id:
                fail(f"{tool['name']} pairs_with unknown tool id {other_id}")
            if tools_by_id[other_id]["recommended_status"] == "avoid":
                fail(f"{tool['name']} pairs_with avoid tool {other_id}")

    unused_categories = sorted(categories - used_categories)
    if unused_categories:
        fail(f"unused categories: {', '.join(unused_categories)}")

    for kit_group_name, kits in (("starter_kits", starter_kits), ("evaluation_kits", evaluation_kits)):
        kit_ids = Counter(kit["id"] for kit in kits)
        duplicate_kit_ids = [kit_id for kit_id, count in kit_ids.items() if count > 1]
        if duplicate_kit_ids:
            fail(f"duplicate {kit_group_name} ids: {', '.join(sorted(duplicate_kit_ids))}")
        for kit in kits:
            for tool_id in kit_tools(kit):
                if tool_id not in tools_by_id:
                    fail(f"{kit_group_name}.{kit['id']} references unknown tool id {tool_id}")
                tool = tools_by_id[tool_id]
                status = tool["recommended_status"]
                if status == "avoid":
                    fail(f"{kit_group_name}.{kit['id']} must not reference avoid tool {tool_id}")
                if kit_group_name == "starter_kits" and status == "watch":
                    fail(f"starter_kits.{kit['id']} must not reference watch tool {tool_id}")
                if tool["risk"] == "high" and not kit["guardrails"]:
                    fail(f"{kit_group_name}.{kit['id']} references high-risk {tool_id} without guardrails")
            overlap = set(kit["core_tools"]) & set(kit["optional_tools"])
            if overlap:
                fail(f"{kit_group_name}.{kit['id']} repeats tools across core and optional: {', '.join(sorted(overlap))}")

    print(f"catalog ok: {len(tools)} tools, {len(categories)} categories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
