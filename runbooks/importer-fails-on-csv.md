---
owner: Noor Haddad (backend lead)
last_verified: 2026-11-26
review_every_days: 30
status: gap
sources: Context Pack section 4 "New customer onboarding" (known problem)
---

# Runbook: The importer fails on a customer CSV

Goal: the customer's staff list gets imported anyway, without waiting for Noor.
When to use: the importer fails during onboarding (runbook step 4 in `onboard-a-new-customer.md`).
Owner: Noor Haddad knows the workaround.

## What we know

The importer fails on:

1. Staff names with non-Latin characters.
2. Files exported from Apple Numbers.

## GAP: the workaround

Noor knows the workaround. It has never been written down, so Lukas messages Noor every time. That costs T2L hours on Fernway's most important metric.

Until Noor fills this in:

1. Do not edit or re-type the customer's staff data by hand, and do not paste it into Slack or an AI tool (team rule 3).
2. Message Noor in a public channel (team rule 1), so the answer is visible to the next person.

To close this gap, Noor replaces this section with numbered steps and changes `status` to `current`. Tracked as OQ-3 in `decisions/open-questions.md`.
