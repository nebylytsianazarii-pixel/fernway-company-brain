---
owner: Hana Kim (maintainer)
last_verified: 2026-11-26
review_every_days: 90
status: live
sources: .github/workflows/stale-docs.yml, scripts/check_stale.py, meta/keeping-it-alive.md
---

# Agent: Stale doc check

| Field | Value |
|---|---|
| What it does | Lists every doc whose `last_verified` plus `review_every_days` is in the past, and every doc with `status: gap` or `status: disputed` |
| Trigger | First day of every month (GitHub Actions schedule), or by hand from the Actions tab |
| Where it lives | `.github/workflows/stale-docs.yml` runs `scripts/check_stale.py` |
| What it reads | The YAML header of every Markdown file in this repo |
| What it writes or changes | Opens one GitHub issue with the list, labelled `brain-review` |
| Customer data involved | No |
| Secrets it uses | The workflow's own temporary GitHub token, nothing stored |
| Owner | Hana Kim (maintainer) |
| If it breaks | No monthly issue appears; check the Actions tab |
| How to switch it off | Settings, Actions, disable the "Stale doc check" workflow |

Run it locally: `python3 scripts/check_stale.py`.
