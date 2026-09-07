# BENCH R&D PROGRAM

# OPERATIONS HANDBOOK

| Document Owner | Head of Engineering | Applies To | All R&D Projects |
|---|---|---|---|
| Review Cycle | Quarterly | Version | 1.0 |
| Related Docs | R&D Program Plan · Project Portfolio · Resource Lifecycle Playbook · Templates & Checklists |  |  |



# Purpose

This handbook covers how the R&D program runs day-to-day and month-to-month once resources are in place. It defines rhythms, communication channels, governance decisions, and reporting flows.


Use the Resource Lifecycle Playbook for people transitions. Use this handbook for the ongoing operation of the program itself.



# Section 1 — Weekly Rhythm

## 1.1 The Standard Week

| Day | Activity | Duration | Who |
|---|---|---|---|
| Monday | Bench standup (per project) | 15 min | All rotators + tech leads |
| Monday | R&D program sync | 30 min | Head of Engineering + tech leads |
| Tuesday–Thursday | Execution time | — | Rotators |
| Wednesday | Backlog health check (async) | 10 min | Head of Engineering |
| Friday | MVH package updates | 30 min | Each rotator |
| Friday | Weekly progress post (per project) | 5 min | Each tech lead |

## 1.2 Bench Standup Format (per Project)

15 minutes maximum. Format for each rotator:


    - What shipped since last standup
    - What's being worked on this week
    - Any blockers
    - Any pull-to-client risk this week

Tech lead facilitates. Head of Engineering attends anchor project standup weekly, parallels monthly.

## 1.3 R&D Program Sync

30 minutes. Head of Engineering + all tech leads.


Agenda:


    - Portfolio state review (5 min): active projects, paused projects, dormant
    - Bench capacity check (5 min): who's on bench, who's rolling off, incoming rotations
    - Cross-project blockers (10 min): anything requiring inter-project coordination
    - Skill coverage check (5 min): any in-demand skills currently uncovered?
    - Decisions needed (5 min): project activations, pauses, retirements


# Section 2 — Monthly Rhythm

## 2.1 Monthly R&D Portfolio Review

**When:** First Monday of each month **Duration:** 60 minutes **Attendees:** Head of Engineering, all tech leads, BU heads consuming R&D output


Agenda:


    - Portfolio state (15 min): each active project reports v-milestone progress
    - BU consumption review (15 min): which outputs are being used, what's needed next
    - Operational metrics (10 min): Section 8.1 metrics from bench framework
    - Portfolio adjustments (15 min): activation/pause/retirement decisions
    - Skill gap review (5 min): are we covering the in-demand skills list?
## 2.2 Monthly Show-and-Tell

**When:** Last Friday of each month **Duration:** 30 minutes **Attendees:** Open to all engineering; BU heads invited


Format:


    - Each project that shipped meaningful work in the last month demos
    - 5 minutes per project
    - Contributors named explicitly
    - Recording posted for anyone who missed

**Purpose is recognition, not status reporting.** Keep it energetic. Executives should occasionally attend to see the humans behind the outputs.

## 2.3 Monthly BU Consumption Report

**When:** Last day of month **Format:** Async written report **Author:** Head of Engineering


Covers:


    - Which R&D outputs each BU consumed this month
    - Any feedback received
    - Any new BU requests
    - Consumption trend (up/flat/down per output)


# Section 3 — Quarterly Rhythm

## 3.1 Quarterly Executive Report

Uses the Bench Framework Section 8.3 template. Delivered to executive leadership.


Prepared by Head of Engineering in the last two weeks of each quarter. Contents:


    - Bench volume and conversion rate
    - Strategic output produced (assets, products, capabilities)
    - Key deliverables shipped
    - Reusable assets contributed to the toolkit catalog
    - Capability uplift (engineers moved tiers, tech leads developed)
    - Near-term in-demand skills coverage (per Program Plan Section 1A-2)
    - Pipeline enablement
    - Estimated future delivery savings
    - Next quarter outlook
## 3.2 Quarterly Portfolio Rebalance

**When:** First month of each quarter **Duration:** 90 minutes **Attendees:** Head of Engineering, BU heads, Presales lead, L&D lead


Agenda:


    - Portfolio state review with fresh eyes
    - Pipeline signals from presales — which skills are in demand for coming engagements?
    - Skill list refresh — is the in-demand skills list still accurate?
    - Project priority rebalance — which projects move up, down, retire, or activate
    - Wave planning — what's next for the coming quarter
## 3.3 Quarterly Skill List Review

The Near-Term In-Demand Skills list (Program Plan Section 1A-2) is reviewed every quarter (formal review every 6 months, lightweight check quarterly).


Inputs:


    - Job market data
    - Presales pipeline signals
    - Client RFP patterns
    - Salary premium trends
    - Emerging tech that gained traction

Outputs:


    - Confirmed skill list for the coming quarter
    - Any skills added or removed
    - Any portfolio adjustments needed to cover new gaps


# Section 4 — Communication Channels

## 4.1 Channel Purposes

| Channel | Purpose | Frequency |
|---|---|---|
| Project-specific Slack channels | Day-to-day project work | Continuous |
| #rd-program general Slack channel | Cross-project communication, announcements | Daily |
| #rd-showcase Slack channel | Celebrating shipped work, share-outs | Weekly |
| Backstage IDP | Project state, ownership, catalog | Always current |
| Task management tool | Individual task tracking | Continuous |
| Email | Formal announcements only | Rare |
| BU consumer channels | Delivery of R&D output | Per project cadence |

## 4.2 Communication Norms

    - Async first: written updates preferred over meetings for status
    - Meetings are for decisions: if it's just status, do it in Slack
    - Public over private: default to project Slack channel over DMs so context is preserved
    - Assume everything gets picked up: anyone reading the project channel should be able to catch up
    - Recognition is public: thank contributors in channels where their peers see it
## 4.3 Standard Message Patterns

    - Weekly progress post (tech lead): what shipped, who contributed, what's next
    - Blocker escalation (rotator): what's blocked, what I've tried, what help I need
    - BU delivery notification: what was delivered, when, who to contact for questions

Templates for each in the Templates doc.



# Section 5 — Governance in Practice

## 5.1 Decision Rights

| Decision | Owner | Consulted |
|---|---|---|
| Project activation | Head of Engineering | Tech lead, BU head |
| Project pause | Head of Engineering | Tech lead |
| Project retirement | Head of Engineering | Tech lead, BU head |
| Rotator assignment to project | Engineering Manager | Tech lead |
| Task assignment within project | Tech lead | Rotator |
| Tech lead selection | Head of Engineering | Engineering Manager |
| Scope changes within v1 | Tech lead | BU head |
| Major scope changes (v1→v2) | Head of Engineering | Tech lead, BU head |
| Skill list updates | Head of Engineering | L&D, Presales |
| Portfolio priority order | Head of Engineering | BU heads, Presales |

## 5.2 Escalation Paths

    - Rotator issue: Rotator → Tech Lead → Engineering Manager → Head of Engineering
    - Project issue: Tech Lead → Head of Engineering
    - BU relationship issue: Tech Lead → Head of Engineering → BU Head
    - Cross-project conflict: Tech Leads → Head of Engineering
    - Executive concern: Head of Engineering → Executive Sponsor
## 5.3 What Requires Written Documentation

    - Project activation (one-page spec)
    - Project pause (Resumption Doc)
    - Project retirement (final retro)
    - Tech lead selection (short justification memo)
    - Skill list updates (before/after)
    - Portfolio rebalance decisions (meeting minutes)

Everything else can be Slack-only.



# Section 6 — Metrics and Tracking

## 6.1 Operational Metrics (from Bench Framework Section 8.1)

Tracked by Head of Engineering, reviewed monthly:


| Metric | Target | Where Tracked |
|---|---|---|
| Bench Activation Time | < 24 hours | Bench tracker |
| Milestone Completion Rate | 80%+ | Project trackers |
| Output Rate | 70%+ | Project trackers |
| Handoff Success Rate | 80%+ | Post-handoff review |
| Backlog Readiness | 10+ items | Backlog page |
| Upskilling Conversion Rate | 60%+ | Capability tracker |

## 6.2 Strategic Metrics (from Bench Framework Section 8.2)

Tracked by Head of Engineering, reviewed quarterly:


    - Bench Hours Converted to IP
    - Estimated Future Delivery Savings
    - Sales Pipeline Enablement
    - Capability Uplift
    - Bench-to-Billable Ratio
## 6.3 Program-Specific Metrics

Additional metrics for the R&D program:


| Metric | Target | Cadence |
|---|---|---|
| Active projects in portfolio | Anchor + 1–3 parallels | Continuous |
| Project pause-to-resumption ratio | Most paused projects resume within 90 days | Quarterly |
| Rotator skill uplift rate | 80%+ log measurable in-demand skill growth | Per rotation |
| Portfolio in-demand skill coverage | 100% of listed skills have active coverage | Monthly |
| Contribution track velocity | 2+ contributions merged monthly | Monthly |
| BU consumption breadth | 4+ BUs consuming R&D output within 6 months | Quarterly |



# Section 7 — Common Operational Scenarios

## 7.1 "A rotator has been on bench for 3 days without an assignment"

    - Head of Engineering intervenes directly (this violates the 24-hour activation rule)
    - Root cause: usually a backlog gap or a tech lead capacity issue
    - Fix: assign to any Ready item in the backlog, even if not perfectly matched
    - Log the incident for the monthly ops review
## 7.2 "A tech lead is overwhelmed"

    - Signals: slow PR reviews (> 48 hours), missed weekly posts, rotators reporting blockers
    - Head of Engineering has 1:1 with tech lead
    - Options: reduce project scope, add a co-lead from active seniors, temporarily pause the project
    - Never: leave the tech lead overwhelmed while adding more rotators
## 7.3 "The BU consumer stops using an output"

    - Tech lead reaches out to BU head within 1 week of the drop
    - Possible causes: output no longer relevant, quality issue, delivery friction, BU turnover
    - If output no longer relevant: candidate for project retirement or pivot
    - If quality issue: fix immediately, high priority
    - Always root-cause; never assume BUs will complain proactively
## 7.4 "A parallel project is falling behind schedule"

    - Tech lead flags at monthly portfolio review
    - Options: reduce v1 scope, extend timeline, or pause project
    - Never: silently let it drift; visibility drops when other projects ship
    - If pattern: review if this project should have been activated at all
## 7.5 "Bench suddenly shrinks; multiple parallels have no rotators"

    - Follow capacity rules: anchor keeps its rotators; all parallels pause
    - Pause protocol per Resource Lifecycle Playbook Section 9
    - Tech leads maintain project state during pause
    - Resume when capacity returns
## 7.6 "A rotator wants to grow a specific skill but the current backlog doesn't cover it"

    - Engineering Manager notes the request
    - If it's an in-demand skill with no coverage: this is a portfolio gap
    - Consider activating a new track that covers it
    - If not in-demand: fold into upskilling framework (Bench Framework Section 7) instead
## 7.7 "A tech lead disagrees with the Head of Engineering on priorities"

    - Discussion happens in the monthly portfolio review, not in ad-hoc chats
    - Data wins: bring metrics, BU feedback, skill coverage analysis
    - Head of Engineering has final call but explains reasoning
    - Disagreement, once resolved, is committed to publicly


# Section 8 — Program Health Checks

## 8.1 Monthly Health Check (Head of Engineering, async)

Ask these questions monthly:


    - Is the anchor project on track for its next milestone?
    - Are all active projects producing MVH-updated work weekly?
    - Have any projects been paused > 60 days without resumption planning?
    - Is bench conversion rate trending correctly?
    - Are BU heads consuming R&D output actively?
    - Is the in-demand skills list still fully covered?
    - Are tech leads showing signs of overload?
    - Are rotators reporting positive rotation experiences?

Any "no" answer is an intervention trigger.

## 8.2 Quarterly Program Retrospective

**When:** Last week of each quarter **Attendees:** Head of Engineering, all tech leads, sample of past rotators


Format:


    - What went well this quarter (30 min)
    - What didn't (30 min)
    - What we'll change next quarter (30 min)

Output: 3–5 concrete process improvements for the next quarter, added to the operations handbook.

## 8.3 Annual Program Assessment

**When:** End of program year **Attendees:** Head of Engineering, executive sponsor, BU heads, sample of engineers


Format: full review against the Program Plan's Section 1E "What Success Looks Like" criteria.


Output: annual report, updated Program Plan for next year, communicated broadly.



# Appendix A — Meeting Cadence Summary

| Meeting | Cadence | Duration | Attendees |
|---|---|---|---|
| Per-project bench standup | Weekly | 15 min | Project team |
| R&D program sync | Weekly | 30 min | HoE + tech leads |
| Monthly R&D portfolio review | Monthly | 60 min | HoE + tech leads + BU heads |
| Monthly show-and-tell | Monthly | 30 min | Open |
| Quarterly executive report | Quarterly | Async | HoE → Execs |
| Quarterly portfolio rebalance | Quarterly | 90 min | HoE + BU heads + Presales + L&D |
| Quarterly program retrospective | Quarterly | 90 min | HoE + tech leads + rotators |
| Annual program assessment | Annually | 2 hours | HoE + Execs + BUs + engineers |

## Total leadership time commitment

    - Head of Engineering: ~4 hours/week on program operations
    - Each tech lead: ~30 min/week on program-level activity (in addition to their project work)
    - BU heads: ~1 hour/month
    - Engineering Managers: ~2 hours/week during active rotations

Keep it lightweight. Meeting bloat is a program death sentence.
