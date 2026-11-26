---
owner: Hana Kim (maintainer)
last_verified: 2026-11-26
review_every_days: 90
status: live
sources: .github/workflows/claude.yml, CONTRIBUTING.md
---

# Agent: @claude in this repo

| Field | Value |
|---|---|
| What it does | Answers questions about Fernway from this repo, and drafts changes as branches and pull requests |
| Trigger | A comment, issue or review in this repo that contains `@claude`, from someone with write access |
| Where it lives | `.github/workflows/claude.yml` (GitHub Actions, `anthropics/claude-code-action@v1`, Claude GitHub App) |
| What it reads | This repo, including `CLAUDE.md` |
| What it writes or changes | Issue and pull request comments; new branches with proposed changes |
| Customer data involved | No. The repo holds none by rule, and nobody may paste any into an issue. |
| Secrets it uses | `ANTHROPIC_API_KEY`, stored as a GitHub Actions secret. Value never in a file. |
| Owner | Hana Kim (maintainer) |
| If it breaks | No reply in the issue; check the Actions tab for the failed run |
| How to switch it off | Settings, Actions, disable the "Claude Code" workflow, or delete `.github/workflows/claude.yml` |

## Rules it follows

1. It loads `CLAUDE.md`, so it answers only from the brain, cites files, and says "Not in the brain yet" instead of guessing.
2. It may open branches and pull requests. It never merges: `main` is protected and the doc owner reviews.
3. Only people with write access can trigger it, so outsiders cannot spend the API budget.

## Cost

Each run uses the Anthropic API key and costs money. The maintainer checks usage in the monthly review.
