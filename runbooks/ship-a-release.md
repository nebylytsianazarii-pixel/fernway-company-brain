---
owner: Ivan Petrenko (CTO)
last_verified: 2026-11-26
review_every_days: 90
status: current
sources: Context Pack section 4 "Releases", section 5 rule 5
---

# Runbook: Ship a release

Goal: a change reaches production safely.
When to use: a Linear ticket is ready to go out.
Owner: Ivan Petrenko.

## Steps

1. Make sure the work has a Linear ticket.
2. Open a pull request for it.
3. Ana Silva tests it on staging.
4. Check the day: deploy only on a Tuesday or a Thursday. Never on a Friday (Friday freeze).
5. Deploy.
6. If something breaks in production, Noor Haddad is on call.

## If something goes wrong

1. Staging needs a reset and Ana is away: GAP, see `engineering/staging.md`.
2. Rollback procedure: GAP, ask Ivan or Noor.

## Done when

The change is live in production, deployed on a Tuesday or a Thursday.
