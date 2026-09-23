# Jade Chieh Chen

chiehjadechen@gmail.com · +1 437 660 2419 · [linkedin.com/in/jade-chieh-chen](https://www.linkedin.com/in/jade-chieh-chen/)

**Founding Support Lead — Customer Operations & Production AI Systems**
*Sole support, onboarding, education and demos for a B2B SaaS — then the AI system that handles most of it. I still work the queue every morning.*

---

## SUMMARY

For fourteen months I have been the entire customer-facing function at a B2B data SaaS — support, onboarding, customer education, demos and the product-feedback loop into engineering, alone. Then I built the production AI agent that now carries most of it, including autonomous refunds and credits under hard authorization ceilings. Eight years of client-facing sales sit underneath, which is why the agent's answers sound like a person and its money guardrails were written by someone who still works the queue it serves.

---

## EXPERIENCE

### Founding Support Lead — Evaboot
**Remote · Jul 2025 – Present**
*B2B SaaS (LinkedIn Sales Navigator data extraction) | ~6-person team | Sole customer-facing hire | SMB to Enterprise*

- **Built and shipped the company's production AI support agent end to end** — knowledge base, eval harness, AWS deployment, live audit. New users route to it by default, and it executes refunds, credits, cancellations and invoice voids autonomously under typed ceilings (refund ≤ $29, credit ≤ 200), with idempotency keys, a verified ledger and a weekly audit. Every change gates behind a 114-case eval suite; 603 tests green on the triage layer, which is barred from touching money by a test rather than a comment.
- **Cut median customer wait to 3.3 staffed hours**, retiring a two-hour human monitoring window for a 24-hour automated cycle plus a two-hourly queue digest that reports itself into team chat. Drove the working inbox from 630 active threads to 120 and cleared the owed queue to zero on repeat cycles.
- **Designed the knowledge layer from scratch** — a 15-category taxonomy over 120 articles with SQLite/FTS5 retrieval (skipping vector RAG as over-engineering at 15k words), and a help center rebuilt on Astro Starlight / Cloudflare Pages and migrated off Intercom: 118 articles, zero dead links, 134 images recovered before their CDN expired.
- **Recovered revenue and closed billing leaks** — evidence on 19 disputes across 10 customers (~$1,070 + €49) with zero failures, 21 submissions in 15 minutes once systematized, plus verified money batches against a live reconciled ledger.
- **Found the silent failures no dashboard was reporting**: only 4 of ~296 support emails were reaching the ticketing system, closed-thread counts read 1 against 212 real, and published reply-time medians ran ~3x optimistic on a wrong staffed-day assumption. Archived 18,065 conversations to S3 ahead of a seat sunset with zero fetch failures.
- **Built the onboarding and customer-education function from nothing** — no documentation existed on arrival. Designed the flow, wrote the material, and produced the tutorial library script-to-edit (HubSpot and Clay integrations, recurring-export walkthroughs, in-app onboarding video). Authored the tone handbook every human and agent reply is written against.
- **Carried the commercial surface alongside it** — demos through to close including GDPR-skeptical enterprise buyers, contract execution (1M-credit deal), discount policy, ~3,000 emails/week outbound — and became engineering's defect channel via a machine-readable triage feed. Held all of it through a Chrome Web Store delisting and 400–500 ticket spikes as the only customer-facing person in the company.

### SaaS Sales Executive — All Funeral Services
**New York, USA · Jan 2025 – Jul 2025** · *DeathTech SaaS | 100+ employees | Avg deal $20K*

- Promoted Lead Gen → Pre-Sales in 1 month, onto Account Management at 5; 80–100 cold calls/day booking 5–8 demos/week, supporting a first close inside 30 days against a typical 6-month cycle.

### Senior Team Lead — Globalfaces Direct
**Toronto, Canada · Mar 2024 – Dec 2024** · *Nonprofit fundraising | 1,200 reps | Avg deal $2K*

- Promoted to Senior Team Lead within 1 month; closed 10+ sales/week from 150+ donor presentations and coached 20+ reps.

### Sales Account Manager — Yutian Printing
**Kaohsiung, Taiwan · Sep 2021 – Feb 2024** · *Commercial printing | 20 employees | Avg deal $7K*

- Owned full-cycle sales and rebuilt the pipeline from 0 to 7,000+ contacts via a loyalty program and omni-channel outreach; rebuilt the CRM and led a 4-person team through COVID.

### Earlier
**Recruitment Consultant**, PERSOLKELLY Taiwan · Sep 2020 – Sep 2021 — full-cycle IT recruitment for Ubiquiti, TP-Link, Amazon Eero.
**Product Demonstrator**, Ajinomoto Food Europe · London · Oct 2018 – Sep 2020 — 25 UK venues; 20% lift in customer satisfaction.

---

## SKILLS

**AI & Agents** — Production LLM agent design, prompt engineering, tool/function calling, MCP servers, golden-set eval harnesses, LLM-as-judge scoring, knowledge-base and retrieval design, Claude, Codex, Cursor
**Support & CX** — Intercom (Fin AI agent, workflows, custom answers, escalation rules), help-center architecture, CSAT and resolution instrumentation, triage and queue design, incident response
**Billing & Revenue Ops** — Stripe (disputes, refunds, invoices, subscriptions, idempotency), chargeback evidence automation, dispute prevention, discount policy, DocuSign
**Cloud & Systems Delivery** — AWS (EC2, S3, Lambda, SES, IAM), Cloudflare Pages, Supabase, n8n, webhooks and REST; AI-assisted build workflow (spec → plan → review gates → merge), Git/GitHub, test suites as release gates, behavioural verification against live systems
**Customer Education & GTM** — Onboarding design, tutorial and walkthrough video production (script → record → edit), tone and voice standards, live demos through to close, HubSpot, LinkedIn Sales Navigator

---

## EDUCATION

**Bachelor of Arts (BA), Arts Management** — University of London, UK · 2020
