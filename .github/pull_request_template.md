## Summary

- 

## Issue Coverage

- 

## Catalog Review

- [ ] I updated `catalog/tools.yml` for catalog entry changes.
- [ ] I did not manually edit generated README sections without regenerating or checking them.
- [ ] I checked the category, recommendation status, usefulness ratings, and risk against `docs/curation-governance.md`.
- [ ] I handled duplicate or overlapping tools with distinct notes, status, or removal.

## Evidence

- [ ] Public source URLs support the factual claims.
- [ ] Volatile facts include a confirmation date or were omitted.
- [ ] No private scans, pasted reports, secrets, or unpublished operational details are used as accepted evidence.

## Validation

- [ ] `python -B scripts/validate_catalog.py`
- [ ] `python -B scripts/render_readme.py --check`
- [ ] `python -B scripts/check_links.py`
- [ ] `python -B scripts/check_links.py --live` when the change depends on live URL state
- [ ] `python -B scripts/check_repo_status.py` when the change depends on repository status
