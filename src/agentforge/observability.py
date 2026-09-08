from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field


@dataclass
class Trace:
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    started: float = field(default_factory=time.perf_counter)

    def latency_ms(self) -> float:
        return round((time.perf_counter() - self.started) * 1000, 3)
