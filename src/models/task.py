"""Task model for the Todo application.

This module defines the Task dataclass representing a single todo item.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """Represents a single todo task.

    Attributes:
        id: Unique sequential identifier starting from 1, auto-assigned
        description: User-provided text describing the task, non-empty
        completed: Status flag indicating if task is done (True) or pending (False)
        created: Timestamp when task was added, auto-assigned, used for display ordering
    """
    id: int
    description: str
    completed: bool
    created: datetime
