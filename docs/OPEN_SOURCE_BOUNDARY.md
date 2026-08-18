# Open-source Boundary

Timer OS follows an **open contract / private intelligence** model.

## Public

- event schemas;
- component interfaces;
- provider adapters and examples that contain no secrets;
- architecture documentation;
- interoperability tests;
- developer-facing SDK contracts.

## Private

- Body firmware and hardware implementation;
- audio kernel and routing implementation;
- voiceprint models and biometric pipelines;
- continuous-capture optimization;
- YIdui state model and update engine;
- cognitive conflict-resolution logic;
- attention scheduler implementation;
- proprietary prompt/policy stacks;
- production observability and user data.

The public repository must not contain copied production code from private components. Private components should depend on the public contracts, not the reverse.
