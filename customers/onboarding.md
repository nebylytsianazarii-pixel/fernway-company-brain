---
owner: Lukas Weber (Customer Success)
last_verified: 2026-11-26
review_every_days: 90
status: current
sources: Context Pack section 1 (positioning), section 4 "New customer onboarding", section 6 (T2L, pay rules, the importer)
---

# Customer onboarding

Onboarding speed is Fernway's whole positioning: the pitch is that a venue is live in under a day. So onboarding is measured by T2L (time to live: contract signed to first schedule published).

| | |
|---|---|
| Owner | Lukas Weber, end to end |
| Starts | Contract signed in HubSpot |
| Ends | Handover to support after the 7-day check-in |
| Typical T2L today | 1 to 3 days |
| Promise in the sales pitch | Live in under a day |

The gap between the promise (under a day) and today (1 to 3 days) is worth knowing before you talk to a customer.

## The steps

Full numbered procedure: [runbooks/onboard-a-new-customer.md](../runbooks/onboard-a-new-customer.md).

1. Contract signed in HubSpot.
2. 45-minute setup call.
3. Venue and staff list imported from the customer's CSV.
4. Pay rules configured for the country.
5. Customer publishes their first schedule (T2L stops here).
6. 7-day check-in call.
7. Handover to support.

## Known problem: the importer

The CSV importer fails on names with non-Latin characters and on files exported from Apple Numbers. Noor Haddad knows the workaround. It has never been written down, so Lukas messages Noor every time. See [runbooks/importer-fails-on-csv.md](../runbooks/importer-fails-on-csv.md) (status: gap until Noor writes it).

## Not the same as Activation

T2L ends at the first published schedule. "Activation" has three meanings at Fernway and none is agreed. See `GLOSSARY.md`.
