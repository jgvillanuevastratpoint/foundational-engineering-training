# Security Hygiene — Training Module Source Document

> Source document feeding Skill 1 (Research Synthesizer) → Skill 2 (Learning Path Architect) → Skill 3 (Module Content Builder). Quiz content is intentionally excluded from authoring here — Skill 5 (Quiz Generator) owns that. No hands-on tasks or rubrics — this pipeline is quiz-only.

---

## 0. Module Metadata

- **Audience:**
  - **Cloud Engineers:** cloud engineers provision the identities, credentials, and permission boundaries that every workload runs under; a credential-handling mistake made once in a shared pipeline or a Terraform module can be replicated across every environment that consumes it, making this the single highest-leverage place for a security mistake to compound.
- **Video lecture (if any):** None yet produced. If recorded, keep to a single ~25-minute session — secret management, OIDC vs. static credentials, least privilege, and the case study form one continuous argument and shouldn't be split.
- **Learning objectives:**
  1. Describe the three defaults (credential lifetime, storage location, permission scope) that determine an incident's blast radius.
  2. Explain why hardcoded or long-lived static credentials are a persistent security liability even when "nothing has gone wrong yet."
  3. Explain how OIDC-based workload identity federation removes the need for long-lived cloud credentials in CI/CD pipelines.
  4. Define the principle of least privilege and give a concrete example of violating it.
  5. Explain the distinction between "it works" and "it's safe," and why the former is not evidence of the latter.
  6. Summarize the 2025 Red Hat GitLab-hosted consulting repository compromise and identify which security hygiene failure it illustrates.

---

## 1. Why This Subject Matters (Motivation)

"It works" and "it's safe" are answered by completely different tests, and a huge number of security incidents happen precisely because that distinction gets collapsed — a pipeline runs fine for two years on a static access key baked into a config file, right up until that file or that repository leaks, and then two years of "it worked" turns into an active compromise. Security hygiene isn't a separate phase you do after the infrastructure works; it's a set of defaults (how credentials are issued, how broadly permissions are scoped, where secrets live) that determine how bad the blast radius is when — not if — something eventually goes wrong. This module is about building those defaults in from the start, because retrofitting them after an incident is always more expensive and more painful than choosing them upfront.

---

## 2. Core Concepts

Concepts are grouped into two halves that build in order: credential and secret management fundamentals first (how identities and secrets are actually issued and stored), then the access-control mindset that determines how those credentials should be scoped and evaluated.

### Credential & Secret Management

- **What Is Security Hygiene? Credentials, Access, and Blast Radius**
  - **Context:** security hygiene is the set of defaults governing three questions for every identity (human or workload): how is it authenticated, how long does that authentication remain valid, and how much can it do once authenticated. Those three defaults — credential lifetime, storage location, and permission scope — are what determine blast radius: how much damage a single leaked credential or compromised pipeline can cause. Every concept below is a specific answer to one of those three questions.
  - **Illustration:** not needed — conceptual framing, made concrete by the credential and access-control concepts that follow.
- **Secret Management**
  - **Context:** the practice of storing, distributing, and rotating sensitive values (API keys, database passwords, tokens) through a dedicated system (a secrets manager or vault) rather than embedding them in source code, config files, container images, or documentation.
  - **Illustration:** [x] needed — a comparison diagram: a secret hardcoded in a repo/image (visible to anyone with read access, permanent in history) versus a secret fetched at runtime from a secrets manager (short-lived, access-logged, rotatable).
- **Static Credentials**
  - **Context:** long-lived access keys or passwords that remain valid until manually rotated or revoked; if leaked, they grant an attacker access for as long as they remain unnoticed and unrotated — which, in practice, is often measured in months or years.
  - **Illustration:** not needed — definitional, contrasted directly against OIDC below.
- **OIDC / Workload Identity Federation**
  - **Context:** a mechanism (OpenID Connect) that lets a CI/CD pipeline or workload authenticate to a cloud provider using a short-lived, cryptographically verifiable identity token issued for that specific job run, instead of a stored static credential — the cloud provider trusts the token issuer (e.g., the CI platform) and grants temporary access based on it.
  - **Illustration:** [x] needed — a sequence diagram contrasting a pipeline using a stored static key (secret sitting in config indefinitely) versus a pipeline requesting a short-lived OIDC token from the CI platform, exchanging it for temporary cloud credentials, and the token expiring at job end.

### Access Control & Security Mindset

- **Principle of Least Privilege**
  - **Context:** granting an identity (human or workload) only the specific permissions it needs to do its job, and nothing more; the opposite failure mode is granting broad or administrator-level access "to save time" or "in case it's needed later."
  - **Illustration:** [x] needed — a comparison of an overly broad IAM policy (wildcard resource/action) versus a scoped policy granting only the specific actions and resources required.
- **"It Works" vs. "It's Safe"**
  - **Context:** functional correctness (the system behaves as intended under expected conditions) and security posture (the system resists misuse, leakage, or abuse under adversarial conditions) are independent properties; a system can pass every functional test and still be trivially exploitable, because passing tests were never designed to probe for that.
  - **Illustration:** not needed — conceptual distinction best conveyed through the case study.

---

## 3. Case Studies / Real-World Examples

1. **The 2025 Red Hat GitLab consulting repository compromise → the case for OIDC federation**
   - **Scenario:** In October 2025, a threat actor calling itself "Crimson Collective" breached a self-hosted GitLab instance used by Red Hat's consulting business, claiming access to thousands of private repositories and hundreds of Customer Engagement Reports (CERs). The CERs were not just documentation — they contained network diagrams, configuration data, authentication tokens, and full database URIs for client environments, meaning the reports themselves functioned as both a map of client infrastructure and a set of working keys into it.
   - **Security Hygiene in Action:**
     - *Secret Management:* long-lived credentials had been embedded directly in consulting deliverables rather than issued and stored through a managed secrets system, so a single repository compromise exposed live access to many client environments at once.
     - *Static Credentials:* because the exposed tokens were long-lived, their exposure translated directly into standing access for the attacker until each one was individually identified and revoked — there was no automatic expiry to limit the damage.
     - *"It Works" vs. "It's Safe":* embedding real credentials in a report is the kind of shortcut that "works" for the immediate goal (giving a client a usable reference document) while being fundamentally unsafe, since the report's distribution and storage were never designed with credential-grade access control.
   - **Outcome:** the recommended remediation — echoed broadly across the industry response to this incident — was to migrate toward short-lived, identity-driven credentials issued just-in-time via workload identity federation (including OIDC-based federation for CI/CD access to cloud providers), so that no long-lived static secret exists in a document or repository to be stolen in the first place, and to systematically scan existing repositories for embedded secrets rather than assuming there are none.

2. **A CI pipeline's static cloud key leaks via a public fork**
   - **Scenario:** A pipeline stores a long-lived cloud provider access key as a CI variable so it can deploy infrastructure changes. A contributor accidentally logs the key's value in a debug step, and the log output is visible to anyone who can view the (semi-public) pipeline run.
   - **Security Hygiene in Action:**
     - *Static Credentials:* because the key was long-lived and broadly scoped, its accidental exposure in a log meant standing access until someone noticed and manually revoked it.
     - *OIDC / Workload Identity Federation:* had the pipeline used OIDC-based federation instead, the equivalent leaked value would have been a token already expired by the time anyone could misuse it, and scoped to that single job run.
   - **Outcome:** the team migrates its pipelines from static keys to OIDC federation, eliminating the class of incident entirely rather than just improving log redaction.

3. **An IAM policy granted "just to unblock a deploy"**
   - **Scenario:** Under deadline pressure, an engineer grants a deployment role full administrative access to a cloud account "temporarily" to unblock a release, intending to scope it down later. The scoped-down version never happens.
   - **Security Hygiene in Action:**
     - *Principle of Least Privilege:* the temporary broad grant becomes the permanent, unaudited baseline, meaning a compromise of that one deployment role's credentials would grant an attacker full account control rather than the narrow set of actions the deploy actually needed.
   - **Outcome:** a subsequent access review flags the role, and the team adopts a policy that any "temporary" broad grant must have an expiry date and a tracked follow-up task, not just a verbal intention to fix it later.

---

## 4. Best Practice Checklist / Frameworks

- Never store secrets in source code, config files, container images, or documentation — use a dedicated secrets manager with access logging and rotation.
- Prefer OIDC-based workload identity federation over static, long-lived cloud credentials for CI/CD pipelines and other automated workloads wherever the platform supports it.
- Apply the principle of least privilege by default: grant the minimum permissions needed for the task, and treat any "just in case" broad grant as technical debt with a tracked expiry, not a permanent fixture.
- Rotate any credential that is discovered in a place it shouldn't be (a log, a document, a public repo) immediately, and assume it is compromised the moment it's found there — don't wait to confirm misuse.
- Remember that passing functional tests is not evidence of security; test for misuse and abuse paths deliberately, they are not caught by the same tests that confirm a feature works.
- Periodically audit existing repositories, documents, and pipelines for embedded secrets rather than assuming secret hygiene is a one-time setup step.
- Don't try to cover every compliance framework or every cloud provider's IAM nuances exhaustively in this module — the goal is the underlying defaults (short-lived over static, scoped over broad, managed over embedded) that transfer across any specific platform.

---

## 5. Sources

- Aembit, "Red Hat's GitLab Breach and the Cost of Embedded Credentials" — https://aembit.io/blog/red-hats-gitlab-breach-and-the-cost-of-embedded-credentials/
- OpenID Foundation, "OpenID Connect Core 1.0" — https://openid.net/specs/openid-connect-core-1_0.html
- GitHub Docs, "About security hardening with OpenID Connect" — https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- GitLab Docs, "Connect to cloud services" (OIDC/ID token federation) — https://docs.gitlab.com/ci/cloud_services/
- NIST, "Digital Identity Guidelines" (SP 800-63) — https://pages.nist.gov/800-63-3/
- OWASP, "Least Privilege" — https://owasp.org/www-community/Access_Control#least-privilege
- **Video lectures:** none cited.
