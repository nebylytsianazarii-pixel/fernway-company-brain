---
owner: Hana Kim (Ops lead)
last_verified: 2026-11-26
review_every_days: 90
status: current
sources: Context Pack section 1 (pricing), section 2 (Hana), section 4 "Billing", section 6 (account vs venue)
---

# Billing

| | |
|---|---|
| System | Stripe |
| Invoiced | Monthly, per venue |
| Contracts | Per account (one account, many venues) |
| Failed payments | Chased by hand. Hana checks Stripe every Monday. |
| Owner | Hana Kim |
| External | A Berlin bookkeeping firm |

Price and discounts: `pricing-and-discounts.md`.

## Known gaps

1. GAP: what Hana does with a failed payment after spotting it (who is contacted, after how many days, when service stops). Not in the brain yet. Ask Hana, then turn it into a runbook.
2. GAP: who covers the Monday check when Hana is away. No backup is named.
3. GAP: what the bookkeeping firm needs from Fernway and when. Ask Hana.
