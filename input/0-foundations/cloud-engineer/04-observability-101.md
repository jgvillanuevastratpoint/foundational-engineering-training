# Observability 101 — Training Module Source Document

> Source document feeding Skill 1 (Research Synthesizer) → Skill 2 (Learning Path Architect) → Skill 3 (Module Content Builder). Quiz content is intentionally excluded from authoring here — Skill 5 (Quiz Generator) owns that. No hands-on tasks or rubrics — this pipeline is quiz-only.

---

## 0. Module Metadata

- **Audience:**
  - **Cloud Engineers:** cloud engineers are typically the ones who build and own the observability platform other teams instrument against, and they are usually first responders to infrastructure-level incidents where the difference between having logs, having metrics, and having traces determines whether a root cause is found in minutes or hours.
- **Video lecture (if any):** None yet produced. If recorded, keep to one ~20-minute session — the three pillars plus the observability-vs-monitoring distinction is a coherent single narrative.
- **Learning objectives:**
  1. Define logs, metrics, and traces and explain the kind of question each is best suited to answer.
  2. Explain why metrics, logs, and traces are not interchangeable or substitutable for one another.
  3. Explain what structured logging is and why it matters for large-scale log analysis.
  4. Distinguish observability from monitoring using a concrete test (can a new question be answered without shipping new code?).
  5. Identify the cost and cardinality tradeoffs involved in each of the three pillars.

---

## 1. Why This Subject Matters (Motivation)

During an incident, "it works on my machine" and "it was fine a few minutes ago" are useless statements — what you need is the ability to ask a new question of the running system right now, without waiting for a code deploy. Observability is the discipline of instrumenting systems so that's possible. This is a broader and more useful skill than traditional monitoring, which only answers questions someone anticipated ahead of time on a pre-built dashboard, and it is frequently under-taught relative to how often it's needed in a real incident.

---

## 2. Core Concepts

- **The Three Pillars: Logs, Metrics, and Traces**
  - **Context:** the three distinct categories of telemetry data that observability is commonly described as resting on; each answers a different kind of question and has different cost and storage characteristics.
  - **Illustration:** [x] needed — a comparison diagram showing the same request event represented as a log line, a metric data point, and a trace span, side by side.
- **Logs**
  - **Context:** the historical/archival record of discrete system events; useful for understanding exactly what happened at a specific point in time, but can consume large storage as systems grow, and unstructured logs are difficult to analyze without further processing.
  - **Illustration:** not needed — covered by the three-pillars comparison.
- **Metrics**
  - **Context:** numerical measurements of system performance and behavior (CPU usage, response time, error rate); compact and aggregated, making them more cost-effective at scale than logs, though prone to cost/cardinality blowups if label values are unbounded.
  - **Illustration:** not needed — covered by the three-pillars comparison.
- **Traces**
  - **Context:** the path of an individual request as it moves through a system, especially valuable in distributed environments where one request passes through many services; distributed tracing follows that request end-to-end.
  - **Illustration:** [x] needed — a trace waterfall diagram showing one request's spans across multiple services.
- **Why the Three Pillars Are Not Interchangeable**
  - **Context:** logs are a manual developer tool (flexible but inconsistent, human-driven), while traces are automatically generated and provide cross-service context logs alone cannot, at the cost of being less customizable; this is why they're treated as separate categories rather than one undifferentiated "telemetry."
  - **Illustration:** not needed — definitional, follows directly from the pillar definitions above.
- **Structured Logging**
  - **Context:** writing logs in a consistent, machine-parseable format (commonly JSON) rather than arbitrary text, so log data can be filtered and aggregated programmatically; correlating logs, metrics, and traces (e.g., via a shared trace ID) lets a single request's behavior be reconstructed across all three at once.
  - **Illustration:** [x] needed — a before/after comparison of an unstructured log line versus the same event as a structured JSON log with a correlation ID.
- **Observability vs. Monitoring**
  - **Context:** simply collecting logs, metrics, and traces is not, by itself, observability. The practical test: can an engineer answer a genuinely new question about system behavior without shipping new code? If only pre-anticipated dashboard questions can be answered, the system has monitoring, not observability.
  - **Illustration:** not needed — definitional, best conveyed via the case studies.

---

## 3. Case Studies / Real-World Examples

1. **A dashboard that couldn't answer the actual question**
   - **Scenario:** During an incident, a pre-built dashboard shows elevated error rates but nothing about *which* customers or *which* code path is failing, and the on-call engineer has no way to drill in without shipping a new logging statement and waiting for a redeploy.
   - **Observability 101 in Action:**
     - *Observability vs. Monitoring:* the team has monitoring (a dashboard answering an anticipated question) but not observability (the ability to ask a new question of the live system).
     - *Metrics:* the aggregated error-rate metric told them *that* something was wrong but, by design, discarded the per-request detail needed to say *what*.
   - **Outcome:** the team invests in structured, queryable logs and trace-based drill-down so that the next incident doesn't require a code change just to ask a follow-up question.

2. **A distributed request that "worked" but was mysteriously slow**
   - **Scenario:** A customer-facing request takes 4 seconds end-to-end, but every individual service's own metrics show sub-100ms response times, and no single service's logs show an obvious problem.
   - **Observability 101 in Action:**
     - *Traces:* a distributed trace reveals that the request passes through the same downstream service five times due to a retry loop invisible from any single service's local logs or metrics.
     - *Why the Three Pillars Are Not Interchangeable:* neither the metrics (aggregated, per-service) nor the logs (siloed per-service) alone could have surfaced the cross-service retry pattern; only a trace spanning the whole request could.
   - **Outcome:** the team fixes the retry logic and adopts distributed tracing as a standard requirement for any new service with more than one downstream dependency.

3. **An unbounded metric label that produced a five-figure monthly bill**
   - **Scenario:** A team adds a metric label containing the raw user ID to track per-user latency, and within weeks the time-series database's storage and query cost balloons unexpectedly.
   - **Observability 101 in Action:**
     - *Metrics:* the cost-effectiveness of metrics depends on their compact, aggregated structure; an unbounded label value (a unique ID per user) defeats that aggregation and makes the metric behave like unindexed log storage instead, at metrics-system prices.
   - **Outcome:** the team removes the high-cardinality label, replaces it with a bucketed or sampled approach, and adds a cardinality-review step before new metric labels are approved.

---

## 4. Best Practice Checklist / Frameworks

- Instrument for observability from the start of a project rather than retrofitting it after an incident has already occurred.
- Log in a structured, consistent format (e.g., JSON) so log data can be filtered and aggregated reliably instead of searched with fragile text matching.
- Correlate signals across pillars — attach a shared trace ID to related log lines and metric data points so an anomaly in one signal can be traced back to the logs/traces that explain it.
- Be deliberate about metric cardinality; unbounded label values (raw user IDs, full URLs with query strings) can spike storage and query cost without proportional value.
- Set explicit retention and cost policies for log storage rather than retaining everything indefinitely by default.
- Treat "can I answer an unanticipated question about system behavior without writing new code?" as the practical test of whether a system is actually observable, not just monitored.
- Don't try to instrument every possible signal from day one — prioritize the pillar that answers your team's most common failure mode first (often traces for distributed request-path issues, or structured logs for single-service debugging), and expand from there.

---

## 5. Sources

- Sematext, "Three Pillars of Observability: Logs, Metrics & Traces Defined" — https://sematext.com/glossary/three-pillars-of-observability/
- CrowdStrike, "The Three Pillars of Observability: Logs, Metrics, and Traces" — https://www.crowdstrike.com/en-us/cybersecurity-101/observability/three-pillars-of-observability/
- StrongDM, "Three Pillars of Observability Explained: Metrics, Logs, Traces" — https://www.strongdm.com/blog/three-pillars-of-observability
- SigNoz, "Three Pillars of Observability [And Beyond] - A Beginner's Guide" — https://signoz.io/blog/three-pillars-of-observability/
- OpenTelemetry, "What is OpenTelemetry?" — https://opentelemetry.io/docs/what-is-opentelemetry/
- Google, "Site Reliability Engineering — Monitoring Distributed Systems" — https://sre.google/sre-book/monitoring-distributed-systems/
- **Video lectures:** none cited.
