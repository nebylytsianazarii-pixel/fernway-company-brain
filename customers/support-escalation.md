---
owner: Jonas Berg (support, first line)
last_verified: 2026-11-26
review_every_days: 90
status: current
sources: Context Pack section 2, section 4 "Support escalation", section 6 (ghost shift)
---

# Support and escalation

All support starts in Intercom with Jonas. He routes by the type of problem.

| The problem is... | Goes to | Role |
|---|---|---|
| Anything, first | Jonas Berg | Support agent, first line |
| Technical (product behaves wrong) | Ana Silva | QA and technical support (half her time) |
| A production incident | Noor Haddad | Backend lead, on call |
| Anything involving customer data | Ivan Petrenko | CTO |

Step-by-step: [runbooks/escalate-a-support-ticket.md](../runbooks/escalate-a-support-ticket.md).

## Most common complaint

Ghost shifts: a published shift nobody claimed. It is the single most common support complaint. GAP: the standard answer or fix is not written down. Ask Jonas or Ana.

## Draft replies with Claude

The team is trying Claude for support draft replies. No rules exist yet for what may be pasted into it, and team rule 3 forbids customer data in AI tools. Read `agents/claude-support-drafts.md` before using it.

## Known gaps

1. GAP: response time targets for support are not written down. Ask Jonas.
2. GAP: what counts as a "production incident" versus a technical issue. Ask Noor.
