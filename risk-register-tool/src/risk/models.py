from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Mitigation:
    action: str
    owner: str
    status: str = "Planned"  # Planned, In Progress, Complete

@dataclass
class Risk:
    id: int
    title: str
    description: str
    category: str
    likelihood: int  # 1 (Low) - 5 (High)
    impact: int      # 1 (Low) - 5 (High)
    status: str = "Open"  # Open, Mitigated, Closed
    mitigations: List[Mitigation] = field(default_factory=list)
    framework_alignment: Optional[str] = None  # e.g., NIST, ISO 27001


class Threat:
    def __init__(self, name, description, likelihood):
        self.name = name
        self.description = description
        self.likelihood = likelihood


class Control:
    def __init__(self, name, description, effectiveness):
        self.name = name
        self.description = description
        self.effectiveness = effectiveness

    def apply_control(self):
        # Logic to apply the control
        pass