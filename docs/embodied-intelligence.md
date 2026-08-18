# Embodied Intelligence in Timer OS · 时代系统

Timer OS treats embodied intelligence as a continuously operating system problem rather than a sequence of isolated prompts.

## Core loop

```text
Past experience
      +
Current sensed state
      +
Current intent / task
      ↓
Cognitive scheduling
      ↓
Action / motion allocation
      ↓
Observed outcome
      ↓
Updated evidence and self-model
```

## Three time domains

- **Past is callable** — prior executions, failures, calibration, learned capabilities and context can be recalled.
- **Present is perceivable** — the Body continuously provides state and environmental events.
- **Future is schedulable** — the system can allocate reasoning, actions, attention and future tasks based on current state and intent.

## Self-model

A long-running embodied agent needs more than a static hardware description. It needs a revisable model of itself that can incorporate:

- designed structure and calibration;
- current physical condition;
- observed capability limits;
- accumulated task experience;
- active model or policy versions;
- uncertainty and contradictory evidence.

Timer OS treats human-authored configuration as an initial source of truth, while allowing validated real-world evidence to refine higher-level beliefs about capability and strategy.

## Cognitive scheduling

The central problem is not only providing more context to a model. The system must decide:

- what data deserves real-time attention;
- what history should be recalled;
- what requires deeper reasoning;
- which strategy or model version should be evaluated;
- when an action should execute;
- when the agent should stop, defer or request human involvement.

## Safety boundary

Self-updating cognition is separated from hard real-time control. Motor safety loops and deterministic constraints must remain bounded. New policies or self-model revisions should pass through evaluation and controlled rollout before influencing safety-critical execution.

This repository exposes only the architectural concept. Internal self-model representation, policy competition, validation and scheduling algorithms remain private.
