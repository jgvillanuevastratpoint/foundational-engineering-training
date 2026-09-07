# BENCH R&D PROGRAM

# TEMPLATES & CHECKLISTS

| Document Owner | Head of Engineering | Applies To | All R&D Projects |
|---|---|---|---|
| Review Cycle | Quarterly | Version | 1.0 |
| Related Docs | R&D Program Plan · Project Portfolio · Resource Lifecycle Playbook · Operations Handbook |  |  |



# Purpose

Copy-paste templates and checklists for common R&D program activities. This doc is reference-only — look up what you need, use it, move on.


Templates use [BRACKETS] for placeholders. Replace them.



# Table of Contents

**Onboarding Templates**


    - T1: Rotator Welcome Message
    - T2: Rotator Day 1 Kickoff Agenda
    - T3: 20% Contributor Welcome Message
    - T4: New Tech Lead Onboarding Briefing

**Handoff & Exit Templates**


    - T5: Minimum Viable Handoff (MVH) Package
    - T6: Resumption Document
    - T7: Retro Entry
    - T8: Emergency Handoff (Unplanned Pull)

**Project Templates**


    - T9: v1 Project Spec (One-Page)
    - T10: Project Activation Announcement
    - T11: Project Pause Notice
    - T12: Project Retirement Notice

**Communication Templates**


    - T13: Weekly Progress Post (Tech Lead)
    - T14: Blocker Escalation Post (Rotator)
    - T15: BU Delivery Notification
    - T16: Show-and-Tell Slot Structure

**Governance Templates**


    - T17: Monthly Portfolio Review Agenda
    - T18: Quarterly Executive Report Structure
    - T19: Contribution Acceptance Checklist
    - T20: Skill Growth Log Entry


# T1: Rotator Welcome Message

Sent by Engineering Manager on Day 0 (before rotation starts).


Hi [ROTATOR NAME],


You're joining the [PROJECT NAME] R&D project starting [DATE]. Expected

duration is [ESTIMATED WINDOW], though this may change based on client

demand.


What to expect on Day 1:

- 30-min kickoff call with [TECH LEAD NAME] at [TIME]

- Repo, IDP, and Slack access already provisioned

- First task to pick up from the project backlog


This rotation is targeting growth in [IN-DEMAND SKILL]. By the end,

you should have hands-on experience in this area.


Read before Day 1:

- Project overview: [IDP LINK]

- Current state of work: [MVH LINK]

- Recent retros: [RETRO DIRECTORY LINK]


Any questions before you start, ping me directly.


[ENGINEERING MANAGER NAME]

- 

# T2: Rotator Day 1 Kickoff Agenda

30 minutes. Tech Lead facilitates.


1. Project context (5 min)

   - What this project does

   - Who consumes the output

   - Where it fits in the R&D portfolio


2. Current state (5 min)

   - What's shipped

   - What's in progress

   - What's blocked


3. Your scope (10 min)

   - Which module / open question you're picking up

   - Expected v-milestone by end of rotation

   - Targeted in-demand skill for growth


4. Practical setup (5 min)

   - Repo access confirmed

   - Environment runs locally (verified together if possible)

   - EPAV workflow refresher if needed


5. Cadence and communication (5 min)

   - Weekly standup: [DAY/TIME]

   - Weekly check-in with me: [DAY/TIME]

   - Slack channel norms

   - When to escalate blockers

- 

# T3: 20% Contributor Welcome Message

Sent by Tech Lead when a non-bench engineer joins as 20% contributor.


Hi [CONTRIBUTOR NAME],


Welcome to [PROJECT NAME] as a 20% contributor. Glad to have you.


Time commitment: 4–8 hours per week, whatever fits alongside your

client work. Post updates on Fridays.


Your first contribution: [SPECIFIC SCOPE]. Aim to ship this within

[TIMELINE].


Read to get started:

- Project overview: [IDP LINK]

- Current state: [MVH LINK]


You don't need to attend the daily bench standup. Just post weekly

progress in [PROJECT SLACK CHANNEL].


Ping me anytime with questions.


[TECH LEAD NAME]

- 

# T4: New Tech Lead Onboarding Briefing

Delivered verbally or in writing by Head of Engineering during Day 1 of tech lead onboarding.


Project: [NAME]

Tier: [Anchor / Tier 1 Parallel / Tier 2]


Purpose:

[One paragraph on why this project exists and what it produces]


Portfolio context:

[How this project fits with other active R&D projects]


BU consumer(s):

[Who uses the output and how]


Current state:

- Active rotators: [NAMES + focus areas]

- v-milestone in progress: [MILESTONE]

- Key decisions pending: [LIST]

- Known issues: [LIST]


Your time commitment:

[Formal % allocation, e.g., "20% Fridays plus 1 hour daily"]


Your primary responsibilities:

- Own delivery of v-milestones

- Review rotator PRs within 24 hours

- Maintain project state in IDP

- Coach rotators on EPAV workflow

- Attend weekly R&D program sync


Coaching cadence:

Biweekly 30-min 1:1 with me for the first 2 months.


Success indicators for you in the first 30 days:

- All active rotators feel unblocked

- First v-milestone still on track

- MVH packages current

- BU stakeholders have met you

- 

# T5: Minimum Viable Handoff (MVH) Package

The living document maintained by every rotator. Updated weekly and before any exit.


# MVH Package — [PROJECT NAME] — [ROTATOR NAME]


## 1. Overview

[One paragraph: what this work is, why it exists, what problem it solves.]


## 2. Architecture & Design Decisions

[How the system is structured, what key decisions were made, and why.

Reference any ADRs.]


## 3. Environment Setup

[Step-by-step instructions for a new engineer to run this locally.

List all required env vars (without values). Include seed data steps.]


## 4. Current State

[Exactly what's working today, what's partially implemented, what's not started.]


## 5. Open Decisions

[Technical choices deferred. For each: options considered, current

recommendation, additional info needed.]


## 6. Next Steps

[Prioritized task list for the next engineer. Order = priority, not

order of discovery.]


## 7. Known Issues & Technical Debt

[Bugs, edge cases, shortcuts, workarounds and why they exist.]


---

Last updated: [DATE]

Updated by: [NAME]

- 

# T6: Resumption Document

Created when a project is being paused. Attached to the project IDP entry.


# Resumption Document — [PROJECT NAME]


## Project State at Pause

- Date paused: [DATE]

- Last active rotator: [NAME]

- Last tech lead: [NAME]

- Reason for pause: [Bench shrinkage / client pull / other]


## Where We Left Off

[2–3 sentences on what state the project is in]


## Immediate Next Steps for Returning Contributor

1. [First action]

2. [Second action]

3. [Third action]


## Decisions Pending

[Any technical or scope decisions that were deferred and need to be

made before further work continues]


## Context a Returning Contributor Must Know

[Anything that isn't obvious from the repo or MVH but is critical]


## Contacts

- Previous tech lead (for questions): [NAME + how to reach]

- BU consumer(s): [NAMES]


## Scope Refresh Check

If reading this doc more than 60 days after the pause date, do a scope

refresh before resuming — technology may have moved, requirements may

have shifted.

- 

# T7: Retro Entry

Added to knowledge/retros/ when a rotator exits or a milestone completes.


# Retro — [PROJECT NAME] — [DATE]


## Context

[Brief: what you were working on, over what period]


## What Shipped

[Concrete outputs, PRs merged, features working]


## What Was Learned

[Non-obvious things you discovered — technical, process, or domain]


## What Worked Well

[Approaches, patterns, or tools that turned out to be right choices]


## What Didn't Work

[Approaches you abandoned and why — save the next person the time]


## Skill Growth

[Which in-demand skill did this work develop? Be specific.]


## Recommendations for Next Contributor

[If you were briefing your replacement, what would you tell them?]


## Candidates for Promotion to Patterns

[If any part of this work should become a reusable pattern in

knowledge/patterns/, name it here so the tech lead can promote it]


---

Rotator: [NAME]

- 

# T8: Emergency Handoff (Unplanned Pull)

Minimum viable version when you have < 24 hours notice of being pulled.


# Emergency Handoff — [PROJECT NAME] — [DATE]


## What I was doing

[One sentence]


## Where the code is

- Branch: [NAME]

- Last commit: [HASH]

- State: [Working / Broken / Half-done]


## What's the next step

[One bullet]


## Watch out for

[Any critical thing that would trip up whoever picks this up]


## Reachable for questions

[Yes/No — and if yes, best channel]


---

Rotator: [NAME]

Pulled to: [CLIENT PROJECT]

- 
That's the floor. Anything more is bonus. Do NOT skip this even in a crisis pull.



# T9: v1 Project Spec (One-Page)

Required before a project can activate.


# Project v1 Spec — [PROJECT NAME]


## Purpose

[One sentence: what problem does this solve, for whom?]


## Tier

[Anchor / Tier 1 Parallel / Tier 2 Future]


## v1 Scope

- [Core capability 1]

- [Core capability 2]

- [Core capability 3]

- [Core capability 4]


## v1 Timeline

[Duration + weekly milestones]


## Team

- Tech Lead: [NAME]

- Rotators: [Expected count + discipline mix]


## Near-Term In-Demand Skills Covered

- [Skill 1 from Program Plan Section 1A-2]

- [Skill 2]

- [Skill 3]


## BU Consumer Commitment

- Primary consumer: [BU HEAD NAME]

- What they've committed to: [Specific usage]

- First delivery expected: [DATE]


## Success Criteria for v1

[Concrete, testable — how do we know v1 is done?]


## Dependencies

[Anything that must exist before this can start]


## Sign-off

- BU Head: [NAME] — [DATE]

- Tech Lead: [NAME] — [DATE]

- Head of Engineering: [NAME] — [DATE]

- 

# T10: Project Activation Announcement

Posted in #rd-program channel when a new project activates.


🚀 New R&D project activating: [PROJECT NAME]


Tier: [Tier]

Tech Lead: [NAME]

BU Consumer: [BU]

Target v1 date: [DATE]


What it does:

[1–2 sentences]


Skills this rotation builds:

[Named in-demand skills]


Rotator interest? Ping [ENGINEERING MANAGER] to be considered for

upcoming rotations on this project.


Project details: [IDP LINK]

Project channel: [SLACK LINK]

- 

# T11: Project Pause Notice

Posted in project Slack channel and #rd-program channel when a project pauses.


⏸️ Project pause: [PROJECT NAME]


As of [DATE], [PROJECT NAME] is entering a paused state. No active

rotators until further notice.


State at pause: [1 sentence]

Resumption doc: [LINK]

Reason: [Bench shrinkage / client demand / other]


The project remains in the portfolio and is ready to resume when

capacity returns. Channel stays open.


For BU consumers: [any impact on delivery, if applicable]


Contact for questions: [TECH LEAD]

- 

# T12: Project Retirement Notice

Posted when a project retires.


🏁 Project retirement: [PROJECT NAME]


After [DURATION], [PROJECT NAME] is being retired.


Reason: [Complete / Superseded / Abandoned]


What we shipped:

- [Key output 1]

- [Key output 2]

- [Key output 3]


What we learned:

[Link to final retro]


Reusable assets extracted:

[Link to contributions in shared toolkit catalog]


Contributors:

[List all rotators, tech leads, 20% contributors]


Thank you to everyone who worked on this project.


If Complete: Handover to [MAINTENANCE OWNER]

Slack channel: archived (searchable history preserved)

- 

# T13: Weekly Progress Post (Tech Lead)

Every Friday, in the project Slack channel.


📅 Week of [DATE] — [PROJECT NAME]


Shipped this week:

- [PR/feature/asset 1] — by [CONTRIBUTOR]

- [PR/feature/asset 2] — by [CONTRIBUTOR]


In progress:

- [Item] — [CONTRIBUTOR] — [status]

- [Item] — [CONTRIBUTOR] — [status]


Blockers:

- [None / Item + escalation status]


Coming next week:

- [Milestone or target]


Pull-to-client risk (rotators leaving next week):

- [None / NAME — leaving DATE]


MVH status: [All current / NAME needs update]

- 

# T14: Blocker Escalation Post (Rotator)

When a rotator hits a blocker they can't resolve.


🚧 Blocker — [PROJECT NAME]


What I'm trying to do:

[One sentence]


What's blocking me:

[Specific problem]


What I've tried:

- [Attempt 1]

- [Attempt 2]


What I think I need:

[Specific help — a person, a decision, an access, a tool]


Impact if unblocked today: [What I can ship this week]

Impact if not unblocked: [What slips]

- 

# T15: BU Delivery Notification

When R&D output is delivered to a BU consumer.


📊 [PROJECT NAME] — [DELIVERABLE] delivered


To: [BU HEAD + team]

Delivered: [DATE]

What's included: [Brief description]


How to access: [LINK / attachment / channel]


Feedback: reply in this channel or reach out to [TECH LEAD].


Next delivery: [DATE]

- 

# T16: Show-and-Tell Slot Structure

Each project's demo slot in the monthly show-and-tell.


5 minutes total:


1. What we built (1 min)

   [Very brief context — assume the audience doesn't know the project]


2. Demo (3 min)

   [Live or recorded — show it working]


3. Who contributed (30 sec)

   [Name every contributor since last show-and-tell]


4. What's next (30 sec)

   [Next v-milestone or shift in scope]


No slides longer than 2. Demo > slides. Names > logos.

- 

# T17: Monthly Portfolio Review Agenda

60 minutes. Head of Engineering runs.


1. Portfolio state (15 min)

   For each active project (5 min each):

   - v-milestone progress

   - Rotator status

   - Blockers

   - BU consumption


2. BU consumption review (15 min)

   Each BU head reports on which outputs they used, feedback,

   new asks


3. Operational metrics (10 min)

   Bench framework Section 8.1 metrics; discuss any red flags


4. Portfolio adjustments (15 min)

   Activations, pauses, retirements to decide


5. Skill coverage check (5 min)

   Any near-term in-demand skills currently uncovered

- 

# T18: Quarterly Executive Report Structure

Uses Bench Framework Section 8.3 template with R&D additions.


# R&D Program — Quarterly Report — [QUARTER]


## 1. Bench Volume

[Total bench engineer-months this quarter, by business unit]


## 2. Bench Conversion

[Hours to strategic output vs total bench hours, % and trend]


## 3. Key Deliverables Shipped

[Top 3–5 outputs with business description]


## 4. Reusable Assets Contributed

[Contributions to shared toolkit catalog this quarter]


## 5. Capability Uplift

[Engineers moved billability tiers; tech leads developed;

in-demand skill coverage growth]


## 6. Near-Term In-Demand Skills Status

[List of skills, coverage status, any gaps closed or opened]


## 7. Pipeline Enablement

[POCs, demos, sales assets produced from R&D]


## 8. Estimated Savings

[Projected future delivery cost reduction from assets produced]


## 9. Next Quarter Outlook

[Anticipated bench volume; planned project activations; expected outputs]


## 10. Asks / Risks

[Anything requiring executive input or intervention]

- 

# T19: Contribution Acceptance Checklist

Used by tech leads reviewing rotator or contributor contributions.


Before merging a contribution:


- [ ] EPAV `/validate` passes

- [ ] Code review approved by tech lead

- [ ] Working example demonstrating the contribution's value

- [ ] Documentation included (how to use it, when to use it)

- [ ] Tested on at least one real repository (client or internal)

- [ ] Follows the project's rules in `knowledge/rules/`

- [ ] If it's a reusable pattern candidate — flagged for promotion

- [ ] Contributor named in commit and PR

- [ ] Registered in shared toolkit catalog (if applicable)

- [ ] Any relevant retros written

- 

# T20: Skill Growth Log Entry

Captured at rotator exit. Fed into capability tracker.


Rotator: [NAME]

Project: [NAME]

Rotation dates: [START] to [END]

Discipline: [Software / Data / DevOps]


## Targeted skill for this rotation

[Specific in-demand skill from Program Plan Section 1A-2]


## Concrete work done in that skill area

[What they actually built or contributed that grew this skill]


## Growth evidence

[Not "worked on X" — actual evidence: shipped feature, merged pattern,

etc.]


## Billability tier impact

[Does this rotation qualify them for a higher tier? What certification

or capability level does this now unlock?]


## Manager confirmation

[Engineering Manager sign-off that this growth is real]

- 

# Appendix — When to Use Each Template

| Situation | Template |
|---|---|
| Bench engineer starting rotation next week | T1, T2 |
| Non-bench engineer wants to contribute 20% | T3 |
| New tech lead starting on a project | T4 |
| Weekly MVH update | T5 |
| Project entering pause | T6, T11 |
| Rotator ending planned rotation | T7 (retro) |
| Rotator pulled emergency to client | T8 |
| Proposing a new project | T9 |
| Announcing new project activation | T10 |
| Retiring a completed project | T12 |
| Friday tech lead post | T13 |
| Rotator hits a blocker | T14 |
| Sending deliverable to BU | T15 |
| Preparing show-and-tell slot | T16 |
| Running monthly portfolio review | T17 |
| Preparing quarterly exec report | T18 |
| Reviewing a PR/contribution | T19 |
| Capturing rotator skill growth | T20 |
