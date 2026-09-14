# Technical Writing — Training Module Source Document

> Source document feeding Skill 1 (Research Synthesizer) → Skill 2 (Learning Path Architect) → Skill 3 (Module Content Builder). Quiz content is intentionally excluded from authoring here — Skill 5 (Quiz Generator) owns that. No hands-on tasks or rubrics — this pipeline is quiz-only.

---

## 0. Module Metadata

- **Audience:**
  - **Cloud Engineers:** cloud engineers are frequently the sole owners of infrastructure that other teams depend on but rarely read the source of; a missing or wrong README, ADR, or runbook means every future operator — including the original author, months later — has to reverse-engineer intent from Terraform state and Slack history during an incident.
- **Video lecture (if any):** None yet produced. If recorded, keep to one ~20-minute session — README/ADR/runbook are three distinct document types but share the same underlying argument (bad docs are worse than no docs) and fit one session.
- **Learning objectives:**
  1. Explain why READMEs, ADRs, and runbooks exist as separate document types rather than one general-purpose document.
  2. Explain what a README is for and what information it must reliably answer for a new reader.
  3. Explain what an Architecture Decision Record (ADR) captures that a README does not, and why that record matters after the decision-makers have moved on.
  4. Explain what a runbook is for and why it must be written for someone operating under incident pressure, not someone casually browsing.
  5. Explain the claim "bad docs are worse than no docs" and identify what makes a document actively harmful rather than merely unhelpful.

---

## 1. Why This Subject Matters (Motivation)

No docs tells a reader clearly that they're on their own — they'll go read the code, ask someone, or reconstruct the reasoning from scratch, and they know it going in. Bad docs tell a reader they can trust a shortcut, and then the shortcut is wrong: a README with a setup step that hasn't worked in two versions, an ADR that states a decision but not the reasoning so nobody can tell if the original constraint still applies, a runbook that references a dashboard that was deprecated last quarter. Following bad documentation costs more time than having none, because the reader has to first discover it's wrong before they can go do the reconstruction they would have done anyway — and during an incident, that discovery process happens under pressure, with the system still broken. Technical writing in cloud engineering isn't a courtesy to future readers; it's the artifact that determines whether the operational knowledge in your head is transferable at all once you're unavailable, asleep, or gone.

---

## 2. Core Concepts

Concepts are grouped into two halves that build in order: the document types themselves first (what each one is for and who reads it, under what conditions), then documentation as an ongoing practice — what happens to those documents after they're written.

### Document Types

- **What Is Technical Documentation, and Why Three Different Types?**
  - **Context:** technical documentation exists to transfer operational knowledge across time and people — to someone new, to someone debugging at 2am, to someone re-litigating a decision a year later — none of whom can just ask the original author. A single document can't serve all three moments well: a newcomer needs orientation, an incident responder needs literal steps, and a future decision-maker needs historical reasoning. READMEs, runbooks, and ADRs exist because they're answers to those three distinct questions, not three names for the same kind of writing.
  - **Illustration:** not needed — conceptual framing, made concrete by the three document-type concepts that follow.
- **READMEs**
  - **Context:** the entry-point document for a repository or service, expected to reliably answer: what is this, how do I run/deploy it, what are its dependencies, and where do I go next (owner, related docs); it is not the place for deep design rationale or step-by-step incident procedures.
  - **Illustration:** [x] needed — a simple annotated outline of a good README's structure (purpose, setup, dependencies, ownership/contact, links out) versus a common bad example (a wall of outdated setup commands with no context on what the service even does).
- **Architecture Decision Records (ADRs)**
  - **Context:** a short, immutable record of a specific architectural decision — the context/constraints at the time, the decision made, the alternatives considered, and the consequences — written once and not edited later even if the decision is superseded (a new ADR supersedes an old one instead).
  - **Illustration:** [x] needed — a simple ADR template diagram (Context → Decision → Alternatives Considered → Consequences) contrasted with a superseding-ADR relationship (ADR-004 supersedes ADR-002).
- **Runbooks**
  - **Context:** a procedural document written for someone responding to an active operational issue, under time pressure, possibly unfamiliar with the system; it must be concrete and executable (exact commands, exact dashboards, exact escalation paths) rather than descriptive or conceptual.
  - **Illustration:** [x] needed — a comparison of a bad runbook step ("check if the service is healthy") versus a good one (the exact command/dashboard link and what a healthy vs. unhealthy result looks like).

### Documentation as an Ongoing Discipline

- **"Bad Docs Are Worse Than No Docs"**
  - **Context:** the core claim of this module — a document that is stale, wrong, or misleading actively costs a reader time (they trust it, act on it, discover it's wrong, and only then start the investigation they would have started immediately with no doc at all) rather than merely failing to help.
  - **Illustration:** not needed — conceptual, illustrated concretely via the case studies.
- **Documentation as a Maintenance Obligation, Not a One-Time Artifact**
  - **Context:** a README, ADR, or runbook that isn't updated alongside the system it describes accumulates staleness silently — since nothing forces a doc update the way a broken test forces a code fix, the discipline has to be deliberate (e.g., updating a runbook as part of the same PR that changes the procedure it documents).
  - **Illustration:** not needed — behavioral practice, covered in checklist.

---

## 3. Case Studies / Real-World Examples

1. **A runbook that sent the on-call engineer to a decommissioned dashboard**
   - **Scenario:** During a 2am incident, the on-call engineer follows the team's runbook, which instructs them to check a specific monitoring dashboard for the affected service. The dashboard was decommissioned during a monitoring platform migration six months earlier, and the link 404s.
   - **Technical Writing in Action:**
     - *Runbooks:* the runbook's value depends entirely on being concrete *and current* — a runbook with a broken link under incident pressure is worse than no runbook, because the engineer trusted it and lost minutes discovering the dead end before falling back to manual investigation.
     - *Documentation as a Maintenance Obligation:* the monitoring migration project had no step requiring runbook updates, so the staleness went undetected until an incident exposed it at the worst possible time.
   - **Outcome:** the team adds "update all referenced runbooks" as a mandatory checklist item for any project that changes a tool or dashboard runbooks depend on.

2. **An ADR-less decision that got silently re-litigated for a year**
   - **Scenario:** A team decided a year ago, after significant debate, not to adopt a particular multi-region deployment pattern due to a specific cost constraint at the time. No ADR was written. Over the following year, three different engineers each independently propose the same pattern again, each spending days re-deriving the same conclusion because there was no record of the original decision or its reasoning.
   - **Technical Writing in Action:**
     - *Architecture Decision Records (ADRs):* an ADR capturing the original context, decision, and consequences would have let each new proposer find the prior decision and its reasoning in minutes, and either accept it or explicitly argue that the original constraint (e.g., cost) no longer holds — rather than re-deriving from zero each time.
   - **Outcome:** the team retroactively writes an ADR for the original decision and adopts a policy that any deliberately-rejected significant architectural proposal gets an ADR specifically so it isn't silently re-litigated.

3. **A README that "worked" for the author and no one else**
   - **Scenario:** A README instructs new contributors to run a setup script, but the script silently depends on an environment variable the original author had set globally on their own machine months ago and never documented. Every new contributor's setup fails at the same step with a confusing, unrelated error.
   - **Technical Writing in Action:**
     - *READMEs:* the README's setup section gave the appearance of completeness (a runnable script) while omitting a dependency required for that script to actually work, which is more damaging than an honest "setup is undocumented, ask the team" because it costs each new reader the same debugging time before they discover the gap.
   - **Outcome:** the team requires that README setup instructions be verified against a genuinely clean environment (e.g., a fresh container) before merging, not just verified against the author's own already-configured machine.

---

## 4. Best Practice Checklist / Frameworks

- Write READMEs to reliably answer: what this is, how to run/deploy it, its key dependencies, and who owns it — verified against a clean environment, not the author's already-configured machine.
- Write one ADR per significant architectural decision, including alternatives considered and consequences, and never edit an old ADR to reflect a new decision — write a new one that explicitly supersedes it.
- Write runbooks as literal, executable steps (exact commands, exact links, exact expected output) for someone under incident pressure who may be unfamiliar with the system, and update them as part of any change to the systems or tools they reference.
- Treat documentation staleness as a defect with the same seriousness as a code defect — a stale runbook or README should be fixed or flagged, not left to quietly mislead the next reader.
- When a document can't be kept current, say so explicitly ("this section is unverified since the Q2 migration") rather than leaving it looking authoritative — an honest gap is safer than a confident wrong answer.
- Don't try to document everything exhaustively; prioritize the documents that get read under pressure or by newcomers (README, runbook) and the decisions that get silently re-litigated without a record (ADRs) — a wiki page nobody will ever read is not worth the maintenance burden.

---

## 5. Sources

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR proposal) — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Google, "Technical Writing for Engineers" — https://developers.google.com/tech-writing
- PagerDuty, "How to write a runbook" — https://www.pagerduty.com/resources/learn/what-is-a-runbook/
- Made With ML / community best practices, "How to write a good README" — https://www.makeareadme.com/
- ThoughtWorks Technology Radar, "Lightweight Architecture Decision Records" — https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records
- **Video lectures:** none cited.
