"""Main entry point for the Todo CLI application.

This module sets up the argument parser and dispatches commands to their handlers.
"""

import argparse
import sys

from . import commands


def main() -> int:
    """Main entry point for the CLI application.

    Returns:
        Exit code: 0 for success, 1 for error
    """
    parser = argparse.ArgumentParser(
        prog="todo",
        description="CLI In-Memory Todo System - Manage your tasks from the command line",
        epilog="Use 'todo <command> --help' for command-specific help"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    parser_add = subparsers.add_parser(
        "add",
        help="Add a new task"
    )
    parser_add.add_argument(
        "description",
        type=str,
        help="Task description"
    )

    # List command
    parser_list = subparsers.add_parser(
        "list",
        help="List all tasks"
    )

    # Complete command
    parser_complete = subparsers.add_parser(
        "complete",
        help="Mark a task as complete"
    )
    parser_complete.add_argument(
        "id",
        type=int,
        help="Task ID"
    )

    # Incomplete command
    parser_incomplete = subparsers.add_parser(
        "incomplete",
        help="Mark a task as incomplete"
    )
    parser_incomplete.add_argument(
        "id",
        type=int,
        help="Task ID"
    )

    # Delete command
    parser_delete = subparsers.add_parser(
        "delete",
        help="Delete a task"
    )
    parser_delete.add_argument(
        "id",
        type=int,
        help="Task ID"
    )

    # Update command
    parser_update = subparsers.add_parser(
        "update",
        help="Update a task's description"
    )
    parser_update.add_argument(
        "id",
        type=int,
        help="Task ID"
    )
    parser_update.add_argument(
        "description",
        type=str,
        help="New task description"
    )

    # Search command
    parser_search = subparsers.add_parser(
        "search",
        help="Search tasks by keyword"
    )
    parser_search.add_argument(
        "keyword",
        type=str,
        help="Search keyword"
    )

    # Parse arguments
    args = parser.parse_args()

    # If no command provided, show help
    if not args.command:
        parser.print_help()
        return 0

    # Dispatch to command handlers
    try:
        if args.command == "add":
            return commands.add_command(args.description)
        elif args.command == "list":
            return commands.list_command()
        elif args.command == "complete":
            return commands.complete_command(args.id)
        elif args.command == "incomplete":
            return commands.incomplete_command(args.id)
        elif args.command == "delete":
            return commands.delete_command(args.id)
        elif args.command == "update":
            return commands.update_command(args.id, args.description)
        elif args.command == "search":
            return commands.search_command(args.keyword)
        else:
            print(f"Error: Unknown command '{args.command}'", file=sys.stderr)
            return 1
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
