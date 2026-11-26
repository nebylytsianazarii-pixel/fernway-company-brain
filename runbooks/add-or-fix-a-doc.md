---
owner: Hana Kim (maintainer)
last_verified: 2026-11-26
review_every_days: 180
status: current
sources: CONTRIBUTING.md
---

# Runbook: Add or fix something in the brain

Goal: a correct change lands in main, reviewed by the person who owns that area.
When to use: you answered a question twice, found something wrong, or a decision was made in Slack.
Owner: Hana Kim (maintainer).
Time: 10 to 15 minutes.

## Steps

1. Check `CONTRIBUTING.md` rule 4: no secrets, no customer data, no salaries. If your change needs one of those, stop. It belongs in 1Password, HubSpot, Stripe or with the founders.
2. Create a branch: `git switch -c docs/short-description` (or use the GitHub web editor and choose "create a new branch").
   - Faster: open an issue, describe what is missing, and write `@claude please draft a pull request for this`. Claude drafts it; you still review it.
3. Edit the file, or copy a template from `templates/`.
4. Fill the header: `owner`, `last_verified` (today, only if a person confirmed it), `review_every_days`, `status`, `sources`.
5. If two sources disagree, set `status: disputed` and add the question to `decisions/open-questions.md`. If nobody knows, set `status: gap`.
6. Open a pull request and fill in the template.
7. The owner of that area (see `CONTRIBUTING.md`) reviews and merges. Nobody merges their own change to someone else's area.
8. Delete the branch.

## Done when

The change is in main, and the person who asked the question knows where it is.
