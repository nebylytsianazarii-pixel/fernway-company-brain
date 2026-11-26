# Fernway company brain

Everything the Fernway team knows that you would otherwise have to ask a person for: how work flows, who owns what, the rules, and the words we use in our own way. Plain Markdown in Git, so every change is visible and reviewed, and so both a new colleague and Claude can read it and answer from it.

If you had to ask someone to find something out, it belongs here. If you answer the same question twice, write it down (team rule 2).

## Start here

| I need to... | Go to |
|---|---|
| Understand what Fernway sells and to whom | [company/overview.md](company/overview.md) |
| Find who owns something or who to ask | [company/team-and-owners.md](company/team-and-owners.md) |
| Find where data lives and how to get access | [company/tools-and-data.md](company/tools-and-data.md) |
| Know the team rules | [company/team-rules.md](company/team-rules.md) |
| Handle a customer at any step (lead, pricing, onboarding, support, billing) | [customers/](customers/README.md) |
| Onboard a new customer, step by step | [runbooks/onboard-a-new-customer.md](runbooks/onboard-a-new-customer.md) |
| Route a support ticket | [runbooks/escalate-a-support-ticket.md](runbooks/escalate-a-support-ticket.md) |
| Ship a release | [runbooks/ship-a-release.md](runbooks/ship-a-release.md) |
| Look up a Fernway word (T2L, Mara-check, ghost shift...) | [GLOSSARY.md](GLOSSARY.md) |
| Find out what a bot or automation does and who owns it | [agents/](agents/README.md) |
| Check whether something was decided | [decisions/](decisions/README.md) |
| Add or fix something in the brain | [runbooks/add-or-fix-a-doc.md](runbooks/add-or-fix-a-doc.md) |

## How to use it day to day

1. Ask Claude: open Claude Code in this folder and ask your question in plain words. It answers from these files and names the file it used.
2. Ask in GitHub: open an issue and write `@claude` plus your question. Claude answers in the issue.
3. Read: the table above gets you to the right file in two clicks.
4. Fix: found something wrong or missing? Open a pull request, or open an issue and ask `@claude` to draft one. The doc owner reviews it.

## What you will not find here, on purpose

Passwords and keys (1Password), customer contacts and exports (HubSpot, Stripe, the production database), salaries and HR data (founders only). See [CONTRIBUTING.md](CONTRIBUTING.md).

## Who looks after it

Maintainer (proposed): Hana Kim, Ops lead. Each folder has an owner who reviews changes. How it stays current: [meta/keeping-it-alive.md](meta/keeping-it-alive.md).
