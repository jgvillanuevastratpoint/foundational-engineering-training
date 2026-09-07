# Containers — Research Notes

## Why this subject matters

Containers are the standard way most modern software is built, shipped, and run, but there is a meaningful gap between a container image that simply works and one that a senior engineer would approve for production. Oversized, insecure, or multi-purpose images are a common and largely preventable source of both security exposure and operational cost. This subject is about closing that gap using a small number of well-established, well-documented disciplines rather than advanced or unusual techniques.

## Core concepts

### Docker fundamentals
A container image is a packaged, layered filesystem plus metadata describing how to run a program; a container is a running instance of that image. Docker's own documentation on building images emphasizes several foundational practices, including excluding irrelevant files from the build using a `.dockerignore` file (similar in purpose to a `.gitignore` file for version control), and designing images so that the containers created from them are as disposable, or "ephemeral," as possible (Docker Docs, "General best practices for writing Dockerfiles").

### Multi-stage builds
A multi-stage build uses more than one `FROM` instruction in a single Dockerfile, creating a clean separation between the environment used to build an application (which may need compilers, build tools, and source code) and the environment used to actually run it. Docker's official documentation describes this directly: splitting a Dockerfile into distinct stages ensures that only the files actually needed to run the application end up in the final image, and using multiple stages can also allow build steps to run in parallel, speeding up the overall build (Docker Docs, "Building best practices").

The practical effect is significant. As one guide summarizing the pattern explains, build tools, compilers, and source code can be very large, and without a multi-stage approach, all of that ends up inside the same runtime image that gets deployed, even though the running application never needs any of it (Udara Shanuka Senarath, Medium, "Multi-Stage Docker Builds Explained: Building Smaller, Safer Production Images").

### Image size and base image discipline
Choosing an appropriately small, trusted base image is described across multiple sources as one of the most important decisions in building a secure and efficient image. Docker's own documentation recommends choosing a base image from a trusted source and keeping it as small as possible, noting that Docker Official Images are a curated collection that are regularly updated and documented as a trusted starting point (Docker Docs, "Building best practices").

A more detailed guide distinguishes between several common approaches to shrinking an image: using a minimal distribution such as Alpine Linux, using a "slim" variant of a language's official image, or using a distroless image, which strips out shells, package managers, and other operating system utilities entirely, leaving only what is strictly required to run the application (Eduonix Blog, "Docker Multi-Stage Builds: Powerful Image Optimization"). The trade-off is explicit: removing more from the base image reduces its size and its attack surface, but can also make the image harder to debug interactively, since common debugging tools may no longer be present inside the container.

### One process, one concern per container
Docker's official building-best-practices documentation states that each container should have only one concern, and that decoupling an application into multiple containers makes it easier to scale horizontally and to reuse individual containers. It gives a concrete example: a web application stack made up of separate containers for the web application, the database, and an in-memory cache, each with its own image, managed independently (Docker Docs, "Building best practices"). The same documentation is explicit that this is a guideline rather than an absolute rule: some programs, such as a task queue system that spawns multiple worker processes, or a web server that creates one process per request, legitimately manage more than one operating-system process while still representing a single logical concern.

## Best practices summary

- Use multi-stage builds for any application that requires compiling, bundling, or otherwise transforming source code, so that build-only tools and files never end up in the deployed image.
- Choose a base image deliberately, weighing size and attack-surface reduction (for example, a minimal or distroless base) against the practical need to debug the running container.
- Exclude anything not required for the build using a `.dockerignore` file, which both speeds up the build and reduces the risk of accidentally including files such as local environment configuration.
- Never store secrets or application data inside the image itself; use runtime mechanisms such as volumes or externally injected configuration instead.
- Design containers to be as disposable and stateless as possible, so that anything requiring persistence lives outside the container's own writable layer.
- Order Dockerfile instructions so that steps unlikely to change, such as installing dependencies, come before steps that change frequently, such as copying source code, to make better use of build caching.
- Limit each container to a single logical concern, using judgment for cases where a single concern legitimately involves more than one process.

## Real-world examples

- The "distroless" base image pattern, which removes shells and package managers from the runtime image, was popularized by Google and has since been adopted widely, specifically because fewer installed packages means fewer components that can have a disclosed vulnerability, which reduces both real risk and the volume of findings reported by security scanners (Eduonix Blog, "Docker Multi-Stage Builds: Powerful Image Optimization").
- iximiuz Labs, a training resource focused on containers and Linux internals, frames the entire problem of image bloat as a common outcome of not using multi-stage builds, noting that non-multi-stage Dockerfiles are likely to be shipping unnecessary build tools into production, which both increases image size and broadens the potential attack surface (iximiuz Labs, "How to Build Smaller Container Images: Docker Multi-Stage Builds").
- The "one process per container" principle, as described directly in Docker's own documentation, underlies the common microservices pattern of running a web tier, a cache, and a database as separate, independently scalable containers rather than a single container performing every role.

## Sources

- Docker Docs, "General best practices for writing Dockerfiles" — https://docs.Docker.com/develop/develop-images/guidelines/
- Docker Docs, "Building best practices" — https://docs.docker.com/build/building/best-practices/
- Docker Docs, "Building best practices" (articles mirror) — https://docs.docker.com/articles/dockerfile_best-practices/
- Udara Shanuka Senarath, Medium, "Multi-Stage Docker Builds Explained: Building Smaller, Safer Production Images" — https://medium.com/@udarasenarath/multi-stage-docker-builds-explained-building-smaller-safer-production-images-8b7901e36d06
- Oluoch Odhiambo, Medium, "Docker multi-stage build. An effective strategy to build production ready docker images." — https://oluoch-odhiambo.medium.com/docker-multi-stage-build-an-effective-strategy-to-building-production-ready-docker-images-59fda6e94e0
- Cherry Servers, "Docker Multi-stage Build: How to Make Your Docker Image Smaller" — https://www.cherryservers.com/blog/docker-multistage-build
- Better Stack Community, "Best Practices for Building Docker Images" — https://betterstack.com/community/guides/scaling-docker/docker-build-best-practices/
- iximiuz Labs, "How to Build Smaller Container Images: Docker Multi-Stage Builds" — https://labs.iximiuz.com/tutorials/docker-multi-stage-builds
- Spacelift, "Docker Multistage Builds: How to Optimize Your Images" — https://spacelift.io/blog/docker-multistage-builds
- Eduonix Blog, "Docker Multi-Stage Builds: Powerful Image Optimization" — https://blog.eduonix.com/2026/07/docker-multi-stage-builds-reduce-image-size-container-optimization-guide/
