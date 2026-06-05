# Contributing

This catalog is intentionally small, public, and opinionated. It lists tools
that materially help AI agents or humans work with GitHub, repository
automation, pull requests, CI, browser testing, code intelligence,
documentation, or proof-oriented development.

## Source of Truth

Edit `catalog/tools.yml` for catalog entries. `README.md` is generated from the
catalog; do not edit generated catalog sections by hand.

Use these docs while preparing a change:

- `docs/curation-governance.md` for inclusion, removal, taxonomy, evidence, and
  recommendation status rules.
- `docs/pr-review-checklist.md` for review expectations.
- `docs/maintenance.md` for recurring refresh and public roadmap rules.

## Required Fields

Every catalog entry needs:

- `name`, `repo`, `url`, `kind`, and `category`
- `summary`, `install`, and optional `notes`
- `agent_usefulness`, `human_usefulness`, `risk`, and
  `recommended_status`

Use conservative risk ratings for tools that write files, run commands, access
authenticated services, control browsers, or trigger CI/CD.

Use `watch` for tools that are promising but preview-only, broad-permission,
operationally heavy, or not yet a good default. Use `avoid` only when the entry
should explicitly explain a non-recommendation or migration path.

## Evidence Expectations

Prefer public sources in this order:

1. Official repository, README, docs, release notes, or maintainer source.
2. Public package metadata from Homebrew, npm, crates.io, PyPI, docs.rs, or a
   similar registry.
3. Secondary commentary only when it is clearly labeled.

Volatile facts such as stars, installs, latest release dates, preview status,
archived status, or maintenance activity require a confirmation date. Private
scans, pasted reports, and local-only notes can guide investigation, but they
are not accepted public evidence for catalog claims.

## Opening Issues

Use the issue forms for tool suggestions, existing tool updates, removal or
deprecation requests, and category changes. Include public source URLs and risk
notes so maintainers can make the decision without private context.

## Before Opening a Pull Request

Run the deterministic checks:

```bash
python -B scripts/validate_catalog.py
python -B scripts/render_readme.py --check
python -B scripts/check_links.py
```

Run live checks when the change depends on current URL or repository state:

```bash
python -B scripts/check_links.py --live
python -B scripts/check_repo_status.py
```

The scheduled workflow runs live link and repository status checks. Pull request
validation stays network-free to avoid flaky PR results.
