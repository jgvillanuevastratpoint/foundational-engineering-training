# Containers — Training Module Source Document

> Source document feeding Skill 1 (Research Synthesizer) → Skill 2 (Learning Path Architect) → Skill 3 (Module Content Builder). Quiz content is intentionally excluded from authoring here — Skill 5 (Quiz Generator) owns that. No hands-on tasks or rubrics — this pipeline is quiz-only.

---

## 0. Module Metadata

- **Audience:**
  - **Cloud Engineers:** cloud engineers build and operate the images and orchestration platforms that every other team's workloads run on; a poorly built image or a container running multiple responsibilities becomes a scaling, security, and debugging problem across every environment it's deployed into, not just one team's service.
- **Video lecture (if any):** None yet produced. If recorded, keep to a single ~25-minute session: Docker fundamentals, multi-stage builds, image size discipline, and single-responsibility containers build on each other linearly and don't need separate sessions.
- **Learning objectives:**
  1. Explain what a container is in terms of the OS-level primitives (namespaces, cgroups) it relies on, and how that differs from a virtual machine.
  2. Distinguish a Docker image from a running container and explain the role of image layers.
  3. Explain what a multi-stage build is and what problem it solves that a single-stage `Dockerfile` cannot.
  4. Identify common causes of image bloat and the techniques used to reduce image size.
  5. Explain why running exactly one process/responsibility per container is a design principle, and what breaks when that principle is violated.

---

## 1. Why This Subject Matters (Motivation)

A container that starts up fine on your laptop can still be a liability in production: a bloated image that takes minutes to pull and slows every deploy and autoscale event, a single container quietly running three unrelated processes so that one crash takes down all three, or an image that ships build tools and source code into production because nobody separated "build" from "run." None of these show up as bugs in your application logic — they show up as slow rollouts, confusing incident scope, and larger-than-necessary attack surface. Understanding what a container actually is (not "a lightweight VM," but an isolated process using the host kernel) and building the habit of small, single-purpose, multi-stage images is what separates a container setup that scales cleanly from one that becomes an operational tax on every team that touches it.

---

## 2. Core Concepts

Concepts are grouped into two halves that build in order: container fundamentals first (what a container actually is and how an image relates to it), then the build and design practices that turn that mental model into efficient, well-behaved containers in production.

### Container Fundamentals

- **What Is a Container, and How Does It Work? (Namespaces & cgroups)**
  - **Context:** a container is an isolated process (or process group) on the host's own kernel, using Linux namespaces (for isolated views of processes, network, filesystem, etc.) and cgroups (for resource limits); this is fundamentally different from a VM, which virtualizes hardware and runs a full separate kernel. Everything else in this module — images, layers, builds, and design principles — is about how that one primitive gets packaged and used well.
  - **Illustration:** [x] needed — a side-by-side diagram of VM architecture (hypervisor, multiple guest kernels) versus container architecture (shared host kernel, isolated processes).
- **Image vs. Container**
  - **Context:** an image is an immutable, layered filesystem snapshot plus metadata (entrypoint, exposed ports, etc.); a container is a running (or stopped) instance of an image, with a writable layer on top.
  - **Illustration:** [x] needed — a diagram of stacked read-only image layers with a writable container layer on top.
- **Docker Layer Caching**
  - **Context:** each instruction in a `Dockerfile` produces a cacheable layer; ordering instructions from least-to-most frequently changing (e.g., dependency installation before source copy) lets Docker reuse cached layers and dramatically speeds up rebuilds.
  - **Illustration:** [x] needed — a comparison of a poorly ordered Dockerfile (source copy before dependency install) versus a well-ordered one, showing which layers get invalidated on a source-only change.

### Building Efficient, Well-Designed Containers

- **Multi-Stage Builds**
  - **Context:** a `Dockerfile` pattern using multiple `FROM` stages, where the final image copies only the built artifacts from earlier "build" stages, keeping compilers, build tools, and intermediate files out of the shipped image entirely.
  - **Illustration:** [x] needed — a diagram showing a build stage (with full toolchain) producing an artifact that's copied into a minimal runtime stage, with the build stage discarded.
- **Image Size Discipline**
  - **Context:** the practice of deliberately minimizing image size — via minimal base images, multi-stage builds, `.dockerignore`, combining/cleaning up package manager layers — because smaller images pull faster, scale faster, and expose less attack surface.
  - **Illustration:** not needed — covered concretely by the multi-stage build illustration and case studies.
- **Single-Responsibility Containers**
  - **Context:** the principle that a container should run one process/one responsibility (e.g., the web server, not the web server plus a cron job plus a log shipper bundled in); this makes scaling, restarting, and diagnosing failures independent per responsibility instead of coupled.
  - **Illustration:** [x] needed — a comparison diagram of one container running three unrelated processes (and what happens when one crashes) versus three containers each running one process, orchestrated together.

---

## 3. Case Studies / Real-World Examples

1. **The 1.8 GB image that slowed every deploy**
   - **Scenario:** A team's production image is 1.8 GB because it's built from a full SDK base image, includes the entire source repository (including tests and docs), and never cleans up package manager caches. Every deploy takes several minutes just to pull the image onto new nodes, and autoscaling lags noticeably behind traffic spikes.
   - **Containers in Action:**
     - *Multi-Stage Builds:* the build stage (with the full SDK) was never separated from the runtime stage, so the final image ships the entire toolchain unnecessarily.
     - *Image Size Discipline:* no `.dockerignore` was in place, no minimal base image was used, and package manager caches were never cleaned within the same layer they were created in.
   - **Outcome:** switching to a multi-stage build with a minimal runtime base image reduces the image to under 150 MB, and autoscaling responsiveness improves measurably.

2. **A crash-looping container that was secretly running three services**
   - **Scenario:** A container defined to run a web application is also running a background cron job and a log-forwarding agent via a custom entrypoint script. When the cron job's dependency breaks, the entrypoint script crashes, killing the whole container — including the healthy web application — and the orchestrator restarts all three responsibilities together in a loop.
   - **Containers in Action:**
     - *Single-Responsibility Containers:* because three unrelated responsibilities were coupled into one container, a fault in one (the cron job) produced an outage in an unrelated one (the web application) that had nothing wrong with it.
   - **Outcome:** the team splits the three responsibilities into three containers orchestrated as separate units (e.g., a sidecar for log forwarding, a separate scheduled job for the cron task), so a fault in one no longer takes down the others.

3. **A "works on my machine" image that shipped a security hole to production**
   - **Scenario:** A developer's Dockerfile installs debugging tools and copies `.env` files and local credentials into the image during development, then the same Dockerfile — unmodified — is used to build the production image.
   - **Containers in Action:**
     - *Image vs. Container:* because the image is an immutable layered artifact, anything copied into any layer (even if later "deleted" in a subsequent layer) can still be extracted from the image history, meaning the leaked secret is truly baked in, not just hidden.
     - *Multi-Stage Builds / Image Size Discipline:* a proper multi-stage setup with a `.dockerignore` excluding `.env` and credential files would never have brought those files into the build context in the first place.
   - **Outcome:** the team adds `.dockerignore` rules, rebuilds from a clean multi-stage Dockerfile, and rotates the leaked credentials, treating the incident as a case for mandatory image scanning before any image is pushed to a registry.

---

## 4. Best Practice Checklist / Frameworks

- Default to a multi-stage `Dockerfile`: build with a full toolchain in an early stage, copy only the finished artifact into a minimal runtime stage.
- Order Dockerfile instructions from least-to-most frequently changing to maximize layer cache reuse.
- Use a `.dockerignore` file to keep source control metadata, local secrets, and test artifacts out of the build context entirely.
- Prefer minimal or distroless base images for the runtime stage; only include what the running process actually needs.
- Run exactly one process/responsibility per container; use sidecars or separate scheduled jobs instead of bundling unrelated responsibilities into one entrypoint.
- Scan images for known vulnerabilities and leaked secrets before pushing to a registry, and treat image history as permanent — assume anything ever copied into any layer can be extracted later.
- Don't try to memorize every Dockerfile instruction or every orchestrator's full feature set in this module — the goal is the mental model (namespaces/cgroups, layers, single responsibility) that transfers across any container runtime or orchestrator.

---

## 5. Sources

- Docker Inc., "Docker overview" — https://docs.docker.com/get-started/overview/
- Docker Inc., "Multi-stage builds" — https://docs.docker.com/build/building/multi-stage/
- Docker Inc., "Dockerfile best practices" — https://docs.docker.com/build/building/best-practices/
- Red Hat, "What is a Linux container?" — https://www.redhat.com/en/topics/containers/whats-a-linux-container
- Kubernetes documentation, "Sidecar Containers" — https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
- **Video lectures:** none cited.
