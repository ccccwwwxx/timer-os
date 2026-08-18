# Timer OS Architecture Skeleton

## 1. System objective

Timer OS treats a person's continuous time stream as the primary system context. The operating objective is to connect three temporal domains:

1. **Past** — callable history and durable context.
2. **Present** — continuously perceived state.
3. **Future** — schedulable attention and actions.

The system does not claim to control the future. It schedules future actions and attention using available state and intent.

## 2. Public component model

### Body

The Body is Timer OS's physical presence in the real world. The first reference form is a separated noise-cancelling earbud system plus an intelligent charging case.

Public responsibilities:
- capture signals and device events;
- preserve source and time metadata;
- expose a stable event stream;
- buffer events when connectivity is unavailable;
- execute commands returned by higher layers.

Private implementation areas include voiceprint recognition, audio switching, local decision policy, firmware, signal processing and hardware architecture.

### External Brain

The External Brain converts a continuous event stream into usable context and memory. It is a Timer OS subsystem, not the whole OS.

### YIdui

YIdui is the core cognitive subsystem inside the External Brain. The public skeleton treats it as a black-box state transition service:

`previous cognitive state + new evidence -> updated cognitive state + trace`

Its internal memory structure, update rules, conflict handling, Lens logic and model orchestration remain private.

### Timer Scheduler

The Scheduler consumes present state, remembered context, current intent and pending actions. It produces scheduling decisions such as defer, execute, surface, request confirmation or interrupt.

The private implementation of interruption scoring and attention allocation is intentionally excluded.

## 3. Data-plane principle

Timer OS separates the **data plane** from the **cognitive plane**.

```text
Data plane:       Body -> Event Stream -> durable ingest
Cognitive plane:  ingest -> External Brain / YIdui -> state
Control plane:    state -> Scheduler -> command -> Body / Agent
```

This permits models and cognitive strategies to change without redesigning the physical capture layer.

## 4. Privacy boundary

Raw personal data should be treated as private by default. The public project defines interfaces only; it does not define a requirement to publish, centrally pool or train on user data.

## 5. MVP direction

The first technical target is reliable one-way input:

1. capture;
2. segment;
3. identify source/time;
4. buffer;
5. transmit;
6. reconstruct a trustworthy event stream;
7. generate cloud-side semantic context.

Active interruption is deliberately a later capability.
