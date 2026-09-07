# AI-Assisted Development — Research Notes

## Why this subject matters

Artificial intelligence coding assistants are now a standard part of software development work rather than an optional accelerant, but the available evidence on outcomes is mixed and worth taking seriously. Several 2026 industry studies report that pull requests containing artificial-intelligence-generated code are merged less often than human-authored pull requests, contain more logic errors and security issues, and are associated with an overall increase in review time even as the total volume of pull requests goes up. A fundamentals track that ignores this subject prepares engineers for a job that no longer exists in its previous form; one that treats generated code as automatically trustworthy risks teaching engineers to ship defects faster than before.

## Core concepts

### Documented outcomes for AI-generated code
A guide on reviewing artificial-intelligence-generated code cites research reporting that such code produces roughly one point seven times as many issues per pull request compared to human-written code, with logic errors up seventy-five percent and security vulnerabilities between one point five and two times higher, attributing this figure to CodeRabbit research from December 2025 (CodeAnt, "How to Review AI-Generated Code in 2026: Pipeline, Tools, and Best Practices"). The same source cites separate research from Faros AI, based on more than ten thousand developers, finding that teams with high adoption of these tools merge ninety-eight percent more pull requests, but that pull request review time increases ninety-one percent, and cites a further data point from LinearB's 2026 benchmarks, based on eight point one million pull requests across forty-eight hundred engineering teams, showing an acceptance rate of thirty-two point seven percent for artificial-intelligence-generated pull requests compared to eighty-four point four percent for human-written ones.

Separately, a senior-developer playbook on the subject cites Sonar's 2026 developer survey finding that engineers reported forty-two percent of their committed or contributed code was generated or significantly assisted by artificial intelligence, up from six percent in 2023, and argues that this shift in volume has moved the practical bottleneck in software delivery from writing code to verifying it (RockB, "LLM Coding Workflow Best Practices 2026: A Senior Developer's Playbook").

### Failure modes specific to generated code
Sources describing these tools' failure modes distinguish them from ordinary human coding mistakes. Described patterns include generated code referencing functions or interfaces that do not actually exist (sometimes called a hallucinated interface), code that is locally plausible on its own but fails to account for how the rest of a real system actually behaves (described as context blindness), and a consistently repeated but subtly incorrect pattern spread across an entire change, because the tool was confidently consistent rather than confidently correct (CodeAnt, "How to Review AI-Generated Code in 2026: Pipeline, Tools, and Best Practices").

### Scope-first review
One practitioner account describes a specific technique for reviewing generated code without either reading every line individually or rubber-stamping the change: agree on a short scope and a small number of concrete, checkable acceptance criteria before code is generated or accepted, so that the review question becomes whether the implementation satisfies the stated criteria, rather than an open-ended attempt to judge whether the entire change is correct (Aviator Blog, "AI Code Review Best Practices").

### Where these tools belong, and where they do not
A guide comparing what generated code review tools are good at versus what still requires a person draws a direct line: automated tools are well suited to catching best-practice violations, such as hardcoded secrets or missing error handling, while questions of business logic correctness, architecture decisions, and whether a change actually meets a real user or product need are described as requiring a person, because these require judgment about the wider system rather than pattern recognition within a single change (Fungies.io, "AI Code Review Automation: The Complete Workflow Guide for Development Teams in 2026"). The same source frames the effective split plainly: automated tools for one category of concern, and people for the other, describing this division as the workflow that has been found to actually work.

A separate guide on integrating these tools into review recommends treating them explicitly as an early review layer rather than a final reviewer: a typical described workflow has the assistant review a proposed change first, the author accepts, rejects, or discusses each suggestion, and only then does a human reviewer examine the updated change before it is approved (Sigma Browser, "How to Use AI in Code Review: Tools, Workflow, and Best Practices").

### Separating modes of work
A playbook aimed at senior developers describes organizing work with these tools into explicit, separate modes: a research mode, in which the tool reads existing code, documentation, and test output without making any changes; a planning mode, in which it proposes a set of steps, risks, and affected areas for a person to approve; an implementation mode, in which it edits only the approved scope; and a verification mode, in which it runs tests and reports what passed and what failed (RockB, "LLM Coding Workflow Best Practices 2026: A Senior Developer's Playbook"). The stated purpose of separating these modes explicitly is to give a person a clear review checkpoint at each stage, rather than a single, larger decision about whether to trust an entire finished change at the end.

## Best practices summary

- Review artificial-intelligence-generated changes with at least as much scrutiny as human-authored ones, not less, given the documented difference in issue rates and acceptance rates.
- Agree on a short, explicit scope and a small number of checkable acceptance criteria before code is generated, so review can focus on whether those criteria are met.
- Use automated tools to catch a first layer of concerns, such as best-practice violations, missing error handling, and known security issues, before a human reviewer spends time on the change.
- Reserve business-logic correctness, architectural fit, and product-alignment judgments for a person, since these require context an automated tool does not reliably have.
- Require an explicit accept, reject, or discuss decision on generated suggestions, rather than allowing them to be merged by default, so there is a clear record of what a person actually reviewed and approved.
- Apply the same pull request hygiene standards described in the Git and code review discipline subject (small, focused changes; clear descriptions) regardless of whether a person or a tool authored the change, since generated changes tend to produce larger diffs by default unless a person constrains them.

## Real-world examples

- LinearB's benchmark data, drawn from millions of pull requests across thousands of engineering teams, is cited specifically to demonstrate a large, measurable gap between the acceptance rate of artificial-intelligence-generated and human-authored pull requests, illustrating that this is an industry-wide pattern rather than an issue specific to any single company or tool (CodeAnt, "How to Review AI-Generated Code in 2026: Pipeline, Tools, and Best Practices").
- Tooling vendors in this space, such as CodeAnt AI, have built dedicated products that combine static analysis, secrets detection, infrastructure-as-code scanning, and generated-code-specific review into a single pull request workflow, reflecting an industry response to failure modes that traditional diff-based human review and rule-based static analysis alone were found to miss (CodeAnt, "Code Review Best Practices for Developers in 2026").
- The mode-separated workflow described by senior-developer playbooks (research, plan, implement, verify) has emerged as a recommended pattern specifically for agentic coding tools capable of modifying files directly in a real repository, rather than only suggesting inline code snippets (RockB, "LLM Coding Workflow Best Practices 2026: A Senior Developer's Playbook").

## Sources

- CodeAnt, "How to Review AI-Generated Code in 2026: Pipeline, Tools, and Best Practices" — https://codeant.ai/blogs/how-to-review-ai-generated-code
- CodeAnt, "Code Review Best Practices for Developers in 2026" — https://codeant.ai/blogs/code-review-best-practices
- Aviator Blog, "AI Code Review Best Practices" — https://www.aviator.co/blog/ai-code-review-best-practices/
- Fungies.io, "AI Code Review Automation: The Complete Workflow Guide for Development Teams in 2026" — https://fungies.io/ai-code-review-automation-guide-2026/
- Sigma Browser, "How to Use AI in Code Review: Tools, Workflow, and Best Practices" — https://www.sigmabrowser.com/blog/what-you-need-to-know-about-integrating-ai-into-code-review-for-better-results
- RockB, "LLM Coding Workflow Best Practices 2026: A Senior Developer's Playbook" — https://baeseokjae.github.io/posts/llm-coding-workflow-best-practices-2026/

Note: the figures reported above (issue rates, acceptance rates, adoption percentages) are attributed by the source articles themselves to third-party research groups, including CodeRabbit, Faros AI, LinearB, and Sonar. Readers who want to cite these statistics directly in training material should attempt to locate and verify the original research reports from those named organizations rather than relying solely on secondary summaries, since figures like these can be updated or superseded as newer studies are published.

Additonal information from the inhouse AI-SDLC training. 
The Universal Working Cycle
The same four-step cycle runs through every module and every task, at every scale. When something goes wrong in AI-assisted work, the diagnosis is always the same: which step was skipped?
01
Evaluate
Understand the task and its constraints before touching the AI. Read the Dev Task, the acceptance criteria, the ADR. Know what you're building.
02
Plan
Prompt for a plan first — not output. Review it against the spec. Correct misalignments at plan time, not after generation.
03
Apply
Execute, staying grounded in the plan. Redirect the AI if it drifts. You own every line — if you can't explain it, don't commit it.
04
Validate
Verify against the quality bar. Run the checklist, the tests, the gate. "Feels done" is not done.

From <https://ai-sdlc-training.stratpoint.io/framework> 

Training Requirements:
claude.ai (free) — sign up with your email at claude.ai. The free plan is session-based: usage resets on a rolling five-hour window, and how much you can send varies with overall demand. In practice you produce an artifact, hit the limit, and pick up again after the window refreshes. Plan your Tuesday–Thursday work around that rhythm — draft in focused sessions rather than one long marathon.
Gemini on the web (free) — available through your Google account at gemini.google.com, and through your @stratpoint.com Workspace account for longer documents. Use it as a genuine alternative: generate the same artifact in both, then keep whichever output better satisfies the quality-bar checklist and passes the Friday gate.
OpenCode Zen and the Big Pickle model
OpenCode Zen is OpenCode's curated model gateway — a tested set of models served by the OpenCode team, used like any other provider (sign in, get an API key, run /connect, then /models to pick one). Big Pickle is a stealth model on Zen — free during its current preview period, with a 200K-token context window and tool-calling and reasoning support. It is strong at code analysis, documentation, and implementation planning, which makes it a low-cost way to practice the framework's planning steps.

From <https://ai-sdlc-training.stratpoint.io/module-1> 


Part 4 — MCP Setup
Model Context Protocol (MCP) connects your AI tools to live project data — repositories, filesystems, databases, documentation. Think of MCP servers as plugins.
Scopes
Scope	Who sees it	When to use
local	Only you, only this directory	Testing a new MCP server
user	Only you, across all projects	Personal tools (your Drive, your calendar)
project	Everyone on the team (committed to .mcp.json)	Team tools (project GitHub, shared filesystem, database)
Core MCP Servers
Set these up to be productive on day one:
GitHub
claude mcp add github \
  -- npx -y @modelcontextprotocol/server-github \
  --scope user
 
# Test:
# claude "show me my open PRs on the ai-sdlc repo"
Filesystem
claude mcp add fs \
  -- npx -y @modelcontextprotocol/server-filesystem \
  /path/to/project \
  --scope project
 
# Test:
# claude "read docs/known-issues.md and summarize"
Google Drive
claude mcp add gdrive \
  -- npx -y @anthropic-ai/mcp-gdrive \
  --scope user
 
# Test:
# claude "list documents in my project folder on Drive"
Supabase (if applicable)

From <https://ai-sdlc-training.stratpoint.io/module-1> 


Note: to add the set up tools


Framework Foundations
The Four Principles
Principle	What it means
AI Augments, Humans Decide	Every AI output passes through human review. Anyone can press the keys; only the named owner signs off.
Structure Before Speed	Invest in artifacts before engineering. The BRD, PRD, Architecture, and Dev Tasks are the substrate AI uses to produce useful code. Skip them and you pay in Week 3.
Continuous Validation	Quality gates are distributed across phases, not deferred to the end. Fix Week 1 problems at Week 1’s gate — not in Week 3.
Traceability as First-Class	Every feature traces: BRD → PRD → Architecture → Dev Tasks → code → tests. A broken chain is a gap to fix, not ignore.

From <https://ai-sdlc-training.stratpoint.io/module-2> 

The Five Pillars
Pillar	What it covers
I — Roles & Accountability	Who owns what. Each artifact has exactly one named owner who signs off.
II — Artifact Governance	The structured documents connecting phases. Each has a template, a quality bar, and an owner.
III — AI Integration Layer	Where AI is applied (drafting, reviewing, generating) and where it’s gated (human review, sign-off).
IV — Phase Model	The 6 sequential phases, each with entry conditions, activities, outputs, and an exit gate.
V — Quality & Validation	Gates, peer reviews, acceptance criteria, self-checks. Quality distributed across the timeline.

From <https://ai-sdlc-training.stratpoint.io/module-2> 

The Verification Ladder
Every artifact passes three layers before approval. Each catches what the others miss.
Layer	Who	Catches
1 — Self-check	Artifact owner	Obvious gaps. Cheap, fast. Walk the quality bar yourself before declaring ready.
2 — Peer review	Most-affected downstream role	Implicit assumptions, missing handoff context the owner can’t see.
3 — Gate review	Cohort + facilitator	Cohort alignment. Sign-off form filled, verdict recorded.

From <https://ai-sdlc-training.stratpoint.io/module-2> 

Prompt Engineering

Where Each Technique Gets Used
Technique	Where you apply it downstream
Role + Context + Task + Format + Constraints	Every prompt, every module — BRD/PRD drafting (M2), implementation (M5), agent system prompts (M6)
Chain of thought	Architecture decisions and debugging (M2, M5)
Least-to-most decomposition	PRD generation, large refactors, messy requirement cleanup (M2, M5)
Few-shot examples	Matching a team format — test stubs, user stories (M2, M5)
Iterative refinement (the cycle)	Every artifact in every module
Prompts → agents → skills	Building reusable assets (M6); context isolation (M4)

From <https://ai-sdlc-training.stratpoint.io/module-3> 
Your go-to structure for any serious prompt. Five parts. Once it’s automatic, your output quality jumps.
Part	What it does	Example
Role	Sets the expertise and lens	“You are a senior backend engineer reviewing for security.”
Context	Provides relevant background	“This is a Python Flask API handling user authentication.”
Task	States exactly what you want	“Review the following function for SQL injection.”
Format	Describes the output shape	“List each issue with line number, severity, and fix.”
Constraints	Sets boundaries	“Focus only on security, not style or performance.”

From <https://ai-sdlc-training.stratpoint.io/module-3> 

Part 2 — Core Techniques
Zero-Shot vs Few-Shot
Zero-shot: ask directly, no examples — works for common tasks. Few-shot: provide 2–5 example input/output pairs — use when you need a specific pattern or format matched (test stubs in your team’s style, user stories in a fixed shape).
# Few-shot: give the pattern, then the real input
Generate a unit test stub in this format:
 
Example 1:
  Input: function add(a, b)
  Output: test('add returns sum', () => { ... })
 
Example 2:
  Input: function isEven(n)
  Output: test('isEven detects even numbers', () => { ... })
 
Now generate one for: function parseDate(str)
Chain of Thought
Instruct the model to reason step-by-step before answering. Use for complex problems: debugging, architecture decisions, analysis.
Direct:  "Should we use REST or GraphQL for this API?"
 
Chain of thought:
"Think through this step by step.
 1. List the client consumers.
 2. Evaluate data fetching patterns.
 3. Assess team expertise.
 4. Recommend REST or GraphQL with justification."
Least-to-Most Decomposition
Break a complex task into sub-tasks, solve each in sequence. Each output feeds the next prompt. Use for complex features, multi-step refactors, and long documents — this is the technique behind the BRD/PRD work in Module 2 and the messy-requirement cleanup.
# Least-to-most for PRD generation
Step 1: "Generate a PRD outline for user authentication."
Step 2: "Expand section 2.1 with 5 concrete user stories."
Step 3: "For each user story, add acceptance criteria."
Step 4: "Review the complete PRD and flag any gaps."
Delimiters & Output Formatting
Separate instructions from content with triple backticks, XML tags, or ---. Ask for structured output (JSON, Markdown tables, YAML). Delimiters also reduce prompt-injection risk.
Negative Prompting
Tell the model what NOT to do — sparingly. Too many negatives confuse it; prefer positive framing where you can.
Do not suggest Django.
Do not use deprecated Python 2 syntax.

From <https://ai-sdlc-training.stratpoint.io/module-3> 

Part 4 — From Prompts to Agents to Skills
Once you’ve written a great prompt, the next question is how to reuse it without retyping. Three layered customization mechanisms. You’ll see the map here; you build them hands-on in Module 6.
Layer	What it is	Use when
Rule	Always-on guidance the AI sees at the start of every conversation	The guidance applies to every prompt (coding standards, output format, security policy)
Agent	A named, scoped, reusable role with its own system prompt	You have a recurring scoped role (code reviewer, BRD reviewer) to invoke by name
Skill	Packaged domain expertise loaded dynamically when relevant	Expertise that should load only when needed — not bloat every prompt
Prompt template	A reusable instruction shape that varies by parameters	A reusable shape lighter than an agent (test-from-AC, code-from-task)


Part 1 — What Is Context
Every session runs inside a context window — fixed-size working memory holding your messages, the AI’s responses, loaded files, and the system prompt (including AGENTS.md). When it fills up, older content gets pushed out or compressed. The AI doesn’t announce this — it just starts producing worse output.
The context window is a whiteboard, not a hard drive
When the whiteboard fills, you erase the oldest notes to make room. The AI works with whatever’s still on the board. Your job: keep the most relevant information on the board at all times. Irrelevant context is as bad as missing context — it crowds out what matters.
What Fills the Window
Source	Notes
System prompt / project rules	AGENTS.md and tool-specific rules — loaded automatically, counts toward the window
Files you load	BRD, PRD, Architecture, code, ADR drafts — every file adds to the count
Conversation history	Every message and response — grows with each exchange
Tool outputs	Filesystem reads, GitHub searches, web results — each one adds context
The AI’s own reasoning	Chain-of-thought adds up fast in long sessions
Token Economics by Tool
Context is measured in tokens — roughly 0.75 words per token (1,000 tokens ≈ 750 words). Each model has a maximum window.
Tool	Approx. window	Good for	Watch out for
Claude Code (Opus 4.7 / Sonnet 4.6)	200K standard; 1M on Max / Team / Enterprise	Multi-file dev, long coding, agentic tasks	Auto-compacts near the limit — watch for quality drops before that point
OpenCode (model-dependent)	Set by the chosen model — e.g. Big Pickle 200K, or a 1M+ provider	Same dev/agentic work as Claude Code; pick the model to fit the job	Window is the model’s, not the tool’s — Big Pickle degrades well before 200K (~50–70K)
Gemini (Workspace, Gemini 2.5 Pro)	1M+ tokens	Long-context BRD/PRD/Architecture analysis, multi-doc synthesis	No auto-compact — manage manually; watch for drift in long threads
Cursor (GPT-4o / Sonnet 4.6)	128K–200K by model	Code-focused, file-grounded sessions	Smaller window — be deliberate about which files are open

Part 2 — Loading Context Deliberately
Loading is a design decision. Before any significant session, answer three questions: what does the AI need to know, what’s the minimum that covers it, and in what order should it load?
Relevant beats abundant
Load the specific sections, not the whole document. Working on auth architecture? Load the auth-related BRD requirements and PRD stories — not the full 50-page BRD.
Load in dependency order: upstream artifacts first (BRD before PRD, PRD before Architecture). The AI builds understanding layer by layer.
State what you loaded and why: “I’m loading X, Y, Z to work on [task].” Orients the AI and gives you a checkpoint.
Reload when sessions resume. The AI remembers nothing from yesterday.
What Each Role Loads in Week 2
Role	Load	Don’t over-load
Solutions Architect (Architecture)	Approved BRD + PRD first; add reference architectures and ADR drafts as needed	Don’t pre-load everything — load per section
Tech Lead (Dev Tasks)	Approved PRD + Architecture; for each story, only that story’s section	Not the full PRD at once — one story at a time
Solutions Designer (review)	BRD + PRD + early Architecture draft	Tight scope — checking BRD–Architecture consistency
Product Mgr / Designer (review)	PRD + Architecture draft	Checking UI/UX survives into architecture
Project Manager (coordination)	PRD + quality gates doc	No code or architecture detail needed
Developers (review)	Architecture + Dev Tasks draft	Checking buildability from the task alone
QA / DevOps (review)	PRD/Architecture with testability / deployability lens	Scoped to the lens, not the whole repo

Part 3 — The Session Lifecycle
Every session has a lifecycle: clean window → work → window fills → quality degrades. How you manage it decides whether you get good output for 2 hours or 20 minutes. Three strategies, one decision at each inflection point.
Strategy	What it does	Use when
Continue	Keep the current session going	Task is clearly related, context still relevant, quality still high, under ~40% of the window
Compact	Compress history, preserve key findings	One major sub-task done, starting another; session valuable but getting long
Start fresh	End the session; reload only what the next task needs	Corrected the AI 3+ times on the same mistake; output vague/contradictory; switching artifacts

