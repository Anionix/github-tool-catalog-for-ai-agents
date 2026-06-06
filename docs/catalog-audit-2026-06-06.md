# Catalog Audit: 2026-06-06 JST

This audit covers the 19 entries currently listed in `catalog/tools.yml` after
the GitHub CLI and Git TUI market-map reflection. The checks were run on
2026-06-06 in Asia/Tokyo, which corresponds to 2026-06-05 in UTC for GitHub
commit and workflow timestamps.

## Summary

- Catalog validation: 19 tools and 12 categories.
- README generation: `README.md` is up to date with `catalog/tools.yml`.
- Link syntax: all 19 catalog URLs use valid `https://github.com/` URLs.
- Live link check: all 19 catalog URLs returned HTTP 200.
- GitHub repository status: all 19 repositories were public, reachable,
  non-archived, and not disabled.
- Repository status warning: `mislav/hub` was last pushed 853 days before this
  audit, but it remains intentionally listed as `Legacy / Avoid`.
- Follow-up decisions: none required for broken, moved, archived, or disabled
  repositories.

## Commands

Run from the repository root:

```bash
python -B scripts/validate_catalog.py
python -B scripts/render_readme.py --check
python -B scripts/check_links.py
python -B scripts/check_links.py --live
python -B scripts/check_repo_status.py
```

## Repository Status

| Repository | Catalog position | Audit result |
| --- | --- | --- |
| `ChromeDevTools/chrome-devtools-mcp` | Recommended browser/testing MCP. | Public, reachable, not archived, not disabled. |
| `altsem/gitu` | Watch Git TUI. | Public, reachable, not archived, not disabled. |
| `chmouel/gh-news` | Watch GitHub CLI notification extension. | Public, reachable, not archived, not disabled. |
| `cli/cli` | Recommended GitHub CLI/API control plane. | Public, reachable, not archived, not disabled. |
| `dandavison/delta` | Recommended Git diff/pager utility. | Public, reachable, not archived, not disabled. |
| `dlvhdr/gh-dash` | Situational GitHub CLI triage extension. | Public, reachable, not archived, not disabled. |
| `github/copilot-cli` | Situational agent CLI. | Public, reachable, not archived, not disabled. |
| `github/gh-aw` | Watch agentic workflow extension. | Public, reachable, not archived, not disabled. |
| `github/gh-stack` | Watch stacked PR extension. | Public, reachable, not archived, not disabled. |
| `github/github-mcp-server` | Recommended GitHub MCP connector. | Public, reachable, not archived, not disabled. |
| `gitui-org/gitui` | Situational Git TUI. | Public, reachable, not archived, not disabled. |
| `jesseduffield/lazygit` | Recommended Git TUI. | Public, reachable, not archived, not disabled. |
| `jonas/tig` | Situational lightweight Git TUI. | Public, reachable, not archived, not disabled. |
| `microsoft/playwright-mcp` | Recommended browser/testing MCP. | Public, reachable, not archived, not disabled. |
| `mislav/hub` | Legacy / Avoid CLI. | Public, reachable, not archived, not disabled; last pushed on 2024-02-02; intentionally listed as `avoid` because `gh` supersedes it for new GitHub CLI workflows. |
| `oOo0oOo/lean-lsp-mcp` | Recommended Lean support MCP. | Public, reachable, not archived, not disabled. |
| `oraios/serena` | Recommended code-intelligence MCP. | Public, reachable, not archived, not disabled. |
| `upstash/context7` | Recommended docs/knowledge MCP. | Public, reachable, not archived, not disabled. |
| `x-motemen/ghq` | Situational repo manager. | Public, reachable, not archived, not disabled. |

## Duplicate and Overlap Review

`scripts/validate_catalog.py` enforces unique tool names, repositories, and
URLs. It also confirms that every tool uses a known category and that each URL
matches the declared GitHub repository.

Overlap decisions:

- `GitHub CLI` remains the default GitHub command-line control plane.
- `gh-dash`, `gh-news`, `gh-stack`, and `gh-aw` are separate `gh` extensions
  because they solve different triage, notification, stacked PR, and workflow
  orchestration problems.
- `lazygit`, `gitui`, `tig`, and `gitu` overlap as Git TUIs, so only
  `lazygit` is `recommended`; the others are `situational` or `watch`.
- `delta` is a pager/review readability helper, not a Git TUI.
- `ghq` is a local repository manager, not a GitHub API or PR tool.
- `hub` is intentionally retained as `Legacy / Avoid` to explain migration
  pressure toward the official `gh` CLI.

## Description and Rating Review

Summaries are short, public-safe, and specific to the workflow. Notes explain
when to use each tool and the most important limitation or risk. Risk ratings
are conservative for tools that handle authenticated services, browser state,
workflow execution, or agent access.

Agent and human usefulness ratings are internally consistent:

- Agent-facing MCP and API tools are rated higher for agents.
- Terminal UI tools are rated higher for humans.
- Broad-permission or preview workflow tools are kept in `watch` or
  `situational` even when they may be powerful.
