---
owner: Mara Voss (CEO)
last_verified: 2026-11-26
review_every_days: 30
status: current
sources: Context Pack section 2 "The team" and section 4 "How things actually work"
---

# Team and owners: who to ask

## Who owns which flow

| Flow | Owner | Backup / next in line |
|---|---|---|
| Inbound leads | Priya Raman (SDR) | Sofia Marchetti (Head of Sales) |
| Demos | Daniel Okafor (AE) | Mara joins deals above 10 venues |
| Pricing exceptions (Mara-check) | Mara Voss | none: known bottleneck |
| Customer onboarding | Lukas Weber (Customer Success) | GAP: no backup named |
| Support, first line | Jonas Berg | Ana Silva for technical issues |
| Production incidents | Noor Haddad (on call) | Ivan Petrenko for anything with customer data |
| Billing and failed payments | Hana Kim (Ops lead) | GAP: no backup named |
| Releases | Ivan Petrenko (CTO) | Ana Silva tests on staging |
| Internal automations (n8n) | Ivan Petrenko | none: only Ivan can explain them |
| Hiring | Mara Voss | no process, see `people/hiring-and-new-joiners.md` |
| Tool accounts and vendor admin | Hana Kim | |
| This brain | Hana Kim (proposed maintainer) | see `meta/keeping-it-alive.md` |

## People

| Name | Role | Team |
|---|---|---|
| Mara Voss | CEO, co-founder. Fundraising, pricing, top 5 accounts | Founders |
| Ivan Petrenko | CTO, co-founder. Product and engineering, built all internal automations | Founders, Engineering |
| Noor Haddad | Backend lead, on call for production incidents | Engineering |
| Tom Bäcker | Frontend | Engineering |
| Ana Silva | QA and technical support, 50/50 | Engineering |
| Sofia Marchetti | Head of Sales | Go-to-market |
| Daniel Okafor | Account Executive, runs demos | Go-to-market |
| Priya Raman | SDR, outbound and inbound qualification | Go-to-market |
| Lukas Weber | Customer Success, owns onboarding end to end | Go-to-market |
| Emma Doyle | Marketing, part-time contractor, 2 days a week | Go-to-market |
| Hana Kim | Ops lead: billing, invoices, vendor accounts, tooling admin | Operations |
| Jonas Berg | Support agent, first line | Operations |
| Head of People | Open role, unfilled since March | Operations |

External: a Berlin bookkeeping firm, and a freelance designer used per project.

## Single points of failure (known today)

1. Only Noor knows the importer workaround: `runbooks/importer-fails-on-csv.md`.
2. Only Ana knows how to reset staging, and she is away three weeks in August: `engineering/staging.md`.
3. Only Ivan can explain the n8n workflows: `agents/n8n-workflows.md`.
4. Every pricing exception waits for Mara: `customers/pricing-and-discounts.md`.
