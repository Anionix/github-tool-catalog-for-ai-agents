# PR Review Checklist

Use this checklist for pull requests that add, update, remove, or recategorize
catalog entries.

## Required Checks

- [ ] `catalog/tools.yml` is the source of truth for catalog entries.
- [ ] `README.md` was regenerated or verified with
  `python -B scripts/render_readme.py --check`.
- [ ] `dist/catalog.v2.json` was regenerated or verified with
  `python -B scripts/render_catalog_json.py --check`.
- [ ] `python -B scripts/validate_catalog.py` passes.
- [ ] `python -B scripts/check_links.py` passes.
- [ ] Live checks were run when the change depends on current URL or repository
  state: `python -B scripts/check_links.py --live` and
  `python -B scripts/check_repo_status.py`.

## Source and Evidence

- [ ] The PR links to an official repository, official docs, release notes, or
  public package metadata for every factual claim.
- [ ] Volatile facts include a confirmation date or are omitted.
- [ ] Private scans, pasted reports, and local-only notes are not treated as
  accepted public evidence.

## Curation Review

- [ ] The category matches the boundaries in `docs/curation-governance.md`.
- [ ] The recommendation status matches the generated README legend.
- [ ] Risk is conservative for tools that write files, run commands, access
  authenticated services, control browsers, or trigger CI/CD.
- [ ] Overlap with existing tools is handled by distinct notes, a different
  status, or removal.
- [ ] `watch` and `avoid` entries explain why they are not defaults.

## Practical Advice Review

- [ ] `daily_use`, `agent_use`, `human_use`, `cautious_start`, and `guardrails`
  do not overstate the recommendation status.
- [ ] High-risk tools show a concrete guardrail beside practical advice.
- [ ] `watch` entries are excluded from starter kits unless they are in an
  evaluation kit with caveats.
- [ ] `avoid` entries are excluded from kits and `pairs_with`.
- [ ] `pairs_with` and starter/evaluation kits still reference existing tools
  and reflect combined risk.

## Public Safety

- [ ] Summary and notes are short, public-safe, and specific.
- [ ] The PR does not expose tokens, private scan outputs, private operational
  details, or unpublished evidence.
