---
owner: Ana Silva (QA); escalation Ivan Petrenko
last_verified: 2026-11-26
review_every_days: 30
status: gap
sources: Context Pack section 4 "Releases", section 7 (staging reset)
---

# Staging environment

Every release is tested by Ana on staging before it goes to production (see `releases.md`).

## GAP: how staging is reset

Ana Silva is the only person who knows how the staging environment is reset. It is not written down anywhere. She is away for three weeks in August.

Risk: while Ana is away, nobody can reset staging, so releases that need a clean staging stop.

What has to happen:

1. Ana writes the reset procedure as `runbooks/reset-staging.md` (use `templates/runbook.md`) before August.
2. Somebody else (Noor or Tom) follows it once while Ana is still here, to prove it works.
3. Ivan reviews and merges it.

Tracked as OQ-4 in `decisions/open-questions.md`.
