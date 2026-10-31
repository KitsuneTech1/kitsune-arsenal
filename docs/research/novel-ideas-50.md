# Kitsune Capability Gateway: 50 tools that mostly do not exist yet

These are capabilities to give AI agents, not SaaS replacements. Each one either only makes sense because an agent is the caller, only became buildable now that a model sits on the other end, or collapses a slow human loop into a single call. For each: name, pitch, the gap, who wants it and the hours-saved story, build difficulty, whether it is agent-native, and the nearest existing thing so we can see it is really new.

Naming: "agent-native" means a human could not usefully call it by hand, or would never bother, because the value is in an agent chaining it, running it continuously, or reacting to it.

---

## 1. Recall
- Pitch: a shared long-term memory bus where any agent writes a fact once and every other agent (Claude, Codex, OpenCode) can query it later with provenance and confidence.
- Gap: memory today is per-tool and per-session. There is no neutral store that survives context compaction and is readable across harnesses, with who-said-it and when.
- Who and hours: anyone running many agent sessions. One call replaces re-explaining the same project state to each new session, which is 20 to 40 minutes of re-priming per day across sessions.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: Mem0, Letta, vector stores. Those are single-app memory, not a cross-harness fact bus with provenance and cross-agent write.

## 2. DidItChange
- Pitch: register any URL, API response, file, on-chain value, or DOM selector and get a stable diff token that only flips when the meaningful content changed, not when ads or timestamps did.
- Gap: existing change watchers fire on any byte change and drown agents in noise. Nothing does semantic "did the thing I care about actually change" for arbitrary sources.
- Who and hours: any watcher agent. Replaces hand-built scrapers plus diff logic plus noise filtering, roughly a day of glue per source.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: Visualping, changedetection.io. Those alert humans on raw diffs; they do not give an agent a semantic change token to branch on.

## 3. Ledger
- Pitch: an append-only receipt store where an agent records every consequential action it took, with inputs, outputs, and a signature, so a later agent or human can audit what happened and why.
- Gap: agent actions vanish into chat logs. There is no tamper-evident, queryable record of "agent X did Y at time Z with these inputs."
- Who and hours: anyone who lets agents act on real systems. Replaces reconstructing what an agent did from scattered logs, hours per incident.
- Difficulty: easy. Agent-native: yes.
- Nearest thing: audit logs, LangSmith traces. Those are per-framework observability, not a portable signed action ledger an agent writes to on purpose.

## 4. Checkpoint
- Pitch: freeze the full state of a multi-step agent task (files touched, decisions, partial outputs) into one token, and rehydrate it in any session later.
- Gap: session death loses in-flight work. There is no "save game" for an agent task that another session can load.
- Who and hours: long tasks that outrun a context window. Replaces redoing lost work after a crash or compaction, often an hour or more.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: LangGraph checkpointers. Framework-locked and not portable across harnesses or human handoff.

## 5. Quorum
- Pitch: one call fans a question out to N independent models, returns their answers plus an agreement score and the specific points where they disagree.
- Gap: getting a real second opinion means wiring up several providers by hand and reconciling formats. No single call gives you the disagreement map.
- Who and hours: any agent about to make a costly or hard-to-reverse claim. Replaces manual multi-model checking, 15 to 30 minutes each.
- Difficulty: easy. Agent-native: yes.
- Nearest thing: consensus.app for papers, LLM router services. Routers pick one model; they do not surface structured disagreement for verification.

## 6. Groundwire
- Pitch: give it a claim and it returns whether the claim is currently supported by live sources, with the exact quotes and a stale-by date, or tells you it cannot verify.
- Gap: retrieval tools fetch text; they do not rule on whether a specific claim is true right now and stamp when it will need rechecking.
- Who and hours: any agent quoting a price, spec, version, or stat. Replaces the verify-before-you-assert loop, minutes per claim, and prevents confident wrong answers.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: fact-check APIs, Perplexity. Those answer questions; they do not return a verdict object with a freshness clock for a single claim.

## 7. Handback
- Pitch: an agent parks a task that hit a human-only wall (a payment, a login, a CAPTCHA, a signature) and gets notified the instant a human clears it, then resumes automatically.
- Gap: today the agent either gives up or the human forgets. There is no clean park-and-resume across the human boundary.
- Who and hours: any agent that occasionally needs one human action. Replaces dead tasks and manual re-kickoff, saves the whole rest of a workflow from being abandoned.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: human-in-the-loop hooks in some frameworks. Those block the run; this parks state and resumes cross-session.

## 8. Costmeter
- Pitch: wraps any tool or model call and returns the real money and token cost before and after, with a running budget the agent can check and refuse to blow.
- Gap: agents spend tokens and dollars blind. There is no in-band budget an agent can query mid-task and self-limit against.
- Who and hours: anyone on tight usage. Replaces surprise bills and post-hoc cost forensics, and stops runaway loops.
- Difficulty: easy. Agent-native: yes.
- Nearest thing: Helicone, OpenMeter. Dashboards for humans after the fact, not an in-call budget guard the agent reads.

## 9. Sandhands
- Pitch: give an agent a throwaway identity bundle (disposable email, phone relay, funded burner wallet, clean IP) for one task, auto-destroyed after.
- Gap: agents need to sign up and act on the web without touching the owner's real accounts or dox. Assembling a burner identity by hand is slow and leaky.
- Who and hours: any agent doing signups, trials, or public target work. Replaces manual burner setup, 20 to 40 minutes per identity.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: temp-mail sites, proxy services. Piecemeal and human-driven; nothing bundles a full disposable identity behind one call.

## 10. Rewind
- Pitch: every external action an agent takes is wrapped with a matching undo, and one call rolls back the last N actions across all tools involved.
- Gap: agents can act but cannot cleanly reverse a multi-tool sequence. Undo is per-app and manual.
- Who and hours: anyone letting agents change real state. Replaces frantic manual cleanup after a bad run, hours per mistake.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: database transactions, git. Scoped to one system; nothing gives cross-tool compensating undo.

## 11. Trailhead
- Pitch: turns a vague goal into a verified, executable plan by dry-running each step against the actual tools available and reporting which steps will fail before anything runs.
- Gap: planners hallucinate steps and tools that do not exist. Nothing checks a plan against the live tool surface first.
- Who and hours: any agent facing a multi-tool task. Replaces failed half-runs and rework, often an hour of thrash.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: planning prompts, task decomposition libs. Those plan on faith; this validates against real tool schemas.

## 12. Echo
- Pitch: reads a webhook, email, or event stream and tells the agent in plain language what changed and what it probably needs to do about it.
- Gap: raw events are noise. Agents need a "here is what this means for you" layer, not another JSON blob.
- Who and hours: any reactive agent. Replaces per-event parsing logic, days of glue over a project's life.
- Difficulty: easy. Agent-native: yes.
- Nearest thing: Zapier, n8n. Those route events with rules; they do not interpret intent for a downstream agent.

## 13. Provenance
- Pitch: stamps any file, image, or text an agent produced with a signed record of which model, prompt, and sources made it, verifiable later by anyone.
- Gap: no way to prove what an artifact came from once it leaves the session. Matters for legal, trust, and "did AI write this."
- Who and hours: anyone shipping agent output externally. Replaces the impossible task of proving origin after the fact.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: C2PA content credentials. Media only, camera and editor focused; not a general agent-output provenance call.

## 14. Standin
- Pitch: an agent describes a person or role and gets a faithful simulated stakeholder to pressure-test a plan, message, or design against, with the persona grounded in real public writing where available.
- Gap: getting real user or stakeholder feedback is slow. Generic "act as a user" prompts are shallow and ungrounded.
- Who and hours: any agent drafting something for a specific audience. Replaces a review round, hours to days of waiting.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: synthetic-user startups (Synthetic Users). Web apps for humans, not a grounded persona call an agent chains into its own loop.

## 15. Tripwire
- Pitch: an agent sets a natural-language condition ("if BTC funding flips negative and my position is open") and gets a single durable watcher that fires exactly once when it becomes true.
- Gap: writing a bespoke monitor for each condition is real engineering. Agents need to declare a trigger in words and forget it.
- Who and hours: trading, ops, security agents. Replaces custom watcher code, a day each, and lets an agent set dozens cheaply.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: alerting tools, TradingView alerts. Fixed schemas and human dashboards; not free-text conditions an agent declares on the fly.

## 16. Consent
- Pitch: a permission broker where a human pre-authorizes classes of agent action ("spend up to $5/hr on AWS", "email people in this list") and agents check the grant in one call before acting.
- Gap: permission today is all-or-nothing per tool. There is no fine-grained, queryable grant an agent respects at runtime.
- Who and hours: anyone running autonomous agents. Replaces constant approval prompts while keeping real limits, saves dozens of interruptions a day.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: OAuth scopes, IAM. Coarse and static; not a live human-set policy an agent queries per action.

## 17. Freshcheck
- Pitch: point it at any fact an agent is about to rely on and it returns how stale that fact is likely to be and whether it is worth re-verifying now.
- Gap: agents cannot tell a stable fact (a math constant) from a drift-prone one (a price). They either over-verify and burn tokens or under-verify and get it wrong.
- Who and hours: every agent. Replaces judgment calls on what to recheck, saves both tokens and wrong answers.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: nothing direct. Caching TTLs are hand-set; this predicts staleness per fact type.

## 18. Bridge
- Pitch: one call moves a payload between any two tools that do not speak to each other, translating formats, auth, and pagination on the fly.
- Gap: connecting tool A to tool B is bespoke integration work every time. Agents want to just say "put this there."
- Who and hours: any agent stitching tools. Replaces one-off integration code, hours to days each.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: iPaaS (Zapier, Make). Human-configured flows; this is a generic agent-invoked translator with no prebuilt recipe.

## 19. Witness
- Pitch: records a full replayable trace of a browser or tool session so an agent (or human) can later prove exactly what a page showed or what an API returned at that moment.
- Gap: "the site said X when I looked" is unprovable. Screenshots lie and can be faked; there is no signed, timestamped capture of a live interaction.
- Who and hours: bounty, compliance, dispute, and research agents. Replaces he-said-she-said and repeated re-checks.
- Difficulty: medium. Agent-native: partly (humans want it too).
- Nearest thing: web archiving (archive.org), screen recorders. Not signed, not timestamped-for-proof, not agent-invoked mid-task.

## 20. Distill
- Pitch: hand it a firehose (a Discord, a subreddit, a mailing list, a repo's issues) and get back only the items that matter to a standing interest you described once.
- Gap: filtering a stream to your actual interest needs a model reading everything continuously. No product runs that loop for you cheaply.
- Who and hours: anyone drowning in channels. Replaces hours of daily skimming with a two-line digest.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: RSS filters, keyword alerts. Keyword-based and dumb; this is semantic and continuous.

## 21. Twin
- Pitch: spins up a disposable, faithful clone of a live system (a DB, an API, a wallet state) so an agent can test a destructive action safely, then discards it.
- Gap: agents need to try risky operations without touching production. Building a realistic sandbox per task is heavy.
- Who and hours: any agent doing migrations, deploys, or sweeps. Replaces the fear of testing on prod and the labor of building staging.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: DB branching (Neon, PlanetScale). One data type, human-driven; not a general on-demand clone an agent requests.

## 22. Escrow
- Pitch: holds an agent's proposed high-stakes action for a set delay or a second signal before it fires, so a human or another agent can veto in the window.
- Gap: there is no built-in "cooling off" primitive between an agent deciding and the world changing.
- Who and hours: anyone letting agents touch money or production. Replaces the choice between blocking every action and trusting blindly.
- Difficulty: easy. Agent-native: yes.
- Nearest thing: approval queues. Human-facing and manual; this is a timed, programmable veto window agents build into flows.

## 23. Crossref
- Pitch: give it the same question and it independently answers it two different ways (two data sources, two methods) and flags if they disagree, returning a range instead of a false-precise number.
- Gap: agents pass single-source numbers straight through. Nothing enforces a second independent confirmation automatically.
- Who and hours: any agent reporting a number. Replaces the manual double-check rule, and catches wrong figures before they reach a decision.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: nothing packaged. This is the "double-check every number" discipline turned into a callable tool.

## 24. Warmstart
- Pitch: before an agent starts on a project, one call returns the last N handoffs, open threads, dirty files, and running processes for that project, already summarized.
- Gap: cold-starting a session means hunting through notes and logs. There is no single "where were we" call.
- Who and hours: anyone with long-running projects across sessions. Replaces 10 to 20 minutes of context reassembly every session.
- Difficulty: easy. Agent-native: yes.
- Nearest thing: project wikis, session notes. Passive documents a human reads; this assembles the state on demand for the agent.

## 25. Reflex
- Pitch: an agent registers a standing rule ("whenever a new repo appears, classify and tag it") and the tool runs that rule forever without a session open.
- Gap: agents only act when invoked. There is no way to leave behind a persistent behavior that survives the session ending.
- Who and hours: anyone with recurring maintenance. Replaces remembering to run things, and cron jobs you would otherwise hand-write.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: cron, GitHub Actions. Code you write and maintain; this is a natural-language standing reflex an agent installs.

## 26. Faceoff
- Pitch: pits two candidate outputs (two drafts, two designs, two plans) against each other on criteria you name and returns a scored, reasoned verdict plus the deciding factor.
- Gap: comparing options rigorously is manual. Generic "which is better" prompts are unreliable and unauditable.
- Who and hours: any agent choosing between options. Replaces a deliberation round, and produces a record of why.
- Difficulty: easy. Agent-native: yes.
- Nearest thing: LLM-as-judge scripts. Bespoke and one-off; this is a standing, auditable comparator with a fixed criteria contract.

## 27. Passport
- Pitch: a portable capability card for an agent that a remote service can verify, listing what the agent is allowed to do and who vouches for it, without exposing the owner.
- Gap: services cannot tell a trusted agent from a scraper. There is no agent identity that carries verifiable authorization.
- Who and hours: anyone whose agents interact with cooperating services. Replaces per-service API keys and manual allowlisting.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: API keys, OAuth. Per-service and opaque; this is a verifiable, portable agent credential.

## 28. Backstop
- Pitch: watches an agent's own output as it works and halts it the moment it starts looping, contradicting itself, or drifting off the goal, with a plain reason.
- Gap: agents fail silently by spinning. There is no independent circuit breaker that judges the agent's own behavior in flight.
- Who and hours: anyone running unattended agents. Replaces returning to a burned budget and a stuck task.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: max-iteration caps, guardrail libs. Blunt counters; this is a semantic drift and loop detector.

## 29. Timefold
- Pitch: give it a research question and it runs the same query against snapshots of the web at several past dates, returning how the answer changed over time.
- Gap: agents only see now. Reconstructing how consensus or a fact evolved is heavy manual archive work.
- Who and hours: research, due-diligence, trend agents. Replaces days of archive spelunking with one call.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: Wayback Machine. Raw page snapshots; this synthesizes an answer-over-time from them.

## 30. Handshake
- Pitch: lets two agents that have never met negotiate a shared task contract (who does what, in what format, by when) and hold each other to it.
- Gap: multi-agent systems assume a common owner and schema. Cross-owner agent collaboration has no negotiation primitive.
- Who and hours: anyone chaining agents from different systems. Replaces brittle hardcoded interfaces between agents.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: agent protocols (A2A early drafts). Transport specs; this is the negotiated-contract layer on top.

## 31. Snapback
- Pitch: an agent captures the exact working state of a config, deploy, or environment right before a risky change, tagged so it can restore that exact state in one later call.
- Gap: "it worked five minutes ago" is not recoverable without discipline. Snapshots are manual and per-system.
- Who and hours: any agent editing shared infra. Replaces the panic of an unrecoverable bad change.
- Difficulty: medium. Agent-native: partly.
- Nearest thing: VM snapshots, git stash. Per-system; this is a uniform pre-change capture across whatever the agent is about to touch.

## 32. Interpreter
- Pitch: translates between an agent's intent and a legacy system's ugly interface (a SOAP API, a fixed-width file, a scraped form) so the agent speaks plain and the tool does the ugly part.
- Gap: agents choke on old, badly documented interfaces. Writing an adapter is real work each time.
- Who and hours: any agent forced to touch enterprise or legacy systems. Replaces days of adapter coding.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: API wrappers. Hand-built per API; this generates and maintains the adapter from a description.

## 33. Vouch
- Pitch: before an agent trusts a data source, one call returns that source's track record (how often it was later corrected, how fresh it is, who else relies on it).
- Gap: agents treat all sources as equal. There is no reputation layer for the sources an agent might cite.
- Who and hours: any research or decision agent. Replaces guessing at source quality, and reduces confidently citing junk.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: media-bias trackers. Human-curated and narrow; this is a machine-readable source-reliability call for arbitrary sources.

## 34. Dryrun
- Pitch: simulates the full downstream effect of a proposed action ("if I cancel this order", "if I merge this PR") and reports what would break, before doing it.
- Gap: agents cannot see second-order consequences. Impact analysis is manual and often skipped.
- Who and hours: any agent making changes with ripple effects. Replaces post-hoc firefighting.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: terraform plan, CI checks. Domain-specific; this is a general consequence simulator an agent calls first.

## 35. Locket
- Pitch: an agent stores a secret it will need again (a session token, a derived key) in a broker that only ever returns it to an agent proving the same task identity, never to a human or a log.
- Gap: agents either re-authenticate constantly or leak secrets into context and logs. There is no agent-scoped ephemeral secret store.
- Who and hours: any agent doing repeated authed work. Replaces re-login loops and secret leakage risk.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: Vault, secret managers. Human and service oriented; not an agent-task-scoped return with anti-leak guarantees.

## 36. Chorus
- Pitch: coordinates several agents working the same big task so they claim non-overlapping subtasks, see each other's progress, and never duplicate work, via one shared board.
- Gap: fan-out today produces duplicate effort and collisions. There is no lightweight neutral coordination board across harnesses.
- Who and hours: anyone running parallel agents. Replaces wasted duplicate runs and merge conflicts.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: task queues, Celery. Code-level and single-system; this is a cross-agent claim-and-progress board.

## 37. Litmus
- Pitch: give it a piece of text and it tells you, with evidence, whether it reads as AI-generated and exactly which phrases give it away, so an agent can fix its own tells.
- Gap: AI-detection tools give a score, not the specific tells, and are not built for an agent to self-correct against.
- Who and hours: any agent producing copy that must pass as human. Replaces manual voice review, and bakes the fix into the loop.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: GPTZero, Originality.ai. Human-facing verdict scores; this returns actionable tells for self-editing.

## 38. Beacon
- Pitch: an agent posts a live one-line status of a background task to a durable place, and any other agent or human can read the current state without interrupting the worker.
- Gap: background agent work is a black box until it finishes. There is no low-friction live status any observer can poll.
- Who and hours: anyone running long background jobs. Replaces "is it still going" anxiety and premature kills.
- Difficulty: easy. Agent-native: yes.
- Nearest thing: log tailing, status pages. Heavyweight or human-built; this is a one-call status heartbeat.

## 39. Forage
- Pitch: describe data you wish existed ("every X that has property Y") and it assembles the dataset by orchestrating searches, scrapes, and API calls, returning it with per-row provenance.
- Gap: building a novel dataset is a multi-day project of finding sources and stitching them. Agents want to just ask for the data.
- Who and hours: research, sales, and analysis agents. Replaces days of data assembly with one call.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: scraping platforms (Apify), data brokers. Per-source and manual; this is a goal-driven dataset builder with provenance.

## 40. Referee
- Pitch: two agents (or an agent and a human) disagree; this takes both positions plus the evidence and returns a reasoned ruling that cites which evidence was decisive.
- Gap: agent disagreements have no resolution path except escalate to a human. There is no neutral adjudicator that shows its work.
- Who and hours: multi-agent and human-agent teams. Replaces stalled decisions and endless back-and-forth.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: debate frameworks in research papers. Academic and unpackaged; this is a callable, auditable adjudicator.

## 41. Pulse
- Pitch: an agent asks "what is the current ground truth for X" (a live metric, a system state, an on-chain balance) and gets a cross-checked reading from at least two independent sources with drift flagged.
- Gap: single-endpoint reads lie (cached zeros, stale explorers). Nothing enforces multi-source truth for live metrics as a primitive.
- Who and hours: trading, ops, wallet agents. Replaces hand-rolled multi-RPC reconciliation, and prevents acting on a fake reading.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: oracle networks (Chainlink). On-chain and narrow; this is a general two-source live-metric reader for agents.

## 42. Loom
- Pitch: records the full chain of reasoning and tool calls behind a decision as a shareable thread, so a later agent can pick up exactly where thinking left off instead of restarting.
- Gap: reasoning evaporates at session end. The next agent redoes the analysis from scratch.
- Who and hours: any multi-session analytical work. Replaces re-deriving the same conclusions, hours per handoff.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: trace viewers. Read-only debugging views; this is a resumable reasoning thread agents write and continue.

## 43. Gatekeeper
- Pitch: sits in front of a real-world action (send, publish, pay, delete) and forces a structured "are you sure" that the calling agent must answer with specifics, catching accidental or hallucinated actions.
- Gap: agents fire irreversible actions on flimsy reasoning. There is no in-band challenge that makes the agent justify itself first.
- Who and hours: anyone letting agents act externally. Replaces cleaning up after a confidently wrong action.
- Difficulty: easy. Agent-native: yes.
- Nearest thing: confirmation dialogs. Human clicks; this is a machine challenge the agent must pass with evidence.

## 44. Cartograph
- Pitch: point it at a codebase, an org, or a system and it returns a live map of how the pieces connect, updated as things change, that an agent can query instead of re-reading everything.
- Gap: agents re-explore a large system on every task. There is no shared, current map they can consult.
- Who and hours: any agent working in a big repo or infra. Replaces repeated full-codebase reads, large token savings per task.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: code graph tools (Sourcegraph). Human-facing and code-only; this is a queryable living map for agents across code and infra.

## 45. Understudy
- Pitch: an agent hands off a task to a cheaper model with a tight spec, and this tool verifies the cheap result meets the spec before returning it, escalating only on failure.
- Gap: delegating to a cheap worker risks silent bad output. There is no automatic accept-or-escalate gate on delegated results.
- Who and hours: anyone optimizing token cost with model tiers. Replaces manual QA of worker output, and safely cuts spend.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: model routers. Route on input features; this gates on verified output quality.

## 46. Timelock
- Pitch: an agent schedules a future action in plain language ("next Tuesday if the invoice is still unpaid, send the reminder draft") and the tool holds and re-evaluates the condition at the time.
- Gap: scheduling with a condition attached needs custom code. Agents want to say it once and trust it fires only if still relevant.
- Who and hours: ops, finance, follow-up agents. Replaces reminder scaffolding and stale-action mistakes.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: cron plus if-statements. Hand-built; this is conditional natural-language scheduling as a call.

## 47. Souvenir
- Pitch: after any task, one call produces a compact, reusable skill from what the agent just figured out, so the next agent solves the same problem instantly instead of rediscovering it.
- Gap: hard-won solutions are not captured as reusable capability. Every agent relearns the same tricks.
- Who and hours: anyone whose agents hit recurring problems. Replaces repeated rediscovery, compounding over time.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: skill files, prompt libraries. Human-authored; this auto-mints a skill from a completed task's trace.

## 48. Sentinel
- Pitch: an agent registers a claim it made ("this fix works", "this deploy is stable") and the tool keeps watching reality and pings the agent if the claim later stops being true.
- Gap: agents assert things and move on. Nothing tracks whether past assertions held up.
- Who and hours: any agent making forward claims. Replaces silent regressions and stale confidence.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: monitoring and alerting. Metric thresholds humans set; this tracks an agent's own natural-language claims over time.

## 49. Ferry
- Pitch: moves a task and its full context from one agent or harness to another cleanly, so a Claude session can hand off to a Codex session (or a human) mid-task without losing the thread.
- Gap: handoff between harnesses means copy-pasting context by hand and losing state. There is no clean transfer primitive.
- Who and hours: anyone using multiple harnesses. Replaces manual re-priming on every handoff, 10 to 30 minutes each.
- Difficulty: medium. Agent-native: yes.
- Nearest thing: shared notes files. Passive and lossy; this is a live task transfer with state.

## 50. Oracle-of-me
- Pitch: an agent asks "what would the owner most likely decide here" and gets a grounded answer built from the owner's own past decisions, notes, and stated preferences, with a confidence and the evidence.
- Gap: agents guess at owner preferences or interrupt to ask. Nothing turns an owner's decision history into a queryable preference model.
- Who and hours: any agent making routine calls on the owner's behalf. Replaces constant clarifying questions, dozens a day, while staying faithful to how the owner actually decides.
- Difficulty: hard. Agent-native: yes.
- Nearest thing: preference learning, RLHF at the user level. Research-stage and not packaged; this is a callable personal-decision predictor grounded in real history.

---

## Tiers

### Build now (cheap and high value)
Fast to ship, immediately useful, mostly easy or low-medium difficulty.
- Quorum (5)
- Costmeter (8)
- Echo (12)
- Escrow (22)
- Faceoff (26)
- Beacon (38)
- Gatekeeper (43)
- Warmstart (24)
- Ledger (3)
- Recall (1)
- Distill (20)
- Crossref (23)

### Big swing (hard but special)
High ceiling, real engineering, would be genuinely hard to buy anywhere.
- Checkpoint (4)
- Rewind (10)
- Twin (21)
- Bridge (18)
- Dryrun (34)
- Cartograph (44)
- Reflex (25)
- Forage (39)
- Souvenir (47)
- Passport (27)
- Handshake (30)
- Oracle-of-me (50)
- Interpreter (32)

### Weird bets
Strange framing, uncertain demand, but if they land they are hard to copy.
- Sandhands (9)
- Standin (14)
- Timefold (29)
- Witness (19)
- Litmus (37)
- Referee (40)
- Sentinel (48)
- Vouch (33)
- Understudy (45)
