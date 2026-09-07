# Observability 101 — Research Notes

## Why this subject matters

During an incident, statements like "it works on my machine" or "it was working a few minutes ago" are of little practical use. Observability is the discipline of instrumenting a system so that, when something unexpected happens, an engineer can ask new questions of the running system rather than being limited to whatever dashboards were built in advance. This is a broader and more useful skill than traditional monitoring, which typically only answers questions that were anticipated ahead of time, and it is frequently under-taught relative to how often it is needed in practice.

## Core concepts

### The three pillars: logs, metrics, and traces
Multiple independent sources describe observability as resting on three distinct categories of telemetry data, often called the three pillars: logs, metrics, and traces (Sematext, "Three Pillars of Observability: Logs, Metrics & Traces Defined"; CrowdStrike, "The Three Pillars of Observability: Logs, Metrics, and Traces"). Each pillar answers a different kind of question and has different cost and storage characteristics.

Logs are described as the historical or archival record of system events, which can be plain text, binary, or structured with additional metadata; they are useful for understanding exactly what happened at a specific point in time, but they can consume large amounts of storage as systems grow, and unstructured logs are difficult to analyze without additional processing (CrowdStrike, "The Three Pillars of Observability: Logs, Metrics, and Traces"; Edge Delta, "Three Pillars of Observability: Logs vs. Metrics vs. Traces").

Metrics are numerical measurements of system performance and behavior, such as processor usage, response time, or error rate. Compared to logs, metrics are described as more cost-effective at scale, because their compact, aggregated structure does not grow in the same way that log volume grows as usage increases (CrowdStrike, "The Three Pillars of Observability: Logs, Metrics, and Traces").

Traces represent the path of an individual request as it moves through a system, and are described as especially important in distributed environments, where a single request may pass through many separate services before a response is returned; distributed tracing follows that request across all of those services (Sematext, "Three Pillars of Observability: Logs, Metrics & Traces Defined").

### Why the three pillars are not interchangeable
One source frames the relationship between traces and logs directly: logs are a manual developer tool, meaning developers decide what and how to log, which makes them flexible but also inconsistent and prone to human error, while traces are automatically generated and provide context across a distributed system that logs alone cannot easily provide, at the cost of being less customizable and not offering the same code-level detail as a well-written log line (StrongDM, "Three Pillars of Observability Explained: Metrics, Logs, Traces"). This is the underlying reason the three pillars are described separately rather than as one undifferentiated category of "telemetry."

### Structured logging
A structured log is one written in a consistent, machine-parseable format, commonly JSON, rather than as an arbitrary text string. SigNoz's guide to the three pillars recommends implementing structured logging specifically so that log data is easier to parse and analyze programmatically, and recommends correlating logs, metrics, and traces by linking identifiers such as trace identifiers to log entries, so that a single request's behavior can be reconstructed across all three data types at once (SigNoz, "Three Pillars of Observability [And Beyond] - A Beginner's Guide").

### Observability versus monitoring
A DEV Community guide on the subject makes an explicit distinction that is useful for teaching purposes: simply collecting logs, metrics, and traces is not, by itself, observability. The practical test offered is whether an engineer can answer a genuinely new question about the system's behavior without needing to ship new code to find the answer; if the only questions that can be answered are the ones a pre-built dashboard already anticipated, the system has monitoring, not observability (DEV Community, "The Three Pillars of Observability: Logs, Metrics, and Traces Explained"). The same source lists common mistakes, including instrumenting a system only after an incident has already occurred, when there is no longer time to add tracing calmly, and ignoring the cost of log storage until it becomes a large, unplanned expense.

## Best practices summary

- Instrument a system for observability from the beginning of a project, rather than retrofitting it after a production incident has already occurred.
- Log in a structured, consistently formatted way (such as JSON) so that log data can be filtered and aggregated reliably rather than searched with fragile text matching.
- Correlate signals across pillars, for example by attaching a shared trace identifier to related log lines and metric data points, so an anomaly in one signal can be traced back to the specific logs and traces that explain it.
- Be deliberate about the cost and cardinality of metrics; metrics with unbounded label values can significantly increase storage and query cost without adding proportional value.
- Set explicit retention and cost policies for log storage rather than retaining everything indefinitely by default.
- Treat the ability to answer an unanticipated question about system behavior, without writing new code, as the practical definition of whether a system is actually observable.

## Real-world examples

- OpenTelemetry has become a widely adopted, vendor-neutral standard for instrumenting applications with logs, metrics, and traces, reducing the risk of an application becoming locked into a single vendor's proprietary instrumentation approach; this standard is referenced directly in guidance about correlating systemd's own structured journal logs into a broader observability pipeline (Dash0, "Managing Systemd Logs on Linux with Journalctl").
- TechTarget's overview of the three pillars notes that organizations operating cloud-native environments generally start by collecting and analyzing logs, metrics, and traces together, describing these as the most important sources of visibility into complex, distributed application environments, though not necessarily the only ones (TechTarget, "The 3 pillars of observability: Logs, metrics and traces").
- Elastic's own commentary on the three pillars argues that, for some modern systems, the traditional three signals are not suffient on their own and proposes profiling as an emerging fourth signal, which illustrates that the three-pillars framework, while foundational, continues to evolve as systems grow more complex (Elastic Blog, "The 3 pillars of observability: Unified logs, metrics, and traces").

## Sources

- Sematext, "Three Pillars of Observability: Logs, Metrics & Traces Defined" — https://sematext.com/glossary/three-pillars-of-observability/
- Edge Delta, "Three Pillars of Observability: Logs vs. Metrics vs. Traces" — https://edgedelta.com/company/knowledge-center/three-pillars-of-observability
- StrongDM, "Three Pillars of Observability Explained: Metrics, Logs, Traces" — https://www.strongdm.com/blog/three-pillars-of-observability
- SigNoz, "Three Pillars of Observability [And Beyond] - A Beginner's Guide" — https://signoz.io/blog/three-pillars-of-observability/
- CrowdStrike, "The Three Pillars of Observability: Logs, Metrics, and Traces" — https://www.crowdstrike.com/en-us/cybersecurity-101/observability/three-pillars-of-observability/
- TechTarget, "The 3 pillars of observability: Logs, metrics and traces" — https://www.techtarget.com/searchitoperations/tip/The-3-pillars-of-observability-Logs-metrics-and-traces
- Elastic Blog, "The 3 pillars of observability: Unified logs, metrics, and traces" — https://www.elastic.co/blog/3-pillars-of-observability
- DEV Community, "The Three Pillars of Observability: Logs, Metrics, and Traces Explained" — https://dev.to/young_gao/the-three-pillars-of-observability-logs-metrics-and-traces-in-practice-4537
- Dash0, "Managing Systemd Logs on Linux with Journalctl" (referenced for the OpenTelemetry correlation point) — https://www.dash0.com/guides/systemd-logs-linux-journalctl
