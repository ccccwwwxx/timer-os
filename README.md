# Timer OS · 时代系统

> Past is callable. Present is perceivable. Future is schedulable.
>
> 过去可调用，现在可感知，未来可调度。

**Timer OS（时代系统）** is an experimental operating system centered on **time, attention, context, cognition and action** rather than apps and files.

“时代系统”强调的不只是计时，而是对连续时间中的历史、当前状态与未来行动进行组织和调度。

The project explores a simple premise: if physical space is a scarce resource, then **human attention is the scarce resource of time**. A useful personal AI should therefore do more than answer questions. It should continuously understand context, preserve valuable history, maintain cognitive state, and decide when human attention is actually required.

Timer OS is not limited to humans. The same architecture may also support long-running embodied agents and robots that need continuous sensing, self-model maintenance, cognitive scheduling and action planning.

## Architecture

Timer OS is organized into four conceptual layers:

- **Body** — the physical interface to the real world. Earbuds and an intelligent charging case form the first human reference Body. In embodied robots, Body can include cameras, microphones, force/torque sensors, joint encoders, motors and other physical I/O.
- **External Brain** — the cognitive and memory subsystem that turns continuous experience into usable context.
- **YIdui** — the core cognitive subsystem inside the External Brain, responsible for maintaining knowledge, cognitive state and evidence-backed self-model updates over time.
- **Timer OS Scheduler** — coordinates time, attention, cognition and actions based on history, current state and future intent.

The phone is intentionally treated as a **display/control surface**, not the center of the system.

```text
Real world
   ↓
Body (sensing / edge execution / buffering / connectivity)
   ↓
Timer Event Stream
   ↓
External Brain
   └── YIdui (cognitive state / memory / self-model update)
   ↓
Timer Scheduler
   ↓
Actions / future attention or motion allocation
```

## Cognitive scheduling

As model context handling becomes infrastructure, Timer OS treats **cognitive scheduling** as a higher-level systems problem:

- what should be sensed at high frequency;
- what history should be recalled now;
- which model or reasoning depth should be used;
- when conflicting cognition or policies should trigger re-evaluation;
- when an action should execute;
- when a human should be interrupted;
- for embodied systems, when sensor or motor-state changes should pre-empt current plans.

This separates real-time physical control from slower cognitive evolution. Safety-critical control loops remain deterministic and bounded, while higher-level strategies can be evaluated, compared and updated over time.

## Embodied self-model

For embodied agents, Timer OS explores a persistent **self-model** that is not only configured once by humans but can be continuously revised from real-world evidence.

A self-model may include:

- body structure and current physical state;
- calibrated and observed capability limits;
- learned task competence and failure modes;
- active strategy/policy versions;
- uncertainty about what the agent can or cannot safely do.

New observations should not overwrite old beliefs immediately. Competing models or policies can coexist, accumulate evidence, be tested, and eventually be retained, replaced or conditioned on different environments.

## What is open in this repository

This repository intentionally contains only the **public skeleton** of Timer OS:

- architecture vocabulary and boundaries;
- a minimal event contract for a continuous time stream;
- abstract interfaces for Body, Brain, Scheduler and model providers;
- a reference DeepSeek provider boundary;
- high-level embodied-agent and self-model concepts;
- examples showing how components may be wired together.

The purpose is to make the system architecture discussable and interoperable without exposing proprietary implementation details.

## What is NOT open source

The following components are deliberately kept private:

- Body hardware design and firmware;
- audio routing / seamless recording chain implementation;
- speaker-voiceprint recognition implementation;
- real-time sensor/motor scheduling implementation;
- edge decision logic and local buffering strategy;
- YIdui cognitive-state and self-model update algorithms;
- knowledge, model and policy conflict/update mechanisms;
- strategy evolution and validation logic;
- attention / interruption scheduling strategy;
- production cloud orchestration, prompts, scoring and policy logic;
- proprietary datasets, user data and evaluation data.

Public interfaces may describe how these components connect, but not how the private implementations work internally.

## First product principle: input before interruption

Timer OS starts with a one-way problem:

**Reality → Body → cloud cognition → durable time stream**

The first milestone is not an assistant that constantly talks back. It is a system that can reliably reconstruct high-value parts of a person's day with minimal interaction.

Only after input reliability is proven should Timer OS decide **whether, when and how to interrupt the user**.

The same sequencing applies to embodied systems: first establish reliable state capture and reconstruction, then progressively enable higher-level autonomous scheduling and self-updating strategies.

## DeepSeek

The public skeleton is model-provider-neutral. `DeepSeek` is included as an initial tagged/reference provider for cloud reasoning experiments.

No API keys are stored in this repository. The included provider module is only an interface/example boundary.

Suggested GitHub topics:

`timer-os` `external-brain` `personal-ai` `agent` `deepseek` `edge-ai` `wearable-ai` `embodied-ai` `robotics` `context-engineering`

## Status

Early architecture / skeleton stage. Interfaces are expected to change.

## Contributing

Contributions to public interfaces, event contracts, documentation, interoperability experiments and non-proprietary adapters are welcome. Private subsystem implementations are out of scope for this repository.

## License

MIT License. See [LICENSE](LICENSE).
