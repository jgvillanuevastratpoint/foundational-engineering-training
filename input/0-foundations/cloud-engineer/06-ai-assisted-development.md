# AI-Assisted Development — Training Module Source Document

> Source document feeding Skill 1 (Research Synthesizer) → Skill 2 (Learning Path Architect) → Skill 3 (Module Content Builder). Quiz content is intentionally excluded from authoring here — Skill 5 (Quiz Generator) owns that. No hands-on tasks or rubrics — this pipeline is quiz-only.

---

## 0. Module Metadata

- **Audience:**
  - **Cloud Engineers:** cloud engineers increasingly use AI assistants to generate infrastructure-as-code, scripts, and pipeline configuration — code that, if subtly wrong, can provision the wrong resource, grant excess permissions, or silently diverge from an existing module's conventions; the review burden for AI-generated infrastructure code is at least as high as for AI-generated application code, arguably higher given the blast radius.
- **Video lecture (if any):** None yet produced. If recorded, keep to one ~20-minute session covering prompting, review, and rejection as one continuous workflow narrative.
- **Learning objectives:**
  1. Explain what an AI coding assistant does and does not know about a given environment by default.
  2. Identify what information a prompt needs to include for an AI assistant to generate infrastructure-relevant code correctly (context, constraints, existing conventions).
  3. Explain why AI-generated code requires the same or greater review scrutiny as human-written code, and identify categories of error specific to AI generation (plausible-looking but wrong, outdated APIs, invented interfaces).
  4. Identify the conditions under which AI-generated code should be rejected outright rather than fixed inline.
  5. Distinguish tasks in a cloud engineering workflow where AI assistance is well-suited from tasks where it is not.

---

## 1. Why This Subject Matters (Motivation)

An AI assistant can generate a Terraform module, a shell script, or a Kubernetes manifest in seconds — and it can generate one that looks entirely plausible while granting a wildcard IAM permission, referencing a deprecated API version, or inventing a configuration option that doesn't exist for the resource in question. The risk isn't that AI-generated code is always wrong; it's that when it's wrong, it's wrong in a way that reads as confident and correct, which is exactly the failure mode human reviewers are worst at catching if they let their guard down because "the AI wrote it." Getting real value out of AI-assisted development means knowing how to prompt it with enough context to get a useful first draft, how to review its output with the specific skepticism it requires, and — just as important — when to reject its output entirely and either fix the prompt or do it yourself.

---

## 2. Core Concepts

Concepts are grouped into two halves that build in order: how AI assistance actually fits into a cloud engineering workflow, then the judgment calls (accept, reject, or redirect) that a competent user of that workflow has to make.

### Working With an AI Assistant

- **What Is AI-Assisted Development, and Where Does the Assistant Fit?**
  - **Context:** an AI coding assistant is a collaborator that drafts code, configuration, or explanations from a natural-language prompt, trained on patterns from a large body of existing code rather than on your specific environment. It has no access to your team's unstated conventions, your cost constraints, or your security posture unless you supply them — its output quality is a direct function of what it's given and how critically that output is then checked, not a fixed property of the tool.
  - **Illustration:** not needed — conceptual framing, made concrete by the prompting and review concepts that follow.
- **Prompting with Sufficient Context**
  - **Context:** an AI assistant's output quality depends heavily on what context it's given — existing code conventions, the specific cloud provider/version in use, constraints (cost, compliance, existing module structure); a vague prompt produces plausible-but-generic output that may not fit the actual environment.
  - **Illustration:** [x] needed — a side-by-side comparison of a vague prompt ("write a Terraform module for an S3 bucket") versus a well-scoped prompt (naming the provider version, existing naming conventions, required encryption/versioning settings) and the differing quality of likely output.
- **Reviewing AI-Generated Code**
  - **Context:** AI-generated code should be reviewed with the same rigor as any other contributor's code — arguably more, because AI models can produce confident-sounding output that references outdated APIs, invents plausible-but-nonexistent configuration options, or subtly misapplies a pattern copied from an unrelated context.
  - **Illustration:** not needed — best conveyed through case studies with concrete examples of each error category.
- **Categories of AI-Generation-Specific Error**
  - **Context:** distinct failure patterns worth naming explicitly: (1) plausible-but-wrong logic that reads fine but doesn't do what's needed, (2) outdated or deprecated API/provider syntax from training data, (3) "hallucinated" interfaces — parameters, resources, or CLI flags that sound real but don't exist.
  - **Illustration:** not needed — definitional, illustrated via case studies.

### Judgment Calls

- **Rejecting AI Output Outright**
  - **Context:** not every flawed AI output should be patched inline; when the generated approach is architecturally wrong, insecure by construction, or the reviewer can't fully verify correctness in the available time, the correct response is to discard it and re-prompt with more constraints or write it manually — not to accept a confidently-worded partial fix.
  - **Illustration:** not needed — conceptual, illustrated via case study.
- **Where AI Belongs (and Doesn't) in the Workflow**
  - **Context:** AI assistance tends to be well-suited to boilerplate generation, first-draft scaffolding, explaining unfamiliar code, and repetitive transformations, and poorly suited to novel architectural decisions, security-sensitive design choices, and anything where the "obviously correct" answer requires judgment about tradeoffs specific to the organization's context.
  - **Illustration:** [x] needed — a simple two-column list contrasting well-suited tasks (boilerplate, scaffolding, explaining code) against poorly-suited tasks (security architecture decisions, novel system design, judgment calls with organization-specific tradeoffs).

---

## 3. Case Studies / Real-World Examples

1. **A hallucinated Terraform argument that silently failed on apply**
   - **Scenario:** An engineer prompts an AI assistant for a Terraform resource block for a managed database, and the assistant includes a plausible-sounding argument name for enabling encryption that does not actually exist in that provider's resource schema. The `terraform plan` step errors out, but the engineer initially assumes it's a version mismatch rather than a fabricated argument.
   - **AI-Assisted Development in Action:**
     - *Categories of AI-Generation-Specific Error:* this is a textbook "hallucinated interface" — a parameter that sounds exactly like what the real one should be named, generated with full confidence.
     - *Reviewing AI-Generated Code:* checking the argument against the actual provider documentation (rather than trusting that it compiled/looked right) is what catches this before it reaches a real environment.
   - **Outcome:** the team adopts a rule that any AI-suggested provider argument or API field must be cross-checked against current official documentation before merging, not just checked for "does it look plausible."

2. **A cost-blind autoscaling config that "worked" in review**
   - **Scenario:** An AI assistant is asked to generate an autoscaling configuration for a workload and produces a technically valid config that scales aggressively and without an upper bound, optimizing purely for responsiveness. It's reviewed only for syntactic correctness and merged.
   - **AI-Assisted Development in Action:**
     - *Prompting with Sufficient Context:* the original prompt didn't specify a cost ceiling or maximum instance count, so the assistant had no basis to include one — the gap is a prompting failure, not purely a generation failure.
     - *Where AI Belongs (and Doesn't):* the judgment call of balancing responsiveness against cost is organization-specific and was never actually delegated to the AI in a way it could act on; the reviewer needed to supply that constraint, either in the prompt or in review.
   - **Outcome:** the config causes an unexpectedly large bill during a traffic spike; the team adds a standing prompt template for autoscaling requests that always requires specifying min/max bounds and cost constraints explicitly.

3. **A generated IAM policy rejected outright rather than patched**
   - **Scenario:** An AI assistant is asked to draft an IAM policy for a new service and returns a policy granting a wildcard action on a wildcard resource, with an inline comment claiming this is "for simplicity during initial setup."
   - **AI-Assisted Development in Action:**
     - *Rejecting AI Output Outright:* rather than narrowing the wildcard permissions one by one, the reviewer discards the entire draft and re-prompts with the specific actions and resource ARNs required, because a wildcard-by-default draft suggests the assistant wasn't given (or didn't apply) least-privilege constraints anywhere in its reasoning, and patching individual lines risks missing others.
   - **Outcome:** the re-prompted version, generated with explicit least-privilege instructions and a list of only the required actions, passes review directly; the team notes that "least privilege only, no wildcards" is now a standing instruction in any IAM-related prompt.

---

## 4. Best Practice Checklist / Frameworks

- Give prompts real context: existing conventions, exact provider/tool versions, and explicit constraints (cost ceilings, security requirements) — don't expect the assistant to infer organization-specific tradeoffs.
- Review AI-generated infrastructure code with at least the same scrutiny as human-written code, specifically checking any provider argument, API field, or CLI flag against current official documentation rather than trusting that it looks plausible.
- Watch for the three characteristic AI-generation failure modes: plausible-but-wrong logic, outdated/deprecated syntax, and hallucinated interfaces.
- When generated output requires more than minor fixes, or its approach is fundamentally wrong or insecure, reject it and re-prompt with tighter constraints rather than patching it into a shape you can no longer fully vouch for.
- Reserve AI assistance for boilerplate, scaffolding, and explaining unfamiliar code; keep security-sensitive architecture decisions and organization-specific tradeoffs as human judgment calls, using AI output at most as a first draft to react to.
- Don't treat "the AI generated it" as either a mark of extra trust or a reason for extra suspicion beyond what's warranted — apply the same standard you'd apply to a capable but unfamiliar new team member's first PR.

---

## 5. Sources

- GitHub, "Best practices for using GitHub Copilot" — https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot
- OWASP, "OWASP Top 10 for Large Language Model Applications" — https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Anthropic, "Claude Code best practices" — https://www.anthropic.com/engineering/claude-code-best-practices
- Google Cloud, "AI-assisted software development" — https://cloud.google.com/discover/what-is-ai-assisted-software-development
- **Video lectures:** none cited.
