# Evidence Base — Evaboot claims, with journal dates

Every number on the Evaboot section of the resume, traced to the journal entry it came from. Use this to prepare for interviews. If a claim is challenged, you have the date.

Source: `Journaling_Jade_Chen_-_daily_jade_chen.csv`, 28 Jul 2025 – 14 Sep 2026.

---

## Bullet 1 — Production AI agent, end to end

| Claim | Date | Journal evidence |
|---|---|---|
| Agent is live, new users route to it | mid-2026 | "*Full AI Deployment*: Continue monitoring the live agent now that new users route to it — conversation volume, reply behaviour, and answer quality" |
| Authorization ceilings | 5 Jun 2026 | "auto-action policy (refund ≤ $29 as a launch canary, void open invoices ≥ 1 week, credit ≤ 200) executed through a typed `apply_action` tool that closes the raw bash-Stripe hole" |
| Idempotency + ledger | 10 Aug 2026 | "3 immediate cancellations, 8 refunds totaling $293.97, and 1 invoice void; 12 ledger rows, all verified by fresh reads, with idempotency keys and a collision guard" |
| Weekly action audit | recurring | "*Autonomous Actions Audit*: Review the live week's agent actions against what each customer actually asked for, and confirm the safety ceilings hold." |
| Missing executor found & shipped | 4 Sep 2026 | "The live agent had been built without the part that carries out credits and refunds… Shipped it into both the running image and the bundle." |

## Bullet 2 — Response time and queue depth

| Claim | Date | Journal evidence |
|---|---|---|
| Median wait 3.3 staffed hours | 14 Sep 2026 | "Last 30 days, from the customer's message on both rails, median wait is 3.3 hours staffed and 6.1 on the wall." |
| Baseline was far worse | 31 Jul 2025 | "the gap between first message to second message is around 4 hours. It takes me around 4 to 6 hours to make the first round of message when I wake up." |
| 24-hour cycle replaced 2-hour window | 11 Feb 2026 | "We are pushing for 95% support automation… eliminate the two-hour monitoring window and move to a 24-hour cycle." |
| Two-hourly digest live | 4 Sep 2026 | "The two-hourly queue digest went live Friday evening… the first thing the server has produced that reaches a person without someone fetching it." |
| 630 → 120 active threads | 28 Jul 2026 | "Active tab went from 630 rows to 120, unread from 115 to 62." |
| Queue cleared to zero | 9 Sep 2026 | "Cleared the queue to zero across two passes — refunds, cancellations, credit releases and one account closure." |

**Caveat to know:** 3.3h is the *corrected* figure — the published number had been wrong. That is a strength, not a weakness. Say so.

## Bullet 3 — Knowledge layer and help center

| Claim | Date | Journal evidence |
|---|---|---|
| 15-category taxonomy, 120 articles, SQLite + FTS5 | 16 Apr 2026 | "Created a 15-category taxonomy… Tagged all 120 articles (55 public + 65 internal)… built the SQLite schema with FTS5 search, wrote the loader script" |
| Deliberately skipped RAG | 16 Apr 2026 | "at 15k words across 120 articles, vector embeddings would be over-engineering; category filtering gets 80% of the benefit with zero infrastructure" |
| Astro Starlight / Cloudflare Pages, 55 articles migrated | 17 Apr 2026 | "Built and deployed a new Evaboot Help Center using Astro Starlight, hosted on Cloudflare Pages. Migrated all 55 support articles from Intercom, recovering images before their CDN links expired." |
| 134 broken CDN images | 16 Apr 2026 | "Stripped 134 broken Intercom CDN image URLs across 38 files" |
| Final state: 118 articles, 53 public, zero dead links | 13 Aug 2026 | "It now holds 118 articles, 53 public, zero dead links, with every legacy article accounted for." |

## Bullet 4 — Evaluation gate

| Claim | Date | Journal evidence |
|---|---|---|
| 50 draft + 50 judge subagents, hard 100% | 16 Jun 2026 | "Ran the agent-eval-v2 loop end to end — 50 draft + 50 judge Haiku subagents into the deterministic scorer. Clean run (hard 100%, 0 errored, 0 skipped)" |
| Baseline hard 100% / soft 90% | 17 Jun 2026 | "Closed the golden-eval baseline (first real scorecard, hard 100% / soft 90%)" |
| 114-case suite | 12 Jul 2026 | "The eval pipeline regenerated all 114 cases" |
| 603 tests, money barred by test | 14 Aug 2026 | "all thirteen tasks, 603 tests green… The card layer is now barred from touching money, enforced by a test rather than a comment." |
| Review caught real defects | 12 Aug 2026 / 5 Aug 2026 / 17 Jun 2026 | "One silent-drop bug passed all 531 tests and was only caught in review"; "Reviews caught four real guard defects, including a fail-closed contract that broke on a null"; "an independent plan review caught a real regex bug in the outcome parser before any code was written" |

## Bullet 5 — Revenue recovery

| Claim | Date | Journal evidence |
|---|---|---|
| 19 disputes, 10 customers, ~$1,070 + €49, zero failures | 12 Jun 2026 | "Built and submitted evidence packages for all 19 actionable disputes across 10 customers (~$1,070 + €49) via the dispute-submit skill — every one now under_review, zero failures." |
| 21 submissions in 15 minutes | 14 Jan 2026 | "Completed 21 dispute evidence submissions in 15 minutes. All disputes cleared." |
| Money batch: 8 refunds / $293.97 | 10 Aug 2026 | see Bullet 1 |
| $425 + €9 refunded, $99 collected | 14 Aug 2026 | "Executed the approved billing actions — $425 and €9 refunded, $99 collected, six subscriptions actioned" |
| Email batch: 8 cancels, 4 refunds ($367), 2 credit grants | 12 Jun 2026 | "Ran the email_tools batch over 66 of 161 dogfood email threads" |
| Dispute-prevention policy work | 23 Feb 2026 | "review the dispute reduction guidance provided by Stripe and assess how we can integrate those recommendations" |

## Bullet 6 — Silent failures and archive

| Claim | Date | Journal evidence |
|---|---|---|
| 4 of ~296 emails reaching Intercom | 20 May 2026 | "The Intercom-to-Gmail mirror does not exist at all (zero inbound mirror messages in 30 days)… Only about 4 of ~296 support emails created Intercom conversations." |
| Closed-thread count 1 vs 212 real; medians ~3x optimistic | 14 Sep 2026 | "Closed-thread count was reading 1 against 212 real. Reply-time on the dashboard uses a 10-hour staffed day; the weekly report had been using three, so published medians were about a third of the real wait." |
| 18,065 conversations + ~5,300 attachments to S3 | 10 Aug 2026 | "18,065 conversations (1,829 / 10,331 / 5,905 across 2024–2026) plus ~5,300 attachments, zero fetch failures, uploaded to S3." |
| Security review | 7 Sep 2026 | "Went through Robin's findings, confirmed all of them and found one more. Landed the first round of privacy cleanups." |
| Corrected a wrong weekly report to the founder | 6 Jul 2026 | "checked every item against the actual repo and live state and about half was wrong or stale. Rewrote the section." |

## Bullet 7 — Solo through incidents + GTM load

| Claim | Date | Journal evidence |
|---|---|---|
| 400–500 ticket spikes | 19 Aug 2025 | "Volume might spike to 400–500 tickets tomorrow." |
| 120-ticket audit | 19 Aug 2025 | "I audit 120 tickets to make sure everyone's up to date… all the pause accounts are acting in accordance and the Stripe and Admin are in sync." |
| Chrome Web Store delisting incident | 2 Apr 2026 | "A flood of users came into support chat reporting the Chrome extension was removed from the Chrome Store… no one could use the extension during that time." |
| 1M-credit contract via DocuSign | 2 Apr 2026 | "In the middle of signing a contract with a client requiring 1 million credits… modify the contract and send it via DocuSign" |
| ~3,000 emails/week campaigns | 22 Jan 2026 | "Around 3,000 emails per week seems reasonable for maintenance" |
| Discount policy design | 30 Mar 2026 | "Discount policy document appended with $299/mo threshold and two-route logic" |
| Live demos, incl. GDPR-skeptical enterprise | 21 Jan 2026 | "a demo with a client who is very skeptical about products, especially with the security… GDPR compliance concerns" |
| Reply time -30% via React artifact | 3 Mar 2026 | "It is reducing reply time by roughly 30%, and the new guidelines are producing strong response quality." |

---

## Strong material NOT on the resume (interview ammunition)

Keep these in your pocket. They are too granular for the page but excellent answers to "tell me about a time…":

- **MCP server documentation, 9 Sep 2026** — "settled the tool count at thirty-seven, against two internal figures that were both wrong. Twenty tools that write to a customer's real LinkedIn account were undocumented." *Answer to: tell me about finding a risk nobody had flagged.*
- **Prompt-injection caught in production, 30 Jun 2026** — "a verify agent caught a prompt-injection attempt in one thread." *Answer to: how do you think about agent security.*
- **Repo hygiene at scale, 23 Jun & 9 Sep 2026** — 24 worktrees → 3; 17 working copies and 30 branches → 3 and 4, every deletion backed up first. *Answer to: how do you handle technical debt.*
- **Nightly repo steward, 20 Jul 2026** — brainstorm → spec → three review rounds → merged and running, in one day. *Answer to: how fast do you ship.*
- **Cadence insight, 27 Jul 2026** — "A 24-hour batch is roughly 70 tickets while a two-hour sweep is five or six. Cadence is the fix, not the surface." *Answer to: tell me about a non-obvious insight.*
- **The capacity-answer bug, 10 Aug 2026** — "The bot told a customer her balance was 'more than enough' three times while she was 169 credits short; capacity answers must come from arithmetic, not sentiment." *Answer to: tell me about an LLM failure mode you had to design around. This is your best single story — use it.*
- **Learning something twice, 4 Sep 2026** — "A green status line proves the job ran, not that anything arrived — the same lesson the sweep loop taught three weeks ago, learned twice in one week." *Answer to: tell me about a mistake. It is honest, specific, and shows you track your own error patterns.*

---

## Claims I deliberately did NOT put on the resume

Discipline matters more than volume. These were tempting and are not defensible enough:

- **"95% support automation."** That was the *target* set on 11 Feb 2026, and the journals record reaching "around the 70% mark" on 18 Feb. No entry confirms 95% was achieved. Do not claim it.
- **Deflection rate / CSAT improvement.** CSAT capture was only merged in Jul 2026 and 15 Jan 2026 notes "resolution rates remain low." There is no clean before/after. Leave it out.
- **Ticket volume reduction.** Plausible but never measured end to end in the journals.
- **"20% boost in customer satisfaction" (Ajinomoto, 2018)** and **"30% engagement improvement."** These are on your old CV with no supporting source. I kept the 20% (it was already public) and dropped the 30%. If either is challenged and you cannot source it, say so plainly — a candidate who retracts a number cleanly is more trustworthy than one who defends it vaguely.

---

## Bullets 7–8 — onboarding, customer education, commercial surface

Added after Jade correctly flagged that the first pass under-weighted this stream.

| Claim | Date | Journal evidence |
|---|---|---|
| No onboarding docs existed; built from scratch | 23 Nov 2025 | "we didn't really have any onboarding documents, so I have to kind of set up the bare bones first, so I'm rewriting the onboarding document as I progress" |
| Three-node onboarding flow plus pricing node | 12 Dec 2025 | "Broke onboarding into 3 main nodes, plus an additional pricing-related node" |
| Designed Fin as onboarding/CSM function | 25 Nov & 10 Dec 2025 | "Begin designing a structured onboarding system for FIN… clear, guided steps and educational support features"; "onboarding FIN AI agent to handle Customer Success Manager functions" |
| HubSpot integration tutorial | 29–30 Jan 2026 | "Create a video tutorial to walk through the HubSpot integration" → "I finished the integration tutorial for HubSpot." |
| Clay integration videos | 15 Dec 2025 | "started recording the integration videos for Clay, which is a bit more complicated" |
| In-app onboarding video, full production | 22 Dec 2025 | "creating and editing a vertical onboarding video for Intercom (adding subtitles, images, and animations)" — approved by JP |
| Recurring-export walkthrough, reshot for quality | 2–4 Mar 2026 | "Recorded the recurring export walkthrough video" → "Reshot the video… wasn't happy with the result, so shot it again." |
| Loom for marketing/outreach | 9 Feb & 23 Mar 2026 | one-click export-to-integration walkthrough; 3-minute outreach Loom |
| Trained a delegate | 30 Jan 2026 | "I continue to delegate some of the tasks… to Francine… I have recorded a video and make sure everything is set up on her end." |
| Tone handbook ownership | 9 Jan & 28 Aug 2026 | "consolidated rules… into a single rule set: one-to-one tone, no marketing language, no assumptions about memory"; "Reviewed an external support-writing toolkit and rejected it — it teaches exactly the robotic voice we ban." |
| Demos through to close, incl. GDPR-skeptical enterprise | Oct 2025 – Mar 2026 | multiple; 21 Jan 2026: "a demo with a client who is very skeptical… GDPR compliance concerns" |
| Discount policy design | 30 Mar 2026 | "$299/mo threshold and two-route logic" |
| Machine-readable defect feed for engineering | 31 Jul 2026 | "Specced and published a machine-readable, defect-shaped feed so engineering's AI can triage signal without opening conversations, one record per signature rather than one per customer." |

**The framing that came out of this:** you were not a support hire who took on projects. You were the entire customer-facing function — support, onboarding, education, demos, and the product-feedback loop — and then you built the system that carries most of it. Use that sentence.

---

## The Intercom replacement — the lead claim

Added after Jade flagged that earlier drafts framed this as "configured Intercom Fin" and "migrated the help center." It was a full vendor replacement, and it is the strongest thing on the resume.

| Claim | Date | Journal evidence |
|---|---|---|
| Full stack built on AWS | 16 May 2026 | "stand up the full support stack (widget + admin inbox + backend)… DynamoDB, Lambdas, API Gateways, Cognito, S3… a human can click through widget → DDB → admin inbox → reply → widget" |
| Deployed to real AWS, proven end to end | 21 May 2026 | "Migrated the dogfood support backend onto real AWS in eu-central-1, deploying the Python Lambdas, DynamoDB tables, two Cognito pools, and HTTP plus WebSocket API Gateways, and proved the flow end-to-end from widget to router to agent." |
| Multi-conversation threading | 22 May 2026 | "an Intercom-style multi-conversation widget model… per-conversation rows, user-partitioned keys, auto-reopen, hybrid state migration" |
| Email channel replacing Intercom's | 26–29 May 2026 | SES inbound/outbound channel; "Closed out the SES/email-channel milestone end to end" |
| Intercom sunsets at cutover | 5 Jun 2026 | "Intercom dedup is transitional (sunsets at backend cutover)" |
| Stripe back-office panel inside the inbox | 12 Jun 2026 | "Built the read-only live Stripe panel for the inbox MVP… 73 frontend + 167 backend tests green" |
| **Cutover executed** | **31 Jul 2026** | "Closed the spec through further Codex rounds and built the transcript importer with a ledger and a rollback path… **Ran the import and flipped the widget on for every dashboard user through the feature flag.**" |
| Design fork settled | 30 Jul 2026 | "Dropped the holdout-list model in favour of flipping every user at once" |
| Three rails unified | 10 Aug 2026 | "Rebuilt 68 triage cards across Intercom, email, and widget" |
| Intercom seats retired | 10 Aug 2026 | "Landed the cold-archive tool ahead of the seat sunset… 18,065 conversations… uploaded to S3" |
| Widget shipped to production | 10 Aug 2026 | "Widget PR #9 shipped through the Cloudflare Pages deploy" |
| Inbox/widget in ongoing production use | 19 Aug 2026 | "Shipped markers that tell AI replies apart from human ones so the team can audit at a glance… fixed an attachment error" |

### Self-improving loop

| Claim | Date | Journal evidence |
|---|---|---|
| Designed from scratch | 22–23 Jun 2026 | "*Agent self-learning loop*: New design work (no spec yet) — start at brainstorm." |
| Weekly cycle running | 24 Jul 2026 | "*Weekly Agent Improvement Loop*: Run the reporting defect queue weekly… persist reply mode plus retrieved KB article ids to unblock the deferred model-judged quality" |
| Live defects feed it | 3 & 10 Aug 2026 | "Work cutover and email-rail stragglers as they surface, feed defects into the improvement loop." |
| Defects become eval cases | 3 Aug 2026 | "An existing golden case did not prevent the defect it was written for. New cases were parked with a resume trigger rather than added to a suite about to change." |

### Two numbers I could NOT source — you must be able to defend these

| Claim | Status |
|---|---|
| **~$100K/year saved in tooling** | Not in the journals. It is your figure and your company's data, so it stays on the resume — but be ready to break it down: Intercom seats × price, Fin resolution charges, the Pro add-on you assessed at $99+/month, minus what AWS now costs you. An interviewer who works in support tooling *will* ask, and "roughly" is a fine answer only if you can show the arithmetic. |
| **~50% cut in support handling time** | Not directly stated. The journals support: reply time down ~30% from the React artifact (3 Mar 2026); a two-hour monitoring window replaced by a 24-hour cycle; median wait 3.3 staffed hours; inbox 630 → 120. If your 50% comes from a measurement you ran, keep it and cite the basis. If it is an estimate, say "roughly halved" in conversation and let the 3.3-hour median and the 630 → 120 carry the written claim. |

Do not let either number be the thing that unravels an otherwise airtight page. Everything else here has a date.
