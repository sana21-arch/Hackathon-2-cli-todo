#!/usr/bin/env python3
"""Interactive CLI Task App - User-friendly guided task entry.

This is the main entry point for the interactive task application.
Simply run: python todo.py

For the old command-based CLI, run: python todo.py classic
For the interactive demo, run: python todo.py demo
"""

import sys
from datetime import datetime


class Task:
    """Represents a single task with name, description, and due date."""

    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f"[Task] {self.name}\n   Description: {self.description}\n   Due Date: {self.due_date}"


def print_separator():
    """Print a visual separator."""
    print("-" * 60)


def get_input(prompt, allow_empty=False):
    """Get user input with error handling."""
    while True:
        try:
            value = input(prompt).strip()
            if not value and not allow_empty:
                print("   This field cannot be empty. Please try again.")
                continue
            return value
        except (EOFError, KeyboardInterrupt):
            print("\n\n   Input interrupted. Exiting...")
            sys.exit(0)


def validate_date(date_str):
    """Validate and format the due date."""
    if not date_str:
        return "Not specified"

    # Try to parse common date formats
    date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%m-%d-%Y"]

    for fmt in date_formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            return parsed_date.strftime("%Y-%m-%d")  # Standardize format
        except ValueError:
            continue

    # If no format matches, just return the input (be flexible)
    return date_str


def get_task_details():
    """Guide user through entering task details."""
    print("\nLet's create a new task!\n")

    # Field 1: Task Name
    task_name = get_input("Task Name: ")
    print("   [OK] Task name recorded")

    # Field 2: Description
    print()
    description = get_input("Description: ")
    print("   [OK] Description recorded")

    # Field 3: Due Date
    print()
    due_date_input = get_input("Due Date (e.g., 2025-12-31 or 12/31/2025): ", allow_empty=True)
    due_date = validate_date(due_date_input)
    print("   [OK] Due date recorded")

    return Task(task_name, description, due_date)


def ask_continue():
    """Ask user if they want to add another entry."""
    print()
    print_separator()
    while True:
        response = input("\nDo you want to add another entry? (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("   Please enter 'yes' or 'no'")


def display_all_tasks(tasks):
    """Display all entered tasks in a numbered list."""
    if not tasks:
        print("\nNo tasks were entered.")
        return

    print("\n" + "=" * 60)
    print("YOUR TASKS")
    print("=" * 60)

    for i, task in enumerate(tasks, 1):
        print(f"\n{i}. {task}")

    print("\n" + "=" * 60)


def run_interactive_mode():
    """Run the interactive task entry mode."""
    # Welcome message
    print("\n" + "=" * 60)
    print(" " * 15 + "Welcome to the CLI Task App!")
    print("=" * 60)
    print("\nThis app helps you organize your tasks with ease.")
    print("Just follow the prompts and we'll guide you through!\n")
    print_separator()

    tasks = []

    try:
        while True:
            # Get task details
            task = get_task_details()
            tasks.append(task)

            # Confirmation message
            print("\n" + "=" * 60)
            print("Entry completed!")
            print("=" * 60)

            # Ask if user wants to continue
            if not ask_continue():
                break

        # Display all tasks before exiting
        display_all_tasks(tasks)

        # Goodbye message
        print("\n" + "=" * 60)
        print("Goodbye!")
        print("=" * 60)
        print()

    except KeyboardInterrupt:
        print("\n\n" + "=" * 60)
        print("Program interrupted by user")
        print("=" * 60)

        # Still show what was entered
        if tasks:
            display_all_tasks(tasks)

        print("\nGoodbye!\n")
        sys.exit(0)

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please try running the program again.\n")
        sys.exit(1)


def run_classic_mode():
    """Run the original command-based CLI mode."""
    from src.cli.main import main
    return main()


def run_demo_mode():
    """Run an interactive demo showing all features in a single session."""
    from src.services import task_service
    from src.services.task_service import TaskNotFoundError, ValidationError

    print("=" * 70)
    print("  CLI TODO TRACKER - INTERACTIVE DEMO MODE")
    print("=" * 70)
    print("\nThis demo runs all commands in a single session to show persistence.\n")

    # Add tasks
    print("1. Adding tasks...")
    try:
        t1 = task_service.add_task("Buy groceries")
        print(f'   Added task #{t1.id}: "{t1.description}"')
        t2 = task_service.add_task("Write monthly report")
        print(f'   Added task #{t2.id}: "{t2.description}"')
        t3 = task_service.add_task("Call dentist for appointment")
        print(f'   Added task #{t3.id}: "{t3.description}"')
        t4 = task_service.add_task("Review code changes")
        print(f'   Added task #{t4.id}: "{t4.description}"')
    except Exception as e:
        print(f"   Error: {e}")
        return 1

    # List tasks
    print("\n2. Listing all tasks...")
    tasks = task_service.list_tasks()
    print("   ID | Status | Description")
    print("   ---|--------|------------")
    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"   {task.id:<2} | {status:^6} | {task.description}")

    # Mark tasks complete
    print("\n3. Marking tasks complete...")
    task = task_service.toggle_complete(1, True)
    print(f'   Marked task #{task.id} as complete: "{task.description}"')
    task = task_service.toggle_complete(3, True)
    print(f'   Marked task #{task.id} as complete: "{task.description}"')

    # List updated tasks
    print("\n4. Viewing updated task list...")
    tasks = task_service.list_tasks()
    print("   ID | Status | Description")
    print("   ---|--------|------------")
    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"   {task.id:<2} | {status:^6} | {task.description}")

    # Update a task
    print("\n5. Updating task description...")
    task = task_service.update_task(2, "Write and submit monthly report")
    print(f'   Updated task #{task.id}: "{task.description}"')

    # Search tasks
    print("\n6. Searching for tasks containing 'report'...")
    results = task_service.search_tasks("report")
    print(f"   Found {len(results)} task(s):")
    for task in results:
        status = "[X]" if task.completed else "[ ]"
        print(f"   {task.id} {status} {task.description}")

    # Delete a task
    print("\n7. Deleting a task...")
    task = task_service.delete_task(4)
    print(f'   Deleted task #{task.id}: "{task.description}"')

    # Final list
    print("\n8. Final task list...")
    tasks = task_service.list_tasks()
    print("   ID | Status | Description")
    print("   ---|--------|------------")
    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"   {task.id:<2} | {status:^6} | {task.description}")
    print(f"\n   Total tasks: {len(tasks)}")

    # Error handling demo
    print("\n9. Error handling demo...")
    try:
        task_service.add_task("")
    except ValidationError:
        print("   [X] Empty description rejected correctly")

    try:
        task_service.delete_task(999)
    except TaskNotFoundError:
        print("   [X] Invalid task ID rejected correctly")

    print("\n" + "=" * 70)
    print("  DEMO COMPLETE - All features working correctly!")
    print("=" * 70)
    print("\n  Features demonstrated:")
    print("  - Add tasks")
    print("  - List tasks with status indicators")
    print("  - Mark tasks complete/incomplete")
    print("  - Update task descriptions")
    print("  - Search tasks by keyword")
    print("  - Delete tasks")
    print("  - Error handling and validation")
    print("\n  Note: Tasks are stored in memory only (lost after program exits)")
    print("=" * 70)
    return 0


def main():
    """Main entry point - route to appropriate mode."""
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode == "demo":
            return run_demo_mode()
        elif mode == "classic":
            return run_classic_mode()
        elif mode in ["help", "-h", "--help"]:
            print("\nCLI Task App - Usage:\n")
            print("  python todo.py           # Interactive mode (default)")
            print("  python todo.py classic   # Command-based mode")
            print("  python todo.py demo      # Demo mode")
            print("  python todo.py help      # Show this help\n")
            return 0

    # Default: Run interactive mode
    run_interactive_mode()
    return 0


if __name__ == "__main__":
    sys.exit(main())
