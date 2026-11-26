---
owner: Hana Kim (maintainer); each term's owner in the table
last_verified: 2026-11-26
review_every_days: 90
status: current
sources: Fernway Company Context Pack, section 6 "How people talk here"
---

# Glossary: how Fernway talks

Words Fernway uses in its own way. If a new hire or Claude gets one of these wrong, the answer is wrong.

| Term | What it means at Fernway | Watch out |
|---|---|---|
| **Account** | One customer company. Contracts are per account. | One account can have many venues. |
| **Venue** | One location (café or restaurant) of an account. Billing is per venue: €39 per venue per month. | New hires mix up account and venue constantly. "40 accounts, 140 venues" is the right way to say it. |
| **Pay rules** | The per-country break and overtime configuration, set by Lukas during onboarding. | Different in Germany, the Netherlands and Ireland. |
| **The importer** | The CSV staff-import tool used in onboarding. | Fails on non-Latin names and Apple Numbers exports. See `runbooks/importer-fails-on-csv.md`. |
| **T2L** | Time to live: contract signed to first schedule published. Fernway's main onboarding metric. Typical today: 1 to 3 days. | Not the same as Activation. |
| **Ghost shift** | A published shift nobody claimed. | The single most common support complaint. |
| **Friday freeze** | No deploys on Friday (team rule 5). | Releases go out on Tuesdays and Thursdays. |
| **Mara-check** | A pricing exception that needs the CEO, Mara Voss. | Anything below list price or the 15% annual discount. Known bottleneck. |
| **Activation** | **Not defined.** Sales means the first published schedule. Lukas means a full week scheduled. The Metabase dashboard measures something else. | Always say which meaning you use. Open question OQ-2 in `decisions/open-questions.md`. |

To add a term: open a pull request with the term, the meaning the team actually uses, and the source.
