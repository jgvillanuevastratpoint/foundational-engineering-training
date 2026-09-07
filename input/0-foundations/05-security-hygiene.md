# Security Hygiene — Research Notes

## Why this subject matters

Functionally correct code and secure code are not the same thing, and this distinction is rarely made explicit to engineers early in their career. In practice, security failures at the level of an individual contributor are much more often the result of ordinary hygiene problems, such as a leaked static credential or an overly broad permission grant, than they are the result of a sophisticated attack technique. Because these problems are well understood and largely preventable, they are well suited to being taught directly as part of a fundamentals track, rather than left as something engineers only learn about after being involved in an incident.

## Core concepts

### Secrets management
Secrets management refers to the practice of never embedding credentials, API keys, or tokens directly into source code or container images, and instead retrieving them at runtime from a dedicated secrets management system with controlled, auditable access. Guidance from HashiCorp on managing its Vault secrets management product recommends avoiding the storage of long-lived static secrets in tools such as Terraform in the first place, and, where credentials must be used, preferring short-lived, dynamically generated credentials over long-lived static ones, specifically because short-lived credentials reduce the impact of an accidental exposure, such as a compromised state file (HashiCorp Developer, "best practices for programmatic Vault management").

A broader guide on cloud secrets management notes that a single leaked key can expose a production database, a continuous integration and deployment pipeline, and every other system that key touches, and that credential abuse is cited as the initial point of entry in a large share of data breaches (Aembit, "Secrets Management Best Practices for Cloud Environments").

### Static credentials versus workload identity federation using OpenID Connect
A static credential, such as a long-lived cloud provider access key or a service account key file, is a standing liability from the moment it is created: it does not expire on its own, it can be copied and reused indefinitely once obtained by an unauthorized party, and it remains valid until someone notices the exposure and manually rotates it. GitLab's own documentation on connecting to cloud services describes an alternative model, in which a continuous integration job authenticates using a temporary identity token, and a cloud provider's identity federation service exchanges that token for a short-lived, scoped credential valid only for the duration of that specific job (GitLab Docs, "Configure OpenID Connect with GCP Workload Identity Federation").

A guide describing the general pattern across providers explains the underlying mechanism in plain terms: instead of storing a long-lived key as a pipeline secret, a workflow presents a short-lived, cryptographically verifiable identity token, and the cloud provider's security token service exchanges that token for a temporary credential scoped to that specific job run; because the tokens are short-lived and issued per run, they cannot be reused across separate sessions the way a static key can (Firefly, "Workload Identity Federation: GitLab CI/CD and Google Cloud").

### Principle of least privilege
The principle of least privilege holds that any identity, whether a human user or an automated workload, should be granted only the permissions it actually needs to perform its current task, and no more. Google Cloud's own guidance on its Secret Manager product states this directly, recommending that organizations follow the principle of least privilege when granting permissions to secrets, limiting broad organizational ownership to a small number of secured administrator accounts, and separating environments such as staging and production so that permissions in one environment cannot be used to affect another (Google Cloud, "best practices" for Secret Manager).

A related, more advanced pattern is scoping identity federation trust policies tightly. One account of a real migration to identity federation describes a mistake in which the trust policy was initially configured too broadly, allowing any branch in a repository to assume a production deployment role, and the fix was to scope the condition down so that only the default branch could assume the production role, with a separate, less privileged role used for other branches (Vroble, "From Static Keys to Zero Trust: How OIDC-Driven Ephemeral Identities Slashed Our CI/CD Risk by 70%"). This illustrates that adopting a more modern authentication mechanism does not automatically produce a secure outcome; the permissions attached to that mechanism still need to be scoped deliberately.

## Real-world case study: the 2025 breach of Red Hat's self-managed GitLab instance

In October 2025, a group identifying itself as "Crimson Collective" publicly disclosed a breach of a self-managed, self-hosted instance of GitLab Community Edition operated by Red Hat's consulting division. Red Hat confirmed the incident and clarified that it involved specifically an instance used for its consulting engagements, and was explicit that this incident did not involve any breach of GitLab's own managed, cloud-hosted product or infrastructure (GitLab Support, "FAQ: Data breach of Red Hat's self-managed GitLab instance"). GitLab's own statement, quoted in that support article, stated plainly that there had been no breach of GitLab's managed systems or infrastructure, and that the incident referred only to Red Hat's separately operated, self-managed instance.

Reporting on the incident describes the attackers claiming to have exfiltrated roughly five hundred seventy gigabytes of compressed data from more than twenty-eight thousand internal repositories, including approximately eight hundred internal documents called Customer Engagement Reports, which were used to record details of client engagements (Security Boulevard, "Red Hat's GitLab Breach and the Cost of Embedded Credentials"). Analysis of the incident notes that these reports mixed architectural context, such as network diagrams and configuration data, with live authentication tokens and, in some cases, full database connection strings, meaning the stolen documents functioned simultaneously as a map of a client's environment and as a set of working keys into that environment (Security Boulevard, "Red Hat's GitLab Breach and the Cost of Embedded Credentials").

Commentary following the incident drew a consistent lesson: the underlying failure was not a sophisticated attack technique, but the accumulation of static, long-lived credentials embedded in documents and repositories over time, and the recommended remediation was to apply workload identity federation and just-in-time, short-lived credentials broadly across development and consulting platforms, so that static tokens do not accumulate in repositories or in delivered documents in the first place (Identity Defined Security Alliance, "Red Hat's GitLab Breach and the Cost of Embedded Credentials").

## Best practices summary

- Avoid embedding credentials directly in source code, container images, or delivered documents such as internal reports; retrieve credentials at runtime from a dedicated, access-controlled secrets management system instead.
- Prefer short-lived, dynamically issued credentials over long-lived static ones wherever a provider supports it, particularly for continuous integration and deployment pipelines connecting to cloud infrastructure.
- Where workload identity federation using OpenID Connect is available, use it in place of storing long-lived cloud provider keys as pipeline secrets.
- Scope any identity's permissions, and any federation trust policy's conditions, as tightly as the task actually requires; a role or policy that is broader than necessary increases the impact of any single compromise.
- Apply the principle of least privilege to human operators as well as automated systems, particularly for direct, interactive access used for debugging or operational tasks.
- Where static credentials cannot be avoided, rotate them on a defined schedule, and prefer a rotation process where the new credential is issued and validated before the old one is revoked, so that rotation does not itself create downtime pressure to delay it.

## Sources

- HashiCorp Developer, "best practices for programmatic Vault management" — https://developer.hashicorp.com/vault/docs/configuration/programmatic-best-practices
- Aembit, "Secrets Management Best Practices for Cloud Environments" — https://aembit.io/blog/best-practices-for-secrets-management-in-the-cloud/
- HashiCorp Developer, "Cloud access management" (Vault) — https://developer.hashicorp.com/vault/docs/concepts/cloud-access-management
- Google Cloud, "best practices" (Secret Manager) — https://cloud.google.com/secret-manager/docs/best-practices
- AWS Prescriptive Guidance, "Security best practices" (Terraform AWS Provider) — https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/security.html
- GitLab Docs, "Configure OpenID Connect with GCP Workload Identity Federation" — https://docs.gitlab.com/ci/cloud_services/google_cloud/
- Firefly, "Workload Identity Federation: GitLab CI/CD and Google Cloud" — https://www.firefly.ai/academy/setting-up-workload-identity-federation-between-gitlab-ci-cd-and-google-cloud
- GitLab, "OIDC simplifies GitLab CI/CD authentication with Google Cloud" — https://about.gitlab.com/blog/introduction-of-oidc-modules-for-integration-between-google-cloud-and-gitlab-ci/
- Vroble, "From Static Keys to Zero Trust: How OIDC-Driven Ephemeral Identities Slashed Our CI/CD Risk by 70%" — https://www.vroble.com/2025/11/from-static-keys-to-zero-trust-how-oidc.html
- GitLab Support, "FAQ: Data breach of Red Hat's self-managed GitLab instance" — https://support.gitlab.com/hc/en-us/articles/23301188655900-FAQ-Data-breach-of-Red-Hat-s-self-managed-GitLab-instance
- Security Boulevard, "Red Hat's GitLab Breach and the Cost of Embedded Credentials" — https://securityboulevard.com/2025/10/red-hats-gitlab-breach-and-the-cost-of-embedded-credentials/
- Identity Defined Security Alliance, "Red Hat's GitLab Breach and the Cost of Embedded Credentials" — https://www.idsalliance.org/blog/red-hat-gitlab-breach/
- GitGuardian, "Red Hat GitLab Data Breach: The Crimson Collective's Attack" — https://blog.gitguardian.com/red-hat-gitlab-breach-the-crimson-collectives-attack/
- DeepStrike, "Red Hat GitLab Breach 2025: 28,000 Customers at Risk" — https://deepstrike.io/blog/red-hat-acknowledges-gitlab-hack-resulting-in-data-breach

Note: readers should be careful to distinguish this incident, which involved a self-managed GitLab Community Edition instance operated by Red Hat's consulting division, from GitLab's own managed, cloud-hosted product, which both GitLab and Red Hat's own disclosures state was not affected.
