# Handoff — verify two resume claims against live systems

**For:** a local session with access to Jade's machine, Intercom (billing history), AWS, and the Evaboot support repo.
**From:** a cloud session with no machine access. Everything below is derived from 422 days of Jade's work journals (Jul 2025 – Sep 2026).
**Goal:** turn two estimated numbers on her resume into measured ones, or correct them.

---

## Why this matters

Jade's resume is being rewritten for AI-support / CX-operations roles. Every claim on it traces to a dated journal entry **except two**, which are her own estimates:

| Claim (as currently written) | Status |
|---|---|
| "saved ~$100K a year in tooling" | Unverified. Not in the journals. |
| "resolves ~85% of conversations without a human" | Unverified as a figure, but ~83% is derivable (see §3). |

Both appear in the resume's subheadline — the first thing a reader sees. Both are the kind of number an interviewer at a support-tooling company will drill into. If either is wrong, it undermines an otherwise fully-sourced document.

**Target outcome:** replace each estimate with a measured figure, a window, and a stated definition. Or, if the data does not support it, rewrite the claim.

---

## Ground rules for this session

Jade is job-searching **without her employer's knowledge**, and she personally wrote Evaboot's deletion and erasure policy.

1. **Aggregates only.** Counts, sums, rates, dates. Never export or paste conversation bodies, customer names, emails, or any PII.
2. **Read-only.** No writes to any production system. No changes to Stripe, DynamoDB, Intercom, or the support repo's live config.
3. **Billing data is fine.** Invoices and subscription records are company financial data she has legitimate access to as the person who ran the tooling. That is a different category from customer conversation data.
4. **Do not touch anything that would notify a teammate** — no shared-doc edits, no Slack posts, no new dashboards.
5. Record findings in a local scratch file, not in the `Personal` repo, until Jade decides what to keep.

---

## 1. The $100K saving — Intercom cost vs. AWS cost

The claim is a **net annual saving**. It needs both halves:

```
annual saving  =  what Intercom+Fin cost per year
                −  what the replacement costs per year (AWS + Cloudflare + any tooling)
```

### 1a. What Intercom cost

In Intercom: **Settings → Subscription** (or Billing). Pull:

- [ ] Plan tier and the contracted seat price
- [ ] Number of paid seats at peak (before the sunset)
- [ ] **Fin resolution charges** — billed per resolution, often the largest line. Get the monthly figure across several months, not one.
- [ ] Any add-ons. Jade assessed a "Pro add-on (Monitors + Insights)" at **$99+/month** on 25 Mar 2026 — check whether it was ever purchased.
- [ ] Annual vs monthly billing, and whether there was a discount
- [ ] **Download the last 12 months of invoices** — this is the defensible artifact

Best source: the invoices themselves. A contract or renewal quote is even better if she can find one in email.

### 1b. What the replacement costs

AWS Cost Explorer, filtered to the support-platform account/region (journals say **eu-central-1**, and note "dogfood is the same AWS account as production"):

- [ ] Monthly cost since the 31 Jul 2026 cutover, broken out by service (Lambda, DynamoDB, API Gateway, S3, SES, Cognito, EC2)
- [ ] Cloudflare Pages cost (likely $0 or near it)
- [ ] Anthropic/LLM API spend for the agent — **do not forget this one**; it is the replacement's real variable cost and omitting it inflates the saving
- [ ] Any other paid tooling that replaced an Intercom function

### 1c. Do the arithmetic

Report: `Intercom annual − replacement annual = net saving`. If it lands near $100K, the claim stands with a citation. If it lands at $60K or $140K, **use the real number** — a specific odd figure is more credible than a round one.

---

## 2. The 85% automation rate — her own system

**Do not use Intercom for this.** Intercom was retired on 31 Jul 2026; it holds the *before* picture. The claim describes the platform Jade built.

The right instrument already exists and she built it: the **resolution data pool**, merged 17–18 Jul 2026. From the journals:

> "Merged the resolution-tracking feature to main, landing all four categorization rules (confirmed, assumed, abandoned mid-conversation, and conversation length) with its table, hooks, daily sweep, and IAM wiring in place." — 17 Jul 2026

> "The close and CSAT hooks give the pool live confirmed-versus-abandoned signal, and the daily sweep backfills the rest." — 17 Jul 2026

Related names seen in the journals (confirm actual identifiers in the repo): `resolution_sweep`, the auto-close path, CSAT capture, the queue watcher service that "re-reads the actual messages every pass instead of trusting stored status flags" (14 Aug 2026).

### Steps

- [ ] Locate the resolution pool table and its schema in the support repo
- [ ] Confirm what each category means in code — `confirmed`, `assumed`, `abandoned mid-conversation`
- [ ] Find whether human-reply presence is stored directly, or must be derived from message rows

### Pick ONE definition and state it

Automation rate can mean at least three different things, giving three different numbers:

1. **Conversations where no human ever replied** ← recommended; closest to how buyers read it
2. Conversations resolved without escalation to a human
3. Conversations where the AI sent the final message

Compute **definition 1** as the headline. Compute the others if cheap, so Jade knows the spread and cannot be surprised.

### Window

Use a clean window **after 31 Aug 2026**. Reasons from the journals:

- The cutover landed 31 Jul and **contaminated the reporting window**: "imported threads carry their original timestamps and the raw numbers are contaminated" (3 Aug 2026)
- Auto-close was **disabled** from 3 Aug after a false-closure incident affecting 109 threads, and was still off on 14 Sep — so `closed` status alone is not a reliable resolution signal in Aug
- A migration backlog was still being merged across rails on 11 Aug

**Suggested:** the 30 days ending on the most recent complete day. Report the exact window.

### Also worth pulling while in there

- [ ] Total conversation volume in the window (validates the "~70 tickets/day" figure from 27 Jul 2026)
- [ ] The **before** baseline, if obtainable — Fin's resolution rate from Intercom's reporting pre-cutover. A "from X% to Y%" claim is far stronger than "85%"
- [ ] Median reply time, to confirm the **3.3 staffed hours / 6.1 wall** figure from 14 Sep 2026 still holds

---

## 3. What the journals already support (so you know what you are checking against)

Derivation currently backing the 85%:

- 27 Jul 2026: "A 24-hour batch is roughly 70 tickets while a two-hour sweep is five or six."
- 14 Sep 2026: "twelve owed down to one"
- 17 Aug 2026: "the queue came down from eighteen owed to nine"
- 10 Aug 2026: "55 open narrowed to 25 real customers"

≈12 owed against ≈70/day ⇒ **~83% never reach a person.** Different windows, so it is corroboration, not proof.

Context: a **95% target** was set 11 Feb 2026 ("We are pushing for 95% support automation"), with the push at the **70% mark** on 18 Feb 2026.

Caution flag from 4 Sep 2026: *"A third of the owed queue was not support mail at all. The filter that drops automated senders matches a fixed list of addresses."* — If that filter is still naive, the owed count is **overstated**, which means the true automation rate may be **higher** than 85%. Worth checking; it would be a pleasant surprise rather than a problem.

---

## 4. What to bring back

A short plain-text block, numbers only:

```
INTERCOM COST
  plan / seats / seat price:
  Fin resolution charges (monthly, several months):
  add-ons:
  ANNUAL TOTAL:

REPLACEMENT COST
  AWS monthly (by service):
  LLM API monthly:
  other tooling:
  ANNUAL TOTAL:

NET ANNUAL SAVING:

AUTOMATION RATE
  window (exact dates):
  definition used:
  total conversations:
  no human reply:
  RATE:
  (other definitions, if computed:)

BEFORE BASELINE (Fin resolution rate pre-cutover, if available):

REPLY TIME
  median staffed / wall, last 30 days:
```

No customer data. No conversation text.

---

## 5. What changes on the resume depending on results

Current wording, in `resume/Jade_Chen_Resume.html` (and the `.md` twin):

> **Subheadline:** "...retired Intercom and Fin, resolves ~85% of conversations without a human, and saved ~$100K a year in tooling."

> **Bullet 1:** "Designed and shipped the support platform that replaced Intercom and Fin — ~$100K/year saved in tooling."

> **Bullet 5:** "Took the agent to ~85% of conversations resolved without a human — up from a manual queue, against a 95% target set at the start of the push."

**If the numbers hold:** swap the tildes for the measured figures and add the window. `"84.6% of conversations resolved with no human reply (30 days to 14 Sep 2026)"` is far stronger than `"~85%"`.

**If the saving is materially lower:** use the true figure. Even $40K is a strong claim for a six-person company, and it is defensible. Do not keep a number that cannot survive a follow-up question.

**If the automation rate cannot be computed cleanly:** fall back to the figures that *are* sourced — median wait 3.3 staffed hours, inbox 630 → 120 threads, owed queue repeatedly cleared to zero — and drop the percentage rather than guess.

**If a "before" baseline exists:** rewrite as a delta. "From X% under Fin to Y% on the platform I built" is the single strongest sentence available here, and it maps directly onto how the target roles are measured. (One target role, Reap's AI Operations Engineer, is hiring specifically to move an Independently Resolved Rate from 39% to 80%.)

---

## 6. Afterwards

Report the numbers back to Jade. Supporting context, including every other claim on the resume with its journal date, is in `resume/EVIDENCE.md` on the branch `claude/resume-optimization-qd82rw`.

Do not edit the resume files in that session unless Jade asks — the cloud session holds the current drafts and the two tailored variants in `resume/tailored/`.
