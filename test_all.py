#!/usr/bin/env python3
"""Comprehensive test script for CLI Todo MVP.

This script tests all service layer functionality and validates
that the implementation meets the specification requirements.
"""

from src.services import task_service
from src.services.task_service import TaskNotFoundError, ValidationError


def print_header(title):
    """Print a formatted test section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def print_tasks(tasks):
    """Print tasks in formatted table."""
    if not tasks:
        print("  No tasks in list")
        return

    print("  ID | Status | Description")
    print("  ---|--------|------------")
    for task in tasks:
        status = "[✓]" if task.completed else "[ ]"
        print(f"  {task.id:<2} | {status:^6} | {task.description}")


def test_add_tasks():
    """Test adding tasks (User Story 1 - Part 1)."""
    print_header("TEST 1: Add Tasks")

    t1 = task_service.add_task("Buy groceries")
    print(f"  ✓ Added task #{t1.id}: \"{t1.description}\"")
    assert t1.id == 1, "First task should have ID 1"
    assert t1.description == "Buy groceries"
    assert t1.completed == False

    t2 = task_service.add_task("Pay electricity bill")
    print(f"  ✓ Added task #{t2.id}: \"{t2.description}\"")
    assert t2.id == 2, "Second task should have ID 2"

    t3 = task_service.add_task("Call dentist")
    print(f"  ✓ Added task #{t3.id}: \"{t3.description}\"")
    assert t3.id == 3, "Third task should have ID 3"

    print("  ✅ PASSED: All tasks added successfully")


def test_list_tasks():
    """Test listing tasks (User Story 1 - Part 2)."""
    print_header("TEST 2: List Tasks")

    tasks = task_service.list_tasks()
    print(f"  Found {len(tasks)} tasks:")
    print_tasks(tasks)

    assert len(tasks) == 3, "Should have 3 tasks"
    assert tasks[0].id == 1
    assert tasks[1].id == 2
    assert tasks[2].id == 3

    print("  ✅ PASSED: Task list retrieved successfully")


def test_mark_complete():
    """Test marking tasks complete/incomplete (User Story 2)."""
    print_header("TEST 3: Mark Task Complete")

    # Mark task 1 complete
    task = task_service.toggle_complete(1, True)
    print(f"  ✓ Marked task #{task.id} as complete")
    assert task.completed == True

    # Verify in list
    tasks = task_service.list_tasks()
    print("\n  Updated task list:")
    print_tasks(tasks)

    assert tasks[0].completed == True
    assert tasks[1].completed == False
    assert tasks[2].completed == False

    # Mark incomplete again
    task = task_service.toggle_complete(1, False)
    print(f"\n  ✓ Marked task #{task.id} as incomplete")
    assert task.completed == False

    print("  ✅ PASSED: Complete/Incomplete toggle works")


def test_delete_task():
    """Test deleting tasks (User Story 3)."""
    print_header("TEST 4: Delete Task")

    # Delete task 3
    deleted = task_service.delete_task(3)
    print(f"  ✓ Deleted task #{deleted.id}: \"{deleted.description}\"")

    # Verify it's gone
    tasks = task_service.list_tasks()
    print(f"\n  Remaining tasks ({len(tasks)}):")
    print_tasks(tasks)

    assert len(tasks) == 2, "Should have 2 tasks after deletion"
    assert tasks[0].id == 1
    assert tasks[1].id == 2

    # Add new task - should get ID 4, not 3 (IDs never reused)
    new_task = task_service.add_task("New task after deletion")
    print(f"\n  ✓ Added new task #{new_task.id}: \"{new_task.description}\"")
    assert new_task.id == 4, "New task should have ID 4 (IDs never reused)"

    print("  ✅ PASSED: Delete works, IDs never reused")


def test_update_task():
    """Test updating task descriptions (User Story 4)."""
    print_header("TEST 5: Update Task")

    # Update task 2
    updated = task_service.update_task(2, "Pay electricity bill URGENTLY")
    print(f"  ✓ Updated task #{updated.id}")
    print(f"    New description: \"{updated.description}\"")

    assert updated.description == "Pay electricity bill URGENTLY"

    # Verify in list
    task = task_service.get_task(2)
    assert task.description == "Pay electricity bill URGENTLY"

    print("  ✅ PASSED: Update works correctly")


def test_search_tasks():
    """Test searching tasks by keyword (User Story 5)."""
    print_header("TEST 6: Search Tasks")

    # Search for "bill"
    results = task_service.search_tasks("bill")
    print(f"  Searching for 'bill' - found {len(results)} result(s):")
    print_tasks(results)

    assert len(results) == 1
    assert "bill" in results[0].description.lower()

    # Search for "task" (case-insensitive)
    results = task_service.search_tasks("TASK")
    print(f"\n  Searching for 'TASK' (case-insensitive) - found {len(results)} result(s):")
    print_tasks(results)

    assert len(results) >= 1

    print("  ✅ PASSED: Search works (case-insensitive)")


def test_validation_empty_description():
    """Test validation for empty descriptions."""
    print_header("TEST 7: Validation - Empty Description")

    try:
        task_service.add_task("")
        print("  ✗ FAILED: Should have raised ValidationError")
        assert False, "Should have raised ValidationError"
    except ValidationError as e:
        print(f"  ✓ Correctly rejected empty description")
        print(f"    Error message: \"{e}\"")

    try:
        task_service.add_task("   ")
        print("  ✗ FAILED: Should have raised ValidationError for whitespace")
        assert False, "Should have raised ValidationError"
    except ValidationError as e:
        print(f"  ✓ Correctly rejected whitespace-only description")
        print(f"    Error message: \"{e}\"")

    print("  ✅ PASSED: Empty description validation works")


def test_validation_invalid_id():
    """Test validation for invalid task IDs."""
    print_header("TEST 8: Validation - Invalid Task ID")

    # Non-existent ID should return None for get_task
    result = task_service.get_task(999)
    print(f"  ✓ get_task(999) returned: {result}")
    assert result is None

    # Operations on non-existent ID should raise TaskNotFoundError
    try:
        task_service.toggle_complete(999, True)
        print("  ✗ FAILED: Should have raised TaskNotFoundError")
        assert False, "Should have raised TaskNotFoundError"
    except TaskNotFoundError as e:
        print(f"  ✓ Correctly raised TaskNotFoundError")
        print(f"    Error message: \"{e}\"")

    try:
        task_service.delete_task(999)
        print("  ✗ FAILED: Should have raised TaskNotFoundError")
        assert False, "Should have raised TaskNotFoundError"
    except TaskNotFoundError as e:
        print(f"  ✓ Correctly raised TaskNotFoundError for delete")

    print("  ✅ PASSED: Invalid ID validation works")


def test_validation_empty_search():
    """Test validation for empty search keyword."""
    print_header("TEST 9: Validation - Empty Search Keyword")

    try:
        task_service.search_tasks("")
        print("  ✗ FAILED: Should have raised ValidationError")
        assert False, "Should have raised ValidationError"
    except ValidationError as e:
        print(f"  ✓ Correctly rejected empty search keyword")
        print(f"    Error message: \"{e}\"")

    print("  ✅ PASSED: Empty search validation works")


def test_final_state():
    """Display final state of task list."""
    print_header("FINAL STATE")

    tasks = task_service.list_tasks()
    print(f"  Total tasks: {len(tasks)}")
    print_tasks(tasks)

    completed = sum(1 for t in tasks if t.completed)
    incomplete = len(tasks) - completed
    print(f"\n  Completed: {completed}")
    print(f"  Incomplete: {incomplete}")


def run_all_tests():
    """Run all tests in sequence."""
    print("\n" + "=" * 60)
    print("  CLI TODO - COMPREHENSIVE TEST SUITE")
    print("  Testing MVP Implementation (User Stories 1-5)")
    print("=" * 60)

    try:
        test_add_tasks()
        test_list_tasks()
        test_mark_complete()
        test_delete_task()
        test_update_task()
        test_search_tasks()
        test_validation_empty_description()
        test_validation_invalid_id()
        test_validation_empty_search()
        test_final_state()

        print("\n" + "=" * 60)
        print("  🎉 ALL TESTS PASSED!")
        print("  MVP is fully functional and meets specifications")
        print("=" * 60)
        print("\n  ✅ User Story 1 (Add/View): WORKING")
        print("  ✅ User Story 2 (Complete/Incomplete): WORKING")
        print("  ✅ User Story 3 (Delete): WORKING")
        print("  ✅ User Story 4 (Update): WORKING")
        print("  ✅ User Story 5 (Search): WORKING")
        print("  ✅ Input Validation: WORKING")
        print("  ✅ Error Handling: WORKING")
        print("\n")
        return 0

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(run_all_tests())
