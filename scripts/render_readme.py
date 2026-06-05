#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import textwrap
from collections import defaultdict

from catalog_common import README_PATH, load_catalog, sort_tools


STATUS_LABELS = {
    "recommended": "Recommended",
    "situational": "Situational",
    "watch": "Watch",
    "avoid": "Avoid",
}

RISK_LABELS = {
    "low": "Low",
    "medium": "Medium",
    "high": "High",
}


def md_escape(value: object) -> str:
    text = str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def render_table(tools: list[dict[str, object]]) -> list[str]:
    lines = [
        "| Tool | Status | Agent | Human | Risk | Install |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for tool in sort_tools(tools):
        install = f"`{md_escape(tool['install'])}`"
        lines.append(
            "| "
            f"[{md_escape(tool['name'])}]({md_escape(tool['url'])})"
            f" | {STATUS_LABELS[str(tool['recommended_status'])]}"
            f" | {md_escape(tool['agent_usefulness'])}"
            f" | {md_escape(tool['human_usefulness'])}"
            f" | {RISK_LABELS[str(tool['risk'])]}"
            f" | {install}"
            " |"
        )
    return lines


def render_readme() -> str:
    catalog = load_catalog()
    tools = catalog["tools"]
    categories = catalog["categories"]
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for tool in tools:
        grouped[tool["category"]].append(tool)

    lines: list[str] = []
    lines.extend(
        [
            "# Awesome GitHub Tools",
            "",
            "A strict, machine-readable catalog of GitHub-adjacent tools for AI agents and the humans supervising them.",
            "",
            "> This README is generated from `catalog/tools.yml`. Edit the catalog, then run `python scripts/render_readme.py`.",
            "",
            "## Selection Criteria",
            "",
            "- Helps AI agents or maintainers work with GitHub, pull requests, CI, browser testing, code intelligence, documentation, or proof workflows.",
            "- Has a public source or documentation URL.",
            "- Can be classified by usefulness, operational risk, and recommendation status.",
            "- Uses `watch` for promising tools that are preview-only, broad-permission, or not yet a good default.",
            "",
            "## Governance and Contributions",
            "",
            "- See `CONTRIBUTING.md` before opening issues or pull requests.",
            "- See `docs/curation-governance.md` for inclusion, removal, taxonomy, evidence, and recommendation rules.",
            "- See `docs/maintenance.md` for refresh cadence, automation policy, and public roadmap rules.",
            "- See `docs/pr-review-checklist.md` for maintainer review expectations.",
            "",
            "## Recommendation Legend",
            "",
            "| Status | Meaning |",
            "| --- | --- |",
            "| Recommended | Good default for the right workflow. |",
            "| Situational | Useful when the workflow clearly needs it. |",
            "| Watch | Promising, preview-only, heavy, or not yet a safe default. |",
            "| Avoid | Known mismatch for this catalog's default recommendations. |",
            "",
            "## Quick Picks",
            "",
        ]
    )

    recommended = [tool for tool in tools if tool["recommended_status"] == "recommended"]
    lines.extend(render_table(recommended))
    lines.append("")
    lines.append("## Catalog")
    lines.append("")

    for category in categories:
        lines.append(f"### {category}")
        lines.append("")
        category_tools = grouped.get(category, [])
        if not category_tools:
            lines.append("_No entries yet._")
            lines.append("")
            continue
        for tool in sort_tools(category_tools):
            lines.append(f"#### [{tool['name']}]({tool['url']})")
            lines.append("")
            lines.append(textwrap.fill(str(tool["summary"]), width=100))
            lines.append("")
            lines.append(f"- Repo: `{tool['repo']}`")
            lines.append(f"- Kind: `{tool['kind']}`")
            lines.append(f"- Status: `{tool['recommended_status']}`")
            lines.append(f"- Agent usefulness: `{tool['agent_usefulness']}`")
            lines.append(f"- Human usefulness: `{tool['human_usefulness']}`")
            lines.append(f"- Risk: `{tool['risk']}`")
            lines.append(f"- Install: `{tool['install']}`")
            if tool.get("notes"):
                lines.append(f"- Notes: {tool['notes']}")
            lines.append("")

    lines.extend(
        [
            "## Validation",
            "",
            "```bash",
            "python scripts/validate_catalog.py",
            "python scripts/render_readme.py --check",
            "python scripts/check_links.py",
            "```",
            "",
            "## License",
            "",
            "CC0-1.0. See `LICENSE`.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if README.md is not up to date")
    args = parser.parse_args()

    rendered = render_readme()
    if args.check:
        current = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""
        if current != rendered:
            print("README.md is out of date. Run: python scripts/render_readme.py", file=sys.stderr)
            return 1
        print("README.md is up to date")
        return 0

    README_PATH.write_text(rendered, encoding="utf-8")
    print(f"wrote {README_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
