# CLI Contracts: Todo Commands

**Feature**: `001-cli-todo`
**Created**: 2025-12-30

## Overview

This directory contains the interface specifications for all CLI commands. Each command defines:
- Input parameters and types
- Output format (stdout)
- Error messages (stderr + exit code 1)
- Examples

## Commands

1. **[add](../plan.md#command-todo-add-description)** - Add a new task
2. **[list](../plan.md#command-todo-list)** - List all tasks
3. **[complete](../plan.md#command-todo-complete-id)** - Mark task as complete
4. **[incomplete](../plan.md#command-todo-incomplete-id)** - Mark task as incomplete
5. **[delete](../plan.md#command-todo-delete-id)** - Delete a task
6. **[update](../plan.md#command-todo-update-id-description)** - Update task description
7. **[search](../plan.md#command-todo-search-keyword)** - Search tasks by keyword

## Common Patterns

### Exit Codes
- `0` - Success
- `1` - Error (invalid input, task not found, etc.)

### Output Streams
- **stdout**: Success messages and data output
- **stderr**: Error messages

### Error Message Format
```
Error: <problem description>. <suggested action>
```

**Examples**:
- `Error: Task ID 5 not found. Use 'todo list' to see valid IDs.`
- `Error: Task description cannot be empty`
- `Error: Task ID must be a number`

### Success Message Format
```
<Action> task #<id>: "<description>"
```

**Examples**:
- `Added task #1: "Buy groceries"`
- `Marked task #2 as complete: "Pay bills"`
- `Updated task #3: "Call dentist tomorrow"`
- `Deleted task #4: "Old task"`

### List Output Format
```
ID | Status | Description
---|--------|------------
1  | [ ]    | Task 1 description
2  | [✓]    | Task 2 description
```

**Status Indicators**:
- `[ ]` - Incomplete
- `[✓]` - Complete

## Validation

### Task ID Validation
- MUST be a valid integer
- MUST be positive (> 0)
- MUST exist in task store

### Description Validation
- MUST NOT be empty string
- MAY contain any printable characters

### Keyword Validation (search)
- MUST NOT be empty string

## Help Text

All commands support `--help` or `-h` flag for usage information.

**Main help** (`todo --help`):
```
usage: todo <command> [<args>]

Available commands:
  add <description>       Add a new task
  list                    List all tasks
  complete <id>           Mark a task as complete
  incomplete <id>         Mark a task as incomplete
  delete <id>             Delete a task
  update <id> <desc>      Update a task's description
  search <keyword>        Search tasks by keyword

Use 'todo <command> --help' for command-specific help
```

## Full Specifications

See [plan.md - Phase 1: CLI Contracts](../plan.md#cli-contracts-contracts) for detailed specifications of each command including:
- Input parameters
- Output formats
- Error conditions
- Examples
- Matching logic (for search)
