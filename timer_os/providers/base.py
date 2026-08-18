from __future__ import annotations

from typing import Protocol


class ReasoningProvider(Protocol):
    """Model-neutral cloud reasoning boundary."""

    def reason(self, *, context: str, instruction: str) -> str: ...
