# Engineering Enablement Framework

## Bench & R&D Learning Program — Data · Cloud · DevOps · Software

**Owner:** Head of Engineering **Audience:** Engineers between billable engagements (bench) and dedicated R&D staff **Duration:** 12 weeks per cohort (part-time compatible; full-time preferred for bench) **Version:** 1.0 draft



## 1. Philosophy

Five principles govern every decision in this program. If a proposal violates one, it doesn't ship.


    - Producer, not consumer. Every hour of learning ends with an artifact someone else can use — code, a doc, a diagram, an exercise. Reading and watching alone don't count as progress.
    - Compounding library. Capstones become the next cohort's raw material. Cohort 5 learns from cohorts 1–4. The program gets more valuable every quarter without more of the leader's time.
    - Real problems, not toy problems. Use cases are sourced from the actual client backlog, internal tooling gaps, or the R&D roadmap. No fictional "ACME Corp" scenarios.
    - T-shape enforced. A shared core (Phase 0) prevents specialists who can't talk to each other. Data engineers who can't read Terraform and DevOps engineers who can't write a dbt model are program failures.
    - Bench time is a resource, not a vacation — but not a squeeze either. Cadence is real (weekly checkpoints, hard deadlines), but pace respects the fact that bench engineers may be reassigned mid-program. Modules are designed to be resumable.


## 2. Program Structure

Twelve weeks, four phases, all tracks share the same skeleton.


| Phase | Weeks | Focus | Output |
|---|---|---|---|
| 0 — Foundations | 1–2 | Shared core, all tracks together | Baseline competency check |
| 1 — Track Fundamentals | 3–6 | Track-specific depth | 3 graded exercises per track |
| 2 — Applied Projects | 7–9 | Guided real-world work | 1 working system, code-reviewed |
| 3 — Capstone | 10–12 | Use case + training module | 2 artifacts (see §5) |


**Cadence:**


    - Daily: Async standup post (3 lines: yesterday, today, blockers) in the cohort channel.
    - Weekly: 60-min demo/checkpoint per track. Mentor + peers attend.
    - Bi-weekly: Cross-track show-and-tell. 15 min per track. Builds the T-shape.
    - End of phase: Formal review with rubric (see §6).


## 3. Phase 0 — Shared Core (2 weeks)

Every engineer, regardless of track, must complete this. It's the language the rest of the program is written in.

### Modules

    - Git & Code Review Discipline — trunk-based dev, PR hygiene, semantic commits, review as teaching.
    - Linux & Networking Basics — shell fluency, systemd, DNS, TLS, HTTP/2, TCP basics. If you can't curl -v an endpoint and explain what happened, you're not ready.
    - Containers — Docker fundamentals, multi-stage builds, image size discipline, running one thing well in a container.
    - Observability 101 — the three pillars, structured logging, why metrics ≠ logs ≠ traces.
    - Security Hygiene — secret management, OIDC vs static credentials, principle of least privilege, the difference between "it works" and "it's safe." (Reference case study: the 2025 GitLab compromise → OIDC federation migration.)
    - AI-Assisted Development — how to prompt, review, and reject AI-generated code. Where AI belongs in your workflow and where it doesn't.
    - Technical Writing — the READMEs, ADRs, and runbooks you're expected to produce. Bad docs are worse than no docs.
### Baseline check (end of Phase 0)

A single practical exercise: containerize a small service, deploy it locally, wire structured logs and one metric, write the README, submit as a PR. Reviewed against a rubric. Pass or repeat.



## 4. Tracks

Each track runs Phases 1–3 in parallel, with cross-track sync every two weeks.

### 4.1 Data Engineering Track

**Learning outcomes.** By week 12, the engineer can design, build, and operate a production-grade batch or streaming pipeline; model data for a warehouse; instrument quality checks; and articulate trade-offs between orchestration platforms.


**Phase 1 modules (weeks 3–6):**


    - Ingestion patterns: batch, micro-batch, streaming, CDC
    - Storage layers: warehouses, lakes, lakehouses (Snowflake / BigQuery / Postgres / Iceberg)
    - Transformation: SQL depth, dbt fundamentals, testing
    - Orchestration: n8n as reference (aligned with existing curriculum), plus one of Airflow / Dagster / Prefect for comparison
    - Data quality & lineage: Great Expectations or equivalent
    - Metrics layer / semantic modeling

**Phase 2 applied project:** Build an end-to-end pipeline against a real internal or public dataset. Must include: ingestion, transformation, quality checks, orchestration, one dashboard.


**Capstone use case options:** client-billable data platform starter, internal metrics warehouse, OpsAI data pipeline module, ETL migration reference.



### 4.2 Cloud Engineering Track

**Learning outcomes.** Design a multi-account AWS landing zone, write production-grade Terraform, implement OIDC-based CI federation, and defend architectural decisions against cost, security, and operability criteria.


**Phase 1 modules (weeks 3–6):**


    - Terraform in depth: modules, remote state, workspaces, drift management
    - AWS networking: VPCs, subnets, TGW, PrivateLink, endpoint patterns
    - Identity & access: IAM policies, permission boundaries, OIDC federation, SCPs
    - Multi-account patterns: Control Tower, Organizations, landing zones
    - Cost visibility: tagging strategy, Cost Explorer, budgets, anomaly detection
    - Security controls: GuardDuty, CloudTrail, Security Hub, Config
    - Zero-trust primitives

**Phase 2 applied project:** Provision a small multi-account landing zone from scratch. Must include: baseline guardrails, OIDC-federated CI, centralized logging, one workload deployed via IaC.


**Capstone use case options:** Stratpoint landing zone template v2, client onboarding accelerator, security transformation playbook, cost governance framework.



### 4.3 DevOps / Platform Track

**Learning outcomes.** Own a CI/CD platform, run containers in production, implement GitOps, build an observability stack, and lead an incident from detection to postmortem.


**Phase 1 modules (weeks 3–6):**


    - CI/CD pipeline design: GitHub Actions / GitLab CI patterns, caching, matrix builds
    - Container orchestration: Kubernetes fundamentals or ECS, whichever the primary client stack uses
    - GitOps: ArgoCD or Flux, environment promotion
    - Observability stack: OpenTelemetry, Prometheus, Grafana, Loki/Tempo
    - Progressive delivery: canary, blue/green, feature flags
    - Incident response: on-call, alerting hygiene, runbook writing, blameless postmortems
    - Self-hosted infrastructure patterns (Coolify, Hetzner) as a low-cost lab environment

**Phase 2 applied project:** Build a platform starter kit — a repo a new project can fork and be in production in a day. Pipelines, observability, deployment, docs.


**Capstone use case options:** Platform starter kit v2, iOS CI/CD with TestFlight + Proxmox macOS runners, incident response playbook, developer portal MVP.



### 4.4 Software Engineering Track

**Learning outcomes.** Design and ship maintainable services, apply testing strategy across the pyramid, make principled framework and language choices, and integrate AI assistance into daily engineering work.


**Phase 1 modules (weeks 3–6):**


    - API design: REST, GraphQL, tRPC, versioning, error models
    - Testing strategy: unit → integration → contract → E2E; when each pays off
    - Design patterns for maintainability: hexagonal architecture, dependency inversion, feature slices
    - Performance & profiling: language-appropriate tools, common bottlenecks
    - AuthN/AuthZ patterns: OAuth flows, session vs token, RBAC vs ABAC
    - AI-augmented workflows: pair-programming with LLMs, spec-driven generation, review discipline
    - One frontier area chosen by the engineer: server-driven UI, edge compute, WASM, streaming UI, etc.

**Phase 2 applied project:** Build a reference application in a chosen stack (Next.js, Blazor, Go, etc.). Must include auth, tests, observability hooks, and CI.


**Capstone use case options:** internal tool for a real workflow, prototype for a client pitch, reference architecture demo, boot.dev-style coding education platform module.



## 5. Capstone Framework

The capstone is the point of the whole program. It produces **two artifacts, both required**.

### Artifact A — Practical Use Case

    - Working, deployed system (not a slide deck)
    - Source-controlled with meaningful commit history
    - Full README + one ADR explaining a key decision
    - Instrumented (logs + one metric minimum)
    - Reviewed by mentor and one senior engineer
### Artifact B — Training Module

    - Covers the domain the use case is drawn from
    - ≥ 4 hours of learner content (mix of reading, video, or live)
    - Includes: learning objectives, at least 3 hands-on exercises with solutions, one assessment
    - Written for the next cohort to consume with minimal facilitator time
    - Published to the internal content library

**The link between them is not optional.** The use case *is* the exercise the training module teaches. This is why the capstone compounds — every cohort adds a real project *and* the material to teach it.

### Suggested use case sources

    - Client backlog items too small to staff a project against
    - Internal tool gaps (OpsAI modules, AMS3 utilities, Career Compass features)
    - R&D exploration (server-driven UI, agentic workflows, novel stacks)
    - Security or reliability improvements to existing systems
    - Migration accelerators (OutSystems → unified stack patterns)


## 6. Assessment Rubric

Both capstone artifacts are graded on six criteria, 1–5 each. Threshold to pass: ≥ 20/30, no criterion below 3.


| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Technical depth | Surface-level | Solid working implementation | Non-obvious design decisions, defensible trade-offs |
| Production-readiness | Runs on my machine | Deployed, basic ops | Observable, secure, documented ops story |
| Documentation clarity | Sparse | Complete but dry | A new engineer can onboard in an hour |
| Training reusability | One-off | Structured, exercises included | Genuinely drop-in for the next cohort |
| Presentation | Rambling | Clear, on time | Compelling, teaches the audience something |
| Business relevance | Toy problem | Plausible use case | Directly connects to client or internal need |



## 7. Governance & Operations

**Cohort size:** 4–8 engineers per track. Below 4, cross-pollination suffers. Above 8, mentor load breaks.


**Mentorship:** 1 senior engineer per 4 learners. Mentor commits ~2 hours/week: one 30-min 1:1 + demo attendance + async review.


**Cadence rituals:**


    - Weekly track demo (mandatory attendance for track members)
    - Bi-weekly cross-track show-and-tell (mandatory for everyone)
    - End-of-phase review (formal, rubric-scored)

**Content review board:** 2 senior engineers review every capstone Artifact B before it enters the library. Rejection is allowed; the goal is a library people want to use, not a graveyard.


**Bench reassignment:** If an engineer is pulled back to billable work mid-program, their in-progress capstone is paused (not abandoned). They resume in the next cohort at the same phase. Track this explicitly — resumption rate is a program KPI.


**Program KPIs:**


    - Capstone completion rate (target: ≥ 80%)
    - Library reuse: how often prior capstones are cited or forked by later cohorts
    - Time-to-productivity for graduates on next billable engagement
    - Mentor satisfaction (mentors are also a scarce resource)


## 8. Content Library Model

Every Artifact B lands in a searchable, versioned library. Suggested minimum metadata:


    - Track, cohort, author
    - Learning objectives
    - Prerequisites (which other modules)
    - Domain tags
    - Estimated learner hours
    - Related use case link
    - Last review date

**Suggested platforms** (pick one, don't debate for six months):


    - Notion or Confluence for a low-friction start
    - Directus + a static site (Astro) for a longer-term durable option that fits the existing stack
    - GitHub-based with a docs site (Docusaurus, Astro Starlight) if the culture is git-native

The important discipline is *versioning* and *decay management* — modules older than 18 months get flagged for review or archival.



## 9. First-Cohort Rollout Checklist

Practical steps to launch cohort 1.


    - Pick 4 use case candidates per track from the real backlog (16 total; each learner selects one)
    - Assign mentors and confirm their 2 hours/week
    - Stand up the content library platform
    - Draft the Phase 0 syllabus in the library as the first module (dogfood the format)
    - Set up the cohort channel, standup thread, and shared calendar for demos
    - Publish this framework to the library as an ADR the cohort can critique
    - Schedule the end-of-phase reviews now, all four of them, before week 1 starts
    - Define "done" for graduation and communicate it before day 1


## Appendix A — Capstone Proposal Template

Each learner submits this at the start of Phase 3. One page maximum.


Capstone Proposal — [Learner Name] — [Track]


Use case: [1 sentence]

Business/technical relevance: [2 sentences]


Artifact A — Use Case

  What it does:

  Stack:

  Deployment target:

  Definition of done:


Artifact B — Training Module

  Target audience:

  Learning objectives (3–5):

  Format (reading, video, live, mix):

  Exercises planned:

  Assessment approach:


Risks & mitigations:

Mentor sign-off:

- 

## Appendix B — Recommended Sourcing for Modules

Not endorsements — starting points. Learners are expected to synthesize, not copy.


    - Data: DataExpert.io, dbt Learn, Designing Data-Intensive Applications (Kleppmann)
    - Cloud: AWS Skill Builder, HashiCorp Learn (Terraform), Cloud Resume Challenge
    - DevOps: KodeKloud, CNCF training, Google SRE books, Learn Kubernetes the Hard Way
    - Software: Refactoring UI, System Design Primer, framework-official docs, real open source repos


## Appendix C — Anti-Patterns to Avoid

Lessons from programs that don't work.


    - Video-only modules. No exercises = no learning. Every module requires hands-on work.
    - Capstones with no deploy. "It ran locally" is not a capstone.
    - Training material with no use case attached. Abstract courses date fast and nobody wants to teach them.
    - Skipping cross-track sync. Silos form in 3 weeks if you let them.
    - Optional mentor time. If mentoring is optional, it doesn't happen.
    - Grading without a rubric. Turns feedback into personality conflict.
    - Library without curation. A dumping ground kills reuse.
