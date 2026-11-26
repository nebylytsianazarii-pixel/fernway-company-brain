---
owner: GAP, not named in the pack (proposed: Jonas Berg as support owner, with Ivan Petrenko for data rules)
last_verified: 2026-11-26
review_every_days: 30
status: trial
sources: Context Pack section 7 (Claude for support drafts), section 5 rule 3, section 4 "Support escalation"
---

# Agent: Claude support draft replies

| Field | Value |
|---|---|
| What it does | Drafts replies to customer support tickets, which a person then edits and sends |
| Trigger | A person pastes ticket text into Claude and asks for a draft |
| Where it lives | Claude (the team is trying it out) |
| What it reads | Whatever is pasted in: ticket text from Intercom |
| What it writes or changes | Nothing directly; a person copies the draft back into Intercom |
| Customer data involved | Yes, unless people strip it before pasting |
| Secrets it uses | None known |
| Owner | GAP: nobody is named as owner of the trial |
| If it breaks | Drafts are wrong or contain made-up product facts; the person sending must check every draft |
| How to switch it off | Stop pasting tickets into it; there is no integration to disconnect |

## Why this is registered even though it is "just a trial"

It is the one AI automation Fernway already runs, and it collides with a team rule:

1. Team rule 3: customer data stays in HubSpot, Stripe and the production database. No exports into AI tools.
2. Support drafts need the ticket text, and tickets contain customer names, venues and staff details.
3. The pack says no rules exist yet for what may be pasted in.

## Until the owner and the rule are decided

Not a decision, a holding position for whoever uses it this week:

1. Paste only the question itself. Remove customer names, venue names, staff names, emails and phone numbers first.
2. Never paste exports, screenshots of the product with staff data, or billing details.
3. A person reads and edits every draft before it is sent.

The real rule is open question OQ-7 in `decisions/open-questions.md`, for Ivan (data) and Jonas (support) to decide, with Mara signing off.
