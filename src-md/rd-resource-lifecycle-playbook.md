# BENCH R&D PROGRAM

# RESOURCE LIFECYCLE PLAYBOOK

| Document Owner | Head of Engineering | Applies To | All R&D Projects |
|---|---|---|---|
| Review Cycle | Quarterly | Version | 1.0 |
| Related Docs | R&D Program Plan · Project Portfolio · Operations Handbook · Templates & Checklists |  |  |



# Purpose

This playbook covers every point at which a person moves into, through, or out of an R&D project. Rotators, tech leads, 20% contributors, BU consumers. Planned transitions and emergency pulls. Project activations and retirements.


It exists because the highest-risk moments in the R&D program are transitions. Bad onboarding wastes the first week of a rotation. Bad offboarding kills the project. Good process here is the difference between a program that compounds and a program that leaks.


**Use this doc in the moment.** Don't memorize it. When a rotator is joining, open Section 1 and follow the checklist.



# Section 1 — Rotator Onboarding

Triggered when a bench engineer is assigned to an R&D project.

## 1.1 Day 0 (Before Rotation Starts)

**Owner:** Engineering Manager + Tech Lead


    - Engineering Manager confirms rotator assignment in bench tracker
    - Engineering Manager notifies Tech Lead with expected start date and estimated bench window
    - Tech Lead identifies specific project scope for the rotator (which module, which open questions)
    - Tech Lead pre-provisions repo access, Slack channel invite, IDP entry access
    - Tech Lead selects one near-term in-demand skill the rotation will target for growth
    - Engineering Manager sends rotator the welcome message (template in Templates doc)
## 1.2 Day 1 — Kickoff

**Owner:** Rotator + Tech Lead


    - 30-minute kickoff call between rotator and tech lead
    - Tech Lead walks rotator through: project purpose, current state, open questions, chosen contribution scope
    - Tech Lead confirms the targeted in-demand skill for this rotation
    - Rotator confirms scope understanding
    - Rotator gets pointed to: repo, IDP entry, MVH package, knowledge/ directory, past retros
    - Rotator joins project Slack channel and introduces themselves
    - End of day: rotator has cloned repo and verified local environment runs
## 1.3 Day 2 — First Task

**Owner:** Rotator


    - Rotator picks first task from the project backlog (or accepts one assigned by tech lead)
    - Rotator opens EPAV /evaluate on the task
    - Rotator posts first progress note in project Slack channel
    - End of day: at least one commit or documented investigation
## 1.4 Day 5 — First Week Check-In

**Owner:** Rotator + Tech Lead


    - 15-minute check-in call
    - Rotator demos progress or discusses blockers
    - Tech Lead reviews rotator's MVH package baseline (should exist by end of week 1)
    - Confirm rotator is on track for their first shippable contribution
    - Adjust scope if week 1 revealed the task is too large or too small
## 1.5 Rotator Onboarding Complete When

    - Rotator has environment working
    - Rotator has first task in progress via EPAV
    - MVH package baseline created
    - Weekly check-in cadence established
    - Rotator knows which in-demand skill they're growing


# Section 2 — Rotator Active Period

The steady state during a rotation.

## 2.1 Weekly Rhythm for a Rotator

| Day | Activity |
|---|---|
| Monday | Attend bench standup (15 min); confirm this week's target with tech lead |
| Tuesday–Thursday | Execute EPAV cycles; commit progress; update task status |
| Friday | Update MVH package; post weekly progress note; flag any pull-to-client risk |

## 2.2 Progress Tracking

    - All work is tracked in the project's task management (whatever the org uses)
    - Rotator updates task status daily
    - MVH package updated weekly (Fridays) at minimum
    - Any blocker open more than 24 hours is flagged in Slack
## 2.3 Contribution Flow

    - Rotator completes task via EPAV
    - /validate passes
    - Pull request opened
    - Tech lead reviews (target: 24-hour review turnaround)
    - Rotator addresses review comments
    - Tech lead merges
    - Rotator posts completion note in project Slack
## 2.4 Blocker Escalation

| Blocker Duration | Escalation |
|---|---|
| < 24 hours | Rotator posts in project Slack; tech lead assists |
| 24–48 hours | Tech lead escalates to Engineering Manager |
| > 48 hours | Engineering Manager escalates to Head of Engineering; possible task reassignment |
| > 5 days | Task is unblockable at project level; consider project pause or re-scope |



# Section 3 — Rotator Offboarding (Planned)

Triggered when the rotator's bench window is ending with at least 3 days notice.

## 3.1 Day -3 (3 Days Before Rotation Ends)

**Owner:** Rotator + Tech Lead


    - Rotator confirms rotation end date to tech lead
    - Tech Lead decides: is this rotator's work finishing, or handing off to another rotator?
    - If handing off: identify incoming rotator (or mark project for future pickup)
    - Rotator begins wind-down; no new tasks started
## 3.2 Day -2

**Owner:** Rotator


    - Rotator completes final in-progress task or brings to a clean pause point
    - MVH package fully updated
    - Any open PRs merged or clearly labeled "in progress"
## 3.3 Day -1

**Owner:** Rotator + Tech Lead


    - Rotator creates or updates the Resumption Document (template in Templates doc)
    - Rotator writes retro entry in knowledge/retros/ covering: what shipped, what was learned, what's next, any gotchas
    - Skill growth captured in capability tracker (which in-demand skill grew and how)
    - 15-minute exit review with tech lead
## 3.4 Day 0 — Last Day

**Owner:** Rotator


    - Post final update in project Slack acknowledging contribution
    - Confirm handoff email/message sent to incoming rotator (if applicable)
    - Get recognition at next show-and-tell scheduled
## 3.5 Planned Offboarding Complete When

    - MVH package current
    - Retro entry written
    - Resumption document current
    - Skill growth logged
    - Incoming rotator identified (or project state marked "paused, ready for pickup")


# Section 4 — Rotator Offboarding (Unplanned Pull)

Triggered when a rotator is pulled to client work with less than 3 days notice — the more common scenario in outsourcing.

## 4.1 Emergency Handoff Protocol (< 24 hour notice)

**Owner:** Rotator + Tech Lead


**Within 4 hours of notification:**


    - Rotator notifies tech lead immediately
    - Tech lead assesses: what state is the work in?
    - Rotator stops in-progress task at nearest clean boundary (commit early, commit often)

**Within 24 hours (before rotator's last day on R&D):**


    - Rotator commits and pushes all work-in-progress with clear commit messages ("WIP: [task] — [state]")
    - Rotator updates MVH package with current state (even if incomplete)
    - Rotator writes short Resumption Document — bullet points only, minimum viable
    - Rotator writes quick retro entry in knowledge/retros/ — what was tried, what worked, what to avoid
    - Rotator posts final note in project Slack with @tech-lead tagged
    - Tech lead confirms receipt of handoff artifacts
## 4.2 Unplanned Offboarding Minimum Viable Handoff (MVH)

Even in a crisis pull, these are non-negotiable:


    - Current code committed and pushed
    - One-paragraph note on "what state is this in"
    - Contact info if any question arises (rotator is willing to answer 1-2 questions post-pull)

Anything beyond that is a bonus. The above is the *floor*.

## 4.3 Post-Pull: Tech Lead Actions

**Within 48 hours of rotator's pull:**


    - Tech lead reviews handoff artifacts
    - Tech lead decides: pick up the work themselves, reassign to another rotator, or pause the specific task
    - Tech lead updates project state in IDP if project is now short-staffed
    - If project is now unstaffed: mark project as Paused, create Resumption Doc
## 4.4 If No Handoff Was Possible

Sometimes the pull is so fast the rotator can't do handoff. In that case:


    - Tech lead runs git log to reconstruct rotator's last work
    - Tech lead writes the Resumption Doc themselves based on commits
    - Note in knowledge/retros/ that handoff was impossible — improvement item for the next rotator onboarding (add earlier MVH updates)


# Section 5 — Tech Lead Onboarding

Triggered when a new tech lead takes on an R&D project (new project, or replacing previous tech lead).

## 5.1 Tech Lead Selection Criteria

    - Senior engineer (3+ years relevant experience)
    - Currently on client work at ≤80% allocation OR post-bench transitioning back to client
    - Interested in the project domain
    - Comfortable reviewing others' work daily
    - Willing to commit 10–20% time (formal allocation, not "when free")
## 5.2 First-Week Onboarding for New Tech Lead

**Owner:** Head of Engineering + Previous Tech Lead (if replacement)

### Day 1

    - Head of Engineering briefs new tech lead on project purpose, current state, portfolio context
    - Formal time allocation documented (e.g., "20% Fridays + 1 hour daily") and communicated to their client team
    - Access provisioned: repo admin, IDP admin for the project, project Slack ownership
### Day 2–3

    - Deep-dive with previous tech lead (if replacement): architecture walkthrough, open questions, current rotators, known issues
    - Read the Resumption Doc, MVH package, and recent knowledge/retros/ entries
    - Meet each active rotator 1:1 (15 min each)
    - Meet the BU stakeholder(s) consuming the project's output
### Day 4–5

    - Attend weekly bench standup as project representative
    - Post introduction in project Slack
    - Do first tech lead review of an active PR
    - Confirm rotator assignments for the coming 2 weeks
## 5.3 Tech Lead Onboarding Complete When

    - Time allocation formalized
    - Rotator 1:1s done
    - First PR review completed
    - BU stakeholders identified and met
    - Coaching cadence set with Head of Engineering (biweekly for first 2 months)


# Section 6 — Tech Lead Transitions

Triggered when a tech lead needs to step down or hand off.

## 6.1 Common Triggers

    - Client engagement pulling their full time
    - Personal circumstances
    - Better tech lead candidate available
    - Project transitioning to a new phase requiring different expertise
## 6.2 Transition Protocol

**Ideal case (2+ weeks notice):**


    - Outgoing tech lead notifies Head of Engineering
    - Head of Engineering identifies replacement candidate
    - Overlap period: 2 weeks of joint operation
    - Outgoing tech lead runs Section 5 onboarding for incoming
    - Formal handoff at end of overlap (project state, key decisions pending, rotator status, stakeholder relationships)

**Short-notice case (< 1 week):**


    - Outgoing tech lead updates all project artifacts (MVH, Resumption Doc, tech decision log)
    - Head of Engineering steps in as interim tech lead
    - Head of Engineering runs replacement selection over 2–4 weeks
    - New tech lead onboards per Section 5 with Head of Engineering as previous-lead proxy

**Crisis case (immediate):**


    - Project marked Paused immediately
    - Head of Engineering owns Resumption Doc creation
    - Project resumes when new tech lead is assigned (may be weeks later)
    - Accept that scope may need refresh before resumption


# Section 7 — 20% Contributor Onboarding

Triggered when a non-bench engineer wants to contribute part-time to an R&D project.

## 7.1 Eligibility

    - Engineer's current client work must have capacity for 4–8 hours/week of R&D time
    - Engineer's manager approves the time commitment
    - Engineer picks ONE track (not multiple — prevents scattering)
    - Engineer commits to at least 8 weeks of engagement (below that, ramp-up cost exceeds contribution)
## 7.2 Onboarding Flow

### Week 1

    - Engineer expresses interest to their Engineering Manager
    - Engineering Manager confirms client-work capacity, approves the time
    - Engineer picks track and contacts that track's tech lead
    - Tech Lead confirms suitability and available contribution scope
    - Engineer added to project Slack, given repo access
### Week 2

    - Engineer completes lightweight version of Section 1 onboarding (Day 0, Day 1 kickoff, environment setup)
    - Engineer picks first small contribution (aim for 2–3 week completion)
    - First contribution shipped or shown to tech lead
## 7.3 20% Contributor Weekly Rhythm

    - No mandatory standup attendance (they have client standups)
    - Post weekly progress update in project Slack (Fridays)
    - Tech lead reviews contributions in normal PR flow
    - No MVH package requirement (contributions are self-contained enough)
## 7.4 20% Contributor Offboarding

Simpler than rotator offboarding:


    - Complete current contribution or hand off partial work with commit + note
    - Post departure note in project Slack
    - Contribution added to capability tracker


# Section 8 — Project Activation

Triggered when a new R&D project is being added to the portfolio.

## 8.1 Pre-Activation Checklist

Before a project can activate:


    - Project fits capacity-elastic model (Anchor / Tier 1 Parallel / Tier 2 Future)
    - Tech lead identified and committed
    - BU consumer identified and committed to using output
    - v1 scope defined (one-page spec)
    - At least 2 near-term in-demand skills coverage confirmed
    - Rotator capacity available (per capacity table in Program Plan)
    - Fits within active portfolio without displacing higher-priority projects
## 8.2 Activation Flow

**Week 1 of new project:**


    - Project registered as component in Backstage IDP with owner, tech lead, description
    - Repo created and scaffolded via toolkit initialization + /scaffold
    - knowledge/ directory initialized with project-specific rules and patterns
    - Initial task backlog created (EPAV task CSV)
    - Project Slack channel created and populated
    - Tech Lead onboarded per Section 5
    - First rotators identified for Week 2 start

**Week 2:**


    - First rotators onboarded per Section 1
    - First EPAV cycles running
    - Weekly cadence established
## 8.3 Activation Complete When

    - Project state is Active in IDP
    - Tech lead running weekly standups
    - MVH packages being maintained
    - First contribution merged (target: end of Week 3)


# Section 9 — Project Pause and Dormancy

Triggered when a project loses all active rotators (usually due to bench shrinkage).

## 9.1 Pause Protocol

**When last rotator is being pulled:**


    - Rotator completes offboarding per Section 3 or 4
    - Tech Lead reviews handoff artifacts, ensures Resumption Doc is current
    - Tech Lead updates project state in IDP: Active → Paused
    - Tech Lead posts pause notice in project Slack (channel stays open)
    - Project remains in portfolio, ready to resume
## 9.2 During Pause

    - Tech lead maintains project (light touch — no code work, but keeps IDP entry current)
    - Resumption Doc remains accessible
    - Any inbound BU questions handled by tech lead
    - No new work until resumption
## 9.3 Dormancy (60+ Days Paused)

    - Tech lead reviews project for scope refresh
    - May propose scope changes based on tech evolution
    - Update Resumption Doc with refreshed context
    - Project state remains Paused until resumption triggers
## 9.4 Resumption Protocol

**Triggered when rotator capacity becomes available:**


    - Head of Engineering + Tech Lead confirm project is next priority
    - Tech Lead does scope refresh if dormant > 60 days
    - New rotator picks up per Section 1 onboarding + reads Resumption Doc
    - Project state updated: Paused → Active
    - Resumption noted in knowledge/retros/


# Section 10 — Project Retirement

Triggered when a project is complete, abandoned, or superseded.

## 10.1 Retirement Reasons

    - Complete: v-final shipped, feature-complete, in production, no further R&D needed (moves to maintenance)
    - Superseded: newer approach makes this project obsolete
    - Abandoned: project failed to produce value, or scope proved wrong
## 10.2 Retirement Protocol

    - Head of Engineering approves retirement decision
    - Final retro written in knowledge/retros/ covering: what was learned, why retiring, what to preserve
    - Any reusable assets extracted and contributed to shared toolkit catalog
    - If Complete: project handed to maintenance owner (BU team, product team, etc.)
    - If Abandoned: honest post-mortem — what would we do differently
    - Project state updated: → Retired
    - Slack channel archived (not deleted; searchable history preserved)


# Section 11 — BU Consumer Onboarding

Triggered when a new BU wants to consume output from an existing R&D project.

## 11.1 Onboarding Flow

    - BU head contacts Head of Engineering or project tech lead
    - Requirements gathered: what output does the BU need, how often, in what format
    - Tech lead confirms scope fits existing project or requires new module
    - If new module: added to project's next-milestone planning
    - BU stakeholder invited to project Slack channel
    - Delivery mechanism configured (email list, chat channel, etc.)
    - First delivery scheduled
## 11.2 BU Feedback Loop

    - BU head is expected to give feedback within 2 weeks of first delivery
    - Ongoing feedback captured in project Slack or in a shared doc
    - Major feedback drives next-milestone scope
    - BU is a stakeholder for show-and-tells


# Appendix A — Quick Reference Card

Print this and pin it somewhere visible.


**When a rotator is joining:** Section 1 **When a rotator is leaving (planned):** Section 3 **When a rotator is being pulled unexpectedly:** Section 4 **When a new tech lead is starting:** Section 5 **When a tech lead is stepping down:** Section 6 **When a 20% contributor wants in:** Section 7 **When a new project is starting:** Section 8 **When a project needs to pause:** Section 9 **When a project is done:** Section 10 **When a new BU wants output:** Section 11

## Non-Negotiables (Do NOT skip, regardless of speed)

    - MVH package before any rotator exit — even 4 bullet points is better than nothing
    - Resumption Doc before project pause — the project can wait; the context can't be recovered later
    - Tech lead formal time allocation — "when they have time" fails; documented percentage succeeds
    - BU commitment before project activation — no committed consumer means no real project
    - Skill growth logged per rotation — the whole program is measured on this; don't skip capture
