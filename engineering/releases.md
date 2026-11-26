---
owner: Ivan Petrenko (CTO)
last_verified: 2026-11-26
review_every_days: 90
status: current
sources: Context Pack section 4 "Releases", section 5 rule 5, section 6 (Friday freeze)
---

# Releases

| | |
|---|---|
| Owner | Ivan Petrenko |
| Flow | Linear ticket, pull request, Ana tests on staging, deploy |
| Deploy days | Tuesdays and Thursdays |
| Never | Fridays (Friday freeze, team rule 5) |
| Testing | Ana Silva on staging |
| Production incidents | Noor Haddad, on call |

Step-by-step: [runbooks/ship-a-release.md](../runbooks/ship-a-release.md).

## Known gaps

1. GAP: what to do with an urgent fix on a Friday (does the Friday freeze have an exception for production incidents?). Ask Ivan.
2. GAP: how to roll back a bad deploy. Ask Ivan or Noor.
3. Staging depends on one person, see `staging.md`.
