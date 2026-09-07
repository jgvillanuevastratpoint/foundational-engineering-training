# Git and Code Review Discipline — Research Notes

## Why this subject matters

A developer's ability to write working code is only part of the job. In any team setting, a developer's work has to travel through a shared history, get reviewed by other people, and remain safe to roll back if something goes wrong. Engineers who never learned this discipline tend to produce changes that are slow to review, risky to merge, and difficult to undo. This subject is about legibility: making a change easy for another engineer, or the same engineer months later, to understand, trust, and reverse if necessary.

## Core concepts

### Trunk-based development
Trunk-based development is a version-control approach where developers integrate their changes frequently, often multiple times a day, into a single shared branch (commonly called "main" or "trunk"), instead of maintaining long-lived feature branches that diverge from the shared branch for days or weeks. When branches are used at all under this approach, they are expected to live for hours, not weeks, before being merged back in.

The Atlassian documentation on the subject describes trunk-based development as a required practice for continuous integration and continuous delivery, and contrasts it with Gitflow, an alternative model built around long-lived feature branches and multiple primary branches (Atlassian, "Trunk-based Development"). The reasoning is straightforward: the longer a branch lives apart from the shared branch, the more it diverges, and the more painful and risky the eventual merge becomes.

Feature flags (also called feature toggles) are commonly paired with trunk-based development. They allow a team to merge code that is not yet finished or not yet ready for users directly into the shared branch, hidden behind a runtime toggle, rather than hiding unfinished work inside a long-lived branch (Unleash, "How To Implement Trunk-Based Development: A Practical Guide").

### Pull request and code review size
Google's internal engineering practices, published publicly as the "eng-practices" documentation, are frequently cited as the origin of several review conventions that are now common industry-wide, including small, focused changes and a shared vocabulary for review comments (for example, marking a comment as a minor/optional note versus a required change). A summary of these practices notes that Google recommends keeping pull requests small and focused on a single objective, because this makes review easier and reduces the chance that a defect goes unnoticed (Medium, Sergio Santos, "Mastering Pull Requests! A Brief Look at Google's Engineering Practices").

Multiple independent sources describe the same finding from different angles: review quality and thoroughness measurably decline once a change exceeds roughly two hundred to four hundred changed lines, and smaller changes are reviewed faster, more thoroughly, and merged more often as a result (Engineering Manager Tools, "Pull Request Size: Ideal Limits & How to Enforce Them"). A separate guide describes "rubber-stamping" — approving a change without a genuine review, often triggered by change size or delivery pressure — as a known failure mode that is more likely to occur on oversized pull requests (DEV Community, "Code Review Best Practices - The Complete Guide for Engineering Teams").

### Semantic (Conventional) commit messages
Conventional Commits is a lightweight specification for structuring commit messages using a `type(scope): description` format, where the type describes the kind of change being made (for example, a new feature versus a bug fix) (Marc Nuri, "Conventional Commits: A Complete Guide to Better Git Commit Messages"). The two required types in the specification, a new feature and a bug fix, map directly to semantic versioning: a new feature corresponds to a minor version increase, and a bug fix corresponds to a patch version increase.

This structure is not purely cosmetic. Tooling that follows the specification can automatically determine the next version number and generate a changelog directly from the commit history, removing the need for a person to manually track and summarize what changed in a release (DEV Community, "Mastering Conventional Commit Messages: A Guide for Developers"). A commit that is difficult to categorize under a single type is often a signal that the change itself is doing more than one thing and should be split into separate commits.

### Code review as a teaching moment
Beyond defect detection, code review is described across multiple sources as one of the highest-leverage moments for spreading knowledge across a team: conventions, business logic, and the reasoning behind past decisions are transferred far more effectively through review comments than through documentation alone (GitHub, mgreiler, "all-about-code-review"). Guides summarizing Google's internal practices highlight the importance of recognizing good work during review, not only flagging problems, as a way of keeping the review culture constructive rather than adversarial (Acid Tango, "How to review Pull Requests like a Google Engineer").

## Best practices summary

- Keep the shared branch always in a releasable state; a broken shared branch should be treated as an incident and fixed immediately, not left for later.
- Keep pull requests small and focused on one logical change; a widely cited soft limit is roughly two hundred changed lines, with a higher hard ceiling depending on the team.
- Use a consistent commit message structure (such as Conventional Commits) so that the history itself communicates intent and can support automated versioning and changelog generation.
- Establish a shared vocabulary for review comments so that reviewers and authors both understand which comments are optional and which are blocking.
- Assign clear ownership of code (for example, through owner files or equivalent mechanisms) so review responsibility is explicit rather than left to whoever happens to be available.
- Treat review as an opportunity to teach and to recognize good work, not only to find faults.
- Avoid approving a change without genuinely reading it, particularly under time pressure or on a large diff; if a change is too large to review carefully, ask the author to split it.

## Real-world examples

- Google's internal culture of small, reviewed changes ("CLs" in Google's internal terminology) is the origin of review conventions that have since spread to GitHub-style pull request workflows across the industry, including the practice of labeling comments by severity (Pasquale Pillitteri, "Google Code Review Guidelines: The Internal Principles That Set the Industry Standard").
- Semantic-release tooling, used across many open-source and commercial JavaScript and Node.js projects, computes version numbers and changelogs automatically from Conventional Commit history, which only works if the team consistently follows the commit convention (Shakil Alam, DEV Community, "Commit Like a Pro: A Beginner's Guide to Conventional Commits").
- Stacked pull request tooling, such as Graphite, was built specifically because keeping pull requests small is difficult to sustain without tooling support; these tools let a large change be broken into an ordered chain of small, dependent pull requests that can each be reviewed independently (DEV Community, "Code Review Best Practices - The Complete Guide for Engineering Teams").

## Sources

- Atlassian, "Trunk-based Development" — https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
- Aviator, "What is Trunk-Based Development: Advantages, Disadvantages, and Best Practices" — https://www.aviator.co/blog/trunk-based-development/
- Unleash, "How To Implement Trunk-Based Development: A Practical Guide" — https://www.getunleash.io/blog/how-to-implement-trunk-based-development-a-practical-guide
- Harness, "A Complete Guide to Trunk-Based Development" — https://www.harness.io/blog/a-complete-guide-to-trunk-based-development
- Marc Nuri, "Conventional Commits: A Complete Guide to Better Git Commit Messages" — https://blog.marcnuri.com/conventional-commits
- DEV Community (Ashen Dunusinghe via Medium), "Mastering Conventional Commit Messages: A Guide for Developers" — https://medium.com/@avdunusinghe/mastering-conventional-commit-messages-a-guide-for-developers-9cca075eab00
- DEV Community (Shakil Alam), "Commit Like a Pro: A Beginner's Guide to Conventional Commits" — https://dev.to/itxshakil/commit-like-a-pro-a-beginners-guide-to-conventional-commits-34c3
- Medium (Sergio Santos), "Mastering Pull Requests! A Brief Look at Google's Engineering Practices" — https://medium.com/@sdesantos/techietuesday-mastering-pull-requests-a-brief-look-at-googles-engineering-practices-ba808d17e3bf
- DEV Community, "Code Review Best Practices - The Complete Guide for Engineering Teams" — https://dev.to/rahulxsingh/code-review-best-practices-the-complete-guide-for-engineering-teams-2026-52a4
- Pasquale Pillitteri, "Google Code Review Guidelines: The Internal Principles That Set the Industry Standard" — https://pasqualepillitteri.it/en/news/3317/google-code-review-guidelines-internal-principles-industry-standard
- Engineering Manager Tools, "Pull Request Size: Ideal Limits & How to Enforce Them" — https://www.em-tools.io/engineering-metrics/pull-request-size
- Acid Tango, "How to review Pull Requests like a Google Engineer" — https://acidtango.com/blog/how-pull-request-google-engineer/
- GitHub (mgreiler), "all-about-code-review" — https://github.com/mgreiler/all-about-code-review/

Note: Google's original engineering practices documentation was published on GitHub as "google/eng-practices"; several of the secondary sources above summarize and reference it directly. Readers who want the primary source should search for "google eng-practices" to locate the current location of that repository, since project URLs can change over time.
