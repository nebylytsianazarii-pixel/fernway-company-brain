---
owner: Nazarii Nebylytsia (proposed it); Mara Voss to confirm
last_verified: 2026-11-26
review_every_days: 180
status: proposed
sources: Context Pack sections 2 and 3 (nobody owns documentation; Notion is where documents go to die)
---

# Decision: Keep the company's knowledge in a Git repo, not in Notion

Date: 2026-11-26
Proposed by: Nazarii Nebylytsia (newest team member). Needs Mara Voss to confirm.

Context: nobody owns documentation. Notion holds about 60 pages, almost all untouched since the first six months. Decisions happen in Slack threads and are never recorded. New people interrupt colleagues for every answer and get two different answers half the time.

Options considered:

1. Clean up Notion. Rejected: it has no review step and no owner per page, which is how it rotted.
2. Pinned Slack messages. Rejected: not searchable as a whole, no history of changes.
3. A Git repo of Markdown files with owners, review dates and pull requests. Chosen.

Decision: one Git repo, plain Markdown, every change through a pull request reviewed by the area owner, every doc with an owner and a review date, readable by Claude Code and by @claude in GitHub.

Consequences:

1. Notion pages are not deleted; when someone needs one, they move the content here, verified, and add a link from Notion to here.
2. Hana Kim is proposed as maintainer (OQ-9).
3. The team rule "answer twice, write it down" now has a place and a process: `runbooks/add-or-fix-a-doc.md`.
