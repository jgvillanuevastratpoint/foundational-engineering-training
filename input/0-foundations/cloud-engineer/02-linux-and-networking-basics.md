# Linux & Networking Basics — Training Module Source Document

> Source document feeding Skill 1 (Research Synthesizer) → Skill 2 (Learning Path Architect) → Skill 3 (Module Content Builder). Quiz content is intentionally excluded from authoring here — Skill 5 (Quiz Generator) owns that. No hands-on tasks or rubrics — this pipeline is quiz-only.

---

## 0. Module Metadata

- **Audience:**
  - **Cloud Engineers:** every cloud service ultimately runs on Linux, and nearly every cloud incident eventually reduces to a Linux process, a systemd unit, a misconfigured network boundary, or a network call failing in a specific, diagnosable way. A cloud engineer who cannot navigate a Linux box confidently, reason about how a request actually reaches an instance (VPC, subnet, security group), and read `curl -v` output down to the TCP/TLS layer is limited to whatever a managed console happens to show them.
- **Video lecture (if any):** None yet produced. If recorded, split into two: (1) Linux fundamentals — shell fluency, permissions, systemd, SSH, package management, shell scripting; (2) networking — cloud network building blocks, DNS, TCP, TLS, HTTP, `curl -v`. Each half should stay under 30 minutes on its own; combining them into one recording would blow the cap.
- **Learning objectives:**
  1. Define Linux and describe how its core components (kernel, shell, filesystem, services/processes) fit together.
  2. Navigate a Linux filesystem and use core commands to inspect processes, permissions, and package state without a GUI.
  3. Explain what systemd manages and how to inspect a unit's status and logs.
  4. Explain why key-based SSH authentication is preferred over passwords for remote cloud administration.
  5. Explain the relationship between a VPC, its subnets (public vs. private), and security groups in controlling what can reach an instance.
  6. Trace a DNS resolution from client query to authoritative answer, including how a cloud DNS service fits into that chain.
  7. Explain what happens during a TCP handshake and a TLS handshake, and what distinct problem each layer solves.
  8. Distinguish HTTP/1.1, HTTP/2, and HTTP/3 in terms of connection handling, not just version number.
  9. Read the output of `curl -v` against an endpoint and identify, at each stage (DNS, TCP, TLS, HTTP), whether it succeeded and why.

---

## 1. Why This Subject Matters (Motivation)

When a service is unreachable, the console dashboard tells you *that* something is wrong, not *where*. Is the instance even up, or did the process crash? Is a security group silently dropping the request before it ever reaches the box? Is DNS resolving to the right IP? Is the TLS certificate valid, or expired, or issued for the wrong hostname? Is the server sending back a 200 with a body the client can't parse, or a 503 the load balancer swallowed before it ever showed up in application logs? Every one of those is a different failure, at a different layer, requiring a different fix — and they all look identical from the outside as "the site is down." Fluency with a Linux shell and a working mental model of how a request travels from DNS through a cloud network boundary down to TCP, TLS, and HTTP are what let you go from "it's down" to "the certificate expired six hours ago" in minutes instead of escalating and waiting. This is the single most practical filter for whether someone is ready to operate infrastructure on call: if you can't run `curl -v` against an endpoint and narrate what happened at each layer, you're not yet ready to be the first responder.

---

## 2. Core Concepts

Concepts are grouped into two halves that build in order: Linux fundamentals first (what it is, how it works, the commands and services you operate it with), then networking fundamentals (how a request actually reaches, and is served by, the systems those Linux fundamentals let you operate).

### Linux Fundamentals

- **What Is Linux, and How Does It Work?**
  - **Context:** Linux is an operating system — like Windows or macOS — that manages a machine's hardware resources (CPU, memory, storage, files). It underlies most cloud servers, Kubernetes clusters, and Docker containers because it's fast, stable, secure, and lightweight. It works through four cooperating parts: the **kernel** (communicates with hardware), the **shell** (the command-line interface you issue commands through), the **filesystem** (organizes files and directories), and **services & processes** (background programs, such as a web server, that keep running independently of any interactive session). Everything else in this module is a deeper look at one of these four parts.
  - **Illustration:** [x] needed — a simple layered diagram: hardware → kernel → shell/services sitting on top, with the filesystem shown as the shared structure both the shell and services read/write through.
- **Shell Fluency & the Linux Filesystem**
  - **Context:** comfort navigating the filesystem (`pwd`, `ls -la`, `cd`, `find`, `grep`), knowing what standard directories like `/etc`, `/var`, `/home`, and `/bin` are for, and composing commands with pipes and redirection quickly enough to investigate a live system without reaching for a GUI; this is the substrate everything else in this module is diagnosed through. Cloud engineers don't need full system-administrator depth — a working set of roughly twenty to thirty commands used daily covers the vast majority of real diagnostic work.
  - **Illustration:** not needed — best taught through worked command examples, not a diagram.
- **File Permissions, Ownership & Package Management**
  - **Context:** controlling access with `chmod`/`chown`, and installing or updating software through a distribution's package manager (`apt`, `yum`); misconfigured permissions and unmanaged, ad hoc software installs are recurring, low-drama causes of "it works on one box but not another."
  - **Illustration:** [x] needed — a simple diagram of a file's permission bits (owner/group/other × read/write/execute) mapped to the effect of a `chmod` change.
- **Process Management & systemd**
  - **Context:** systemd is the init system and service manager on most modern Linux distributions; it starts, stops, restarts, and supervises services described as "units," and centralizes their logs via the journal. `ps` and `top` give the live process view systemd's own state should agree with.
  - **Illustration:** [x] needed — a diagram of systemd's relationship to a unit file, the process it supervises, and the journal it writes to.
- **SSH & Key-Based Remote Access**
  - **Context:** SSH is the standard way to reach a remote Linux host for administration; key-based authentication (a private key held by the operator, a public key authorized on the host) is preferred over password authentication because it can't be guessed or brute-forced and isn't reused across systems the way a memorized password often is.
  - **Illustration:** not needed — definitional, best reinforced by the SSH-and-security-group case study.
- **Shell Scripting for Automation**
  - **Context:** using variables, conditionals, and loops in a shell script to automate repetitive infrastructure tasks (health checks, deployment steps, log rotation) instead of running the same sequence of commands by hand every time; this is the bridge between one-off shell fluency and reliable, repeatable operations.
  - **Illustration:** not needed — definitional, best shown via a short worked script rather than a diagram.

### Networking Fundamentals

- **Cloud Network Building Blocks: VPCs, Subnets & Security Groups**
  - **Context:** a Virtual Private Cloud (VPC) is an isolated network in the cloud; a subnet is a slice of that network's IP range, conventionally split into public subnets (reachable from the internet, typically holding load balancers) and private subnets (not directly reachable, typically holding application instances and databases); a security group acts as an instance-level firewall controlling exactly which ports and sources may reach it. Together these three define whether a request can physically reach a workload at all, before DNS, TCP, or TLS ever come into play.
  - **Illustration:** [x] needed — a diagram of a VPC containing a public subnet (load balancer, security group open on 80/443) and a private subnet (application instances, security group only accepting traffic from the load balancer).
- **DNS Resolution**
  - **Context:** the process of turning a hostname into an IP address, involving a resolver, potentially a cache, and a chain of authoritative servers (root → TLD → authoritative); in a cloud environment this is often a managed DNS service (e.g., Route 53) mapping a domain name to a load balancer. DNS failures or stale caches, and cloud-side records pointing at decommissioned resources, are among the most common causes of "it works for me but not for them."
  - **Illustration:** [x] needed — a sequence diagram of a DNS query traveling from client resolver through root, TLD, and authoritative name servers, with a callout showing a cloud DNS record resolving to a load balancer.
- **Load Balancers as the Bridge Between DNS and the Backend**
  - **Context:** a load balancer is the resource DNS typically points to; it terminates the client-facing connection (often TLS), distributes requests across backend instances in private subnets, and is the reason security groups are usually configured to open ports 80/443 on the load balancer while restricting SSH (port 22) to administrators only. It sits directly between the networking concepts above and the transport/application-layer concepts below.
  - **Illustration:** not needed — covered concretely by the VPC/subnet illustration and the case studies.
- **TCP Basics (Three-Way Handshake, Connection States)**
  - **Context:** the transport-layer protocol underlying HTTP; understanding the SYN/SYN-ACK/ACK handshake and the difference between "connection refused" (something answered and rejected) and "connection timed out" (nothing answered at all, often a security group or routing block) is essential for localizing a failure to client, network boundary, or server.
  - **Illustration:** [x] needed — a sequence diagram of the TCP three-way handshake, annotated with what a refusal versus a timeout looks like at each step.
- **TLS Handshake**
  - **Context:** the protocol that establishes an encrypted, authenticated channel on top of TCP before HTTP data is exchanged; it involves certificate validation (is this host who it claims to be?) and negotiation of encryption parameters, and it is a common, distinct point of failure from plain connectivity.
  - **Illustration:** [x] needed — a simplified TLS handshake sequence diagram showing ClientHello, ServerHello + certificate, and key exchange.
- **HTTP/1.1 vs HTTP/2 vs HTTP/3**
  - **Context:** successive HTTP versions changing how connections are used — HTTP/1.1 typically one request per connection (or pipelined with head-of-line blocking), HTTP/2 multiplexing many requests over one TCP connection, HTTP/3 moving the transport itself to QUIC over UDP to avoid TCP-level head-of-line blocking.
  - **Illustration:** [x] needed — a comparison diagram showing request/connection multiplexing differences across the three versions.
- **Reading `curl -v` Output**
  - **Context:** the practical synthesis skill of this module — mapping the verbose output of `curl -v` (DNS lookup, TCP connect, TLS handshake detail, request/response headers) back onto every concept above, from network boundary through DNS, TCP, TLS, and HTTP, to localize a failure to a single layer.
  - **Illustration:** [x] needed — an annotated `curl -v` transcript with each stage labeled against the concept it corresponds to.

---

## 3. Case Studies / Real-World Examples

1. **"The site is down" that was actually an expired certificate**
   - **Scenario:** Users report a service is completely unreachable. The on-call engineer runs `curl -v https://api.example.com` and sees the TCP connection succeed but the TLS handshake fail with a certificate expiry error.
   - **Linux & Networking Basics in Action:**
     - *TCP Basics:* the successful three-way handshake in the output rules out a network boundary or firewall block.
     - *TLS Handshake:* the specific handshake failure (certificate expired, not a hostname mismatch or untrusted CA) narrows the fix to certificate renewal rather than a broader network investigation.
     - *Reading `curl -v` Output:* the engineer's ability to separate "TCP connected" from "TLS failed" in the transcript is what turns a vague outage into a five-minute diagnosis.
   - **Outcome:** the team adds certificate-expiry monitoring so this class of failure is caught before users notice.

2. **A service works from one region but not another**
   - **Scenario:** An internal service is reachable from the US region but times out from the EU region, and the application logs show nothing because the request never reaches the application.
   - **Linux & Networking Basics in Action:**
     - *DNS Resolution:* the engineer checks whether the EU region resolves the hostname to a different (possibly stale or wrong) cloud DNS record than the US region.
     - *TCP Basics:* a connection timeout, rather than an immediate refusal, points toward a network path or security group silently dropping the request, not the application rejecting it.
   - **Outcome:** the root cause is a regional DNS record pointing at a decommissioned load balancer; fixing the record resolves the outage without touching application code.

3. **A locked-down security group that broke a health check instead of an attacker**
   - **Scenario:** After a security review, an engineer tightens a private-subnet application instance's security group to accept traffic only from a specific source. Shortly after, the load balancer starts marking every instance unhealthy and traffic drops to zero.
   - **Linux & Networking Basics in Action:**
     - *Cloud Network Building Blocks: VPCs, Subnets & Security Groups:* the tightened security group no longer allowed traffic from the load balancer's own subnet, so the load balancer's health checks — which look exactly like a normal client to the instance — were silently dropped, indistinguishable from an outage.
     - *TCP Basics:* the health check requests were timing out rather than being refused, which is the specific signature of a security-group-level block rather than an application error.
   - **Outcome:** the team adds "does the load balancer's subnet still have an explicit allow rule?" to its standard checklist for any security group change on a backend instance.

4. **A slow API blamed on the backend that was actually a protocol limitation**
   - **Scenario:** A frontend team complains an API "feels slow" only when a page issues many small requests to the same host, even though each individual request is fast on the backend.
   - **Linux & Networking Basics in Action:**
     - *HTTP/1.1 vs HTTP/2 vs HTTP/3:* the investigating engineer determines the API is still served over HTTP/1.1 without connection reuse tuned properly, so the browser serializes requests behind a small per-host connection limit — a transport-layer bottleneck, not a backend performance problem.
     - *Load Balancers as the Bridge Between DNS and the Backend:* because the load balancer is what actually terminates the client connection and negotiates the HTTP version, enabling HTTP/2 there — not on the backend instances — is what fixes the client-visible behavior.
   - **Outcome:** enabling HTTP/2 on the load balancer removes the artificial serialization, and backend latency numbers (which were fine all along) finally match perceived page speed.

---

## 4. Best Practice Checklist / Frameworks

- Practice narrating `curl -v` output stage by stage (DNS → network boundary → TCP → TLS → HTTP) until it's automatic — this is the single highest-leverage diagnostic habit in this module.
- Use `journalctl -u <unit> -f` (or equivalent) as the default first step when a systemd-managed service misbehaves, before checking application-level logs separately.
- Always authenticate to remote Linux hosts with SSH keys, never passwords, and never commit private keys or credentials to version control.
- When something is "down," first determine which layer failed (network boundary/security group, DNS, TCP, TLS, HTTP) before guessing at a fix — each layer has a distinct and non-overlapping set of causes.
- Treat "connection refused" and "connection timed out" as different diagnoses, not interchangeable symptoms of "network problem" — a timeout is the characteristic signature of a security group or routing block.
- Before changing a security group on a backend instance, explicitly check whether the load balancer's own subnet still has an allow rule — a health-check outage looks identical to a real one.
- Know that HTTP/2's multiplexing is a connection-level property negotiated at the load balancer, not something visible by just reading HTTP status codes — check what protocol is actually negotiated when diagnosing perceived slowness.
- Automate repetitive diagnostic or deployment sequences with a short shell script rather than repeating the same manual commands, but don't over-invest — a one-off investigation doesn't need a reusable script.
- Do not try to become an expert in every corner of `iptables`/`nftables`, every cloud provider's full networking feature set, or exotic shell one-liners as part of this module — the goal is fluent, correct use of the common diagnostic path, not mastery of every networking edge case.

---

## 5. Sources

- Joyal B Biju (DEV Community), "Cloud Engineer Journey #2: Linux Made Simple for Cloud/DevOps Beginners" — https://dev.to/joyal_b_biju/cloud-engineer-journey-2-linux-made-simple-for-cloud-devops-beginners-34a4
- Cloud Engineer Academy, "Linux Fundamentals for Cloud Engineers" — https://learn.cloudengineeracademy.io/blog/linux-fundamentals-cloud-engineers
- Network Kings (via LinkedIn), "Linux Fundamentals for DevOps and Cloud Engineers" — https://www.linkedin.com/pulse/linux-fundamentals-devops-cloud-engineers-networkkings-fffse/
- Lisa Ellington (Medium), "Cloud Networking Full Guide: Building the Backbone of Modern Cloud Environments" — https://medium.com/@lisaellingtonwrites/cloud-networking-full-guide-building-the-backbone-of-modern-cloud-environments-a28e43871841
- freedesktop.org, "systemd System and Service Manager" — https://www.freedesktop.org/wiki/Software/systemd/
- Cloudflare Learning Center, "What is DNS?" — https://www.cloudflare.com/learning/dns/what-is-dns/
- Cloudflare Learning Center, "What happens in a TLS handshake?" — https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/
- Cloudflare Learning Center, "What is TCP/IP?" — https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/
- Cloudflare Learning Center, "HTTP/2 vs HTTP/1.1" — https://www.cloudflare.com/learning/performance/http2-vs-http1.1/
- Cloudflare Learning Center, "What is HTTP/3?" — https://www.cloudflare.com/learning/performance/what-is-http3/
- curl, "Everything curl — Verbose Operations" — https://everything.curl.dev/usingcurl/verbose
- **Video lectures:** none cited.
