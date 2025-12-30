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
    try:
        task = task_service.toggle_complete(task_id, completed=True)
        print(f'Marked task #{task.id} as complete: "{task.description}"')
        return 0
    except TaskNotFoundError as e:
        print(f"Error: {e}. Use 'todo list' to see valid task IDs.", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def incomplete_command(task_id: int) -> int:
    """Handle the 'incomplete' command.

    Args:
        task_id: ID of task to mark incomplete

    Returns:
        Exit code: 0 for success, 1 for error
    """
    try:
        task = task_service.toggle_complete(task_id, completed=False)
        print(f'Marked task #{task.id} as incomplete: "{task.description}"')
        return 0
    except TaskNotFoundError as e:
        print(f"Error: {e}. Use 'todo list' to see valid task IDs.", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def delete_command(task_id: int) -> int:
    """Handle the 'delete' command.

    Args:
        task_id: ID of task to delete

    Returns:
        Exit code: 0 for success, 1 for error
    """
    try:
        task = task_service.delete_task(task_id)
        print(f'Deleted task #{task.id}: "{task.description}"')
        return 0
    except TaskNotFoundError as e:
        print(f"Error: {e}. Use 'todo list' to see valid task IDs.", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def update_command(task_id: int, description: str) -> int:
    """Handle the 'update' command.

    Args:
        task_id: ID of task to update
        description: New task description

    Returns:
        Exit code: 0 for success, 1 for error
    """
    try:
        task = task_service.update_task(task_id, description)
        print(f'Updated task #{task.id}: "{task.description}"')
        return 0
    except TaskNotFoundError as e:
        print(f"Error: {e}. Use 'todo list' to see valid task IDs.", file=sys.stderr)
        return 1
    except ValidationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def search_command(keyword: str) -> int:
    """Handle the 'search' command.

    Args:
        keyword: Search term to find in task descriptions

    Returns:
        Exit code: 0 for success, 1 for error
    """
    try:
        tasks = task_service.search_tasks(keyword)

        if not tasks:
            print(f'No tasks found matching "{keyword}"')
            return 0

        # Print header
        print(f'Tasks matching "{keyword}":')
        print("ID | Status | Description")
        print("---|--------|------------")

        # Print matching tasks
        for task in tasks:
            status = "[✓]" if task.completed else "[ ]"
            print(f"{task.id:<2} | {status:^6} | {task.description}")

        return 0
    except ValidationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1
