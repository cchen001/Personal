# Jade Chieh Chen

chiehjadechen@gmail.com · +1 437 660 2419 · [linkedin.com/in/jade-chieh-chen](https://www.linkedin.com/in/jade-chieh-chen/)

**AI Support Operations & Conversational Design**
*Designed the conversation, shipped the agent, built the evaluation that proves it works — and still work the queue every morning.*

---

## SUMMARY

Fourteen months as the sole customer-facing hire at a B2B SaaS, where I designed the conversation architecture for Intercom Fin across three successive roles, then built and shipped the production AI agent that now carries most of the queue — knowledge base, evaluation harness, escalation logic, and autonomous refunds and credits under hard authorization ceilings. I also built the resolution-tracking layer that measures whether the agent actually resolved anything, and authored the tone system every human and agent reply is written against. Eight years of client-facing work underneath, across the UK, Taiwan, Canada and a France-based team.

---

## EXPERIENCE

### Founding Support Lead — Evaboot
**Jul 2025 – Present**
*Remote (UTC+8) · B2B SaaS, LinkedIn Sales Navigator data extraction | ~6-person team | Sole customer-facing hire | SMB to Enterprise*

- Designed and shipped the production AI support agent end to end — conversation architecture, knowledge base, retrieval, evaluation harness, AWS deployment, live audit. New users route to it by default. It executes refunds, credits, cancellations and invoice voids autonomously under typed ceilings (refund ≤ $29 as a launch canary, credit ≤ 200), with idempotency keys, a verified ledger and a weekly audit against what each customer actually asked for.
- Designed the conversation architecture and the tone system behind it — broke onboarding into three triggered nodes plus a pricing node, each with a defined entry condition and purpose, after scrapping a first design when the highly interactive model proved wrong for the platform. Configured Fin across three successive roles (support, onboarding, customer success), and authored a tone handbook of explicit rulings — reply visibility, capacity state, apology dating, professional register — not style preferences. Rejected an external support-writing toolkit that taught the robotic voice we ban, then traced our own bad tone to one upstream instruction and deleted it.
- Built the evaluation loop and the resolution tracking that prove a change helped — a 114-case golden suite scored by 50 draft and 50 judge subagents through a deterministic scorer (hard rules 100%, soft 90%), a fifteen-persona DeepEval run against a live agent constitution, and a data pool categorising every conversation as confirmed, assumed or abandoned mid-conversation, fed live by auto-close and CSAT hooks with a daily backfill sweep. 603 tests green on the triage layer, which is barred from touching money by a test rather than a comment.
- Tuned escalation logic, fallbacks and guardrails ahead of a 24-hour automated cycle — audited every escalation rule for effectiveness and disabled the majority; rewrote the human-handoff fallback with expectation-setting language. Median customer wait now 3.3 staffed hours, after finding published medians had been running ~3x optimistic on a wrong staffed-day assumption. Working inbox down from 630 active threads to 120, and the owed queue cleared to zero on repeat cycles.
- Built the knowledge layer and the enablement that keeps customers independent — a 15-category taxonomy over 120 articles with SQLite/FTS5 retrieval, maintained as the agent's live source; a help center rebuilt on Astro Starlight / Cloudflare Pages and migrated off Intercom (118 articles, zero dead links); and a tutorial library scripted, recorded and edited in-house covering HubSpot and Clay integrations, recurring exports and in-app onboarding.
- Built the integrations and automation the agent runs on — n8n workflows and Zapier automations, two real-time webhook listeners, an LLM chain returning structured JSON, a bearer-token JSON API client, and a documented MCP server whose live tool count I settled at 37 against two wrong internal figures — surfacing 20 undocumented tools that write to customers' own accounts.
- Owned payments operations and the commercial surface alone — Stripe disputes, chargebacks, refunds and subscriptions — evidence on 19 disputes across 10 customers (~$1,070 + €49) with zero failures, 21 submissions in 15 minutes once systematized. Wrote the deletion and erasure policy, handled GDPR and PII boundaries, and confirmed every finding of an external security review plus one more. Ran demos through to close including GDPR-skeptical enterprise buyers, contract execution, and discount policy design — through a Chrome Web Store delisting and 400–500 ticket spikes, as the only customer-facing person in the company.

### SaaS Sales Executive — All Funeral Services
**Jan 2025 – Jul 2025**
*New York, USA · DeathTech SaaS | 100+ employees | Avg deal $20K*

- Promoted Lead Gen → Pre-Sales in 1 month and onto Account Management at 5, on initiative and speed through the funnel.
- Ran discovery and product demos for SMB and mid-market buyers at 80–100 cold calls/day, booking 5–8 demos/week; supported a first close inside 30 days against a typical 6-month cycle.

### Senior Team Lead — Globalfaces Direct
**Mar 2024 – Dec 2024**
*Toronto, Canada · Nonprofit fundraising | 1,200 reps*

- Promoted to Senior Team Lead within 1 month; led a door-to-door nonprofit fundraising team.
- Closed 10+ sales/week from 150+ donor presentations; trained and coached 20+ reps on script, objection handling and delivery consistency.

### Sales Account Manager — Yutian Printing
**Sep 2021 – Feb 2024**
*Kaohsiung, Taiwan · Commercial printing | 20 employees | B2C & SMB | Avg deal $7K*

- Owned full-cycle sales and rebuilt the pipeline from 0 to 7,000+ contacts through a loyalty programme and omni-channel outreach.
- Rebuilt the CRM, scoped pricing, led a 4-person team, and launched market strategies that held through COVID; analysed campaign ROI to find and fix revenue inefficiencies.

### Earlier
**2018 – 2021**

**Recruitment Consultant**, PERSOLKELLY Taiwan · Taipei · Sep 2020 – Sep 2021 — full-cycle IT recruitment for enterprise clients (Ubiquiti, TP-Link, Amazon Eero); sourced via LinkedIn Recruiter at 50+ cold calls/day.
**Product Demonstrator**, Ajinomoto Food Europe · London, UK · Oct 2018 – Sep 2020 — 25 UK venues; drove a 20% lift in customer satisfaction and trained new hires on client-facing delivery.

---

## SKILLS

**AI Support Operations** — Intercom Fin configuration (workflows, custom answers, data connectors, escalation rules, guardrails), resolution-rate and CSAT instrumentation, triage and queue design, ticket-level root cause analysis, incident response
**Conversational Design** — Conversation architecture and node design, virtual agent scoping, tone and voice systems, fallback and escalation design, persona definition, agent constitutions, prompt engineering
**Evaluation & QA** — Golden-set evaluation harnesses, LLM-as-judge scoring, DeepEval persona runs, resolution-state tracking, staged rollouts, dry-run verification, post-launch optimisation
**Automation & Integration** — n8n, Zapier, webhooks, REST APIs, structured JSON pipelines, Model Context Protocol (MCP), tool/function calling, knowledge-base and retrieval design, Claude, Codex, Cursor
**Payments & Regulated Ops** — Stripe (disputes, chargebacks, refunds, invoices, subscriptions, idempotency), dispute prevention, GDPR erasure and PII handling, security review, audit ledgers
**Delivery & Enablement** — End-to-end ownership (discovery → requirements → design → build → QA → launch), enablement programme design, tutorial and walkthrough video production (script → record → edit), help-center architecture, live demos, stakeholder management
**Cloud & Tooling** — AWS (EC2, S3, Lambda, SES, IAM, Secrets Manager), Cloudflare Pages, Supabase, Bubble, Astro, Notion, Git/GitHub, AI-assisted build workflow (spec → plan → review gates → merge)

---

## EDUCATION

**Bachelor of Arts (BA), Arts Management** — University of London, London, UK · 2020

---

## AWARDS

"Explaining Technology to Boomers" Award, 2025
