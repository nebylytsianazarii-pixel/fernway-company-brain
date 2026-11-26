---
owner: Hana Kim (proposed maintainer)
last_verified: 2026-11-26
review_every_days: 90
status: current
sources: CONTRIBUTING.md, decisions/2026-11-26-start-a-company-brain.md
---

# How the brain stays alive

A brain nobody feeds is worse than no brain: people stop asking and start trusting it. Git only keeps history; it does not keep anything true. These are the habits and checks that do.

## Who

| Role | Person | Does what |
|---|---|---|
| Maintainer | Hana Kim (proposed, OQ-9) | Owns this repo, runs the monthly review, merges when an area owner is away |
| Area owners | See `CONTRIBUTING.md` | Review and merge pull requests for their folder; confirm `last_verified` |
| Everyone | All 15 | Ask the brain first; fix what is wrong; write down what they answer twice |
| New joiners | Whoever joins next | Read it in week 1 and open an issue for everything missing or wrong |

Why Hana: she already owns tooling admin and already has a Monday routine (the Stripe check). The brain review hooks onto a habit that exists.

## When

1. Every change: through a pull request, reviewed by the area owner. `main` is protected.
2. Every month, first Monday, 30 minutes: Hana goes through the issue the stale doc check opened, pings each owner, and closes the issue when every listed doc is re-verified, marked `gap`, or deleted.
3. Every decision: copied from Slack into `decisions/` the same week.
4. Every quarter: Mara looks at `decisions/open-questions.md` and closes at least the oldest open question.

## How a doc shows it might be wrong

1. Every doc has `last_verified` and `review_every_days` in its header. Past that date, Claude warns that the doc may be outdated, and the monthly check lists it.
2. `status: disputed` means two versions exist and nobody decided. `status: gap` means nobody wrote it down. Both are visible on purpose.
3. A doc that nobody can verify gets deleted, not kept "just in case". An outdated confident doc is more dangerous than a missing one.

## The monthly check

The stale doc check (GitHub Actions, first day of the month) opens an issue listing every doc that is past its review date or marked gap or disputed. Run it by hand any time: `python3 scripts/check_stale.py`.
