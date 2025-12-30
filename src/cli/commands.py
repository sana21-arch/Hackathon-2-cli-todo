"""Command handlers for the Todo CLI.

This module implements all CLI command logic, formatting output and handling errors.
"""

import sys

from ..services import task_service
from ..services.task_service import TaskNotFoundError, ValidationError


def add_command(description: str) -> int:
    """Handle the 'add' command.

    Args:
        description: Task description provided by user

    Returns:
        Exit code: 0 for success, 1 for error
    """
    try:
        task = task_service.add_task(description)
        print(f'Added task #{task.id}: "{task.description}"')
        return 0
    except ValidationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def list_command() -> int:
    """Handle the 'list' command.

    Returns:
        Exit code: 0 for success, 1 for error
    """
    try:
        tasks = task_service.list_tasks()

        if not tasks:
            print("No tasks yet. Add one with: todo add '<description>'")
            return 0

        # Print header
        print("ID | Status | Description")
        print("---|--------|------------")

        # Print tasks
        for task in tasks:
            status = "[✓]" if task.completed else "[ ]"
            print(f"{task.id:<2} | {status:^6} | {task.description}")

        return 0
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def complete_command(task_id: int) -> int:
    """Handle the 'complete' command.

    Args:
        task_id: ID of task to mark complete

    Returns:
        Exit code: 0 for success, 1 for error
    """
    # Stub - to be implemented in Phase 4
    print("complete command - not yet implemented", file=sys.stderr)
    return 1


def incomplete_command(task_id: int) -> int:
    """Handle the 'incomplete' command.

    Args:
        task_id: ID of task to mark incomplete

    Returns:
        Exit code: 0 for success, 1 for error
    """
    # Stub - to be implemented in Phase 4
    print("incomplete command - not yet implemented", file=sys.stderr)
    return 1


def delete_command(task_id: int) -> int:
    """Handle the 'delete' command.

    Args:
        task_id: ID of task to delete

    Returns:
        Exit code: 0 for success, 1 for error
    """
    # Stub - to be implemented in Phase 5
    print("delete command - not yet implemented", file=sys.stderr)
    return 1


def update_command(task_id: int, description: str) -> int:
    """Handle the 'update' command.

    Args:
        task_id: ID of task to update
        description: New task description

    Returns:
        Exit code: 0 for success, 1 for error
    """
    # Stub - to be implemented in Phase 6
    print("update command - not yet implemented", file=sys.stderr)
    return 1


def search_command(keyword: str) -> int:
    """Handle the 'search' command.

    Args:
        keyword: Search term to find in task descriptions

    Returns:
        Exit code: 0 for success, 1 for error
    """
    # Stub - to be implemented in Phase 7
    print("search command - not yet implemented", file=sys.stderr)
    return 1
