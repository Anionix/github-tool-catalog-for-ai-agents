#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import textwrap
from collections import defaultdict
from typing import Any

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

DAILY_USE_LABELS = {
    "routine": "Routine",
    "reviewed": "Reviewed",
    "specialist": "Specialist",
    "not_default": "Not default",
}


def md_escape(value: object) -> str:
    text = str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def tool_link(tool: dict[str, Any]) -> str:
    return f"[{md_escape(tool['name'])}]({md_escape(tool['url'])})"


def tool_links(tool_ids: list[str], tools_by_id: dict[str, dict[str, Any]]) -> str:
    return ", ".join(tool_link(tools_by_id[tool_id]) for tool_id in tool_ids)


def tags(values: list[str]) -> str:
    return ", ".join(f"`{md_escape(value)}`" for value in values)


def render_recommended_table(tools: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| Tool | Best for | Agent | Human | Risk | Caution |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for tool in sort_tools(tools):
        practical = tool["practical"]
        lines.append(
            "| "
            f"{tool_link(tool)}"
            f" | {tags(practical['best_for'])}"
            f" | {md_escape(tool['agent_usefulness'])}"
            f" | {md_escape(tool['human_usefulness'])}"
            f" | {RISK_LABELS[str(tool['risk'])]}"
            f" | {md_escape(practical['cautious_start'])}"
            " |"
        )
    return lines


def render_status_decision_table(tools: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| Tool | Status | Daily use | Risk | Why not a default |",
        "| --- | --- | --- | --- | --- |",
    ]
    for tool in sort_tools(tools):
        practical = tool["practical"]
        lines.append(
            "| "
            f"{tool_link(tool)}"
            f" | {STATUS_LABELS[str(tool['recommended_status'])]}"
            f" | {DAILY_USE_LABELS[str(practical['daily_use'])]}"
            f" | {RISK_LABELS[str(tool['risk'])]}"
            f" | {md_escape(tool.get('notes') or practical['cautious_start'])}"
            " |"
        )
    return lines


def render_kit(kit: dict[str, Any], tools_by_id: dict[str, dict[str, Any]]) -> list[str]:
    lines = [
        f"### {kit['title']}",
        "",
        str(kit["purpose"]),
        "",
        f"- Core: {tool_links(kit['core_tools'], tools_by_id)}",
    ]
    if kit["optional_tools"]:
        lines.append(f"- Optional: {tool_links(kit['optional_tools'], tools_by_id)}")
    lines.append(f"- Caution: {kit['caution']}")
    lines.append(f"- Guardrails: {tags(kit['guardrails'])}")
    lines.append("- Install:")
    for tool_id in [*kit["core_tools"], *kit["optional_tools"]]:
        tool = tools_by_id[tool_id]
        lines.append(f"  - `{tool['install']}`")
    lines.append("")
    return lines


def render_daily_workflows(tools_by_id: dict[str, dict[str, Any]]) -> list[str]:
    gh = tool_link(tools_by_id["github-cli"])
    github_mcp = tool_link(tools_by_id["github-mcp-server"])
    serena = tool_link(tools_by_id["serena"])
    context7 = tool_link(tools_by_id["context7"])
    playwright = tool_link(tools_by_id["playwright-mcp"])
    chrome = tool_link(tools_by_id["chrome-devtools-mcp"])
    lazygit = tool_link(tools_by_id["lazygit"])
    delta = tool_link(tools_by_id["delta"])
    lean = tool_link(tools_by_id["lean-lsp-mcp"])
    gh_dash = tool_link(tools_by_id["gh-dash"])
    gh_stack = tool_link(tools_by_id["gh-stack"])
    gh_aw = tool_link(tools_by_id["github-agentic-workflows"])
    copilot_cli = tool_link(tools_by_id["github-copilot-cli"])
    return [
        "## Daily Workflows",
        "",
        f"- Agent PR review: inspect issue and PR state with {github_mcp} or {gh}, navigate code with {serena}, fetch current docs with {context7}, validate behavior with {playwright}, then read back checks with {gh}.",
        f"- Human PR review: use {gh} for PR state, {delta} for readable diffs, {lazygit} for local Git actions, and {gh_dash} only when a terminal review queue helps.",
        f"- Browser validation: start with {playwright}; add {chrome} when DevTools-level network, console, performance, or screenshot diagnostics are needed.",
        f"- Lean or proof repository: bind project scope for {lean}, use {gh} for PR/check readback, and use {delta} for proof diff review.",
        f"- Agentic workflow evaluation: keep {gh_stack}, {gh_aw}, and {copilot_cli} in sandbox or explicitly reviewed workflows before routine rollout.",
        "",
    ]


def render_readme() -> str:
    catalog = load_catalog()
    tools = catalog["tools"]
    categories = catalog["categories"]
    starter_kits = catalog["starter_kits"]
    evaluation_kits = catalog["evaluation_kits"]
    tools_by_id = {tool["id"]: tool for tool in tools}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for tool in tools:
        grouped[tool["category"]].append(tool)

    lines: list[str] = []
    lines.extend(
        [
            "# GitHub Tool Catalog for AI Agents",
            "",
            "A small, conservative, machine-readable catalog of GitHub-adjacent tools for AI agents and the humans supervising them.",
            "",
            "> This README is generated from `catalog/tools.yml`. Edit the catalog, then run `python scripts/render_readme.py`.",
            "",
            "## Start Here",
            "",
            "| Workflow | Use first | Add when | Caution |",
            "| --- | --- | --- | --- |",
            "| Agent repo maintenance | Agent repo maintenance kit | Browser validation kit for UI behavior | Limit tokens and require human approval for writes. |",
            "| Human daily review | Human daily review kit | gh-dash when terminal queues help | Review local diffs before push or merge. |",
            "| Polyrepo work | Human polyrepo work kit | ghq for local clone organization | ghq does not replace GitHub API tooling. |",
            "| Lean or proof repo | Proof repo support kit | Context7 when docs are relevant | Bind proof tooling to the active project. |",
            "| Agentic workflow evaluation | Evaluation kit | Only after team workflow review | Keep it out of default rollout until permissions, billing, and review boundaries are clear. |",
            "",
            "## Starter Kits",
            "",
        ]
    )
    for kit in starter_kits:
        lines.extend(render_kit(kit, tools_by_id))
    lines.extend(
        [
            "## Evaluation Kits",
            "",
            "These are not default stacks. Use them only for reviewed experiments or team-specific workflows.",
            "",
        ]
    )
    for kit in evaluation_kits:
        lines.extend(render_kit(kit, tools_by_id))
    lines.extend(render_daily_workflows(tools_by_id))
    lines.extend(
        [
            "## Selection Criteria",
            "",
            "- Helps AI agents or maintainers work with GitHub, pull requests, CI, browser testing, code intelligence, documentation, or proof workflows.",
            "- Has a public source or documentation URL.",
            "- Can be classified by usefulness, operational risk, recommendation status, and practical use constraints.",
            "- Uses `watch` for promising tools that are preview-only, broad-permission, or not yet a safe default.",
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
            "## Recommended Defaults",
            "",
        ]
    )

    recommended = [tool for tool in tools if tool["recommended_status"] == "recommended"]
    lines.extend(render_recommended_table(recommended))
    lines.append("")
    lines.append("## Watch / Avoid Decisions")
    lines.append("")
    watch_or_avoid = [tool for tool in tools if tool["recommended_status"] in {"watch", "avoid"}]
    lines.extend(render_status_decision_table(watch_or_avoid))
    lines.append("")
    lines.append("## Full Catalog")
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
            practical = tool["practical"]
            lines.append(f"- Repo: `{tool['repo']}`")
            lines.append(f"- Kind: `{tool['kind']}`")
            lines.append(f"- Status: `{tool['recommended_status']}`; risk: `{tool['risk']}`; daily use: `{practical['daily_use']}`")
            lines.append(f"- Best for: {tags(practical['best_for'])}")
            lines.append(f"- Agent use: {practical['agent_use']}")
            lines.append(f"- Human use: {practical['human_use']}")
            lines.append(f"- Cautious start: {practical['cautious_start']}")
            if practical["guardrails"]:
                lines.append(f"- Guardrails: {tags(practical['guardrails'])}")
            if practical["pairs_with"]:
                pair_text = ", ".join(
                    f"{tools_by_id[pair['tool_id']]['name']} ({pair['combined_risk']})"
                    for pair in practical["pairs_with"]
                )
                lines.append(f"- Pairs with: {pair_text}")
            lines.append(f"- Agent usefulness: `{tool['agent_usefulness']}`")
            lines.append(f"- Human usefulness: `{tool['human_usefulness']}`")
            lines.append(f"- Install: `{tool['install']}`")
            if tool.get("notes"):
                lines.append(f"- Notes: {tool['notes']}")
            lines.append("")

    lines.extend(
        [
            "## Machine-Readable Data",
            "",
            "- Source of truth: `catalog/tools.yml`",
            "- Schema: `schema/tool.schema.json`",
            "- Generated JSON: `dist/catalog.v2.json`",
            "- Generated README: `README.md`",
            "",
            "## Governance and Contributions",
            "",
            "- See `CONTRIBUTING.md` before opening issues or pull requests.",
            "- See `docs/curation-governance.md` for inclusion, removal, taxonomy, evidence, and recommendation rules.",
            "- See `docs/maintenance.md` for refresh cadence, automation policy, and public roadmap rules.",
            "- See `docs/pr-review-checklist.md` for maintainer review expectations.",
            "",
            "## Validation",
            "",
            "```bash",
            "python scripts/validate_catalog.py",
            "python scripts/render_readme.py --check",
            "python scripts/render_catalog_json.py --check",
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
