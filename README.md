# Timer OS

> Past is callable. Present is perceivable. Future is schedulable.
>
> 过去可调用，现在可感知，未来可调度。

Timer OS is an experimental personal operating system centered on **time, attention, context and action** rather than apps and files.

The project explores a simple premise: if physical space is a scarce resource, then **human attention is the scarce resource of time**. A useful personal AI should therefore do more than answer questions. It should continuously understand context, preserve valuable history, maintain cognitive state, and decide when human attention is actually required.

## Architecture

Timer OS is organized into four conceptual layers:

- **Body** — the physical interface to the real world. Earbuds and an intelligent charging case form the first reference Body. The Body captures audio/context, performs edge-side routing and buffering, maintains connectivity, and executes real-time decisions.
- **External Brain** — the cognitive and memory subsystem that turns continuous experience into usable context.
- **YIdui** — the core cognitive subsystem inside the External Brain, responsible for maintaining knowledge and cognitive state over time.
- **Timer OS Scheduler** — coordinates time, attention and actions based on history, current context and future intent.

The phone is intentionally treated as a **display/control surface**, not the center of the system.

```text
Real world
   ↓
Body (sensing / edge execution / buffering / connectivity)
   ↓
Timer Event Stream
   ↓
External Brain
   └── YIdui (cognitive state / memory update)
   ↓
Timer Scheduler
   ↓
Actions / future attention allocation
```

## What is open in this repository

This repository intentionally contains only the **public skeleton** of Timer OS:

- architecture vocabulary and boundaries;
- a minimal event contract for a continuous time stream;
- abstract interfaces for Body, Brain, Scheduler and model providers;
- a reference DeepSeek provider boundary;
- examples showing how components may be wired together.

The purpose is to make the system architecture discussable and interoperable without exposing proprietary implementation details.

## What is NOT open source

The following components are deliberately kept private:

- Body hardware design and firmware;
- audio routing / seamless recording chain implementation;
- speaker-voiceprint recognition implementation;
- edge decision logic and local buffering strategy;
- YIdui cognitive-state update algorithms;
- knowledge conflict and update policies;
- attention / interruption scheduling strategy;
- production cloud orchestration, prompts, scoring and policy logic;
- proprietary datasets, user data and evaluation data.

Public interfaces may describe how these components connect, but not how the private implementations work internally.

## First product principle: input before interruption

Timer OS starts with a one-way problem:

**Reality → Body → cloud cognition → durable time stream**

The first milestone is not an assistant that constantly talks back. It is a system that can reliably reconstruct high-value parts of a person's day with minimal interaction.

Only after input reliability is proven should Timer OS decide **whether, when and how to interrupt the user**.

## DeepSeek

The public skeleton is model-provider-neutral. `DeepSeek` is included as an initial tagged/reference provider for cloud reasoning experiments.

No API keys are stored in this repository. The included provider module is only an interface/example boundary.

Suggested GitHub topics:

`timer-os` `external-brain` `personal-ai` `agent` `deepseek` `edge-ai` `wearable-ai` `context-engineering`

## Status

Early architecture / skeleton stage. Interfaces are expected to change.

## Contributing

Contributions to public interfaces, event contracts, documentation, interoperability experiments and non-proprietary adapters are welcome. Private subsystem implementations are out of scope for this repository.

## License

MIT License. See [LICENSE](LICENSE).
