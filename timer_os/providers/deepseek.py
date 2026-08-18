"""DeepSeek reference provider boundary.

This public module intentionally contains no production endpoint, authentication
logic, private prompts or cognitive policy. Implement those outside the public
skeleton.
"""

from dataclasses import dataclass
from typing import Callable


@dataclass
class DeepSeekProvider:
    call_model: Callable[[str, str], str]

    def reason(self, *, context: str, instruction: str) -> str:
        return self.call_model(context, instruction)
