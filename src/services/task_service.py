"""Task service layer for business logic and data management.

This module provides the TaskService class that manages in-memory task storage
and implements all CRUD operations plus search functionality.
"""

from datetime import datetime
from typing import Optional

from ..models.task import Task


# Custom Exceptions
class TaskNotFoundError(Exception):
    """Raised when a task with the specified ID does not exist."""
    pass


class ValidationError(Exception):
    """Raised when input validation fails (e.g., empty description, invalid ID)."""
    pass


# Module-level storage (in-memory only, session-scoped)
_task_store: list[Task] = []
_next_id: int = 1


def add_task(description: str) -> Task:
    """Add a new task with the given description.

    Args:
        description: Non-empty text describing the task

    Returns:
        The newly created Task with auto-assigned ID and timestamp

    Raises:
        ValidationError: If description is empty
    """
    global _next_id

    if not description or not description.strip():
        raise ValidationError("Task description cannot be empty")

    task = Task(
        id=_next_id,
        description=description.strip(),
        completed=False,
        created=datetime.now()
    )
    _next_id += 1
    _task_store.append(task)
    return task


def list_tasks() -> list[Task]:
    """Get all tasks in creation order.

    Returns:
        List of all tasks, ordered by creation timestamp
    """
    return _task_store.copy()


def get_task(task_id: int) -> Optional[Task]:
    """Find a task by its ID.

    Args:
        task_id: The unique task identifier

    Returns:
        The Task if found, None otherwise
    """
    for task in _task_store:
        if task.id == task_id:
            return task
    return None


def update_task(task_id: int, description: str) -> Task:
    """Update a task's description.

    Args:
        task_id: The unique task identifier
        description: New non-empty description

    Returns:
        The updated Task

    Raises:
        TaskNotFoundError: If task_id doesn't exist
        ValidationError: If description is empty
    """
    if not description or not description.strip():
        raise ValidationError("Task description cannot be empty")

    task = get_task(task_id)
    if task is None:
        raise TaskNotFoundError(f"Task ID {task_id} not found")

    task.description = description.strip()
    return task


def delete_task(task_id: int) -> Task:
    """Remove a task from the store.

    Args:
        task_id: The unique task identifier

    Returns:
        The deleted Task

    Raises:
        TaskNotFoundError: If task_id doesn't exist

    Note:
        Task IDs are never reused. The next added task will get the next
        sequential ID, not the deleted task's ID.
    """
    task = get_task(task_id)
    if task is None:
        raise TaskNotFoundError(f"Task ID {task_id} not found")

    _task_store.remove(task)
    return task


def toggle_complete(task_id: int, completed: bool) -> Task:
    """Mark a task as complete or incomplete.

    Args:
        task_id: The unique task identifier
        completed: True to mark complete, False to mark incomplete

    Returns:
        The updated Task

    Raises:
        TaskNotFoundError: If task_id doesn't exist
    """
    task = get_task(task_id)
    if task is None:
        raise TaskNotFoundError(f"Task ID {task_id} not found")

    task.completed = completed
    return task


def search_tasks(keyword: str) -> list[Task]:
    """Search for tasks containing the keyword (case-insensitive).

    Args:
        keyword: Search term to match in task descriptions

    Returns:
        List of tasks containing the keyword (substring match, case-insensitive)

    Raises:
        ValidationError: If keyword is empty
    """
    if not keyword or not keyword.strip():
        raise ValidationError("Search keyword cannot be empty")

    keyword_lower = keyword.strip().lower()
    return [task for task in _task_store if keyword_lower in task.description.lower()]
