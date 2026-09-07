# R&D PROJECT PORTFOLIO

# TIMEFRAMES, RESOURCES & DISCIPLINE UTILIZATION

| Document Owner | Head of Engineering | Applies To | All R&D Projects |
|---|---|---|---|
| Review Cycle | Quarterly | Version | 1.0 |
| Companion Doc | Bench R&D Program — Capacity-Elastic Operating Model |  |  |



# 1. Overview

This document lists all active, planned, and candidate R&D projects with:


    - Timeframe — expected v1 duration and full lifecycle horizon
    - Resource composition — tech lead + rotators by discipline
    - AI utilization — where AI tools (the SDLC toolkit, LLM APIs, etc.) are integrated
    - Deliverables — what "done" means for v1 and beyond
    - Priority tier — Anchor / Tier 1 Parallel / Tier 2 Future Wave
    - Near-term in-demand skills coverage — which skills from the current market-demand list this project develops

Every project is designed to utilize a mix of **software, data, and DevOps engineers**, with AI integrated where it adds meaningful value. Every project is also evaluated for **near-term in-demand skills coverage** — the market-demand principle detailed in the R&D Program Plan document (Section 1A-2).

## Portfolio-Level Near-Term In-Demand Skills Coverage

The portfolio as a whole covers the following market-demand skills. Any skill without production-grade coverage across the portfolio is flagged as a gap requiring project adjustment or new project activation.


| Skill Category | Coverage Level | Primary Projects |
|---|---|---|
| AI Engineering — LLM integration, prompt engineering | Strong | Report Dashboard, Client Intake, AI Code Review, SDLC Toolkit Contribution |
| AI Engineering — RAG, vector databases | Medium | Report Dashboard (Triage phase), SDLC Toolkit Contribution |
| AI Engineering — Agentic workflows / MCP tools | Medium | AI Code Review Platform, SDLC Toolkit Contribution |
| AI-augmented development (EPAV, custom skills) | Strong | Every project (universal build methodology) |
| Platform Engineering — IDP, developer platforms | Strong | Bench & R&D IDP Plugin, n8n Automation |
| Platform Engineering — Kubernetes, cloud-native | Strong | All projects deploy on Kubernetes (mandated across portfolio) |
| DevSecOps — automated security, policy-as-code | Medium | /security-review skill (SDLC Toolkit Contribution), all project pipelines |
| Observability — OpenTelemetry, metrics, tracing | Medium | Standard across all deployed projects |
| Data Engineering — real-time streaming (Kafka/Flink) | Medium | Report Dashboard v2 (real-time report triggers) |
| Data Engineering — vector DBs, RAG pipelines | Medium | Report Dashboard Triage, SDLC Toolkit Contribution |
| Data Engineering — modern data stack (dbt, Airflow) | Medium | Report Dashboard data pipelines |
| Data Engineering — MLOps, model deployment | Light | AI Code Review Platform (LLM serving patterns) |
| Python proficiency | Strong | Report Dashboard backend, data pipelines, AI services |
| TypeScript/JavaScript proficiency | Strong | Report Dashboard frontend, Bench & R&D IDP Plugin |
| Java proficiency | Strong | Java Modernization Playbook, enterprise client engagements |
| Go proficiency | Light | Infrastructure and platform work when needed |


**Language mandate:** Every rotator, regardless of primary language, gains working exposure to **Python** during their rotation. Python is the dominant language across AI engineering, data engineering, and automation — non-negotiable as a foundational capability.

## Portfolio at a Glance

| Project | Tier | v1 Timeframe | Team Size | Status |
|---|---|---|---|---|
| Report Dashboard | Anchor | 8 weeks | 5–7 | Ready to start |
| Bench & R&D IDP Plugin | Tier 1 Parallel | 6 weeks | 3–4 | Ready to activate |
| n8n Internal Ops Automation | Tier 1 Parallel | 4 weeks | 2–3 | Ready to activate |
| Java Modernization Playbook | Tier 1 Parallel | 8 weeks | 2–3 | Ready to activate |
| SDLC Toolkit Contribution Track | Continuous | Rolling | 1–3 at a time | Always open |
| Client Project Intake Accelerator | Tier 2 Future | 10 weeks | 4–5 | Wave 2 candidate |
| AI Code Review Platform | Tier 2 Future | 12 weeks | 4–5 | Wave 3 candidate |


**Note on starter packs:** Earlier portfolio drafts included stack-specific "starter packs" (Spring Boot, Next.js, etc.). These were removed because the SDLC toolkit's /scaffold command already generates production-grade project boilerplate per-project from an architecture doc. Building generic starter packs would duplicate this. Instead, stack-specific reusable assets — custom skills, reviewer variants, patterns, prompts — are contributed through the **SDLC Toolkit Contribution Track** (Section 3.5).



# 1B. Strategic Value Ranking

The tier assignments above are based on strategic value and readiness. This section explains **why** each project sits where it does, so future decisions about activation, prioritization, or portfolio rebalancing are grounded in explicit reasoning rather than gut feel.

## Ranking Criteria

Each project was evaluated against six criteria:


| Criterion | What It Measures |
|---|---|
| Executive visibility | How directly and quickly executives see the output |
| BU adoption breadth | Number of business units that consume or benefit from the output |
| Revenue impact potential | Direct or indirect contribution to client work, sales cycles, or new revenue lines |
| Compounding value | Whether output grows in value with each additional contribution or use |
| Readiness to build | Availability of tech lead, clarity of scope, absence of blockers |
| Platform Fit | Whether the project extends and reinforces existing platform assets |

## The Ranking

### Rank 1 — Report Dashboard (Anchor)

**Why it's the anchor:** highest combined score on executive visibility + BU adoption breadth. Every BU is a stakeholder. Every BU head sees output in their inbox weekly. Impossible for the R&D program to become invisible to leadership. Also naturally decomposable by BU module, which fits the rotator-based staffing model better than any other candidate.


**Strategic role:** proves the R&D model works. Establishes the reusable Ask → Triage → Approve → Deliver spine that future projects inherit. Earns the mandate for everything else in the portfolio.

### Rank 2 — Bench & R&D IDP Plugin (Tier 1 Parallel)

**Why it ranks high:** highest **strategic** value for making the bench framework real, not just documented. Ship this and the framework stops being a governance artifact and starts being a daily practice inside the tool engineers already use. Smallest technical footprint (Backstage plugin, not standalone app) leverages existing Backstage IDP investment. Meta-strategic: managing the R&D program *is* the product.


**Strategic role:** internal operations backbone. Not directly revenue-impacting, but the foundation that makes every other track's output measurable and visible.

### Rank 3 — Client Project Intake Accelerator (Tier 2 Future)

**Why it ranks high strategically but sits in Tier 2:** highest **revenue** impact of any project in the portfolio. Every new client engagement runs through it. Shortens sales cycles, improves proposal quality, feeds the SDLC toolkit's /scaffold directly. It's the missing front door of the internal engineering platform.


**Why it's deferred to Wave 2:** requires more coordination with presales and larger team than anchor + first parallel can support. Better built after Report Dashboard proves the R&D model and tech lead capacity has grown.


**Strategic role:** turns R&D from cost story into revenue story. This is the project you point to when executives ask "what has R&D done for the top line."

### Rank 4 — AI Code Review Platform (Tier 2 Future)

**Why it ranks strategically:** extends the SDLC toolkit's reviewer skills from single-developer use to hosted, continuous, multi-repo service. Meaningful differentiator for enterprise client engagements needing standards enforcement at scale.


**Why it's deferred to Wave 3:** overlaps with what AI-assisted SDLC toolkit already does on-demand; higher trust/security overhead per client (repo access); requires more mature R&D machine before tackling.


**Strategic role:** scales an existing internal engineering platform asset into a productized capability. Long-term commercial potential as sellable software.

### Rank 5 — Sales Intelligence & Case Study Generator (Not yet in portfolio)

**Why it ranks strategically:** turns every completed project into compounding sales ammunition. Auto-generated case studies, searchable capability library, prospect matching. Massive long-term value.


**Why it's not yet in portfolio:** needs enough completed projects (client + internal) to have raw material worth mining. Better as a Year 2 project once the portfolio has depth.


**Strategic role:** closes the loop from project execution to sales asset. Every project delivered feeds this platform, which feeds the next sale.

### Rank 6 — Client Onboarding & Discovery Automation (Folded into Rank 3)

**Why it doesn't stand alone:** significantly overlaps with the Client Intake Accelerator (Rank 3). If Rank 3 is built well, most of onboarding automation comes with it.


**Strategic role:** merged into Client Intake Accelerator scope.

## Ranking of Tier 1 Parallels (When Activation Choice Is Needed)

When multiple Tier 1 parallels could activate but capacity only permits one, use this ranking:


| Order | Parallel Project | Primary Reason for Priority |
|---|---|---|
| 1 | Bench & R&D IDP Plugin | Meta-strategic; makes the R&D framework itself operational |
| 2 | SDLC Toolkit Contribution Track | Always-on; every contribution compounds across all future toolkit-based work |
| 3 | n8n Internal Ops Automation | Fastest shipping value (4 weeks); each workflow ships independently |
| 4 | Java Modernization Playbook | High client demand; slower to demonstrate ROI but strong for enterprise pipeline |


The Contribution Track is unique in that it can run **alongside** any other project — it consumes 20% contributor capacity from non-bench engineers and small bench allocations, without competing for the same rotator pool as the main parallel projects.


**The ranking is a default, not a mandate.** It can shift based on pipeline signals. If presales reports a surge in legacy Java modernization RFPs, that playbook moves up. If a specific stack-related pain emerges from client work, the Contribution Track absorbs it directly.

## What This Ranking Deliberately Excludes

Not everything valuable is in the portfolio. Explicit exclusions and why:


    - Full OpsAI-equivalent for internal use — too large in scope; competes with anchor for attention. Report Dashboard captures the highest-value slice of the OpsAI pattern (Ask → Triage → Approve → Deliver) without the full continuous-assessment complexity.
    - Direct clones of existing platform components — the SDLC toolkit and Backstage IDP already fill their roles; org R&D should build complementary assets, not duplicate what already works.
    - Stack-specific "starter packs" (Spring Boot, Next.js, etc.) — the SDLC toolkit's /scaffold command already generates production-grade project boilerplate per-project from the arch doc. Building generic starter packs duplicates this. Stack-specific reusable knowledge, skills, and patterns flow through the SDLC Toolkit Contribution Track instead.
    - Category 5 upskilling programs — handled by L&D per Section 7 of the Bench Framework, not the R&D portfolio.
    - Category 6 client prep work — handled by BU leads per Section 4, not the R&D portfolio.
## Re-Ranking Cadence

This ranking is reviewed:


    - Quarterly at the R&D portfolio review
    - On demand when a major pipeline shift makes an existing ranking obsolete
    - After each Wave 1 v1 ships to inform Wave 2 activation choices


# 2. Anchor Project — Report Dashboard

## 2.1 Description

A cross-BU reporting platform that serves Sales, Marketing, Resource Management, DPMO, HR, L&D, and other business units. Built on the OpsAI pattern: **Ask → Triage → Approve → Deliver** with human approval gates before any output leaves the system.


**Core value:** every BU gets consistent, on-demand reporting through a single interface, with human sign-off ensuring output quality before delivery.

## 2.2 v1 Scope (8 Weeks)

Two BU modules in v1:


    - Resource Management module — bench utilization, project allocation, capability coverage reports
    - Sales module — pipeline, win rate, deal velocity reports

Plus the reusable spine:


    - Ask flow (file upload + query)
    - Triage engine (module/template/prompt selection)
    - Approve UI (preview + human sign-off + undo window)
    - Deliver dispatch (email; Chat delivery in v2)
## 2.3 Team Composition

| Role | Count | Discipline Focus |
|---|---|---|
| Tech Lead | 1 | Senior full-stack; owns spine + rotator coherence |
| Software Engineers (rotators) | 2–3 | Frontend (Next.js / TypeScript), backend API (Python or NestJS), spine components |
| Data Engineers (rotators) | 1–2 | Python-based ETL, BU data source integration, real-time streaming for v2 report triggers, vector DB integration for Triage semantic search |
| DevOps Engineers (rotators) | 1 | Kubernetes deployment, observability (OpenTelemetry), email delivery infra, secrets management, automated security scanning |
| Total | 5–7 |  |


**Language exposure:** All rotators work with Python at some point in the project (backend services or data pipelines). Frontend rotators additionally work with TypeScript/Next.js.

## 2.4 Near-Term In-Demand Skills Coverage

This project develops the following market-demand skills:


    - AI Engineering: LLM integration (Triage + report generation), prompt engineering, RAG for Triage semantic search, vector databases
    - Platform Engineering: Kubernetes deployment, observability, secrets management
    - Data Engineering: Modern data pipelines (Python + orchestration), real-time streaming in v2, data quality patterns
    - DevSecOps: Automated security scanning in CI/CD pipeline
    - Languages: Python (backend + data), TypeScript (frontend)
## 2.5 AI Utilization

    - Triage phase: LLM-assisted suggestion of correct module/template/prompt from attached file context; RAG-based retrieval from vector DB of past reports and templates for semantic matching
    - Report generation: LLM-assisted summarization and narrative generation for report content
    - Approve phase: AI-generated preview highlighting anomalies or unusual values for human reviewer attention
    - Build methodology: Full SDLC toolkit EPAV workflow throughout
## 2.6 Timeframe & Milestones

| Week | Milestone |
|---|---|
| 1 | v1 spec finalized with 2 BU heads; repo scaffolded via toolkit initialization + /scaffold |
| 2 | Spine architecture complete (Kubernetes-based); task CSV built; rotators onboarded |
| 3–4 | Spine functional end-to-end with mock modules; RAG + vector DB for Triage integrated |
| 5–6 | RM module and Sales module built in parallel |
| 7 | Integration testing with real data sources; approval flow tested; security scan passing |
| 8 | v1 deployed on Kubernetes; first real reports sent to RM head and Sales head |

## 2.7 Post-v1 Roadmap

    - v2 (Months 3–4): Add Marketing and DPMO modules; Chat delivery; real-time streaming for event-triggered reports (Kafka/equivalent)
    - v3 (Months 5–6): Add HR and L&D modules; scheduled/recurring reports; expanded vector search across all reports
    - v4 (Months 7–9): Continuous assessment mode (per OpsAI Phase 4 pattern) — proactive AI-driven report suggestions; agentic report composition
## 2.8 Deliverables

    - Deployed platform serving 2+ BUs weekly by end of v1
    - Reusable spine module (Ask → Triage → Approve → Deliver) available for future R&D projects
    - Documented patterns in knowledge/patterns/ for report module construction
    - Backstage IDP entry with owner, docs, and API surface
    - Real-time streaming reference implementation (v2)


# 3. Tier 1 Parallel Projects

Activated when bench exceeds anchor capacity. Each is self-contained, pause-friendly, and produces value even if partially completed.

## 3.1 Bench & R&D IDP Plugin

### Description

A Backstage plugin extending the Backstage IDP with three views: Bench dashboard (who's on bench), R&D Tracks portfolio (what's being built), and Contributions log (who shipped what). Makes the bench framework operational inside the tool engineers already use.

### v1 Scope (6 Weeks)

    - Bench view: current bench engineers, since when, current assignment
    - Tracks view: active + paused R&D projects with tech lead, rotators, status
    - Contributions view: running feed of shipped work
### Team Composition

| Role | Count | Discipline Focus |
|---|---|---|
| Tech Lead | 1 | Backstage plugin expertise required |
| Software Engineers (rotators) | 2 | React/TypeScript for plugin UI; Python or Node.js for backend integration |
| Data Engineers (rotators) | 1 | Python-based bench data ingestion from resource management tool; contribution analytics |
| DevOps Engineers (rotators) | 0–1 | Plugin deployment on Kubernetes; integration with existing Backstage IDP infra |
| Total | 3–4 |  |

### Near-Term In-Demand Skills Coverage

    - Platform Engineering: Backstage IDP (top-demand platform engineering skill), plugin architecture, Kubernetes deployment
    - AI Engineering: LLM-assisted summarization for contribution digests
    - Languages: TypeScript (plugin UI), Python (data ingestion and analytics)
### AI Utilization

    - LLM-assisted auto-summarization of contribution feeds for weekly digest
    - SDLC toolkit EPAV for the build itself
### Timeframe

6 weeks to v1. Ongoing enhancement thereafter as the R&D program evolves.

### Deliverables

    - Backstage plugin deployed on the internal Backstage IDP
    - Integration with existing bench tracker data
    - Contribution log integrated with Slack (or existing chat tool)


## 3.2 n8n Internal Ops Automation Library

### Description

A library of n8n workflows automating recurring internal operational pain points. Each workflow is independent; the library grows over time.

### v1 Scope (4 Weeks)

Ship 3–5 automated workflows. Suggested starters:


    - Engineer onboarding automation (accounts, repos, docs setup)
    - Bench event notifications (Slack alert when engineer hits bench)
    - Weekly bench standup preparation (auto-generated agenda from tracker)
    - Client project kickoff (auto-provisioning of Slack, repo, IDP entry)
    - Timesheet reminder + escalation workflow
### Team Composition

| Role | Count | Discipline Focus |
|---|---|---|
| Tech Lead | 1 | n8n expertise; automation architecture |
| Software Engineers (rotators) | 1 | Custom n8n nodes if needed (TypeScript); Python for advanced scripting; API integrations |
| Data Engineers (rotators) | 1 | Python-based data source connections and transformations |
| DevOps Engineers (rotators) | 1 | n8n hosting on Kubernetes, monitoring, secrets management |
| Total | 2–3 | Small team; each workflow can be owned solo |

### Near-Term In-Demand Skills Coverage

    - AI Engineering: LLM node integration, AI-driven decision routing, prompt engineering for automation contexts
    - Platform Engineering: Kubernetes hosting, secrets management, workflow observability
    - Automation: Workflow orchestration patterns (transferable to Airflow, Prefect, Dagster mental models)
    - Languages: Python (scripting and integrations), TypeScript (custom nodes)
### AI Utilization

    - LLM nodes in n8n for content generation (welcome messages, digest summaries)
    - AI-driven routing decisions (e.g., which team owner to notify)
### Timeframe

4 weeks to first 3 workflows in production. Continuous expansion thereafter (each new workflow is 2–5 days).

### Deliverables

    - n8n workflows running in production against internal systems
    - Workflow catalog registered in Backstage IDP
    - Pattern templates in knowledge/patterns/ for future workflows


## 3.3 Java Legacy Modernization Playbook

### Description

A reusable methodology + reference implementation for taking Java 8 client codebases to modern Java 21+. Pure knowledge asset — documentation, example repos, before/after transformations. Very pause-friendly.

### v1 Scope (8 Weeks)

    - Written methodology covering common migration patterns (records, pattern matching, virtual threads, sealed classes, etc.)
    - 3+ reference "before / after" repos showing real transformations
    - Playbook of common client scenarios (Spring 4→6, JDK 8→21, monolith decomposition entry points)
    - Custom AI SDLC skill for guided migration: /java-modernize
### Team Composition

| Role | Count | Discipline Focus |
|---|---|---|
| Tech Lead | 1 | Senior Java engineer, must be current on Java 21+ |
| Software Engineers (rotators) | 1–2 | Java refactoring work; example implementations; Python for automation scripts |
| Data Engineers (rotators) | 0–1 | Only if migration involves data layer patterns |
| DevOps Engineers (rotators) | 0–1 | Kubernetes-based CI/CD examples for migration pipelines |
| Total | 2–3 | Smallest team of Tier 1 projects |

### Near-Term In-Demand Skills Coverage

    - Languages: Modern Java (21+) — including virtual threads, records, pattern matching, sealed classes
    - AI Engineering: AI-assisted refactoring workflows, custom SDLC skill development, prompt engineering for code transformation
    - DevSecOps: Security implications of legacy code (older Spring versions, deprecated crypto)
    - Enterprise Systems: Monolith decomposition patterns, incremental migration strategies
### AI Utilization

    - SDLC toolkit + custom skill for AI-assisted refactoring
    - LLM-generated migration documentation
    - AI-generated test coverage for legacy code before refactoring
### Timeframe

8 weeks to v1 playbook. Continuous expansion as new migration scenarios are encountered on client engagements.

### Deliverables

    - Written playbook in knowledge/patterns/
    - Reference repositories publicly visible in Backstage IDP catalog
    - Custom AI SDLC skill contributed to internal library
    - Optional: sales/marketing collateral for the modernization service offering


## 3.4 SDLC Toolkit Contribution Track (Continuous)

### Description

A rolling, always-open channel for engineers to contribute stack-specific, discipline-specific, or task-specific extensions directly to the SDLC toolkit. Not a "project" with a v1 date — a continuous contribution mechanism that produces reusable platform assets as engineers encounter opportunities during client work or bench time.


**Why this exists as a track:** the SDLC toolkit's extensibility model (toolkit skill add, toolkit agent add, toolkit rule add) is designed for exactly this. Rather than bundling stack-specific work into artificial "starter pack" projects, individual contributions flow directly into the framework and immediately benefit every future project using it.

### What Gets Contributed

| Asset Type | Examples | Typical Effort |
|---|---|---|
| Custom AI SDLC skills | /security-review, /jpa-review, /spring-security-review, /accessibility-review, /nextjs-performance-review, /threading-review, /rag-review, /k8s-review | 2–5 days each |
| Reviewer agent variants | Spring-aware code reviewer, JPA-aware database reviewer, mobile-specific performance reviewer, RAG-aware code reviewer | 3–7 days each |
| knowledge/patterns/ entries | Multi-tenancy pattern for Spring Boot, RLS pattern for Supabase, streaming UI pattern for Next.js, RAG pipeline pattern, Kafka streaming pattern | 1–3 days each |
| knowledge/rules/ entries | Company coding standards, security defaults, API conventions, K8s deployment defaults | 1–2 days each |
| knowledge/prompts/dev/ entries | Prompt templates for common recurring dev tasks per stack | 0.5–1 day each |
| MCP tool additions | New tools that extend the AI toolkit MCP server capabilities | 5–10 days each |

### Priority Contributions (Aligned to Near-Term In-Demand Skills)

The following contributions are prioritized because they map directly to top-demand market skills:


    - /security-review skill — closes the DevSecOps coverage gap; automated security scanning for code changes
    - /rag-review skill — reviewer for RAG implementations (vector DB usage, retrieval quality, context window management)
    - RAG reference architecture pattern — canonical RAG implementation pattern for knowledge/patterns/
    - Kafka/Flink streaming pattern — canonical real-time streaming pattern for data pipelines
    - Kubernetes deployment rule set — production-grade K8s defaults for knowledge/rules/
    - Agentic workflow patterns — multi-step AI orchestration patterns with human approval gates
    - Vector DB integration patterns — patterns for pgvector, Pinecone, Weaviate, Qdrant integration
### Contribution Modes

Contributors engage in one of three ways:


| Mode | Who | Time Commitment | Trigger |
|---|---|---|---|
| Bench rotator | Bench engineer during rotation | Full-time for 1–2 weeks | Rotator picks a contribution from the queue during bench window |
| 20% contributor | Non-bench engineer | 4–8 hours per week | Engineer identifies a useful contribution during client work |
| Client-triggered | Any engineer on a client project | As needed | Real client project reveals a reusable pattern worth extracting |

### Team Composition (When Rotators Are Active)

| Role | Count | Discipline Focus |
|---|---|---|
| Track Lead | 1 | Senior engineer who owns SDLC toolkit contribution quality and coherence |
| Active Contributors | 1–3 at any time | Rotating; discipline varies by contribution type. Python and TypeScript are common; language matches contribution scope. |
| Total | 2–4 | Highly variable; contributions are individually scoped |

### Near-Term In-Demand Skills Coverage

    - AI Engineering: LLM-powered skill development, prompt engineering, agentic workflow design, MCP tool building
    - Security: DevSecOps skill contributions
    - Data Engineering: RAG and streaming pattern contributions
    - Platform Engineering: K8s and IDP-related patterns
    - Languages: Python (dominant for AI skill implementations), TypeScript (for tool integrations)
### AI Utilization

    - Every contribution is built and tested using the SDLC toolkit's EPAV workflow itself (dogfooding)
    - Custom skills often are AI capabilities (LLM-powered reviewers, generators, analyzers)
    - LLM-assisted documentation for each contribution
### Contribution Queue

The track lead maintains a prioritized queue of desired contributions in Backstage IDP. Sources for queue items:


    - BU heads flagging repeatedly-needed patterns
    - Retros from completed client projects surfacing reusable insights
    - Engineer suggestions from bench standups or 20% work
    - Track lead's own strategic assessment of SDLC toolkit gaps
### Acceptance Criteria for Contributions

Every contribution before merge to the SDLC toolkit:


    - Working example demonstrating the contribution's value
    - Documentation explaining when and how to use it
    - Tested on at least one real repository (client or internal)
    - Reviewed by track lead
    - Registered in the shared SDLC toolkit catalog (Backstage IDP entry)
### Timeframe

Continuous. No v1 date. Success measured by contribution velocity and quality, not project completion.

### Deliverables (Rolling)

    - New platform assets shipped to the framework monthly
    - Growing contribution catalog visible in Backstage IDP
    - Quarterly summary of contributions by discipline and stack
    - Compounding capability across all future client projects and internal builds
### Why This Replaces "Starter Packs"

/scaffold already generates production-grade project boilerplate per-project from the arch doc. Building generic "starter pack" repos would duplicate that work. What /scaffold doesn't do is ship reusable, battle-tested, stack-specific knowledge and skills that any project can benefit from. This track produces those — the right shape for how the SDLC toolkit is designed to extend.



# 4. Tier 2 Future Wave Projects

Reserved for Wave 2 (Month 4+) once anchor is stable and Tier 1 patterns are proven.

## 4.1 Client Project Intake Accelerator

### Description

Automates the "signed client → running project" gap. Takes intake data → generates initial project docs → auto-scaffolds via the SDLC toolkit → registers in Backstage IDP → sets up communication channels.

### v1 Scope (10 Weeks)

    - Structured intake form / Slack bot for discovery data
    - LLM-assisted generation of BRD/PRD/architecture doc drafts (with RAG over past project templates)
    - Auto-scaffolding pipeline that runs toolkit initialization + /scaffold
    - Auto-registration in Backstage IDP with team assignment
    - Auto-provisioning of Slack, repos, project boards
### Team Composition

| Role | Count | Discipline Focus |
|---|---|---|
| Tech Lead | 1 | Senior full-stack; integration architecture experience |
| Software Engineers (rotators) | 2 | Full-stack (TypeScript frontend + Python backend); heavy LLM integration work |
| Data Engineers (rotators) | 1 | Python-based intake data storage, vector DB for historical project retrieval, RAG pipeline |
| DevOps Engineers (rotators) | 1 | Multi-system integration on Kubernetes (GitHub, Slack, Jira, GDrive); secrets management |
| Total | 4–5 |  |

### Near-Term In-Demand Skills Coverage

    - AI Engineering: Heavy LLM integration, RAG for historical project retrieval, prompt engineering for document generation, agentic orchestration of scaffolding pipeline
    - Platform Engineering: Kubernetes deployment, multi-system integration architecture
    - Data Engineering: Vector DB for project templates, structured data storage for intake
    - Languages: Python (backend + AI services), TypeScript (frontend + integrations)
### AI Utilization

    - Heavy LLM usage for document generation
    - RAG-based retrieval of similar past project patterns
    - AI-driven team composition recommendations based on discovery data
    - SDLC toolkit EPAV for the build itself
### Timeframe

10 weeks to v1. Wave 2 candidate.

### Deliverables

    - End-to-end intake → project spin-up automation
    - Presales enablement (proposal generation shortcuts)
    - Integration with existing internal engineering platform (SDLC toolkit + Backstage IDP)


## 4.2 AI Code Review Platform

### Description

Extends the SDLC toolkit's reviewer skills from "developer's terminal" to "continuous service across all client repos." Multi-tenant SaaS-style platform for hosted, continuous code review. Explicitly designed as an **agentic workflow** — autonomous multi-step review with human approval gates before findings escalate.

### v1 Scope (12 Weeks)

    - Webhook integration with GitHub/GitLab
    - Multi-repo aggregation dashboard
    - Continuous review using AI reviewer skills as agentic workflows
    - Trend analysis and drift detection
    - Finding management and escalation
    - MLOps for LLM serving (prompt versioning, evaluation, monitoring)
### Team Composition

| Role | Count | Discipline Focus |
|---|---|---|
| Tech Lead | 1 | Senior backend architect; distributed systems + LLM ops experience |
| Software Engineers (rotators) | 2 | Backend API (Python or Go) + TypeScript dashboard frontend |
| Data Engineers (rotators) | 1 | Streaming findings aggregation, trend analysis pipelines, vector DB for pattern matching |
| DevOps Engineers (rotators) | 1 | Multi-tenant Kubernetes infra, worker queue management, webhook processing, LLM serving observability |
| Total | 4–5 |  |

### Near-Term In-Demand Skills Coverage

    - AI Engineering: Agentic workflows (multi-step autonomous review), LLM serving at scale, prompt engineering, prompt evaluation, RAG for context-aware review
    - Platform Engineering: Multi-tenant Kubernetes architecture, distributed systems, worker queues
    - Data Engineering: Real-time streaming findings aggregation, trend analysis, vector DB for pattern matching
    - MLOps: LLM serving patterns, prompt versioning and evaluation, model output monitoring
    - DevSecOps: Security is a core review dimension
    - Languages: Python (LLM services), TypeScript (dashboard), possibly Go (worker infrastructure)
### AI Utilization

    - Core value driver — LLM-powered continuous code review as agentic workflow
    - AI reviewer skills as the analysis engine
    - AI-generated trend summaries for dashboard
    - RAG for repository-specific context injection
### Timeframe

12 weeks to v1. Wave 3 candidate.

### Deliverables

    - Deployed multi-tenant platform on Kubernetes
    - Integration with 2+ real client repos as pilot
    - Aggregated findings dashboard
    - Extension of AI reviewer skill ecosystem
    - MLOps reference patterns for LLM serving contributed to knowledge/patterns/


# 5. Resource Allocation Reference Table

Cross-project view of resource requirements when multiple projects are active.


| Project | Tech Lead | SW | Data | DevOps | Total | AI-Intensive |
|---|---|---|---|---|---|---|
| Report Dashboard (Anchor) | 1 | 2–3 | 1–2 | 1 | 5–7 | Yes |
| Bench & R&D IDP Plugin | 1 | 2 | 1 | 0–1 | 3–4 | Light |
| n8n Automation Library | 1 | 1 | 1 | 1 | 2–3 | Light |
| Java Modernization Playbook | 1 | 1–2 | 0–1 | 0–1 | 2–3 | Medium |
| SDLC Toolkit Contribution Track | 1 | Variable | Variable | Variable | 2–4 | Medium–Heavy |
| Client Intake Accelerator | 1 | 2 | 1 | 1 | 4–5 | Heavy |
| AI Code Review Platform | 1 | 2 | 1 | 1 | 4–5 | Heavy |

## Realistic Concurrent Portfolios by Bench Size

| Bench Size | Active Portfolio | Total Engineers | Tech Leads Needed |
|---|---|---|---|
| 5 | Anchor only | 5 | 1 |
| 8 | Anchor + n8n | 8 | 2 |
| 10 | Anchor + Bench Plugin | 10 | 2 |
| 12 | Anchor + Bench Plugin + n8n | 12 | 3 |
| 15 | Anchor + Bench Plugin + Java Modernization + Contribution Track | 14–15 | 4 |
| 18 | Anchor + Bench Plugin + n8n + Java Modernization + Contribution Track | 17–18 | 5 |
| 20+ | Full lab mode: Anchor + all Tier 1 parallels + Contribution Track + 1 Tier 2 project | 20+ | 6+ |


**Note:** The SDLC Toolkit Contribution Track's engineer count is highly variable because contributions can be small (1 engineer, 3 days) or larger (2–3 engineers, 2 weeks). Track lead time is stable; contributor time flexes with contribution demand.



# 6. Discipline Utilization Notes

## Software Engineers

    - Present in every project
    - Rotate across full-stack, frontend-heavy, or backend-heavy roles depending on project needs
    - Anchor project and AI-heavy Tier 2 projects offer the widest range of full-stack + AI integration work
    - Python exposure is universal — every rotator writes Python during their rotation
    - TypeScript exposure via anchor project frontend and Bench IDP Plugin
    - Growth path: engineers exit rotation with real AI-augmented development experience, LLM integration skills, and portfolio-worthy production systems
## Data Engineers

    - Every project includes at least some data engineering work
    - Report Dashboard, Client Intake, and AI Code Review Platform are most data-heavy
    - Python-first: all data pipeline work is Python-based, aligning with market-demand tooling (Airflow, Prefect, Dagster, dbt)
    - Real-time streaming exposure via Report Dashboard v2 (Kafka or equivalent for event-triggered reports)
    - Vector DB and RAG exposure via Report Dashboard Triage phase and Client Intake historical retrieval
    - Growth path: engineers gain the two highest-premium data skills in 2026 — real-time streaming and vector DB/RAG pipeline work
## DevOps Engineers

    - Present in every project except Java Modernization (optional there)
    - Anchor project + n8n Automation offer high-visibility infrastructure work
    - Kubernetes mandate: every R&D project deployment runs on Kubernetes, giving every DevOps rotator hands-on production K8s experience
    - DevSecOps integration: every project pipeline includes automated security scanning
    - Backstage IDP work via Bench & R&D IDP Plugin — directly develops the top-demand platform engineering skill
    - Growth path: engineers exit rotation with production Kubernetes experience, IDP platform work, and DevSecOps automation — the three highest-demand DevOps skills
## AI Integration

    - Heavy AI: Anchor (Report Dashboard), Client Intake, AI Code Review Platform
    - Medium AI: Java Modernization (through custom AI SDLC skills), SDLC Toolkit Contribution Track
    - Light AI: Bench IDP Plugin, n8n Library (AI used but not core to value)
    - Universal: All projects use the SDLC toolkit's EPAV workflow as build methodology, giving every rotator hands-on AI-assisted development experience
## Language Coverage Across Portfolio

| Language | Coverage | Where Engineers Encounter It |
|---|---|---|
| Python | Universal — every rotator | Backend services, data pipelines, AI integrations, automation scripts, custom AI skill implementations |
| TypeScript/JavaScript | Strong | Frontend (Report Dashboard, Client Intake), Backstage plugins, n8n custom nodes |
| Java | Specialized track | Java Modernization Playbook; enterprise client engagements |
| Go | Optional/emerging | Infrastructure and platform work in AI Code Review Platform when needed |
| SQL | Universal for data work | All data engineering rotators |



# 7. Project Selection Decision Matrix

When bench allows a parallel activation, use this matrix to pick which parallel to activate:


| Factor | Weight | Rationale |
|---|---|---|
| Tech lead availability | Critical | No tech lead = no project. Non-negotiable. |
| Near-term in-demand skills coverage | High | Prioritize projects that grow rotators into market-demand skills (see Program Plan Section 1A-2) |
| Rotator skill match | High | Match project discipline needs to available bench skills |
| Pipeline alignment | High | Prioritize projects producing assets for near-term client work |
| Pause tolerance | Medium | Prefer highly pause-tolerant projects during volatile bench periods |
| Executive visibility need | Medium | Consider projects that produce demoable output for upcoming exec reviews |
| Team development | Medium | Weight projects that grow rotators into new capabilities |
| Portfolio skill gap closure | Medium | If a top-demand skill has no active coverage, favor projects that add it |



# Appendix A: Project Template for Adding New Candidates

Use this template when proposing new R&D projects to the portfolio.


| Field | Content |
|---|---|
| Project Name |  |
| Tier | Anchor / Tier 1 Parallel / Tier 2 Future |
| Description | 2–3 sentences |
| v1 Scope | Bulleted list of core capabilities |
| Timeframe | v1 duration + full lifecycle horizon |
| Software Engineer Rotators | Count + skill focus + primary language(s) |
| Data Engineer Rotators | Count + skill focus + Python confirmation |
| DevOps Engineer Rotators | Count + skill focus + Kubernetes confirmation |
| Tech Lead Requirements | Seniority + specific expertise needed |
| Near-Term In-Demand Skills Coverage | Which skills from the current Program Plan Section 1A-2 list this project develops. Minimum 2 required. |
| AI Utilization | Where AI adds value in the build and product |
| Deliverables | What "done" means for v1 |
| Pause Tolerance | How gracefully can this project pause and resume |
| Dependencies | Prerequisites or blockers |
| Platform Fit | How this integrates with SDLC toolkit / Backstage IDP / other platform components |
| Proposed By |  |
| Date Proposed |  |
