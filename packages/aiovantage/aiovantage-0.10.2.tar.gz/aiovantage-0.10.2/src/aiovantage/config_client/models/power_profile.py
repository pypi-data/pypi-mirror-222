"""Power profile object."""

from dataclasses import dataclass, field

from .system_object import SystemObject


@dataclass
class PowerProfile(SystemObject):
    """Power Profile object."""

    min: float = field(
        metadata={
            "name": "Min",
        }
    )

    max: float = field(
        metadata={
            "name": "Max",
        }
    )

    adjust: int = field(
        metadata={
            "name": "Adjust",
        }
    )

    freq: int = field(
        metadata={
            "name": "Freq",
        }
    )

    inductive: bool = field(
        metadata={
            "name": "Inductive",
        }
    )

    @property
    def is_dimmable(self) -> bool:
        """Return True if loads with this profile are dimmable."""
        return self.max > self.min
