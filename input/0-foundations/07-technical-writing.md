# Technical Writing (READMEs, Architecture Decision Records, Runbooks) — Research Notes

## Why this subject matters

Poor documentation is worse than no documentation at all, because it actively misleads a reader before they discover it is wrong, costing them time on top of the time they would have spent with nothing to go on. Technical writing is frequently treated as a soft skill and rarely taught directly, despite being one of the strongest determinants of whether an engineer's work remains usable after they move to another project or leave the company. A well-built service with no explanation of what it does, no record of why it was built a particular way, and no operational guide for when it breaks becomes a liability the moment its original author is unavailable.

## Core concepts

### The README: what this is and how to use it
Multiple community guides converge on a consistent structure for a README file. A widely referenced guide describes the minimum bar as a title and a short description explaining what the project is, why it was built, and what problem it solves (JosephJamesCoop, "README-deployer", readme guide). A separate community discussion on writing a good README lists a consistent set of sections: a project overview describing what the project does and why it exists, installation and setup instructions for running the project locally, usage examples, configuration details such as environment variables or dependencies, guidance for contributors, and licensing information (GitHub community discussion, "How to write a good README?").

Another guide frames the README's purpose in stronger terms, describing it as often the first and only thing anyone will see about a piece of software, and noting that a README is frequently shipped alongside the code itself within package managers, meaning it functions as both documentation and, in effect, marketing material for the project (banesullivan, GitHub, "README: How to write a good README").

### The architecture decision record: what this is and how it differs from other documents
An architecture decision record, commonly abbreviated as an ADR, is a short document that captures a single architectural decision and the reasoning behind it. The dedicated reference site for this practice defines an architectural decision as a justified design choice addressing a requirement that has a measurable effect on a system's architecture, and defines the record itself as the artifact that captures that decision along with its trade-offs and consequences (adr.github.io, "Architectural Decision Records").

A detailed guide on the practice is explicit about what an architecture decision record is not: it is not a design document, because it explains why an approach was chosen rather than how it was implemented; it is not a request for comments, because a request for comments is a proposal for discussion while a record documents a decision that has actually been made; and it is not meeting notes, because it captures the outcome and its reasoning rather than the discussion that led to it (Archyl, "Architecture Decision Records: The Complete Guide"). The same guide notes that a well-written record can typically answer four questions in less than a page: what was the context, what options were considered, what was decided, and what the consequences are.

A separate, more operationally focused guide distinguishes these records clearly from two other formats they are sometimes confused with: records capture decisions, runbooks capture operational procedures, and README files capture how to use a system, and blurring these categories together is described as a common failure mode that produces a large volume of low-value documents where the genuinely important decisions become difficult to find (Catio, "Architecture Decision Records (ADRs): The 2026 Guide"). The same source recommends against writing a record for every minor or easily reversible choice, on the reasoning that doing so dilutes the value of the practice and trains readers to skim past records rather than take them seriously.

Guidance on where to store these records is consistent across sources: keep them close to the source code, typically in a dedicated folder within the same repository, numbered sequentially, and indexed from the README so they are easy to find later (Architect View Master, "Building an Architecture Decision Record (ADR) Library"; Red Hat, "Why you should be using architecture decision records to document your project"). One guide also emphasizes the importance of superseding an outdated record with a new one when a decision changes, rather than leaving the original record in an "accepted" state indefinitely after it no longer reflects reality, since an unmarked stale record can actively mislead a future reader (Scribelet, "Architecture decision record examples: 10 real ADRs + template").

### The runbook: what this is and how it differs from the other two
A runbook is a document written for operational use during an incident: it is meant to guide a person, often under time pressure and with limited context, through the concrete steps needed to diagnose or resolve a specific operational problem. Sources on architecture decision records consistently place runbooks in a separate category from both decision records and README files specifically because a runbook's job is procedural and situational, not explanatory or introductory (Catio, "Architecture Decision Records (ADRs): The 2026 Guide"; Archyl, "Architecture Decision Records: The Complete Guide").

## Best practices summary

- Write the README to answer what the project is, why it exists, and how to get it running, assuming the reader has no prior context; keep it current, since a stale README actively wastes a reader's time before they discover it is inaccurate.
- Document configuration and environment requirements explicitly in the README, without embedding actual secret values, consistent with the practices described in the security hygiene subject.
- Reserve an architecture decision record for decisions that are genuinely hard to reverse, cross ownership boundaries, or are likely to be questioned again later; avoid writing one for routine implementation choices, since doing so reduces the value of the practice as a whole.
- Keep each architecture decision record short, focused on a single decision, and structured around context, options considered, the decision made, and its consequences.
- Store architecture decision records close to the source code they describe, numbered sequentially, and indexed from the README so they remain discoverable.
- When a decision changes, write a new record that explicitly supersedes the old one, rather than leaving an outdated record without any indication that it no longer applies.
- Write runbooks around concrete, procedural steps aimed at a reader under time pressure, and treat an out-of-date runbook as a defect to be fixed, ideally verified periodically by actually following it rather than only reading it.
- Assign clear ownership for keeping each of these three types of documents current, particularly during staffing transitions, in the same way code ownership is transferred when someone leaves a project.

## Real-world examples

- The architecture decision record format in common use today traces back to a proposal by Michael Nygard in 2011, and has since been adopted by organizations ranging from government digital services to large-scale technology companies, according to a guide summarizing the practice's history and adoption (Archyl, "Architecture Decision Records: The Complete Guide").
- A guide focused on operationalizing the practice across a team notes that the Azure Well-Architected Framework itself references architecture decision records as part of its own guidance, and that the practice has been the subject of dedicated conference presentations on making architectural decisions visible and traceable within agile and iterative engineering processes (hidekazu-konishi.com, "Architecture Decision Records: Templates and Operational Patterns for Teams That Actually Maintain Them"; adr.github.io, "Architectural Decision Records").
- Curated collections of exemplary open-source README files are maintained publicly specifically because well-written examples are considered a practical teaching tool, and one such collection catalogs specific projects and calls out what each one does well, such as clear organization, useful badges, and a well-explained rationale for why the project exists (matiassingers, GitHub, "awesome-readme").

## Sources

- JosephJamesCoop, GitHub, "README-deployer" readme guide — https://github.com/JosephJamesCoop/README-deployer/blob/main/readme-guide.md
- GitHub community discussion, "How to write a good README?" — https://github.com/orgs/community/discussions/170496
- GitHub community discussion, "What are your best practices for writing clear and helpful README files?" — https://github.com/orgs/community/discussions/164366
- banesullivan, GitHub, "README: How to write a good README" — https://github.com/banesullivan/README
- matiassingers, GitHub, "awesome-readme: A curated list of awesome READMEs" — https://github.com/matiassingers/awesome-readme
- jehna, GitHub, "readme-best-practices" — https://github.com/jehna/readme-best-practices/blob/master/README.md
- adr.github.io, "Architectural Decision Records" — https://adr.github.io/
- Archyl, "Architecture Decision Records (ADR): The Complete Guide" — https://www.archyl.com/blog/architecture-decision-records-complete-guide
- Catio, "Architecture Decision Records (ADRs): The 2026 Guide" — https://www.catio.tech/blog/architecture-decision-record
- Red Hat, "Why you should be using architecture decision records to document your project" — https://www.redhat.com/en/blog/architecture-decision-records
- Architect View Master, "Building an Architecture Decision Record (ADR) Library" — https://www.architectviewmaster.com/blog/building-architecture-decision-record-adr-library/
- Scribelet, "Architecture decision record examples: 10 real ADRs + template" — https://scribelet.app/blog/architecture-decision-record-examples
- hidekazu-konishi.com, "Architecture Decision Records: Templates and Operational Patterns for Teams That Actually Maintain Them" — https://hidekazu-konishi.com/entry/architecture_decision_records_templates_and_operations.html
- AWS Architecture Blog, "Master architecture decision records (ADRs): Best practices for effective decision-making" — https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/
- Rockstar Developer University, "Architecture Decision Records: ADR Guide" — https://rockstardeveloperuniversity.com/architecture-decision-records-guide/
