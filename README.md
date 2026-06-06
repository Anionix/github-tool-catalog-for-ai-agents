# GitHub Tool Catalog for AI Agents

A small, conservative, machine-readable catalog of GitHub-adjacent tools for AI agents and the humans supervising them.

> This README is generated from `catalog/tools.yml`. Edit the catalog, then run `python scripts/render_readme.py`.

## Start Here

| Workflow | Use first | Add when | Caution |
| --- | --- | --- | --- |
| Agent repo maintenance | Agent repo maintenance kit | Browser validation kit for UI behavior | Limit tokens and require human approval for writes. |
| Human daily review | Human daily review kit | gh-dash when terminal queues help | Review local diffs before push or merge. |
| Polyrepo work | Human polyrepo work kit | ghq for local clone organization | ghq does not replace GitHub API tooling. |
| Lean or proof repo | Proof repo support kit | Context7 when docs are relevant | Bind proof tooling to the active project. |
| Agentic workflow evaluation | Evaluation kit | Only after team workflow review | Keep it out of default rollout until permissions, billing, and review boundaries are clear. |

## Starter Kits

### Agent repo maintenance

Inspect GitHub state, navigate code, fetch current docs, and prepare supervised repository changes.

- Core: [GitHub CLI](https://github.com/cli/cli), [GitHub MCP Server](https://github.com/github/github-mcp-server), [Serena](https://github.com/oraios/serena), [Context7](https://github.com/upstash/context7)
- Caution: Use limited GitHub scopes, project-scoped code tools, and human approval for writes.
- Guardrails: `limited-token`, `read-only-mode`, `project-scope`, `human-approval`
- Install:
  - `brew install gh`
  - `codex mcp add github --url https://api.githubcopilot.com/mcp/ --bearer-token-env-var GITHUB_PAT_TOKEN`
  - `codex mcp add serena -- serena start-mcp-server --project-from-cwd --context=codex`
  - `codex mcp add context7 -- npx -y @upstash/context7-mcp@latest`

### Agent browser validation

Validate UI and browser behavior through constrained automation and diagnostics.

- Core: [Playwright MCP](https://github.com/microsoft/playwright-mcp)
- Optional: [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- Caution: Prefer isolated browser contexts and non-production targets before using authenticated profiles.
- Guardrails: `isolated-browser`, `no-user-profile`, `non-production`
- Install:
  - `codex mcp add playwright -- npx -y @playwright/mcp@latest`
  - `codex mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --slim --headless --isolated`

### Human daily review

Review pull requests, inspect diffs, and manage local Git state during everyday maintenance.

- Core: [GitHub CLI](https://github.com/cli/cli), [lazygit](https://github.com/jesseduffield/lazygit), [delta](https://github.com/dandavison/delta)
- Optional: [gh-dash](https://github.com/dlvhdr/gh-dash)
- Caution: Review local diffs before push or merge; gh-dash remains a reviewed extension, not a required default.
- Guardrails: `human-approval`
- Install:
  - `brew install gh`
  - `brew install lazygit`
  - `brew install git-delta`
  - `gh extension install dlvhdr/gh-dash`

### Human polyrepo work

Keep many local repositories organized while preserving GitHub operations in gh.

- Core: [GitHub CLI](https://github.com/cli/cli), [lazygit](https://github.com/jesseduffield/lazygit), [delta](https://github.com/dandavison/delta)
- Optional: [ghq](https://github.com/x-motemen/ghq)
- Caution: Use ghq for local repository organization only; do not treat it as GitHub API coverage.
- Guardrails: `project-scope`, `human-approval`
- Install:
  - `brew install gh`
  - `brew install lazygit`
  - `brew install git-delta`
  - `brew install ghq`

### Proof repo support

Support Lean proof work with scoped diagnostics, PR readback, and readable diffs.

- Core: [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp), [GitHub CLI](https://github.com/cli/cli), [delta](https://github.com/dandavison/delta)
- Optional: [Context7](https://github.com/upstash/context7)
- Caution: Bind Lean tooling to the active proof project before exposing diagnostics to agents.
- Guardrails: `project-scope`
- Install:
  - `codex mcp add lean-lsp --env LEAN_PROJECT_PATH=/path/to/lean/project -- uvx lean-lsp-mcp`
  - `brew install gh`
  - `brew install git-delta`
  - `codex mcp add context7 -- npx -y @upstash/context7-mcp@latest`

## Evaluation Kits

These are not default stacks. Use them only for reviewed experiments or team-specific workflows.

### Agentic workflow evaluation

Evaluate stacked PRs, Actions-backed agent workflows, or a separate terminal agent runtime.

- Core: [gh-stack](https://github.com/github/gh-stack), [GitHub Agentic Workflows](https://github.com/github/gh-aw), [GitHub Copilot CLI](https://github.com/github/copilot-cli)
- Caution: Evaluation only: use sandbox repositories, define billing and review boundaries, and avoid default rollout claims.
- Guardrails: `sandbox-repo`, `human-approval`, `non-production`
- Install:
  - `gh extension install github/gh-stack`
  - `gh extension install github/gh-aw`
  - `brew install copilot-cli`

## Daily Workflows

- Agent PR review: inspect issue and PR state with [GitHub MCP Server](https://github.com/github/github-mcp-server) or [GitHub CLI](https://github.com/cli/cli), navigate code with [Serena](https://github.com/oraios/serena), fetch current docs with [Context7](https://github.com/upstash/context7), validate behavior with [Playwright MCP](https://github.com/microsoft/playwright-mcp), then read back checks with [GitHub CLI](https://github.com/cli/cli).
- Human PR review: use [GitHub CLI](https://github.com/cli/cli) for PR state, [delta](https://github.com/dandavison/delta) for readable diffs, [lazygit](https://github.com/jesseduffield/lazygit) for local Git actions, and [gh-dash](https://github.com/dlvhdr/gh-dash) only when a terminal review queue helps.
- Browser validation: start with [Playwright MCP](https://github.com/microsoft/playwright-mcp); add [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) when DevTools-level network, console, performance, or screenshot diagnostics are needed.
- Lean or proof repository: bind project scope for [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp), use [GitHub CLI](https://github.com/cli/cli) for PR/check readback, and use [delta](https://github.com/dandavison/delta) for proof diff review.
- Agentic workflow evaluation: keep [gh-stack](https://github.com/github/gh-stack), [GitHub Agentic Workflows](https://github.com/github/gh-aw), and [GitHub Copilot CLI](https://github.com/github/copilot-cli) in sandbox or explicitly reviewed workflows before routine rollout.

## Selection Criteria

- Helps AI agents or maintainers work with GitHub, pull requests, CI, browser testing, code intelligence, documentation, or proof workflows.
- Has a public source or documentation URL.
- Can be classified by usefulness, operational risk, recommendation status, and practical use constraints.
- Uses `watch` for promising tools that are preview-only, broad-permission, or not yet a safe default.

## Recommendation Legend

| Status | Meaning |
| --- | --- |
| Recommended | Good default for the right workflow. |
| Situational | Useful when the workflow clearly needs it. |
| Watch | Promising, preview-only, heavy, or not yet a safe default. |
| Avoid | Known mismatch for this catalog's default recommendations. |

## Recommended Defaults

| Tool | Best for | Agent | Human | Risk | Caution |
| --- | --- | --- | --- | --- | --- |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | `browser-debugging`, `performance`, `network-inspection` | high | medium | High | Use slim, headless, isolated mode unless user profile state is explicitly required. |
| [Context7](https://github.com/upstash/context7) | `current-docs`, `framework-apis`, `agent-research` | high | medium | Medium | Use it to support implementation claims, then verify behavior with project tests or official sources. |
| [delta](https://github.com/dandavison/delta) | `diff-review`, `readability`, `git-pager` | medium | high | Low | Configure as a pager first; it improves review readability without changing GitHub state. |
| [GitHub CLI](https://github.com/cli/cli) | `github-api`, `pr-review`, `actions-readback`, `release-workflows` | high | high | Medium | Authenticate with the minimum scopes needed for the current repository or organization task. |
| [GitHub MCP Server](https://github.com/github/github-mcp-server) | `agent-github-api`, `issues-prs`, `workflow-readback` | high | medium | High | Start with the narrowest available token scope or read-only toolset before allowing write operations. |
| [lazygit](https://github.com/jesseduffield/lazygit) | `local-git`, `branch-review`, `staging` | medium | high | Medium | Review staged changes before committing or pushing. |
| [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp) | `lean-proof`, `proof-diagnostics`, `formal-methods` | high | medium | Medium | Bind LEAN_PROJECT_PATH to the active Lean project before exposing proof tooling. |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | `browser-validation`, `ui-testing`, `agent-e2e` | high | medium | High | Run against a constrained browser context and non-production target when possible. |
| [Serena](https://github.com/oraios/serena) | `code-intelligence`, `repo-navigation`, `agent-editing` | high | medium | High | Start with project-scoped startup from the active repository, not broad filesystem access. |

## Watch / Avoid Decisions

| Tool | Status | Daily use | Risk | Why not a default |
| --- | --- | --- | --- | --- |
| [gh-news](https://github.com/chmouel/gh-news) | Watch | Not default | Medium | Promising notification-focused gh extension; it uses token-backed GitHub notification actions, so keep it in watch until publisher trust and team fit are reviewed. |
| [gh-stack](https://github.com/github/gh-stack) | Watch | Not default | High | Preview-oriented stacked PR workflow; use only when stacked PRs are enabled and the team's auth model supports the extension. |
| [GitHub Agentic Workflows](https://github.com/github/gh-aw) | Watch | Not default | High | Powerful but operationally heavy; treat permissions, billing, guardrails, and workflow safety as first-class review items. |
| [gitu](https://github.com/altsem/gitu) | Watch | Not default | Medium | Promising Magit-style TUI with narrower adoption than lazygit and gitui; keep in watch until use cases are clearer. |
| [hub](https://github.com/mislav/hub) | Avoid | Not default | Medium | Keep only to explain migration pressure toward gh; do not recommend for new GitHub CLI workflows. |

## Full Catalog

### GitHub MCP / Connectors

#### [GitHub MCP Server](https://github.com/github/github-mcp-server)

Official GitHub MCP server for repository, issue, pull request, workflow, project, org, and gist
access from AI agents.

- Repo: `github/github-mcp-server`
- Kind: `mcp`
- Status: `recommended`; risk: `high`; daily use: `reviewed`
- Best for: `agent-github-api`, `issues-prs`, `workflow-readback`
- Agent use: Let an agent inspect and update GitHub repository, issue, pull request, workflow, project, org, or gist state when the task explicitly needs GitHub context.
- Human use: Use through an agent when GitHub state needs exact readback or controlled repository actions.
- Cautious start: Start with the narrowest available token scope or read-only toolset before allowing write operations.
- Guardrails: `limited-token`, `read-only-mode`, `human-approval`
- Pairs with: GitHub CLI (high), Serena (high), Context7 (high)
- Agent usefulness: `high`
- Human usefulness: `medium`
- Install: `codex mcp add github --url https://api.githubcopilot.com/mcp/ --bearer-token-env-var GITHUB_PAT_TOKEN`
- Notes: Use targeted toolsets or read-only mode when broad write access is unnecessary.

### GitHub CLI and API

#### [GitHub CLI](https://github.com/cli/cli)

Official GitHub command line interface for issues, pull requests, Actions, releases, rulesets, API
calls, and authenticated automation.

- Repo: `cli/cli`
- Kind: `cli`
- Status: `recommended`; risk: `medium`; daily use: `routine`
- Best for: `github-api`, `pr-review`, `actions-readback`, `release-workflows`
- Agent use: Use for auditable GitHub operations, exact API calls, and PR/check readback when connector coverage is insufficient.
- Human use: Use as the baseline command line for issues, pull requests, Actions, releases, and authenticated automation.
- Cautious start: Authenticate with the minimum scopes needed for the current repository or organization task.
- Guardrails: `limited-token`, `human-approval`
- Pairs with: lazygit (medium), delta (medium), GitHub MCP Server (high)
- Agent usefulness: `high`
- Human usefulness: `high`
- Install: `brew install gh`
- Notes: Prefer gh api for exact REST or GraphQL operations that are not exposed by a connector or MCP tool; treat gh skill as a gh capability rather than a separate tool entry.

### gh Extensions

#### [gh-dash](https://github.com/dlvhdr/gh-dash)

Terminal dashboard for GitHub pull requests, issues, custom sections, custom actions, and keyboard-
driven triage.

- Repo: `dlvhdr/gh-dash`
- Kind: `gh-extension`
- Status: `situational`; risk: `medium`; daily use: `reviewed`
- Best for: `human-triage`, `pr-queues`, `issue-queues`
- Agent use: Low fit for autonomous agents; treat as a human-facing queue dashboard.
- Human use: Use for keyboard-driven PR and issue triage when a terminal dashboard improves review flow.
- Cautious start: Install only after reviewing third-party extension trust and terminal UI assumptions for the team.
- Guardrails: `human-approval`
- Pairs with: GitHub CLI (medium), lazygit (medium)
- Agent usefulness: `low`
- Human usefulness: `high`
- Install: `gh extension install dlvhdr/gh-dash`
- Notes: Great for human review queues; audit third-party extension trust and Nerd Font/UI assumptions before default rollout.

#### [gh-news](https://github.com/chmouel/gh-news)

GitHub CLI notification TUI for reading, filtering, previewing, muting, snoozing, and archiving
GitHub notifications from the terminal.

- Repo: `chmouel/gh-news`
- Kind: `gh-extension`
- Status: `watch`; risk: `medium`; daily use: `not_default`
- Best for: `notifications`, `human-triage`, `team-evaluation`
- Agent use: Not an agent default; notifications usually need human prioritization.
- Human use: Evaluate for terminal notification review when the team accepts the extension trust model.
- Cautious start: Review publisher trust and token-backed notification actions before routine use.
- Guardrails: `limited-token`, `human-approval`
- Pairs with: GitHub CLI (medium)
- Agent usefulness: `low`
- Human usefulness: `medium`
- Install: `gh extension install chmouel/gh-news`
- Notes: Promising notification-focused gh extension; it uses token-backed GitHub notification actions, so keep it in watch until publisher trust and team fit are reviewed.

#### [gh-stack](https://github.com/github/gh-stack)

GitHub extension for stacked branches and stacked pull requests, including agent-facing skill
guidance.

- Repo: `github/gh-stack`
- Kind: `gh-extension`
- Status: `watch`; risk: `high`; daily use: `not_default`
- Best for: `stacked-prs`, `branch-stacks`, `team-evaluation`
- Agent use: Evaluate only for teams that explicitly run stacked PR workflows with review boundaries.
- Human use: Use when a team has adopted stacked pull requests and understands the extension workflow.
- Cautious start: Try in a sandbox repository before using it on production branches.
- Guardrails: `sandbox-repo`, `human-approval`
- Pairs with: GitHub CLI (high)
- Agent usefulness: `medium`
- Human usefulness: `high`
- Install: `gh extension install github/gh-stack`
- Notes: Preview-oriented stacked PR workflow; use only when stacked PRs are enabled and the team's auth model supports the extension.

### Agentic Workflows

#### [GitHub Copilot CLI](https://github.com/github/copilot-cli)

GitHub Copilot coding agent for terminal workflows, with configurable permissions and built-in
GitHub MCP support.

- Repo: `github/copilot-cli`
- Kind: `agent-cli`
- Status: `situational`; risk: `high`; daily use: `reviewed`
- Best for: `terminal-agent`, `agent-runtime`, `human-supervised-coding`
- Agent use: Use as a separate terminal-native agent runtime when the workflow calls for Copilot CLI rather than Codex tooling.
- Human use: Use for human-supervised terminal agent tasks with configured permissions.
- Cautious start: Review permissions and repository write boundaries before using it on important branches.
- Guardrails: `human-approval`, `project-scope`
- Pairs with: GitHub CLI (high), Context7 (high)
- Agent usefulness: `medium`
- Human usefulness: `high`
- Install: `brew install copilot-cli`
- Notes: A separate agent runtime rather than a Codex tool; prefer this standalone CLI over retired legacy gh-copilot workflows.

#### [GitHub Agentic Workflows](https://github.com/github/gh-aw)

GitHub CLI extension for defining and running repository agent workflows through GitHub Actions.

- Repo: `github/gh-aw`
- Kind: `agent-workflow`
- Status: `watch`; risk: `high`; daily use: `not_default`
- Best for: `agentic-workflows`, `github-actions`, `team-evaluation`
- Agent use: Evaluate for repository agent workflows only with explicit billing, permission, and review boundaries.
- Human use: Use to prototype GitHub Actions-backed agent workflows after operational review.
- Cautious start: Start in a sandbox repository with clear workflow permissions and cost boundaries.
- Guardrails: `sandbox-repo`, `human-approval`, `non-production`
- Pairs with: GitHub CLI (high), GitHub Copilot CLI (high)
- Agent usefulness: `medium`
- Human usefulness: `medium`
- Install: `gh extension install github/gh-aw`
- Notes: Powerful but operationally heavy; treat permissions, billing, guardrails, and workflow safety as first-class review items.

### Browser and Testing MCP

#### [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)

Chrome DevTools MCP server for navigation, script execution, screenshots, performance, network, and
debugging workflows.

- Repo: `ChromeDevTools/chrome-devtools-mcp`
- Kind: `mcp`
- Status: `recommended`; risk: `high`; daily use: `reviewed`
- Best for: `browser-debugging`, `performance`, `network-inspection`
- Agent use: Let an agent inspect navigation, screenshots, performance, network, and console behavior in a constrained Chrome context.
- Human use: Use for browser debugging when DevTools-level inspection is more useful than a test runner.
- Cautious start: Use slim, headless, isolated mode unless user profile state is explicitly required.
- Guardrails: `isolated-browser`, `no-user-profile`, `non-production`
- Pairs with: Playwright MCP (high), GitHub CLI (high)
- Agent usefulness: `high`
- Human usefulness: `medium`
- Install: `codex mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --slim --headless --isolated`
- Notes: The slim isolated mode is a safer default for general coding-agent use.

#### [Playwright MCP](https://github.com/microsoft/playwright-mcp)

Browser automation MCP server for testing and data extraction through Playwright's accessibility-
oriented model.

- Repo: `microsoft/playwright-mcp`
- Kind: `mcp`
- Status: `recommended`; risk: `high`; daily use: `reviewed`
- Best for: `browser-validation`, `ui-testing`, `agent-e2e`
- Agent use: Let an agent validate web behavior through Playwright accessibility and browser automation flows.
- Human use: Use when browser validation needs reproducible automation rather than manual clicking.
- Cautious start: Run against a constrained browser context and non-production target when possible.
- Guardrails: `isolated-browser`, `no-user-profile`, `non-production`
- Pairs with: GitHub CLI (high), Chrome DevTools MCP (high)
- Agent usefulness: `high`
- Human usefulness: `medium`
- Install: `codex mcp add playwright -- npx -y @playwright/mcp@latest`
- Notes: Prefer constrained browser contexts for agent runs that do not need local user profile state.

### Code Intelligence MCP

#### [Serena](https://github.com/oraios/serena)

Semantic code retrieval and editing MCP server for coding agents, backed by language-server style
project understanding.

- Repo: `oraios/serena`
- Kind: `mcp`
- Status: `recommended`; risk: `high`; daily use: `reviewed`
- Best for: `code-intelligence`, `repo-navigation`, `agent-editing`
- Agent use: Let an agent navigate and edit a repository with project-scoped semantic code understanding.
- Human use: Use through an agent when semantic navigation is faster than plain text search.
- Cautious start: Start with project-scoped startup from the active repository, not broad filesystem access.
- Guardrails: `project-scope`, `human-approval`
- Pairs with: GitHub CLI (high), Context7 (high)
- Agent usefulness: `high`
- Human usefulness: `medium`
- Install: `codex mcp add serena -- serena start-mcp-server --project-from-cwd --context=codex`
- Notes: Best used with project-scoped startup rather than broad filesystem access.

### Docs and Knowledge MCP

#### [Context7](https://github.com/upstash/context7)

Documentation MCP server that injects current library docs and examples into agent prompts.

- Repo: `upstash/context7`
- Kind: `mcp`
- Status: `recommended`; risk: `medium`; daily use: `routine`
- Best for: `current-docs`, `framework-apis`, `agent-research`
- Agent use: Fetch current library docs and examples before implementing against APIs likely to change.
- Human use: Use as an agent-assisted documentation source when current API behavior matters.
- Cautious start: Use it to support implementation claims, then verify behavior with project tests or official sources.
- Guardrails: `human-approval`
- Pairs with: Serena (medium), GitHub CLI (medium)
- Agent usefulness: `high`
- Human usefulness: `medium`
- Install: `codex mcp add context7 -- npx -y @upstash/context7-mcp@latest`
- Notes: Useful when framework or API behavior is likely to have changed since model training.

### Formal Proof / Lean support

#### [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)

Lean LSP MCP server for proof diagnostics, goal inspection, Loogle-style search, and optional Lean
REPL acceleration.

- Repo: `oOo0oOo/lean-lsp-mcp`
- Kind: `mcp`
- Status: `recommended`; risk: `medium`; daily use: `specialist`
- Best for: `lean-proof`, `proof-diagnostics`, `formal-methods`
- Agent use: Let an agent inspect Lean proof goals, diagnostics, and search in a bound Lean project.
- Human use: Use for proof development support when working in Lean repositories.
- Cautious start: Bind LEAN_PROJECT_PATH to the active Lean project before exposing proof tooling.
- Guardrails: `project-scope`
- Pairs with: GitHub CLI (medium), delta (medium)
- Agent usefulness: `high`
- Human usefulness: `medium`
- Install: `codex mcp add lean-lsp --env LEAN_PROJECT_PATH=/path/to/lean/project -- uvx lean-lsp-mcp`
- Notes: Strong fit for Lean repositories; scope LEAN_PROJECT_PATH to the active proof project.

### Git TUI

#### [lazygit](https://github.com/jesseduffield/lazygit)

Terminal UI for everyday Git workflows such as staging, committing, rebasing, stashing, branch
navigation, and conflict-oriented local review.

- Repo: `jesseduffield/lazygit`
- Kind: `git-tui`
- Status: `recommended`; risk: `medium`; daily use: `routine`
- Best for: `local-git`, `branch-review`, `staging`
- Agent use: Medium fit; useful mainly when a human supervises local Git state around agent changes.
- Human use: Use for everyday staging, commits, rebases, stashes, branch navigation, and conflict review.
- Cautious start: Review staged changes before committing or pushing.
- Guardrails: `human-approval`
- Pairs with: GitHub CLI (medium), delta (medium)
- Agent usefulness: `medium`
- Human usefulness: `high`
- Install: `brew install lazygit`
- Notes: Best default local Git TUI; pair with gh or gh-dash for GitHub pull request and issue workflows.

#### [gitui](https://github.com/gitui-org/gitui)

Fast Rust terminal UI for local Git workflows, including diff, commit, stash, blame, log, and index
operations.

- Repo: `gitui-org/gitui`
- Kind: `git-tui`
- Status: `situational`; risk: `medium`; daily use: `specialist`
- Best for: `local-git`, `rust-tui`, `terminal-review`
- Agent use: Low fit for agents; use mainly as a human local Git interface.
- Human use: Use as a lightweight Rust TUI alternative for local Git operations.
- Cautious start: Keep it as an alternative until it clearly fits the user workflow better than lazygit.
- Guardrails: `human-approval`
- Pairs with: GitHub CLI (medium), delta (medium)
- Agent usefulness: `low`
- Human usefulness: `medium`
- Install: `brew install gitui`
- Notes: Lightweight Rust Git TUI alternative; keep as an alternative rather than the default over lazygit.

#### [tig](https://github.com/jonas/tig)

Mature text-mode interface for browsing Git history, diffs, refs, blame, and repository state in
minimal terminal environments.

- Repo: `jonas/tig`
- Kind: `git-tui`
- Status: `situational`; risk: `low`; daily use: `specialist`
- Best for: `git-history`, `ssh-terminal`, `minimal-environments`
- Agent use: Low fit for agents; use as a simple history and diff browser in constrained terminals.
- Human use: Use for browsing history, blame, refs, and diffs in minimal terminal environments.
- Cautious start: Use for read-heavy inspection before changing local Git state.
- Guardrails: `human-approval`
- Pairs with: GitHub CLI (low), delta (low)
- Agent usefulness: `low`
- Human usefulness: `medium`
- Install: `brew install tig`
- Notes: Good fallback for SSH, server, and low-dependency environments; less guided than newer Git TUIs.

#### [gitu](https://github.com/altsem/gitu)

Magit-inspired terminal Git client for hunk and line staging, commits, fixups, rebases, stashes, and
local history workflows.

- Repo: `altsem/gitu`
- Kind: `git-tui`
- Status: `watch`; risk: `medium`; daily use: `not_default`
- Best for: `magit-style-git`, `hunk-staging`, `team-evaluation`
- Agent use: Not an agent default; evaluate only for local Git workflows that need Magit-style interaction.
- Human use: Evaluate for hunk and line staging when the team wants a Magit-inspired terminal client.
- Cautious start: Try on a non-critical branch before adopting it as a daily Git interface.
- Guardrails: `human-approval`, `sandbox-repo`
- Pairs with: delta (medium)
- Agent usefulness: `low`
- Human usefulness: `medium`
- Install: `cargo install gitu`
- Notes: Promising Magit-style TUI with narrower adoption than lazygit and gitui; keep in watch until use cases are clearer.

### Git Diff and Repo Utilities

#### [delta](https://github.com/dandavison/delta)

Syntax-highlighting pager for Git, diff, grep, ripgrep JSON, and blame output that improves review
readability.

- Repo: `dandavison/delta`
- Kind: `git-pager`
- Status: `recommended`; risk: `low`; daily use: `routine`
- Best for: `diff-review`, `readability`, `git-pager`
- Agent use: Use to make diff and review output easier for humans supervising agent changes.
- Human use: Use as a pager upgrade for readable Git, diff, grep, ripgrep JSON, and blame output.
- Cautious start: Configure as a pager first; it improves review readability without changing GitHub state.
- Pairs with: GitHub CLI (medium), lazygit (medium)
- Agent usefulness: `medium`
- Human usefulness: `high`
- Install: `brew install git-delta`
- Notes: High-value diff and pager upgrade; improves review readability without replacing Git or GitHub workflows.

#### [ghq](https://github.com/x-motemen/ghq)

Local repository manager that standardizes clone locations and makes multi-host or polyrepo
workspaces easier to navigate.

- Repo: `x-motemen/ghq`
- Kind: `repo-manager`
- Status: `situational`; risk: `low`; daily use: `reviewed`
- Best for: `repo-organization`, `polyrepo`, `local-workspaces`
- Agent use: Medium fit for agents that need predictable local clone locations across many repositories.
- Human use: Use to standardize clone locations and navigate multi-host or polyrepo workspaces.
- Cautious start: Treat it as local repository organization, not as GitHub API or PR tooling.
- Guardrails: `project-scope`
- Pairs with: GitHub CLI (low), lazygit (medium)
- Agent usefulness: `medium`
- Human usefulness: `high`
- Install: `brew install ghq`
- Notes: Useful for polyrepo and multi-host local repository organization; not a GitHub API tool.

### Legacy / Avoid

#### [hub](https://github.com/mislav/hub)

Legacy command line wrapper that extends Git with GitHub operations but has largely been superseded
by the official GitHub CLI.

- Repo: `mislav/hub`
- Kind: `cli`
- Status: `avoid`; risk: `medium`; daily use: `not_default`
- Best for: `legacy-migration`, `non-recommendation`
- Agent use: Do not use for new agent workflows; prefer GitHub CLI.
- Human use: Keep only as migration context for legacy users moving to gh.
- Cautious start: Do not start new GitHub workflows with hub; migrate to gh instead.
- Guardrails: `human-approval`
- Agent usefulness: `low`
- Human usefulness: `low`
- Install: `brew install hub`
- Notes: Keep only to explain migration pressure toward gh; do not recommend for new GitHub CLI workflows.

## Machine-Readable Data

- Source of truth: `catalog/tools.yml`
- Schema: `schema/tool.schema.json`
- Generated JSON: `dist/catalog.v2.json`
- Generated README: `README.md`

## Governance and Contributions

- See `CONTRIBUTING.md` before opening issues or pull requests.
- See `docs/curation-governance.md` for inclusion, removal, taxonomy, evidence, and recommendation rules.
- See `docs/maintenance.md` for refresh cadence, automation policy, and public roadmap rules.
- See `docs/pr-review-checklist.md` for maintainer review expectations.

## Validation

```bash
python scripts/validate_catalog.py
python scripts/render_readme.py --check
python scripts/render_catalog_json.py --check
python scripts/check_links.py
```

## License

CC0-1.0. See `LICENSE`.
