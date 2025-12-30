#!/usr/bin/env python3
"""Interactive demo script for the CLI Todo application."""

import subprocess
import sys

print("=" * 70)
print("  CLI TODO TRACKER - INTERACTIVE DEMO")
print("=" * 70)
print()
print("This demo shows all available commands. Note: tasks are in-memory only,")
print("so each command runs independently and tasks won't persist between commands.")
print()
print("For real usage, run commands sequentially in a Python script or use")
print("the interactive Python shell to maintain state.")
print("=" * 70)
print()

def run_command(description, command):
    """Run a CLI command and display the output."""
    print(f"\n>>> {description}")
    print(f"$ python todo.py {command}")
    print("-" * 70)
    result = subprocess.run(
        f"python todo.py {command}",
        shell=True,
        capture_output=True,
        text=True
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)
    print()

# Demo commands
print("\n1. HELP - View available commands")
run_command("Show help information", "--help")

print("\n2. ADD - Add new tasks")
run_command("Add a task", 'add "Buy groceries"')
run_command("Add another task", 'add "Write report"')
run_command("Add a third task", 'add "Call dentist"')

print("\n3. LIST - View all tasks")
run_command("List all tasks (empty because each command is separate process)", "list")

print("\n4. ERROR HANDLING - Try invalid operations")
run_command("Try to add empty task", 'add ""')
run_command("Try to complete non-existent task", "complete 999")

print("=" * 70)
print("\n  INTERACTIVE USAGE EXAMPLE")
print("=" * 70)
print()
print("To use the CLI with persistent state during a session, use the service layer")
print("directly in Python:")
print()
print("    from src.services import task_service")
print()
print("    # Add tasks")
print('    task1 = task_service.add_task("Buy groceries")')
print('    task2 = task_service.add_task("Write report")')
print()
print("    # List tasks")
print("    tasks = task_service.list_tasks()")
print("    for task in tasks:")
print('        print(f"{task.id} - {task.description}")')
print()
print("    # Mark complete")
print("    task_service.toggle_complete(1, True)")
print()
print("    # Update task")
print('    task_service.update_task(2, "Write monthly report")')
print()
print("    # Search tasks")
print('    results = task_service.search_tasks("report")')
print()
print("    # Delete task")
print("    task_service.delete_task(1)")
print()
print("=" * 70)
print("\nRun 'python manual_test.py' to see all features working together!")
print("=" * 70)
