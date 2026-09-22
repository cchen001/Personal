# Resume Audit & Strategy — Jade Chieh Chen

Source material: `CV-June.pdf` (June 2025) and 422 days of daily journals, 28 Jul 2025 – 14 Sep 2026 (271 with entries).

---

## 0. The thing you need to hear first

Your June 2025 CV is a **sales resume**. The last 14 months of your life are **not sales work**. You have been building production AI systems, and the CV does not contain a single word of it.

That gap is the entire problem. Everything below is downstream of it.

Second, smaller problem: your CV has a `SKILLS` heading with **nothing under it**. It shipped empty. That is the single cheapest fix on this list and it has been costing you keyword matches for over a year.

Third: you sent me ten prompts with `[Job Title]`, `[Industry]` and `[paste job description]` still in them. Prompts 3 and 7 — the ATS and work-history-realignment ones — cannot be answered without a real posting. I have built you a reusable keyword bank instead (§3). Paste a real JD and I'll do the targeted pass properly.

---

## 1. Professional summary — rewritten

**What you had:**

> Winner of the 2025 "Explaining Technology to Boomers" Award. A SaaS AE who turns product demos into stories, builds instant rapport, and closes with empathy and clarity.

**Why it fails now.** It opens with a joke award, claims a title you no longer occupy, and every noun in it is soft — stories, rapport, empathy, clarity. Nothing falsifiable. A hiring manager for a technical role reads it and stops. Worse: it is *accurate about a person who no longer exists*. You spent the last year shipping eval harnesses and AWS deploys.

**What it is now:**

> Support operator turned builder. Over 14 months at a B2B data SaaS I took a manual queue that spiked to 400–500 tickets a day and replaced it with a production AI agent that triages, answers, and executes refunds, credits and cancellations under hard authorization ceilings — specced, evaluated, deployed to AWS, and audited weekly by me. Eight years of client-facing sales and CX sit underneath the engineering, which is why the agent's answers sound like a person and its money guardrails were written by someone who has personally had to refund an angry customer.

Every clause is checkable. The last sentence does the transition work: it stops your sales past being a liability and makes it the reason you are better at this than a pure engineer.

**Keep the Boomers award** — but at the bottom, in an Awards line. It is genuinely charming and it is a good interview hook. It is a terrible opening sentence.

---

## 2. Bullet points — responsibilities → measurable accomplishments

The Evaboot bullets in the resume are built from journal evidence, dated in `EVIDENCE.md` so you can defend each one.

The pattern I applied, for when you write your own:

| Weak shape | Strong shape |
|---|---|
| "Handled support tickets" | "Cut median wait to 3.3 staffed hours across ~18k conversations" |
| "Worked on AI automation" | "Gated every agent change behind a 114-case eval suite; hard rules 100%, soft 90%" |
| "Managed billing issues" | "19 disputes across 10 customers (~$1,070 + €49), zero failures" |
| "Improved documentation" | "118 articles, 53 public, zero dead links, migrated off Intercom" |

**Three specific rewrites from your old bullets:**

- ~~"Owned full-cycle sales: generated leads, rebuilt CRM, scoped pricing, hosted client meetings, closed deals, ensured QA, and managed accounts"~~ — this is a job description, not an achievement, and it is seven verbs in one breath. Split: the pipeline number (0 → 7,000+ contacts) is the accomplishment. The verb list is context.
- ~~"Trained and coached 20+ reps, improving close rates and team consistency"~~ — "improving" with no number is a claim you are declining to make. Either find the number or cut the clause. I left it because the 20+ carries it, but it is the weakest surviving line on the page.
- ~~"Delivered product demos and high-touch service, driving a 20% boost in customer satisfaction scores"~~ — fine bullet, wrong real estate. It is from 2018. Compressed into a one-line "Earlier" block.

---

## 3. ATS + human readability (no JD supplied — here is the bank)

**How ATS actually works:** most systems score literal string overlap between your resume and the posting. They do not infer that "built an eval harness" means "LLM evaluation." So mirror the posting's exact nouns, in your own true sentences. Never keyword-stuff a block — modern parsers and every human will catch it.

**Your keyword bank, by target.** Pull only the ones the posting actually uses:

*AI / Agent engineering:* LLM, large language model, AI agent, agentic workflow, prompt engineering, tool calling / function calling, RAG, retrieval, knowledge base, evaluation, evals, golden set, LLM-as-judge, guardrails, hallucination mitigation, MCP, Claude, OpenAI, fine-tuning, prompt caching, observability

*Support / CX ops:* customer support, technical support, Tier 2, escalation management, ticket deflection, first response time, resolution rate, CSAT, SLA, macros, help center, knowledge management, Intercom, Zendesk, self-serve, queue management, incident response

*Billing / revenue ops:* Stripe, chargebacks, dispute resolution, refunds, subscription lifecycle, churn, retention, invoicing, revenue recovery, reconciliation, idempotency

*Engineering:* Python, SQL, REST API, webhooks, AWS, EC2, S3, Lambda, SES, IAM, CI/CD, Git, code review, test coverage, pytest, SQLite, React, Cloudflare

**ATS formatting rules your file already follows:** single column, no tables in the body, no text inside images or headers/footers, standard section names (`SUMMARY`, `EXPERIENCE`, `TECHNICAL SKILLS`, `EDUCATION`), dates as `Mon YYYY – Mon YYYY`, `.docx` or text-layer `.pdf` only.

**On your PDF export — a correction.** My first read of your June PDF came back as garbage and I assumed the export was broken. It isn't. Your file embeds proper ToUnicode maps and extracts cleanly once parsed correctly; the fault was my decoder, not your file. Chromium print-to-PDF is fine and I used the same path for the new one (verified: 2 pages, clean text layer, correct em-dashes and accented characters).

The real export rules still worth following: keep it a text-layer PDF, never a scan or image export; send `.docx` instead when a portal explicitly asks for Word; and check the extracted text after any template change rather than trusting that it looks right on screen.

---

## 4. Career transition: Sales → AI / Support Engineering

This is the real story of your resume, so be deliberate about it.

**The honest risk:** you have no CS degree, no prior SWE title, and a resume that until now said "cold calls per day." A skeptical reviewer will assume you configured some no-code tools. You must pre-empt that in the first six seconds.

**Your transferable case, strongest to weakest:**

1. **You shipped to production and owned the consequences.** Not a course project, not a prototype. A live agent moving real money in a real customer's account, with a ledger and a weekly audit you personally run. Very few career-changers have this. Lead with it.
2. **You have the judgment that engineers usually lack here.** You chose *not* to use vector RAG because at 15k words it was over-engineering. You barred the triage layer from touching money with a test rather than a comment. You set a refund ceiling of $29 as a launch canary. That is engineering judgment, and the journals show you reasoning to it, not copying it.
3. **You found failures the instrumentation was hiding.** 4 of 296 emails arriving. Closed-thread count reading 1 against 212. Medians 3x optimistic. This is the single most underrated thing on your resume — it says you don't trust your own dashboard, which is exactly what people hire senior operators for.
4. **The sales background is the moat, not the baggage.** You know what an angry customer sounds like at hour 48. That is why your agent's tone handbook exists. Say this out loud in interviews.

**What to stop saying:** "I'm transitioning into tech" / "even without direct experience." You *have* direct experience — 14 months of it, in production. Framing yourself as a beginner invites them to price you as one. Drop the apology.

---

## 5. Full audit — vague, wordy, or low-impact

**Vague:**
- `SKILLS` heading with no content. Fixed.
- "improving team performance and engagement by 30%" (Ajinomoto) — 30% of *what*, measured how? This is the least defensible number on your old CV. I compressed it out. If pressed in an interview, do not bluff it.
- "consistently outperformed industry benchmarks" (Yutian) — which benchmark, by how much? Kept but it is filler; replace it the moment you recall a real figure.
- "launched market strategies that succeeded despite COVID" — "succeeded" is doing enormous unpaid work here.

**Wordy:**
- The Yutian seven-verb bullet. Split.
- Company context lines (`Industry | Headcount | Client type | Avg deal`) — actually a *good* device, unusual and genuinely informative. Kept and extended to Evaboot. This is the best structural idea on your original CV.

**Not showing enough impact:**
- Your original CV measured **activity** (calls/day, demos/week) rather than **outcomes** (revenue, retention, resolution). Activity metrics read as junior. You had one real outcome metric — 0 → 7,000+ contacts — and buried it third.
- Nothing in the original showed leadership over *systems*, only over people. Evaboot fixes this.

**Tone:** your original was warm and slightly performative ("turns product demos into stories"). Your journals are the opposite — precise, self-correcting, unsentimental, quick to name your own error. **Your journal voice is better than your resume voice.** I wrote the new document closer to the journals.

**Leadership, results, innovation — where each now lives:**
- *Leadership:* sole owner of a function at a 6-person company; ran incidents solo; escalated across three engineers; corrected a founder-facing weekly report that was wrong.
- *Results:* wait times, dispute recovery, queue depth, test counts, article counts.
- *Innovation:* skipping RAG on purpose, test-enforced money boundaries, the self-reporting queue digest.

---

## 6. Format and layout

**Structure, in scan order:**

1. Name + contact (one line, no icons — icons break ATS parsing)
2. Headline + one-line subheadline
3. Summary — 3 lines maximum
4. Experience — reverse chronological, Evaboot taking ~45% of page one
5. Technical Skills — grouped by category, not one flat comma soup
6. Education, Awards — bottom, one line each

**De-emphasis mechanics for older roles:** PERSOLKELLY and Ajinomoto are now a compressed "Earlier" block — one line each, no bullets. They prove continuity and nothing more. Yutian keeps 2 bullets because the 0 → 7,000 pipeline number still earns its place.

**The 10-second test.** A recruiter's eye lands on: your name → your headline → the first bold phrase of your first bullet. Make sure those three read as one sentence. Yours currently do: *Jade Chen → AI Support Engineer → Built and shipped the company's production AI support agent end to end.*

**Length:** two pages is correct for you now. Do not compress to one — you would have to cut the Evaboot evidence, which is the only reason anyone will call.

**Formatting specifics:** 10–11pt body, one accent color maximum, bold only on the lead phrase of each bullet (never whole bullets — if everything is bold, nothing is), 0.5–0.75" margins.

---

## 7. Restructuring work history against a target JD

Needs the actual posting. Method for when you have it:

1. Paste the JD. Highlight every **noun** in the requirements — those are the ATS tokens.
2. Sort them into: *have it and it's on the resume* / *have it and it's missing* / *don't have it*.
3. For column 2, find the journal entry that proves it and write the bullet from the evidence.
4. For column 3, do not fabricate. Decide whether the gap is disqualifying or whether an adjacent bullet covers it.
5. Reorder bullets **within** each role so the top bullet maps to the JD's top requirement. Never reorder the roles themselves.
6. Mirror their vocabulary: if they say "deflection rate" and you wrote "resolution rate," use theirs where it is honestly the same thing.

---

## 8. Technical skills section

Your old one was **empty**. The new one is grouped into six categories because a flat list of 40 tools reads as noise and hides your strongest signal.

Two deliberate choices:
- **"Production LLM agent design" leads the AI group** — it is the rarest thing you have and it should be the first technical phrase anyone reads.
- **Go-to-Market is kept last, not deleted.** It is your differentiator for AI-support, CX and solutions roles. Delete it only for a pure backend engineering application.

**Do not add:** anything you touched once. If you cannot answer a follow-up question about it, it costs you more than it earns.

---

## 9. Headline and subheadline

**Shipping version:**

> **AI Support Engineer — Customer Operations → Production AI Systems**
> *I take support functions that run on people and rebuild them as systems that run themselves, safely.*

The arrow does the narrative work in three words. "Safely" is deliberate — it signals you understand the actual hard part of agents in production, which is the part most candidates have never had to think about.

**Alternates by target:**
- *Head of Support / CX:* "Support Operations Lead — Solo-Owned Functions, Automated" / *Built the support function for a 6-person SaaS, then automated most of it away.*
- *Solutions Engineer:* "Solutions Engineer — Sells It, Then Builds It" / *Eight years closing technical deals; fourteen months shipping the systems behind them.*

---

## 10. Hiring-manager read

Reading this as someone hiring an AI/support engineer at a 20–80 person SaaS:

**What makes me call you.**
Production experience with agents that take real actions on real money. Most applicants have a chatbot demo. You have authorization ceilings, an idempotent ledger and a weekly audit. The eval suite tells me you understand that the hard part is *knowing whether it still works*, which is where most agent projects die. And you found three instrumentation failures that were lying to your own team — that is a senior instinct.

**What makes me hesitate, and what to do about it.**

1. *"Is this real engineering or heavy AI-assisted tooling?"* — You worked with Claude, Codex and Cursor throughout. Some reviewers will discount that. **Do not hide it; reframe it.** You ran spec → plan → review → merge with review gates at each stage and caught real defects in review (a regex bug in an outcome parser, a fail-closed contract that broke on a null, a silent-drop bug that passed all 531 tests). Being effective with AI tooling is a hiring criterion in 2026, not a disqualifier. Own the workflow out loud.
2. *"Six-person company — did anyone check the work?"* — Answer with Robin's security review, the external code-review rounds, and the fact that you confirmed every one of his findings and found one more.
3. *"Four jobs in four countries since 2018."* — Real pattern, visible immediately. Pre-empt it in the cover letter with one honest sentence; do not let them theorize.
4. *No CS credential.* — Non-negotiable at some companies. Filter those out rather than trying to overcome it on paper. Your portfolio argument is stronger than any certificate you could add now.

**What to add that isn't there yet.**
A **public artifact**. The single highest-leverage thing you could do this month: a short write-up of the agent's authorization model — the $29 canary, the typed `apply_action` tool, why the triage layer is test-barred from money. Sanitized, no customer data, no employer internals beyond what is yours. One page. It converts "she says she did this" into "I have read her thinking." With your background, that link in your resume header is worth more than any bullet on the page.

**What to cut.** The Boomers award from the summary (keep at bottom). The unverifiable 30% from 2018. "Consistently outperformed industry benchmarks."

---

## Open items — your calls, not mine

1. **Job title at Evaboot.** The journals never state an official one; I used *AI Support Engineer* because it describes the work. **Check what Evaboot would confirm in a reference call.** If they would only verify "Customer Support Specialist," use that title and let the bullets do the work — an under-titled resume with these bullets reads as *more* credible, not less. Never put a title on paper that a reference will contradict.
2. **All Funeral Services end date.** Your old CV said "Jan 2025 – Present"; Evaboot starts Jul 2025 and you confirmed no overlap. I wrote **Jan 2025 – Jul 2025**. Correct it if that's wrong.
3. **Location line.** Your old CV had none, and I did not invent one. Your number is Toronto (+1 437) but the journals put you on an Asia-Pacific schedule. Add a location or "Remote (UTC+8)" — recruiters filter on it and its absence is read as evasion.
4. **Target confirmation.** This document is built for AI/Support Automation Engineering. Say the word and I'll produce the Head-of-Support or Solutions-Engineer cut instead — it's a re-weighting, not a rewrite.
