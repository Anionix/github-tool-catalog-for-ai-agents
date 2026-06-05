# Maintenance Loop

This project uses public issues, public docs, and lightweight checks to keep the
catalog useful after the first reflection pass.

## Cadence

- Pull requests: run schema validation, generated README drift check, and link
  syntax checks without network-dependent live checks.
- Weekly scheduled workflow: run live link checks and repository status checks.
- Monthly human review: inspect scheduled workflow results, open follow-up
  issues for broken links, archived repositories, unclear categories, or stale
  recommendation status.
- Quarterly curation pass: review `watch`, `situational`, and `avoid` entries
  for promotion, demotion, removal, or clearer notes.

## Volatile Facts

Volatile facts include stars, install counts, latest release dates, preview
status, archived status, disabled status, default branch changes, and visible
maintenance activity. These facts require a confirmation date when they appear
in docs or issue decisions.

The catalog should avoid volatile metrics by default. Use them only when they
change the recommendation decision.

## Automation Policy

PR validation must stay deterministic and network-free:

- `python -B scripts/validate_catalog.py`
- `python -B scripts/render_readme.py --check`
- `python -B scripts/check_links.py`

Scheduled and manual validation can use the network:

- `python -B scripts/check_links.py --live`
- `python -B scripts/check_repo_status.py`

`check_repo_status.py` fails for missing, inaccessible, archived, or disabled
repositories. It warns, but does not fail, for older `pushed_at` dates because
older activity can be acceptable for stable legacy or low-churn tools.

## Public Roadmap Rules

GitHub Issues are the public roadmap surface. A roadmap item is `Done` only
when public evidence exists in the repository or in reproducible command output.
Private agreement, private scans, or local notes are not enough.

Status expectations:

- New ideas start as an issue with public source URLs and risk notes.
- Catalog changes should reference the curation governance and PR checklist.
- Maintenance findings should create follow-up issues instead of hidden TODOs.
- Closing an issue requires a concrete file, command result, PR, or workflow run
  that satisfies its acceptance criteria.
- Reopen or file a follow-up when an entry becomes broken, archived, disabled,
  superseded, or misleading.

## Follow-Up Decisions

When a scheduled check fails:

- Broken or moved URLs: update the URL if the replacement is public and clearly
  authoritative; otherwise open a removal/deprecation issue.
- Archived repositories: move the entry to `watch`, `avoid`, or remove it unless
  the entry explicitly explains why an archived tool remains useful.
- Disabled or inaccessible repositories: remove or replace the entry unless a
  public canonical source exists.
- Stale but reachable repositories: review context before changing status; old
  `pushed_at` alone is warning evidence, not automatic removal.
