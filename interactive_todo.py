#!/usr/bin/env python3
"""Interactive CLI Task App - User-friendly guided task entry."""

import sys
from datetime import datetime


class Task:
    """Represents a single task with name, description, and due date."""

    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f"📋 {self.name}\n   Description: {self.description}\n   Due Date: {self.due_date}"


def clear_screen():
    """Clear the screen for better readability (optional)."""
    pass  # Keep it simple, no clearing for better compatibility


def print_separator():
    """Print a visual separator."""
    print("-" * 60)


def get_input(prompt, allow_empty=False):
    """Get user input with error handling."""
    while True:
        try:
            value = input(prompt).strip()
            if not value and not allow_empty:
                print("⚠️  This field cannot be empty. Please try again.")
                continue
            return value
        except (EOFError, KeyboardInterrupt):
            print("\n\n⚠️  Input interrupted. Exiting...")
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
    print("\n✏️  Let's create a new task!\n")

    # Field 1: Task Name
    task_name = get_input("Task Name: ")
    print("   ✓ Task name recorded")

    # Field 2: Description
    print()
    description = get_input("Description: ")
    print("   ✓ Description recorded")

    # Field 3: Due Date
    print()
    due_date_input = get_input("Due Date (e.g., 2025-12-31 or 12/31/2025): ", allow_empty=True)
    due_date = validate_date(due_date_input)
    print("   ✓ Due date recorded")

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
            print("⚠️  Please enter 'yes' or 'no'")


def display_all_tasks(tasks):
    """Display all entered tasks in a numbered list."""
    if not tasks:
        print("\n📝 No tasks were entered.")
        return

    print("\n" + "=" * 60)
    print("📋 YOUR TASKS")
    print("=" * 60)

    for i, task in enumerate(tasks, 1):
        print(f"\n{i}. {task}")

    print("\n" + "=" * 60)


def main():
    """Main application loop."""
    # Welcome message
    print("\n" + "=" * 60)
    print(" " * 15 + "Welcome to the CLI Task App!")
    print("=" * 60)
    print("\n📌 This app helps you organize your tasks with ease.")
    print("   Just follow the prompts and we'll guide you through!\n")
    print_separator()

    tasks = []

    try:
        while True:
            # Get task details
            task = get_task_details()
            tasks.append(task)

            # Confirmation message
            print("\n" + "=" * 60)
            print("✅ Entry completed!")
            print("=" * 60)

            # Ask if user wants to continue
            if not ask_continue():
                break

        # Display all tasks before exiting
        display_all_tasks(tasks)

        # Goodbye message
        print("\n" + "=" * 60)
        print("Goodbye! 👋")
        print("=" * 60)
        print()

    except KeyboardInterrupt:
        print("\n\n" + "=" * 60)
        print("⚠️  Program interrupted by user")
        print("=" * 60)

        # Still show what was entered
        if tasks:
            display_all_tasks(tasks)

        print("\nGoodbye! 👋\n")
        sys.exit(0)

    except Exception as e:
        print(f"\n⚠️  An unexpected error occurred: {e}")
        print("Please try running the program again.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
