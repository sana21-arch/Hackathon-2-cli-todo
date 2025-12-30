# Data Model: CLI In-Memory Todo System

**Feature**: `001-cli-todo`
**Created**: 2025-12-30

## Entity: Task

### Fields

| Field | Type | Required | Default | Validation | Description |
|-------|------|----------|---------|------------|-------------|
| `id` | `int` | Yes | Auto-assigned | > 0, unique | Sequential identifier starting from 1 |
| `description` | `str` | Yes | N/A | Non-empty, any printable chars | User-provided task text |
| `completed` | `bool` | Yes | `False` | N/A | Completion status flag |
| `created` | `datetime` | Yes | Auto-assigned | N/A | Task creation timestamp (UTC) |

### Python Implementation

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    description: str
    completed: bool
    created: datetime
```

### State Transitions

```
┌─────────────┐
│  New Task   │
│ completed=  │
│   False     │
└──────┬──────┘
       │
       │ complete command
       ↓
┌─────────────┐
│  Completed  │
│ completed=  │
│    True     │
└──────┬──────┘
       │
       │ incomplete command
       ↓
┌─────────────┐
│ Incomplete  │
│ completed=  │
│   False     │
└──────┬──────┘
       │
       │ delete command
       ↓
┌─────────────┐
│   Removed   │
│    from     │
│   storage   │
└─────────────┘
```

### Validation Rules

**Description Field**:
- MUST NOT be empty string (FR-009 from spec.md:spec.md:109)
- MAY contain any printable Unicode characters
- MAY contain quotes, newlines, special characters
- No maximum length enforced (practical limit: in-memory constraints)

**ID Field**:
- MUST be positive integer (> 0)
- MUST be unique across all tasks
- MUST be sequential (auto-increment, starting from 1)
- MUST exist in task store before operations (FR-010 from spec.md:spec.md:110)
- MUST NOT be reused after deletion (permanent IDs)

**Completed Field**:
- Boolean flag: `True` (complete) or `False` (incomplete)
- Defaults to `False` when task is created
- Toggleable via `complete` and `incomplete` commands

**Created Field**:
- Auto-assigned timestamp when task is added
- Immutable after creation
- Used for display ordering (tasks listed in creation order)
- UTC timezone recommended for consistency

### Storage Strategy

**In-Memory Store**:
```python
# Module-level in task_service.py
_task_store: list[Task] = []
_next_id: int = 1
```

**ID Generation**:
- Global counter `_next_id` tracks next available ID
- Incremented after each task creation
- Never decremented (even after deletion)

**Example ID Sequence**:
```
Add task → ID 1
Add task → ID 2
Add task → ID 3
Delete task ID 2 → _next_id still 4
Add task → ID 4 (not 2!)
```

### Lookup Operations

**By ID** (O(n) linear search):
```python
def get_task(task_id: int) -> Task | None:
    for task in _task_store:
        if task.id == task_id:
            return task
    return None
```

**By Keyword** (O(n) linear search with substring match):
```python
def search_tasks(keyword: str) -> list[Task]:
    keyword_lower = keyword.lower()
    return [task for task in _task_store
            if keyword_lower in task.description.lower()]
```

### Performance Characteristics

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Add task | O(1) | Append to list |
| Get task by ID | O(n) | Linear search |
| Update task | O(n) | Find + modify |
| Delete task | O(n) | Find + remove |
| List all tasks | O(n) | Iterate all |
| Search tasks | O(n) | Iterate + substring match |

**Scale**: Target 1,000+ tasks. Linear search acceptable for in-memory Phase 1. Phase 2 could optimize with dict lookup if needed.

### Display Format

**List View**:
```
ID | Status | Description
---|--------|------------
1  | [ ]    | Buy groceries
2  | [✓]    | Pay bills
3  | [ ]    | Call dentist
```

**Status Indicators**:
- `[ ]` - Incomplete (`completed=False`)
- `[✓]` - Complete (`completed=True`)

**Ordering**: Tasks displayed in creation order (sorted by `created` timestamp ascending)

### Edge Cases

**Empty List**: No tasks in `_task_store`. List command displays help message.

**Very Long Descriptions**: Accepted and stored. May truncate in display with ellipsis if >80 characters.

**Special Characters**: Quotes, newlines, Unicode all supported. CLI handles escaping for shell compatibility.

**ID Gaps After Deletion**: Expected behavior. IDs 1, 3, 5 valid after deleting 2, 4.

**Session Scope**: All data lost when program exits (in-memory only, no persistence).
