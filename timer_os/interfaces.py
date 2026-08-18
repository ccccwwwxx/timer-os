from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Protocol, Iterable


@dataclass(frozen=True)
class TimerEvent:
    event_id: str
    occurred_at: datetime
    source: str
    kind: str
    subject_ref: str | None = None
    payload_ref: str | None = None
    summary: str | None = None
    confidence: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class TimerDecision:
    action: str
    reason: str
    priority: float = 0.0
    payload: dict[str, Any] = field(default_factory=dict)


class Body(Protocol):
    """Physical/edge interface. Implementation is intentionally private."""

    def events(self) -> Iterable[TimerEvent]: ...

    def execute(self, decision: TimerDecision) -> None: ...


class ExternalBrain(Protocol):
    """Cognitive-state interface. YIdui may implement this privately."""

    def ingest(self, event: TimerEvent) -> None: ...

    def snapshot(self) -> dict[str, Any]: ...


class TimerScheduler(Protocol):
    """Attention/action scheduling boundary. Strategy remains private."""

    def decide(self, state: dict[str, Any]) -> list[TimerDecision]: ...
