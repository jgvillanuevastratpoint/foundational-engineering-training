# Git & Code Review Discipline — Training Module Source Document

> Source document feeding Skill 1 (Research Synthesizer) → Skill 2 (Learning Path Architect) → Skill 3 (Module Content Builder). Quiz content is intentionally excluded from authoring here — Skill 5 (Quiz Generator) owns that. No hands-on tasks or rubrics — this pipeline is quiz-only.

---

## 0. Module Metadata

- **Audience:**
  - **Cloud Engineers:** cloud engineers routinely change infrastructure-as-code, pipeline definitions, and shared platform modules that other teams depend on immediately after merge — a bad merge or an unreviewed change can take down environments, not just one service, so the discipline requirements are higher than for typical application code.
- **Video lecture (if any):** None yet produced. If recorded, keep to a single session under 30 minutes; trunk-based dev + PR hygiene + semantic commits + review-as-teaching each need only a few minutes of framing since the depth lives in this document.
- **Learning objectives:**
  1. Describe what a commit, a branch, and a merge are in Git, and how they relate to one another.
  2. Explain why trunk-based development reduces integration risk compared to long-lived feature branches.
  3. Identify the properties of a well-formed pull request (size, description, self-review) and explain why each reduces reviewer error.
  4. Write a semantic commit message and distinguish it from a non-semantic one.
  5. Distinguish code review conducted as gatekeeping from code review conducted as teaching, and explain why the latter improves team capability over time.
  6. Identify the risks specific to reviewing infrastructure-as-code changes versus application code changes.

---

## 1. Why This Subject Matters (Motivation)

You will spend more time reading other people's code, and having your own code read, than you will spend writing code that no one ever looks at again. In cloud engineering specifically, a single merged pull request can change the shape of a shared VPC, a Terraform module ten other teams consume, or an IAM policy dozens of services rely on — and it can do so the moment it lands on the trunk, with no separate "deploy day" to catch problems. Git and code review are not administrative overhead around the real work; they are the mechanism by which a team keeps shared infrastructure safe to change quickly. Get this wrong and you get either paralysis (nobody wants to touch shared modules) or fragility (everybody touches them carelessly). Get it right and a team can ship infrastructure changes constantly without constantly breaking things.

---

## 2. Core Concepts

Concepts are grouped into two halves that build in order: version control fundamentals first (what Git tracks and how the workflow practices around it fit together), then code review practices (how a team uses those artifacts to catch problems before they ship).

### Version Control Fundamentals

- **What Is Git, and How Does Version Control Work?**
  - **Context:** Git is a distributed version control system that tracks a repository's history as a chain of commits — immutable snapshots, each pointing to its parent — with branches acting as movable pointers into that history and a merge reconciling two branches' divergent commits into one. Every practice in this module (trunk-based development, PR hygiene, semantic commits) is a convention layered on top of these three primitives, not a separate system.
  - **Illustration:** [x] needed — a simple diagram of a commit graph showing a branch pointer, a sequence of commits, and a merge commit joining two branches back together.
- **Trunk-Based Development**
  - **Context:** a workflow where all developers integrate small, frequent changes into a single shared branch (commonly `main`), avoiding long-lived feature branches that drift out of sync and produce large, risky merges.
  - **Illustration:** [x] needed — a side-by-side diagram contrasting a long-lived feature branch diverging from `main` over weeks versus small commits landing on `main` daily, showing merge-conflict/risk buildup in the first case.
- **Feature Flags as a Trunk-Based Enabler**
  - **Context:** trunk-based development still needs a way to land incomplete work safely; feature flags let unfinished or risky code merge to trunk while staying inactive until explicitly enabled.
  - **Illustration:** not needed — definitional.
- **Pull Request (PR) Hygiene**
  - **Context:** the set of practices — small diff size, a clear description of intent and testing, self-review before requesting others' time — that make a PR fast and safe for a reviewer to evaluate.
  - **Illustration:** [x] needed — a comparison of a "bad PR" (200+ files, no description, mixed concerns) against a "good PR" (single concern, description with context/testing notes, reasonable size).
- **Semantic Commit Messages**
  - **Context:** a commit message convention (e.g., `feat:`, `fix:`, `chore:`, `refactor:`) that encodes the *type* and *intent* of a change in a machine- and human-parseable way, enabling automated changelogs and versioning and making `git log` and `git blame` genuinely useful for debugging later.
  - **Illustration:** not needed — definitional, best shown via short text examples rather than a diagram.
- **Why These Practices Only Work Together**
  - **Context:** trunk-based development, PR hygiene, and semantic commits are not independent, optional add-ons — each one's payoff depends on the others being followed too. Small, frequent PRs are only reviewable quickly if the branch hasn't already drifted (trunk-based dev); a clean commit history is only useful for debugging if commits map to reviewable, single-concern units (PR hygiene) instead of one giant squashed blob; and semantic prefixes only produce a trustworthy changelog if every contributor actually uses them. Skipping one quietly degrades the value of the other two.
  - **Illustration:** not needed — conceptual synthesis, best conveyed through the case studies rather than a diagram.

### Code Review Practices

- **Code Review as Teaching, Not Gatekeeping**
  - **Context:** the same review mechanics (approve/request changes, inline comments) can be used purely to block bad code, or deliberately used to transfer context and raise the whole team's skill level; the distinction affects what comments look like and how a reviewer treats a disagreement.
  - **Illustration:** not needed — definitional/behavioral distinction.
- **Reviewing Infrastructure-as-Code (IaC) Diffs**
  - **Context:** unlike application code, an IaC diff's real effect is only fully visible through its plan/diff output (e.g., a Terraform plan) — a reviewer who reads only the source lines without checking the plan output can approve a change that looks small but destroys and recreates a production resource.
  - **Illustration:** [x] needed — an example showing a one-line Terraform change whose plan output reveals a destructive replace rather than an in-place update.

---

## 3. Case Studies / Real-World Examples

1. **The stale feature branch that broke a shared module**
   - **Scenario:** An engineer works on a two-week-long feature branch upgrading a shared networking Terraform module. By the time they open a PR, three other unrelated changes have landed on `main`, and the merge silently reintroduces a deprecated subnet configuration.
   - **Git & Code Review Discipline in Action:**
     - *Trunk-Based Development:* had the engineer merged small, flag-gated increments daily, the module would never have drifted far enough from `main` to produce a silent reintroduction.
     - *PR Hygiene:* the eventual PR was large enough (touching the whole module) that reviewers could not realistically trace every interaction, illustrating why diff size matters independent of the author's competence.
   - **Outcome:** the team adopts a policy capping how long a branch may live before it must rebase against `main` or be split into smaller merges.

2. **A one-line IaC change that was actually a resource replacement**
   - **Scenario:** A reviewer approves a PR that appears to only rename an S3 bucket variable, without checking the plan output. The apply destroys and recreates the bucket, deleting its contents.
   - **Git & Code Review Discipline in Action:**
     - *Reviewing IaC Diffs:* the review process had no requirement to attach or check plan output before approval, so a destructive change was invisible in the source diff alone.
     - *PR Hygiene:* the PR description did not state expected infrastructure impact, so the reviewer had no prompt to ask "does this replace anything?"
   - **Outcome:** the team adds a checklist requirement that every IaC PR includes plan output in the description, and reviewers are trained to specifically scan for "must be replaced" lines.

3. **Review-as-teaching turning around a recurring incident pattern**
   - **Scenario:** A junior cloud engineer repeatedly opens PRs granting overly broad IAM permissions ("just to get it working"), and a senior reviewer keeps blocking them with terse "no, too broad" comments.
   - **Git & Code Review Discipline in Action:**
     - *Code Review as Teaching, Not Gatekeeping:* the senior engineer switches to explaining, in each comment, the specific principle (least privilege) and pointing to the exact minimal permission set needed, rather than only rejecting.
     - *Semantic Commit Messages:* the junior engineer's fix commits start using `fix(iam):` consistently once shown why it matters, making later audits of permission changes searchable.
   - **Outcome:** within a few review cycles the junior engineer stops proposing overly broad policies unprompted — the review mechanism produced a durable capability change, not just a one-time correction.

---

## 4. Best Practice Checklist / Frameworks

- Merge to trunk at least daily; use feature flags to hide incomplete work rather than isolating it on a long-lived branch.
- Keep PRs to a single logical concern; if you can't summarize the change in one sentence, split it.
- Write PR descriptions that state *what* changed, *why*, and *how it was verified* (tests run, plan output attached, environment tested in).
- Self-review your own diff before requesting review — catch the obvious issues so the reviewer's attention goes to the substantive ones.
- Use a semantic commit prefix (`feat`, `fix`, `chore`, `refactor`, `docs`, `test`) consistently; treat the commit history as a debugging tool, not paperwork.
- For any IaC change, require the plan/diff output (not just the source diff) as part of the review artifact.
- As a reviewer, explain the *why* behind a requested change, not just the *what* — a comment that only says "wrong" transfers no capability.
- Do not try to review everything with equal depth: prioritize scrutiny on changes to shared modules, IAM/permission boundaries, and anything destructive in a plan output; a formatting-only change does not need the same rigor.

---

## 5. Sources

- Git, "Git Basics — Getting a Git Repository" and "Git Branching" (Pro Git book) — https://git-scm.com/book/en/v2
- Google, "Trunk-Based Development" — https://trunkbaseddevelopment.com/
- Google Cloud, "DevOps tech: Trunk-based development" (DORA) — https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development
- Conventional Commits, "Conventional Commits 1.0.0" — https://www.conventionalcommits.org/en/v1.0.0/
- HashiCorp, "Terraform Plan and Apply" (relevant to reviewing IaC diffs) — https://developer.hashicorp.com/terraform/cli/commands/plan
- Google, "Code Review Developer Guide" — https://google.github.io/eng-practices/review/
- GitLab, "Code Review Guidelines" — https://docs.gitlab.com/development/code_review/
- **Video lectures:** none cited.
