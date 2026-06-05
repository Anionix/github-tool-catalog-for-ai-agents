# Contributing

This catalog is intentionally small and opinionated.

Please include tools that materially help AI agents or humans work with GitHub,
repository automation, pull requests, CI, browser testing, code intelligence, or
proof-oriented development.

Before opening a pull request:

1. Add or update entries in `catalog/tools.yml`.
2. Run `python scripts/validate_catalog.py`.
3. Run `python scripts/render_readme.py --check`.
4. Prefer conservative risk ratings for tools that write files, run commands, or
   access authenticated services.

Use `watch` for tools that are promising but preview-only, broad-permission, or
not yet a good default.
