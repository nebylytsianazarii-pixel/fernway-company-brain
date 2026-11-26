# Contributing to the Fernway brain

These rules apply to everyone who changes this repo: people, Claude Code on your laptop, and @claude in GitHub. A brain people trust is only useful while it is true, so the rules are mostly about keeping wrong and dangerous content out.

## The 9 hard rules

1. Source or it stays out. Every fact names where it came from in the doc's `sources` field: a Slack thread link, a decision file, a system, or the person who confirmed it. "Everyone knows" is not a source.
2. Disagreements stay visible. If two people or two docs say different things, set `status: disputed`, write both versions, and name who decides. Do not pick a winner inside a doc. Log it in `decisions/open-questions.md`.
3. Gaps stay visible. If something is not written down anywhere, set `status: gap`, write what is missing, and name the person who knows. Never fill a gap with a guess, from a person or from an AI.
4. Never in this repo: passwords, API keys, tokens or logins (write "in 1Password"); customer personal or financial data, exports, per-account prices or contract terms (they stay in HubSpot, Stripe, the production database); compensation, salaries, HR or health data; personal phone numbers.
5. Every doc has a header (copy `templates/doc.md`): owner, last_verified, review_every_days, status, sources.
6. Nothing lands in main without a pull request reviewed by the doc's owner. Nobody pushes to main directly, admins included. AI may draft and open pull requests, never approve or merge them.
7. Decisions are logged. A decision made in a Slack thread or a meeting is copied into `decisions/` with the date, who decided, and a link.
8. English, plain Markdown, short. Numbered steps for procedures, tables for routing, one topic per file.
9. Answered twice, written once. If you answer the same question a second time, open a pull request (or an issue asking `@claude` to draft one).

## Who can change what

| Area | Owner who reviews pull requests |
|---|---|
| `company/` | Mara Voss (pricing, rules), Hana Kim (tools) |
| `customers/` | Priya Raman (leads), Lukas Weber (onboarding), Jonas Berg (support), Hana Kim (billing), Mara Voss (pricing) |
| `engineering/` | Ivan Petrenko |
| `people/` | Mara Voss (until a Head of People is hired) |
| `runbooks/` | the owner named in the runbook |
| `agents/` | Ivan Petrenko for n8n, the agent's named owner otherwise |
| `decisions/` | Mara Voss |
| `meta/`, `templates/`, `CLAUDE.md`, this file | Hana Kim (maintainer) |

Anyone at Fernway may propose a change to any file. Only the owner (or the maintainer if the owner is away) merges it.

## Who can see it

In real use this repo is private to the Fernway GitHub organisation: all 15 employees can read it. Contractors (marketing, bookkeeping firm, designer) get no repo access by default; send them the specific doc they need. It is public here only because it is a training exercise about a fictional company.

## How a change gets in

1. Create a branch: `git switch -c docs/short-description`.
2. Edit or add the file. Keep the header up to date.
3. Open a pull request. Fill in the template: what changed, the source, who confirmed it.
4. The owner reviews. If the content is a claim nobody can confirm, it goes in as `status: gap` or stays out.
5. The owner merges. Delete the branch.

Full steps: [runbooks/add-or-fix-a-doc.md](runbooks/add-or-fix-a-doc.md).
