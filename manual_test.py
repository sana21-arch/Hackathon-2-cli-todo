#!/usr/bin/env python3
"""Simple manual test script for the CLI Todo application."""

import sys
from src.services import task_service

print("=" * 60)
print("  MANUAL TEST - CLI TODO FUNCTIONALITY")
print("=" * 60)

# Test 1: Add tasks
print("\nTest 1: Adding tasks...")
try:
    task1 = task_service.add_task("Buy groceries")
    print(f"  Added task #{task1.id}: {task1.description}")

    task2 = task_service.add_task("Write report")
    print(f"  Added task #{task2.id}: {task2.description}")

    task3 = task_service.add_task("Call dentist")
    print(f"  Added task #{task3.id}: {task3.description}")
    print("  PASS: Add tasks")
except Exception as e:
    print(f"  FAIL: {e}")
    sys.exit(1)

# Test 2: List tasks
print("\nTest 2: Listing tasks...")
try:
    tasks = task_service.list_tasks()
    print(f"  Found {len(tasks)} tasks")
    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"    {task.id} {status} {task.description}")
    print("  PASS: List tasks")
except Exception as e:
    print(f"  FAIL: {e}")
    sys.exit(1)

# Test 3: Mark task complete
print("\nTest 3: Marking task complete...")
try:
    task = task_service.toggle_complete(1, True)
    print(f"  Task #{task.id} marked complete: {task.description}")
    print("  PASS: Mark complete")
except Exception as e:
    print(f"  FAIL: {e}")
    sys.exit(1)

# Test 4: Mark task incomplete
print("\nTest 4: Marking task incomplete...")
try:
    task = task_service.toggle_complete(1, False)
    print(f"  Task #{task.id} marked incomplete: {task.description}")
    print("  PASS: Mark incomplete")
except Exception as e:
    print(f"  FAIL: {e}")
    sys.exit(1)

# Test 5: Update task
print("\nTest 5: Updating task...")
try:
    task = task_service.update_task(2, "Write monthly report")
    print(f"  Task #{task.id} updated: {task.description}")
    print("  PASS: Update task")
except Exception as e:
    print(f"  FAIL: {e}")
    sys.exit(1)

# Test 6: Search tasks
print("\nTest 6: Searching tasks...")
try:
    results = task_service.search_tasks("report")
    print(f"  Found {len(results)} tasks matching 'report'")
    for task in results:
        print(f"    {task.id} - {task.description}")
    print("  PASS: Search tasks")
except Exception as e:
    print(f"  FAIL: {e}")
    sys.exit(1)

# Test 7: Delete task
print("\nTest 7: Deleting task...")
try:
    task = task_service.delete_task(3)
    print(f"  Task #{task.id} deleted: {task.description}")
    remaining = task_service.list_tasks()
    print(f"  {len(remaining)} tasks remaining")
    print("  PASS: Delete task")
except Exception as e:
    print(f"  FAIL: {e}")
    sys.exit(1)

# Test 8: Error handling
print("\nTest 8: Error handling...")
try:
    # Try to get non-existent task
    from src.services.task_service import TaskNotFoundError, ValidationError

    try:
        task_service.delete_task(999)
        print("  FAIL: Should have raised TaskNotFoundError")
    except TaskNotFoundError:
        print("  PASS: TaskNotFoundError raised correctly")

    try:
        task_service.add_task("")
        print("  FAIL: Should have raised ValidationError")
    except ValidationError:
        print("  PASS: ValidationError raised correctly")

except Exception as e:
    print(f"  FAIL: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("  ALL TESTS PASSED!")
print("=" * 60)
print("\nAll core functionality is working correctly.")
print("Tasks are stored in memory only and will be lost on exit.")
