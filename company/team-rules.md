---
owner: Mara Voss (CEO)
last_verified: 2026-11-26
review_every_days: 180
status: current
sources: Context Pack section 5 "Team rules"
---

# Team rules

The six rules everyone at Fernway works by, with what each means in practice.

| # | Rule | In practice |
|---|---|---|
| 1 | No decisions in DMs. Anything affecting more than one person goes in a public Slack channel. | Then copy the decision into `decisions/`, or it is lost in the thread. |
| 2 | Answer the same question twice and it gets written down. | The rule the team breaks most. The brain exists to make it easy: open a pull request, or ask `@claude` in an issue to draft it. |
| 3 | Customer data stays in the systems it lives in (HubSpot, Stripe, the production database). No exports into docs, spreadsheets or AI tools. | Also applies to this repo and to Claude. Conflicts with the support drafts trial, see `agents/claude-support-drafts.md`. |
| 4 | Secrets live in 1Password. Never in Slack, a document or a repo. | Currently broken in n8n (keys pasted into nodes), see `agents/n8n-workflows.md`. |
| 5 | No deploys on Friday (Friday freeze). | Releases go out Tuesdays and Thursdays, see `engineering/releases.md`. |
| 6 | English is the working language, including in country channels. | This brain is written in English. |
