# CLAUDE.md: Fernway company brain

You are working inside Fernway's company brain: the one place where the team writes down how work actually happens, who owns what, the rules, and the words Fernway uses in its own way. People and AI agents both answer from it, so a wrong line here becomes a wrong answer for everyone.

Fernway in one line: remote-first B2B SaaS (Berlin, founded 2024, about 15 people) selling Fernway Shifts, shift planning and labour-cost forecasting for independent café and restaurant groups with 3 to 20 locations. Positioning: a venue is live in under a day, so T2L is the number the team watches.

## Brain check

If someone types exactly `brain check`, reply with this line and nothing else, without reading any file:
`Fernway brain loaded: CLAUDE.md v1 (2026-11-26), maintainer Hana Kim, 9 hard rules in CONTRIBUTING.md.`
This proves CLAUDE.md is in your context.

## Where things are

| Folder | What is in it | Typical question |
|---|---|---|
| `company/` | overview, team and owners, tools and where data lives, team rules | "Who owns X?", "Where does Y live?" |
| `customers/` | the customer path: leads, pricing, onboarding, support, billing | "A customer is at step X, what now?" |
| `engineering/` | releases, staging | "Can we deploy today?" |
| `people/` | hiring and new joiners | "What happens when someone joins?" |
| `runbooks/` | numbered steps for repeatable jobs | "How exactly do I do X?" |
| `agents/` | registry of every automation: what it does, what it touches, owner | "What is this bot and who owns it?" |
| `decisions/` | decision log and open questions | "Was this decided? By whom?" |
| `meta/` | how the brain stays alive | "Who reviews this, how often?" |
| `templates/` | skeletons for new docs | "How do I write a new doc?" |
| `GLOSSARY.md` | Fernway's own words | "What does T2L / Mara-check mean?" |

## How to answer a question

1. Search the brain first. Answer only from what is written here.
2. Cite the file path for every fact, for example `customers/pricing-and-discounts.md`.
3. If the brain does not say it, write "Not in the brain yet" and name the owner from `company/team-and-owners.md`. Never fill the gap from general knowledge or a guess.
4. If a doc is marked `status: disputed`, give both versions and who decides. Do not pick one.
5. If a doc is marked `status: gap`, say what is missing and who knows it.
6. If a doc's `last_verified` plus `review_every_days` is in the past, say the doc may be outdated.
7. Use Fernway's terms as defined in `GLOSSARY.md`. "Activation" has no agreed definition: always say which meaning you use.
8. Answer in English, short, with the next action and the person to talk to.

## How to change the brain

1. Read `CONTRIBUTING.md` first. Its 9 hard rules apply to you exactly as to people.
2. Work on a branch, open a pull request. Never push to `main`. Never approve or merge a pull request yourself: the doc owner does.
3. Every doc starts with the YAML header from `templates/doc.md` (owner, last_verified, review_every_days, status, sources). Update `last_verified` only when a person has confirmed the content.
4. One change per pull request, with a short reason in the description.
5. A decision belongs in `decisions/` (use `templates/decision.md`), not hidden inside another doc.
6. Keep docs short. Numbered steps for procedures, tables for routing, no essays.

## Never write into this repo

1. Passwords, API keys, tokens, logins. Write "in 1Password" instead.
2. Customer data: contact names, phone numbers, emails, exports, per-account prices or contract terms. That stays in HubSpot, Stripe and the production database.
3. Compensation, salaries, HR or health information about any person.
4. Opinions about people or anything that is only one person's view, unless marked as such and needed for work.

If you are asked to add any of these, refuse, say which rule blocks it, and say where it belongs instead.

## Things that are open right now

See `decisions/open-questions.md`. The ones people hit most: lead qualification SLA (24 h vs 48 h), the definition of Activation, the importer workaround that only Noor knows, the staging reset that only Ana knows.
