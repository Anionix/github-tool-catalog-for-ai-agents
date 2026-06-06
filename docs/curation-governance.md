# Curation Governance

This catalog is intentionally small, public, and conservative. Entries should
help AI agents or maintainers work with GitHub-adjacent workflows without
turning the list into a general developer-tool directory.

## Inclusion Criteria

A tool can be included when all of these are true:

- It materially helps with GitHub, pull requests, CI, browser testing, code
  intelligence, documentation, proof workflows, repository organization, or
  review ergonomics.
- It has a public source or documentation URL that a reviewer can inspect.
- It can be classified by category, kind, recommendation status, usefulness,
  operational risk, and installation path.
- Its public evidence is strong enough to support the summary and notes.
- Its security and maintenance tradeoffs can be described honestly in public.

## Removal Criteria

Remove an entry, or move it to `avoid`, when one of these applies:

- The repository or official source disappears, becomes inaccessible, or no
  longer matches the catalog URL.
- The project is archived, disabled, abandoned in a way that materially affects
  safe use, or superseded by a safer default.
- The tool no longer fits a GitHub-adjacent workflow.
- Public evidence no longer supports the current summary, install command,
  recommendation status, or risk level.
- A security concern is severe enough that continuing to list the tool as useful
  would mislead maintainers.

Archived or superseded tools may remain only when the entry explains why they
are listed, usually as `avoid` or `watch`.

## Recommendation Status

Recommendation status must stay aligned with the generated README legend:

- `recommended`: a good default for the right workflow.
- `situational`: useful when the workflow clearly needs it.
- `watch`: promising, preview-only, operationally heavy, broad-permission, or
  not yet a safe default.
- `avoid`: a known mismatch for this catalog's default recommendations.

Do not use `recommended` for a tool only because it is popular. It must be a
safe default for a clearly stated workflow.

## Taxonomy

Each category has a boundary and a review concern:

| Category | Boundary | Review concern |
| --- | --- | --- |
| GitHub MCP / Connectors | Agent-facing GitHub repository, issue, pull request, workflow, project, org, or gist access. | Token scope, write permissions, read-only modes, and auditability. |
| GitHub CLI and API | Official or primary command-line control planes for GitHub operations. | Auth model, API coverage, automation safety, and exact command semantics. |
| gh Extensions | Tools installed into the GitHub CLI extension model. | Publisher trust, extension permissions, UI assumptions, and team fit. |
| Agentic Workflows | Agent runtimes or workflow systems that operate on repositories or Actions. | Billing, guardrails, workflow safety, and review boundaries. |
| Browser and Testing MCP | Browser automation or debugging MCP servers useful for repository validation. | Browser profile isolation, data exposure, and network or filesystem reach. |
| Code Intelligence MCP | Semantic code retrieval, navigation, or editing services for agents. | Project scoping, filesystem reach, indexing behavior, and language support. |
| Docs and Knowledge MCP | Documentation or knowledge retrieval services used during implementation. | Source freshness, provenance, and whether fetched docs are authoritative. |
| Formal Proof / Lean support | Proof-assistant diagnostics, search, or REPL support. | Project binding, proof environment, and correctness of reported proof state. |
| Git TUI | Terminal interfaces for local Git workflows. | Human ergonomics, local write behavior, and whether GitHub operations are out of scope. |
| Git Diff and Repo Utilities | Local diff, pager, or repository organization helpers. | Scope clarity, filesystem behavior, and whether the tool changes GitHub state. |
| Legacy / Avoid | Superseded tools kept to explain migration or non-recommendation decisions. | Avoiding accidental endorsement. |

## Evidence Standard

Use this public evidence order:

1. Official repository, README, documentation, release notes, or maintainer
   source.
2. Package metadata from a public registry such as Homebrew, npm, crates.io,
   PyPI, or docs.rs.
3. Secondary commentary only when it is clearly labeled and not used as the sole
   source for a catalog claim.

Volatile facts such as stars, install counts, latest release dates, preview
status, and maintenance activity require a confirmation date. Avoid volatile
metrics in catalog entries unless they materially affect the decision.

Private scans, pasted reports, unpublished notes, or local-only observations are
not accepted evidence for public catalog facts. They can guide investigation,
but the final claim must point to a public source or be described as a local
verification result.

## Practical Advice Standard

Practical advice is part of the public recommendation surface. It must stay
aligned with recommendation status, risk, public evidence, and generated output.

- `daily_use` describes defaultness, not popularity. `watch` and `avoid`
  entries cannot be routine defaults.
- `agent_use` must name the supervised workflow and must not imply autonomous
  write, token, browser, filesystem, or CI/CD access without guardrails.
- `human_use` should describe the human decision, review, or maintenance task.
- `cautious_start` describes the lowest-risk first step; it is not a safety
  certification.
- `guardrails` must be concrete, such as limited tokens, read-only modes,
  project scope, isolated browsers, sandbox repositories, or human approval.
- `pairs_with` must reference existing catalog entries and explain workflow fit
  plus combined risk.
- Starter kits are default-facing and must not include `watch` or `avoid`
  entries.
- Evaluation kits can include `watch` entries only when the caveat is visible
  and the workflow is framed as reviewed experimentation.

## Change Review Rules

Every catalog change should answer:

- What workflow does this tool improve?
- Which public source supports the summary and install command?
- What is the recommendation status and why?
- What is the operational risk?
- Is this a duplicate or overlap with an existing entry?
- Do practical fields, pairs, starter kits, and evaluation kits still match the
  status and risk?
- Does the generated README stay in sync with `catalog/tools.yml`?
- Does the generated JSON stay in sync with `catalog/tools.yml`?
