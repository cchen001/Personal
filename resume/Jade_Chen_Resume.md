# Jade Chieh Chen

chiehjadechen@gmail.com · +1 437 660 2419 · [linkedin.com/in/jade-chieh-chen](https://www.linkedin.com/in/jade-chieh-chen/)

**AI Support Engineer — Customer Operations → Production AI Systems**
*I take support functions that run on people and rebuild them as systems that run themselves, safely.*

---

## SUMMARY

Support operator turned builder. Over 14 months at a B2B data SaaS I took a manual queue that spiked to 400–500 tickets a day and replaced it with a production AI agent that triages, answers, and executes refunds, credits and cancellations under hard authorization ceilings — specced, evaluated, deployed to AWS, and audited weekly by me. Eight years of client-facing sales and CX sit underneath the engineering, which is why the agent's answers sound like a person and its money guardrails were written by someone who has personally had to refund an angry customer.

---

## EXPERIENCE

### AI Support Engineer — Evaboot
**Remote · Jul 2025 – Present**
*B2B SaaS (LinkedIn Sales Navigator data extraction) | ~6-person team | Sole owner of the support function | SMB to Enterprise*

- **Built and shipped the company's production AI support agent end to end** — knowledge base, retrieval, eval harness, AWS deployment, live audit. New users now route to it by default, and it executes refunds, credits, cancellations and invoice voids autonomously under typed authorization ceilings (refund ≤ $29, credit ≤ 200), with idempotency keys, a verified action ledger and a weekly audit against what each customer actually asked for.
- **Cut median customer wait to 3.3 staffed hours** by retiring a two-hour human monitoring window for a 24-hour automated cycle plus a two-hourly queue digest that reports itself into team chat — the first support signal that reaches a person without anyone fetching it. Drove a dogfood inbox from 630 active threads to 120 and cleared the owed queue to zero on repeat cycles.
- **Designed the agent's entire knowledge layer from scratch**: a 15-category taxonomy over 120 articles, SQLite + FTS5 retrieval (deliberately skipping vector RAG as over-engineering at 15k words), and a rebuilt help center on Astro Starlight / Cloudflare Pages migrated off Intercom — 118 articles, 53 public, zero dead links, after recovering 134 images before their CDN links expired.
- **Gated every agent change behind a golden eval**: a 114-case regression suite scored by 50 draft and 50 judge subagents through a deterministic scorer (hard rules 100%, soft 90%); 603 tests green on the triage layer, which is barred from touching money by a test rather than a comment.
- **Recovered revenue and closed billing leaks hands-on**: built and submitted evidence on 19 disputes across 10 customers (~$1,070 + €49) with zero failures — 21 submissions in 15 minutes once the process was systematized — and executed verified money batches (8 refunds / $293.97; a later run of $425 + €9 refunded and $99 collected) against a live reconciled ledger.
- **Found the silent failures no dashboard was reporting**: only 4 of ~296 support emails were reaching the ticketing system (a 30-day blind spot), closed-thread counts read 1 against 212 real, and published reply-time medians ran ~3x optimistic on a wrong staffed-day assumption. Archived 18,065 conversations and ~5,300 attachments to S3 ahead of a seat sunset with zero fetch failures.
- **Ran the function solo through every incident** — Chrome Web Store delisting, recurring export failures, 400–500 ticket spikes — while carrying live demos, contract execution (including a 1M-credit deal via DocuSign), discount policy, and outbound campaigns at ~3,000 emails/week.

### SaaS Sales Executive — All Funeral Services
**New York, USA · Jan 2025 – Jul 2025**
*DeathTech SaaS | 100+ employees | SMB to Mid-Market | Avg deal $20K USD*

- Promoted from Lead Generation to Pre-Sales in 1 month and onto the Account Management team at 5 months, on initiative and speed through the funnel.
- Made 80–100 cold calls/day, booking 5–8 demos/week; supported a first closed deal inside 30 days against a typical 6-month cycle.

### Senior Team Lead — Globalfaces Direct
**Toronto, Canada · Mar 2024 – Dec 2024**
*Nonprofit fundraising | 1,200 reps | B2C & SMB | Avg deal $2K USD*

- Promoted to Senior Team Lead within 1 month; led a door-to-door nonprofit fundraising team.
- Closed 10+ sales/week from 150+ donor presentations; trained and coached 20+ reps, lifting close rates and team consistency.

### Sales Account Manager — Yutian Printing
**Kaohsiung, Taiwan · Sep 2021 – Feb 2024**
*Commercial printing | 20 employees | B2C & SMB | Avg deal $7K USD*

- Owned full-cycle sales and rebuilt the pipeline from 0 to 7,000+ contacts through a loyalty program and omni-channel outreach.
- Rebuilt the CRM, scoped pricing, led a 4-person team, and launched market strategies that held through COVID; analyzed campaign ROI to find and fix revenue inefficiencies.

### Earlier
**Recruitment Consultant**, PERSOLKELLY Taiwan · Taipei · Sep 2020 – Sep 2021 — full-cycle IT recruitment for enterprise clients (Ubiquiti, TP-Link, Amazon Eero); 50+ cold calls/day.
**Product Demonstrator**, Ajinomoto Food Europe · London · Oct 2018 – Sep 2020 — 25 UK venues; drove a 20% lift in customer satisfaction and trained new hires.

---

## TECHNICAL SKILLS

**AI & Agents** — Production LLM agent design, prompt engineering, tool/function calling, MCP servers, golden-set evaluation harnesses, LLM-as-judge scoring, prompt caching, knowledge-base and retrieval design, Claude, Codex, Cursor
**Support & CX Platforms** — Intercom (Fin AI agent, workflows, custom answers, data connectors, escalation rules), help-center architecture, CSAT and resolution instrumentation, triage and queue design
**Billing & Revenue Ops** — Stripe (disputes, refunds, invoices, subscriptions, idempotency), chargeback evidence automation, dispute-prevention policy, DocuSign contracts, discount policy design
**Cloud & Infrastructure** — AWS (EC2, S3, Lambda, SES, IAM, Secrets Manager), Cloudflare Pages, Supabase, Astro Starlight, Bubble, n8n, webhooks and REST integrations
**Engineering** — Python, SQL, SQLite/FTS5, React, Git/GitHub (spec → plan → review → merge), pytest, automated code review gates, security review
**Go-to-Market** — Live product demos, cold outreach at scale, HubSpot, LinkedIn Sales Navigator, GDPR-sensitive enterprise conversations

---

## EDUCATION

**Bachelor of Arts (BA), Arts Management** — University of London, London, UK · 2020

---

## AWARDS

"Explaining Technology to Boomers" Award, 2025
