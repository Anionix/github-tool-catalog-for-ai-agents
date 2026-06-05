# Awesome GitHub Tools

A strict, machine-readable catalog of GitHub-adjacent tools for AI agents and the humans supervising them.

> This README is generated from `catalog/tools.yml`. Edit the catalog, then run `python scripts/render_readme.py`.

## Selection Criteria

- Helps AI agents or maintainers work with GitHub, pull requests, CI, browser testing, code intelligence, documentation, or proof workflows.
- Has a public source or documentation URL.
- Can be classified by usefulness, operational risk, and recommendation status.
- Uses `watch` for promising tools that are preview-only, broad-permission, or not yet a good default.

## Governance and Contributions

- See `CONTRIBUTING.md` before opening issues or pull requests.
- See `docs/curation-governance.md` for inclusion, removal, taxonomy, evidence, and recommendation rules.
- See `docs/maintenance.md` for refresh cadence, automation policy, and public roadmap rules.
- See `docs/pr-review-checklist.md` for maintainer review expectations.

## Recommendation Legend

| Status | Meaning |
| --- | --- |
| Recommended | Good default for the right workflow. |
| Situational | Useful when the workflow clearly needs it. |
| Watch | Promising, preview-only, heavy, or not yet a safe default. |
| Avoid | Known mismatch for this catalog's default recommendations. |

## Quick Picks

| Tool | Status | Agent | Human | Risk | Install |
| --- | --- | --- | --- | --- | --- |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Recommended | high | medium | High | `codex mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --slim --headless --isolated` |
| [Context7](https://github.com/upstash/context7) | Recommended | high | medium | Medium | `codex mcp add context7 -- npx -y @upstash/context7-mcp@latest` |
| [delta](https://github.com/dandavison/delta) | Recommended | medium | high | Low | `brew install git-delta` |
| [GitHub CLI](https://github.com/cli/cli) | Recommended | high | high | Medium | `brew install gh` |
| [GitHub MCP Server](https://github.com/github/github-mcp-server) | Recommended | high | medium | High | `codex mcp add github --url https://api.githubcopilot.com/mcp/ --bearer-token-env-var GITHUB_PAT_TOKEN` |
| [lazygit](https://github.com/jesseduffield/lazygit) | Recommended | medium | high | Medium | `brew install lazygit` |
| [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp) | Recommended | high | medium | Medium | `codex mcp add lean-lsp --env LEAN_PROJECT_PATH=/path/to/lean/project -- uvx lean-lsp-mcp` |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Recommended | high | medium | High | `codex mcp add playwright -- npx -y @playwright/mcp@latest` |
| [Serena](https://github.com/oraios/serena) | Recommended | high | medium | High | `codex mcp add serena -- serena start-mcp-server --project-from-cwd --context=codex` |

## Catalog

### GitHub MCP / Connectors

#### [GitHub MCP Server](https://github.com/github/github-mcp-server)

Official GitHub MCP server for repository, issue, pull request, workflow, project, org, and gist
access from AI agents.

- Repo: `github/github-mcp-server`
- Kind: `mcp`
- Status: `recommended`
- Agent usefulness: `high`
- Human usefulness: `medium`
- Risk: `high`
- Install: `codex mcp add github --url https://api.githubcopilot.com/mcp/ --bearer-token-env-var GITHUB_PAT_TOKEN`
- Notes: Use targeted toolsets or read-only mode when broad write access is unnecessary.

### GitHub CLI and API

#### [GitHub CLI](https://github.com/cli/cli)

Official GitHub command line interface for issues, pull requests, Actions, releases, rulesets, API
calls, and authenticated automation.

- Repo: `cli/cli`
- Kind: `cli`
- Status: `recommended`
- Agent usefulness: `high`
- Human usefulness: `high`
- Risk: `medium`
- Install: `brew install gh`
- Notes: Prefer gh api for exact REST or GraphQL operations that are not exposed by a connector or MCP tool; treat gh skill as a gh capability rather than a separate tool entry.

### gh Extensions

#### [gh-dash](https://github.com/dlvhdr/gh-dash)

Terminal dashboard for GitHub pull requests, issues, custom sections, custom actions, and keyboard-
driven triage.

- Repo: `dlvhdr/gh-dash`
- Kind: `gh-extension`
- Status: `situational`
- Agent usefulness: `low`
- Human usefulness: `high`
- Risk: `medium`
- Install: `gh extension install dlvhdr/gh-dash`
- Notes: Great for human review queues; audit third-party extension trust and Nerd Font/UI assumptions before default rollout.

#### [gh-news](https://github.com/chmouel/gh-news)

GitHub CLI notification TUI for reading, filtering, previewing, muting, snoozing, and archiving
GitHub notifications from the terminal.

- Repo: `chmouel/gh-news`
- Kind: `gh-extension`
- Status: `watch`
- Agent usefulness: `low`
- Human usefulness: `medium`
- Risk: `medium`
- Install: `gh extension install chmouel/gh-news`
- Notes: Promising notification-focused gh extension; it uses token-backed GitHub notification actions, so keep it in watch until publisher trust and team fit are reviewed.

#### [gh-stack](https://github.com/github/gh-stack)

GitHub extension for stacked branches and stacked pull requests, including agent-facing skill
guidance.

- Repo: `github/gh-stack`
- Kind: `gh-extension`
- Status: `watch`
- Agent usefulness: `medium`
- Human usefulness: `high`
- Risk: `high`
- Install: `gh extension install github/gh-stack`
- Notes: Preview-oriented stacked PR workflow; use only when stacked PRs are enabled and the team's auth model supports the extension.

### Agentic Workflows

#### [GitHub Copilot CLI](https://github.com/github/copilot-cli)

GitHub Copilot coding agent for terminal workflows, with configurable permissions and built-in
GitHub MCP support.

- Repo: `github/copilot-cli`
- Kind: `agent-cli`
- Status: `situational`
- Agent usefulness: `medium`
- Human usefulness: `high`
- Risk: `high`
- Install: `brew install copilot-cli`
- Notes: A separate agent runtime rather than a Codex tool; prefer this standalone CLI over retired legacy gh-copilot workflows.

#### [GitHub Agentic Workflows](https://github.com/github/gh-aw)

GitHub CLI extension for defining and running repository agent workflows through GitHub Actions.

- Repo: `github/gh-aw`
- Kind: `agent-workflow`
- Status: `watch`
- Agent usefulness: `medium`
- Human usefulness: `medium`
- Risk: `high`
- Install: `gh extension install github/gh-aw`
- Notes: Powerful but operationally heavy; treat permissions, billing, guardrails, and workflow safety as first-class review items.

### Browser and Testing MCP

#### [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)

Chrome DevTools MCP server for navigation, script execution, screenshots, performance, network, and
debugging workflows.

- Repo: `ChromeDevTools/chrome-devtools-mcp`
- Kind: `mcp`
- Status: `recommended`
- Agent usefulness: `high`
- Human usefulness: `medium`
- Risk: `high`
- Install: `codex mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --slim --headless --isolated`
- Notes: The slim isolated mode is a safer default for general coding-agent use.

#### [Playwright MCP](https://github.com/microsoft/playwright-mcp)

Browser automation MCP server for testing and data extraction through Playwright's accessibility-
oriented model.

- Repo: `microsoft/playwright-mcp`
- Kind: `mcp`
- Status: `recommended`
- Agent usefulness: `high`
- Human usefulness: `medium`
- Risk: `high`
- Install: `codex mcp add playwright -- npx -y @playwright/mcp@latest`
- Notes: Prefer constrained browser contexts for agent runs that do not need local user profile state.

### Code Intelligence MCP

#### [Serena](https://github.com/oraios/serena)

Semantic code retrieval and editing MCP server for coding agents, backed by language-server style
project understanding.

- Repo: `oraios/serena`
- Kind: `mcp`
- Status: `recommended`
- Agent usefulness: `high`
- Human usefulness: `medium`
- Risk: `high`
- Install: `codex mcp add serena -- serena start-mcp-server --project-from-cwd --context=codex`
- Notes: Best used with project-scoped startup rather than broad filesystem access.

### Docs and Knowledge MCP

#### [Context7](https://github.com/upstash/context7)

Documentation MCP server that injects current library docs and examples into agent prompts.

- Repo: `upstash/context7`
- Kind: `mcp`
- Status: `recommended`
- Agent usefulness: `high`
- Human usefulness: `medium`
- Risk: `medium`
- Install: `codex mcp add context7 -- npx -y @upstash/context7-mcp@latest`
- Notes: Useful when framework or API behavior is likely to have changed since model training.

### Formal Proof / Lean support

#### [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)

Lean LSP MCP server for proof diagnostics, goal inspection, Loogle-style search, and optional Lean
REPL acceleration.

- Repo: `oOo0oOo/lean-lsp-mcp`
- Kind: `mcp`
- Status: `recommended`
- Agent usefulness: `high`
- Human usefulness: `medium`
- Risk: `medium`
- Install: `codex mcp add lean-lsp --env LEAN_PROJECT_PATH=/path/to/lean/project -- uvx lean-lsp-mcp`
- Notes: Strong fit for Lean repositories; scope LEAN_PROJECT_PATH to the active proof project.

### Git TUI

#### [lazygit](https://github.com/jesseduffield/lazygit)

Terminal UI for everyday Git workflows such as staging, committing, rebasing, stashing, branch
navigation, and conflict-oriented local review.

- Repo: `jesseduffield/lazygit`
- Kind: `git-tui`
- Status: `recommended`
- Agent usefulness: `medium`
- Human usefulness: `high`
- Risk: `medium`
- Install: `brew install lazygit`
- Notes: Best default local Git TUI; pair with gh or gh-dash for GitHub pull request and issue workflows.

#### [gitui](https://github.com/gitui-org/gitui)

Fast Rust terminal UI for local Git workflows, including diff, commit, stash, blame, log, and index
operations.

- Repo: `gitui-org/gitui`
- Kind: `git-tui`
- Status: `situational`
- Agent usefulness: `low`
- Human usefulness: `medium`
- Risk: `medium`
- Install: `brew install gitui`
- Notes: Lightweight Rust Git TUI alternative; keep as an alternative rather than the default over lazygit.

#### [tig](https://github.com/jonas/tig)

Mature text-mode interface for browsing Git history, diffs, refs, blame, and repository state in
minimal terminal environments.

- Repo: `jonas/tig`
- Kind: `git-tui`
- Status: `situational`
- Agent usefulness: `low`
- Human usefulness: `medium`
- Risk: `low`
- Install: `brew install tig`
- Notes: Good fallback for SSH, server, and low-dependency environments; less guided than newer Git TUIs.

#### [gitu](https://github.com/altsem/gitu)

Magit-inspired terminal Git client for hunk and line staging, commits, fixups, rebases, stashes, and
local history workflows.

- Repo: `altsem/gitu`
- Kind: `git-tui`
- Status: `watch`
- Agent usefulness: `low`
- Human usefulness: `medium`
- Risk: `medium`
- Install: `cargo install gitu`
- Notes: Promising Magit-style TUI with narrower adoption than lazygit and gitui; keep in watch until use cases are clearer.

### Git Diff and Repo Utilities

#### [delta](https://github.com/dandavison/delta)

Syntax-highlighting pager for Git, diff, grep, ripgrep JSON, and blame output that improves review
readability.

- Repo: `dandavison/delta`
- Kind: `git-pager`
- Status: `recommended`
- Agent usefulness: `medium`
- Human usefulness: `high`
- Risk: `low`
- Install: `brew install git-delta`
- Notes: High-value diff and pager upgrade; improves review readability without replacing Git or GitHub workflows.

#### [ghq](https://github.com/x-motemen/ghq)

Local repository manager that standardizes clone locations and makes multi-host or polyrepo
workspaces easier to navigate.

- Repo: `x-motemen/ghq`
- Kind: `repo-manager`
- Status: `situational`
- Agent usefulness: `medium`
- Human usefulness: `high`
- Risk: `low`
- Install: `brew install ghq`
- Notes: Useful for polyrepo and multi-host local repository organization; not a GitHub API tool.

### Legacy / Avoid

#### [hub](https://github.com/mislav/hub)

Legacy command line wrapper that extends Git with GitHub operations but has largely been superseded
by the official GitHub CLI.

- Repo: `mislav/hub`
- Kind: `cli`
- Status: `avoid`
- Agent usefulness: `low`
- Human usefulness: `low`
- Risk: `medium`
- Install: `brew install hub`
- Notes: Keep only to explain migration pressure toward gh; do not recommend for new GitHub CLI workflows.

### Watchlist / Not yet recommended

_No entries yet._

## Validation

```bash
python scripts/validate_catalog.py
python scripts/render_readme.py --check
python scripts/check_links.py
```

## License

CC0-1.0. See `LICENSE`.
