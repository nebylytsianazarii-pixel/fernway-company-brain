# agents/: registry of automations

Every automation that does work on its own at Fernway is listed here: what it does, what it touches, who answers for it. An automation that is not in this table is a risk: nobody can fix it, switch it off, or check what data it sees.

To register one, copy `templates/agent.md`.

| Agent | What it does | Touches customer data? | Owner | Status | Card |
|---|---|---|---|---|---|
| Claude support drafts | Drafts replies to support tickets | Yes, if ticket text is pasted in | GAP: not named | Trial, no rules yet | [claude-support-drafts.md](claude-support-drafts.md) |
| Ivan's n8n workflows | Six or seven internal workflows | Unknown | Ivan Petrenko | Undocumented | [n8n-workflows.md](n8n-workflows.md) |
| @claude in this repo | Answers questions and drafts pull requests in GitHub issues | No, by repo rule | Hana Kim (maintainer) | Live | [claude-in-github.md](claude-in-github.md) |

The first two existed before this brain. Automations the brain itself adds are registered here too.
