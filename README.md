# Awesome GitHub Tools

A strict, machine-readable catalog of GitHub-adjacent tools for AI agents and the humans supervising them.

> This README is generated from `catalog/tools.yml`. Edit the catalog, then run `python scripts/render_readme.py`.

## Selection Criteria

- Helps AI agents or maintainers work with GitHub, pull requests, CI, browser testing, code intelligence, documentation, or proof workflows.
- Has a public source or documentation URL.
- Can be classified by usefulness, operational risk, and recommendation status.
- Uses `watch` for promising tools that are preview-only, broad-permission, or not yet a good default.

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
| [GitHub CLI](https://github.com/cli/cli) | Recommended | high | high | Medium | `brew install gh` |
| [GitHub MCP Server](https://github.com/github/github-mcp-server) | Recommended | high | medium | High | `codex mcp add github --url https://api.githubcopilot.com/mcp/ --bearer-token-env-var GITHUB_PAT_TOKEN` |
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
- Notes: Prefer gh api for exact REST or GraphQL operations that are not exposed by a connector or MCP tool.

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
- Notes: Great for human review queues; not a primary AI-agent interface.

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
- Notes: Private preview; use only when stacked PRs are enabled for the target repository.

### Agentic Workflows

#### [GitHub Copilot CLI](https://github.com/github/copilot-cli)

GitHub Copilot coding agent for terminal workflows, with configurable permissions and built-in
GitHub MCP support.

- Repo: `github/copilot-cli`
- Kind: `agent-cli`
- Status: `situational`
- Agent usefulness: `medium`
- Human usefulness: `medium`
- Risk: `high`
- Install: `gh copilot`
- Notes: A separate agent runtime rather than a Codex tool; useful for comparison or Copilot-native workflows.

#### [GitHub Agentic Workflows](https://github.com/github/gh-aw)

GitHub CLI extension for defining and running repository agent workflows through GitHub Actions.

- Repo: `github/gh-aw`
- Kind: `agent-workflow`
- Status: `watch`
- Agent usefulness: `medium`
- Human usefulness: `medium`
- Risk: `high`
- Install: `gh extension install github/gh-aw`
- Notes: Powerful but operationally heavy; treat permissions, billing, and workflow safety as first-class review items.

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
