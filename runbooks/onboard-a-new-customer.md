---
owner: Lukas Weber (Customer Success)
last_verified: 2026-11-26
review_every_days: 90
status: current
sources: Context Pack section 4 "New customer onboarding", section 6 (T2L, pay rules, the importer)
---

# Runbook: Onboard a new customer

Goal: the customer's venues publish their first schedule (T2L stops), then the account is handed to support.
When to use: a contract is signed in HubSpot.
Owner: Lukas Weber. Ask him before changing this runbook.
Time: typical T2L is 1 to 3 days. The sales promise is live in under a day, so every hour counts.

## Steps

1. Check the contract is marked signed in HubSpot. Note how many venues the account has: billing is per venue, the contract is per account.
2. Book a 45-minute setup call with the customer.
3. Get the venue and staff list from the customer as a CSV.
4. Import the CSV with the importer.
   - If it fails on non-Latin names or the file came from Apple Numbers: follow `runbooks/importer-fails-on-csv.md`.
5. Configure the pay rules (break and overtime rules) for the customer's country: Germany, the Netherlands or Ireland.
6. Make sure the customer publishes their first schedule. This is the end of T2L.
7. Book the 7-day check-in call.
8. Hold the check-in call.
9. Hand the account over to support (Jonas Berg).

## If something goes wrong

1. Importer fails: see step 4.
2. GAP: what to do if the pay rules for a country do not match what the customer expects. Ask Lukas.
3. GAP: where T2L is recorded for each customer. Ask Lukas.

## Done when

The customer has published their first schedule, the 7-day check-in has happened, and Jonas knows the account.

## Do not

Paste the customer's staff CSV into Slack, a doc or an AI tool (team rule 3). It stays in the import.
