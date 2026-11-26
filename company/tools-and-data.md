---
owner: Hana Kim (Ops lead, tooling admin)
last_verified: 2026-11-26
review_every_days: 90
status: current
sources: Context Pack section 3 "Tools" and section 5 "Team rules"
---

# Tools and where data lives

Rule of thumb: customer data stays in the system it lives in. No exports into docs, spreadsheets or AI tools (team rule 3). Secrets live in 1Password (team rule 4).

| Tool | Used for | Holds customer data? | Notes |
|---|---|---|---|
| Slack | Main channel for everything | Sometimes, in threads | Most decisions happen in threads and are never recorded elsewhere: copy them to `decisions/`. |
| Notion | About 60 old pages | Unknown | Mostly untouched since the first six months. Do not treat it as current. This brain replaces it page by page. |
| HubSpot | CRM and sales pipeline | Yes | Where every lead and contract lives. Customer contacts stay here. |
| Linear | Engineering tickets | No (should not) | Start of every release. |
| Intercom | Customer support inbox | Yes | Where Jonas works. |
| Stripe | Billing and invoices | Yes, financial | Hana checks failed payments every Monday. |
| Google Workspace | Docs, shared drive, calendars | Possibly | |
| Metabase | Dashboards over the production database | Yes, read-only | One shared read-only login, credentials in 1Password. Its "activation" number is not the sales or CS definition, see `GLOSSARY.md`. |
| n8n | Ivan's automation instance | Unknown | Six or seven workflows nobody else can explain; some have API keys pasted into nodes. See `agents/n8n-workflows.md`. |
| 1Password | Secrets | No | The only place for passwords, API keys and shared logins. |
| Claude | Trial: support draft replies | Risk | No rules yet for what may be pasted in. See `agents/claude-support-drafts.md`. |
| GitHub (this repo) | The company brain | No, by rule | See `CONTRIBUTING.md`. |

## Access

GAP: the pack does not say who grants access to each tool. Hana Kim owns tooling admin, so ask her first. New hires often wait until week two for accounts, see `people/hiring-and-new-joiners.md`.
