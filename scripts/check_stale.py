#!/usr/bin/env python3
"""List brain docs that need attention.

A doc needs attention when:
1. last_verified + review_every_days is in the past (stale), or
2. status is gap, disputed or undocumented (known hole).

Reads only the YAML header at the top of each Markdown file. No dependencies.
Usage: python3 scripts/check_stale.py            -> prints a Markdown report
       python3 scripts/check_stale.py --today 2027-03-01   -> pretend another date
"""
import datetime as dt
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".github", "templates", "scripts", "node_modules"}
OPEN_STATUSES = {"gap", "disputed", "undocumented"}


def header(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    out = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return out
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip()
    return None


def main():
    today = dt.date.today()
    if "--today" in sys.argv:
        today = dt.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1])
    stale, holes, no_header = [], [], []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if set(rel.parts) & SKIP_DIRS or rel.name == "README.md":
            continue
        h = header(path)
        if h is None:
            if rel.parent != pathlib.Path("."):  # root files like CLAUDE.md need no header
                no_header.append(str(rel))
            continue
        owner = h.get("owner", "no owner")
        status = h.get("status", "").split()[0] if h.get("status") else ""
        try:
            verified = dt.date.fromisoformat(h.get("last_verified", ""))
            due = verified + dt.timedelta(days=int(h.get("review_every_days", "90")))
            if due < today:
                stale.append(f"| `{rel}` | {owner} | {verified} | {due} |")
        except ValueError:
            stale.append(f"| `{rel}` | {owner} | missing or invalid | now |")
        if status in OPEN_STATUSES:
            holes.append(f"| `{rel}` | {owner} | {status} |")

    print(f"# Brain review {today:%Y-%m}\n")
    print(f"Checked on {today}. Owners: re-verify, fix, mark as gap, or delete. See `meta/keeping-it-alive.md`.\n")
    print(f"## Past their review date ({len(stale)})\n")
    if stale:
        print("| Doc | Owner | Last verified | Was due |\n|---|---|---|---|")
        print("\n".join(stale))
    else:
        print("None.")
    print(f"\n## Known gaps and disputes ({len(holes)})\n")
    if holes:
        print("| Doc | Owner | Status |\n|---|---|---|")
        print("\n".join(holes))
    else:
        print("None.")
    if no_header:
        print(f"\n## Docs without a header ({len(no_header)})\n")
        print("\n".join(f"- `{p}`" for p in no_header))


if __name__ == "__main__":
    main()
