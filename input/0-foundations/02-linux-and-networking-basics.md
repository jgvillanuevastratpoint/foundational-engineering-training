# Linux and Networking Basics — Research Notes

## Why this subject matters

Most production incidents a new engineer will encounter in the first few years of their career are, underneath the visible symptoms, operating system or networking problems rather than application logic problems: a name did not resolve, a certificate expired, a service did not start because a dependency was not ready, a port was not listening, or a connection timed out for a reason that had nothing to do with the application code. An engineer who cannot investigate these layers independently will escalate every such problem to someone else, which does not scale and slows down the whole team. The specific bar referenced for this subject — being able to run a verbose request against an endpoint and explain what happened at each stage — is a practical, checkable way to confirm this baseline exists.

This baseline is not specific to any one kind of system. The same diagnostic reflex and the same operational expectations — checking service state, reading structured logs, and localizing a failing request to a stage — apply uniformly across every engineering unit: software service (web/mobile), cloud, and data/platform, not only teams that own infrastructure directly.

## Core concepts

### Shell fluency
Shell fluency, in this context, does not mean mastery of shell scripting. It means the reflex to inspect a running system quickly — processes, listening ports, file permissions, and logs — without needing a graphical tool, and to do this fast enough that it becomes a normal first step during troubleshooting rather than a last resort.

### systemd and service management
systemd is the init system and service manager used by most modern Linux distributions. It is the first process started on boot and is responsible for bringing up and supervising other services on the system (Arun Kumar Singh, Medium, "DevOps Notebook: systemd and journalctl"). The `systemctl` command is the primary tool for inspecting and controlling the state of services managed by systemd, including starting, stopping, restarting, enabling, and checking whether a service is active (SUSE, "Introduction to systemd Basics").

systemd unit files can declare ordering relationships to each other using directives such as `Before=` and `After=`, which control the sequence in which services start relative to one another. The SUSE documentation notes that without such directives, systemd may start a group of units at the same time, which can cause problems if one service actually depends on another being ready first (SUSE, "Introduction to systemd Basics"). Understanding this ordering behavior explains a very common class of real-world deployment bug: a service that fails to start correctly because a dependency, such as a database or a network resource, was not yet available.

### journalctl and structured logging at the operating-system level
journalctl is the command-line tool used to query and display logs collected by systemd's logging service, journald. Unlike traditional flat-text log files, journald stores log entries in a structured, indexed, binary format, with each entry broken into searchable key-value fields such as the message text, priority, the originating systemd unit, and the process ID (UptimeRobot Knowledge Hub, "Journalctl Explained: How To View And Analyze Systemd Logs"). Because these fields are indexed, filtering by them is fast even on systems with a large volume of historical logs, and journalctl supports filtering by time window, by specific unit, and by priority level (Loggly, "Using journalctl - The Ultimate Guide To Logging").

This is a useful bridge concept: it is the trainee's first hands-on exposure to structured, field-queryable log data, before the same idea reappears at the application level in the observability subject. One source also notes an important operational caveat: by default, journald may only store logs in memory, meaning they can be lost on reboot unless persistent storage is explicitly configured, and that for anything beyond single-host local debugging, logs are typically forwarded into a centralized logging pipeline (UptimeRobot Knowledge Hub, "Journalctl Explained: How To View And Analyze Systemd Logs"). The same expectation carries into production logging generally: structured, queryable log formats are expected to include a request or correlation identifier so a single event can be traced across log lines and, later, across services — the same searchable key-value structure journald already provides at the OS level.

### DNS, TCP, and TLS as a request pipeline
Every network request a program makes hides a sequence of distinct stages: a domain name is resolved to an address (DNS), a connection is opened to that address (TCP), and, for encrypted connections, a negotiation establishes trust and a shared encryption key before any application data is exchanged (TLS). A guide on debugging with the `curl` command describes this explicitly: a single request involves a DNS lookup, a TCP connection, a TLS handshake if the connection is encrypted, a request, and a response, and when something misbehaves, the diagnostic task is to identify which of these stages went wrong (Flavio Copes, "Inspect a request with verbose output — curl Course").

The TLS handshake specifically is described as a three-phase negotiation — hello, certificate exchange, and key exchange — that establishes encryption before any actual data is sent, and understanding these phases is described as one of the most effective ways to debug failures in secured connections (DEV Community, "TLS/SSL Handshake: Understand in 3 Minutes"). A certificate-related failure (for example, an untrusted or expired certificate) and a network-level failure produce different, recognizable error signatures, and learning to tell them apart is a practical, everyday debugging skill rather than an advanced one.

Diagnosing these signatures correctly also depends on knowing which environment is being tested: development and staging often use self-signed or internally issued certificates and non-public DNS, so an error signature that is normal in development can indicate a genuine outage in production. This is one reason environments are kept clearly separated and staging is treated with the same operational rigor as production — a TLS or DNS diagnosis learned in one environment should transfer cleanly to the next rather than mask a real difference.

### Using curl as a diagnostic instrument
`curl` in verbose mode (the `-v` flag) annotates the entire request lifecycle: lines beginning with an asterisk describe curl's own internal events, such as name resolution and TLS negotiation; lines beginning with a greater-than sign show the data that was sent; and lines beginning with a less-than sign show the data that was received (a knowledge base article on debugging with curl, Stack Harbor, "Debug HTTP requests with curl: verbose output, timing, and headers"). The same source explains curl's timing variables — the time to resolve the name, the time to establish the TCP connection, the time to complete a TLS handshake, and the time to first byte of the response — and notes that these are cumulative from the start of the request, so the duration of any single stage can be calculated by subtracting one cumulative value from the next.

This gives a concrete, teachable diagnostic habit: rather than guessing at the application layer first, a developer can use a single verbose or timed request to localize a problem to a specific stage of the pipeline before investigating further.

## Best practices summary

- Treat a verbose, timed request (for example, using curl's verbose and timing options) as a default first diagnostic step, because it tells the investigator which stage of the request pipeline to look at next, rather than requiring a guess.
- Learn the distinct error signatures produced by DNS failures, TCP-level failures, and TLS/certificate failures, so that the correct fix is applied instead of a guess.
- Default to `journalctl` filtering (by time window, by unit, and by priority) for inspecting service health on a Linux host, instead of manually searching flat log files.
- Understand systemd's unit dependency ordering well enough to explain, given a real example, why a service failed to start because a dependency was not ready in time.
- Recognize when local, host-based logging (such as the systemd journal) is no longer sufficient and logs need to be forwarded into a centralized system for correlation across multiple hosts.
- Verify environment configuration at service startup rather than assuming it is correct, so a bad value is caught immediately instead of after the service is already serving traffic.
- Expect production and staging services to emit logs, metrics, and alerts proportional to their importance, with alerting firing within minutes of a failed step.
- Include a request or correlation identifier in structured logs so a single event can be traced across log lines and, later, across services.
- Record a resolved failure's diagnosis and fix in a runbook so the next engineer does not re-diagnose the same dependency-ordering or connectivity failure from scratch.
- Keep development, staging, and production clearly separated, with staging held to production-level rigor, so a diagnostic pattern learned in one environment transfers correctly to the next.
- Apply this diagnostic and operational discipline uniformly across software service (web/mobile), cloud, and data/platform systems.

## Real-world examples

- Container orchestration platforms commonly run on hosts where systemd manages the underlying container runtime; `journalctl` is frequently the first place engineers look when a problem is suspected to be at the host or node level rather than inside the application itself (Dash0, "Managing Systemd Logs on Linux with Journalctl").
- Curl's timing breakdown (name resolution, TCP connect, TLS handshake, time to first byte) is widely used as a lightweight performance-debugging technique to determine whether latency is coming from DNS, from the network connection, from the TLS negotiation, or from the server's own processing time (OneUptime, "How to Use curl to Test HTTP/HTTPS Connectivity from the Command Line").
- Digital Ocean's community tutorials on `journalctl`, among many similar vendor and community guides, are commonly used as onboarding material for new engineers learning to operate Linux-based infrastructure (DigitalOcean, "How To Use journalctl to View and Manipulate systemd Logs on Linux").

## Sources

- SUSE, "Introduction to systemd Basics" — https://documentation.suse.com/smart/systems-management/html/systemd-basics/index.html
- Arun Kumar Singh, Medium, "DevOps Notebook: systemd and journalctl" — https://arunksingh16.medium.com/notebook-systemd-and-journalctl-33dec3aaf8c1
- Dash0, "Managing Systemd Logs on Linux with Journalctl" — https://www.dash0.com/guides/systemd-logs-linux-journalctl
- UptimeRobot Knowledge Hub, "Journalctl Explained: How To View And Analyze Systemd Logs" — https://uptimerobot.com/knowledge-hub/logging/journalctl-explained-how-to-view-and-analyze-systemd-logs/
- Loggly, "Using journalctl - The Ultimate Guide To Logging" — https://www.loggly.com/ultimate-guide/using-journalctl/
- DigitalOcean, "How To Use journalctl to View and Manipulate systemd Logs on Linux" — https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs
- Flavio Copes, "Inspect a request with verbose output — curl Course" — https://flaviocopes.com/courses/curl/inspect-a-request-with-verbose-output/
- DEV Community, "TLS/SSL Handshake: Understand in 3 Minutes" — https://dev.to/hongster85/tlsssl-handshake-understand-in-3-minutes-2fee
- Stack Harbor Knowledge Base, "Debug HTTP requests with curl: verbose output, timing, and headers" — https://stackharbor.com/en/knowledge-base/curl-debug-http-requests/
- OneUptime, "How to Use curl to Test HTTP/HTTPS Connectivity from the Command Line" — https://oneuptime.com/blog/post/2026-03-20-curl-test-http-https-cli/view
- OneUptime, "How to Use curl and wget for HTTP Troubleshooting on RHEL" — https://oneuptime.com/blog/post/2026-03-04-curl-wget-http-troubleshooting-rhel-9/view
