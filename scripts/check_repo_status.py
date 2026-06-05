#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import UTC, datetime

from catalog_common import load_catalog


STALE_WARNING_DAYS = 730


def github_request(repo: str) -> dict[str, object]:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "Anionix-awesome-github-tools-repo-status/1.0",
            **auth_header(),
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def auth_header() -> dict[str, str]:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        return {}
    return {"Authorization": f"Bearer {token}"}


def pushed_age_days(value: object) -> int | None:
    if not isinstance(value, str) or not value:
        return None
    pushed_at = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return (datetime.now(UTC) - pushed_at).days


def main() -> int:
    catalog = load_catalog()
    repos = sorted({str(tool["repo"]) for tool in catalog["tools"]})
    failures: list[str] = []
    warnings: list[str] = []

    for repo in repos:
        try:
            data = github_request(repo)
        except urllib.error.HTTPError as error:
            failures.append(f"{repo}: GitHub API returned {error.code}")
            continue
        except urllib.error.URLError as error:
            failures.append(f"{repo}: {error.reason}")
            continue
        except TimeoutError:
            failures.append(f"{repo}: request timed out")
            continue

        archived = bool(data.get("archived"))
        disabled = bool(data.get("disabled"))
        private = bool(data.get("private"))
        default_branch = data.get("default_branch")
        pushed_at = data.get("pushed_at")

        if private:
            failures.append(f"{repo}: repository is private")
        if archived:
            failures.append(f"{repo}: repository is archived")
        if disabled:
            failures.append(f"{repo}: repository is disabled")
        if not isinstance(default_branch, str) or not default_branch:
            failures.append(f"{repo}: missing default branch")

        age_days = pushed_age_days(pushed_at)
        if age_days is not None and age_days > STALE_WARNING_DAYS:
            warnings.append(f"{repo}: last pushed {age_days} days ago ({pushed_at})")

        state = "archived" if archived else "active"
        visibility = "private" if private else "public"
        print(f"ok: {repo} ({visibility}, {state}, default={default_branch}, pushed_at={pushed_at})")

    if warnings:
        print("\nwarnings:", file=sys.stderr)
        for warning in warnings:
            print(f"- {warning}", file=sys.stderr)

    if failures:
        print("\nfailed repositories:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"\nrepo status ok: {len(repos)} repositories checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
