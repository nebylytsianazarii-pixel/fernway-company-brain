---
owner: Ivan Petrenko (CTO)
last_verified: 2026-11-26
review_every_days: 30
status: undocumented
sources: Context Pack section 2 (Ivan built all internal automations), section 3 (n8n), section 5 rule 4
---

# Agent: Ivan's n8n workflows

| Field | Value |
|---|---|
| What it does | Six or seven internal workflows. GAP: what each one does is not written down. |
| Trigger | GAP |
| Where it lives | Ivan's own n8n instance |
| What it reads | GAP |
| What it writes or changes | GAP |
| Customer data involved | GAP: unknown |
| Secrets it uses | API keys, some pasted directly into the nodes. Values never go here. |
| Owner | Ivan Petrenko, who built all of them alone |
| If it breaks | Nobody else can explain the workflows, so nobody else can fix them |
| How to switch it off | GAP: ask Ivan |

## Risks today

1. Single point of failure: only Ivan can explain these workflows.
2. Team rule 4 is broken: API keys pasted into nodes instead of stored as credentials from 1Password.
3. Nobody knows whether any workflow moves customer data out of HubSpot, Stripe or the database (team rule 3).

## What closes the gap

1. Ivan adds one card per workflow in this folder (copy `templates/agent.md`), starting with the ones that touch customer data.
2. Ivan moves the pasted API keys into n8n credentials backed by 1Password and rotates the exposed ones.
3. Hana Kim checks in the monthly review that every workflow has a card.

Tracked as OQ-8 in `decisions/open-questions.md`.
