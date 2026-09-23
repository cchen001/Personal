# Reap — three postings, one decision

All three come from the same company filter, so treat them as one decision, not three.

| Posting | Verdict |
|---|---|
| **AI Operations Engineer, CX** | **Apply. This is the one.** |
| Customer Experience Specialist (Operational Support) | **Do not apply.** |
| Onboarding Operation, Lead | **Do not apply.** |

**Apply to exactly one.** A recruiter at a company this size sees every application against their name. Applying to the entry-level CX Specialist alongside the AI Operations role tells them you do not know which one you are, and they will resolve the ambiguity downward — the cheaper hire is always the easier yes. Pick the top role and let them counter-offer if they disagree.

---

## 1. AI Operations Engineer, CX — apply

This posting reads like it was written from your journals. Not an exaggeration: it names Intercom Fin, n8n, MCP, AI evaluation frameworks, guardrails, escalation logic and staged rollouts. You have done all of it, in production, in the last fourteen months.

Their headline metric is **Independently Resolved Rate: 39% today, 80% target**, and they want someone to build the reporting that tracks it. In July you built the resolution data pool — confirmed / assumed / abandoned-mid-conversation categorisation, with close and CSAT hooks feeding it live. That is their core ask, already shipped once.

The "Not suitable if" list is effectively a screen you pass on all four counts: you prefer operations to model building, you ship rather than recommend ("a recommendation just gets re-verified and saves nothing"), you are not chasing purely strategic work, and you have spent fourteen months in a system that was never stable.

Location fits too — APAC with UTC+8 overlap matches the schedule you already work.

### Requirements map

**Have it, and it is already on the resume**

| They ask for | You have |
|---|---|
| Production AI support agent config (*Intercom Fin named*) | Configured Fin as support, onboarding and CSM; custom answers, workflows, data connectors |
| Automation platforms (n8n, Make, Zapier) | n8n throughout; built a Zap for Phil, Mar 2026 |
| Modern ticketing platforms | Intercom, deeply, as sole owner |
| Analytical with support data | Corrected medians, closed-thread counts, staffed-day assumptions |
| Excellent written English | Authored the tone handbook every reply is written against |
| Ambiguity, small fast-changing teams | Six-person company, sole customer-facing hire |
| *Desirable:* agentic AI, tool calling, MCP | Documented a live 37-tool MCP server; typed `apply_action` tool |
| *Desirable:* AI evaluation frameworks / automated QA | 114-case golden eval, LLM-as-judge, deterministic scorer. **Rare — most applicants will not have this** |
| *Desirable:* prompt engineering, Notion | Both, throughout |

**Have it, but it is missing from the resume — add these**

| They ask for | Your evidence | Where it lives now |
|---|---|---|
| **Build reporting tracking IRR** | Resolution data pool: confirmed / assumed / abandoned categorisation, table, hooks, daily sweep, merged Jul 2026 | **Nowhere. Their #1 metric and it is absent** |
| Tune guardrails and escalation logic | Feb 2026: audited Intercom escalation rules, evaluated effectiveness, disabled most ahead of the 24-hour cycle | Not stated |
| Simulation runs, staged rollouts | Dry-run-then-verify on money actions; E2E suite; controlled re-close after the auto-close incident | Not stated |
| Low-code: JSON, REST, webhooks | Built two real-time webhook listeners; LLM chain returning structured JSON; bearer-token JSON API client | Buried in skills |
| *Desirable:* fintech / payments / regulated | Stripe disputes and chargebacks, GDPR erasure policy, PII handling | Present but not framed as regulated |

**Do not have**

| Gap | How real |
|---|---|
| **3+ years in CX / support ops** | Real. You have ~14 months in this function. Eight years customer-facing, but not support ops. Do not obscure it — your dates are visible |
| **Low-code JavaScript functions** | Partial. REST, JSON and webhooks yes; standalone JS functions unaided, no. Small and closeable |
| Lorikeet / Ada / Sierra | Fin is on their list, so this is covered |

### The years gap — how to handle it

Do not hide it and do not apologise. One line in the cover note:

> "I have fourteen months rather than three years in support operations, so I will be direct about it. In that time I have been the sole customer-facing person at a six-person SaaS: I configured Fin, built the resolution-tracking pool that separates confirmed from assumed from abandoned, put a 114-case eval gate in front of every agent change, and shipped autonomous refunds and credits under hard ceilings. Your IRR problem is the problem I have been working on. I would rather be judged on that than on the calendar."

That either works or it does not, and you find out fast. It is a better use of the cover note than restating the resume.

---

## 2. Customer Experience Specialist — do not apply

Explicitly **entry-level**, **24x5 shift-based**, Philippines preferred. The job is handling "Level 1/2 support escalations that AI cannot resolve."

You are the person who builds the AI that stops those escalations reaching a human. This is the "Agent" role in a different costume — and applying to it at the same company you want the AI Operations role from actively damages that application.

---

## 3. Onboarding Operation, Lead — do not apply

This is **KYB/AML compliance onboarding** — identity verification, sanctions screening, regulatory casework. Your onboarding experience is *product* onboarding: teaching users how a tool works. Same word, unrelated discipline.

You would be competing against compliance professionals and ramping from zero on the part that matters. The posting even flags that limited KYC-only experience needs a longer ramp — you have none. 85 applicants already.

---

## Next

`Reap_AI_Ops_Engineer_resume.pdf` is the tailored version: resolution-rate instrumentation promoted to the second bullet, escalation-logic and guardrail work stated, n8n and webhooks surfaced out of the skills block, MCP and the eval harness foregrounded, and the payments work framed as regulated-environment experience.

Everything in it is in `EVIDENCE.md` with a date. Nothing was invented to fit the posting.
