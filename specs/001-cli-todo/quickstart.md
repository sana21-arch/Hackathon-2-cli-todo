# Quickstart Guide: CLI Todo System

**Feature**: `001-cli-todo`
**Created**: 2025-12-30
**Target Audience**: Hackathon judges and beginner software engineers

## Table of Contents

1. [Installation & Setup](#installation--setup)
2. [Basic Usage](#basic-usage)
3. [Task Management](#task-management)
4. [Finding Tasks](#finding-tasks)
5. [Help & Troubleshooting](#help--troubleshooting)
6. [Complete Examples](#complete-examples)

---

## Installation & Setup

### Prerequisites
- Python 3.13 or higher installed
- Command-line terminal (PowerShell, bash, zsh, etc.)

### Setup Steps

1. **Clone or download the project**:
   ```bash
   cd path/to/project
   ```

2. **No dependencies required!** This project uses Python standard library only.

3. **Run the CLI**:
   ```bash
   python src/cli/main.py --help
   ```

   Or create an alias (recommended):
   ```bash
   # On Unix/Mac (add to ~/.bashrc or ~/.zshrc)
   alias todo='python /full/path/to/src/cli/main.py'

   # On Windows PowerShell (add to $PROFILE)
   function todo { python C:\full\path\to\src\cli\main.py $args }
   ```

4. **Verify installation**:
   ```bash
   todo --help
   ```

   You should see the command list.

---

## Basic Usage

### Adding Your First Task

```bash
$ todo add "Buy groceries"
Added task #1: "Buy groceries"
```

### Viewing All Tasks

```bash
$ todo list
ID | Status | Description
---|--------|------------
1  | [ ]    | Buy groceries
```

### Marking a Task Complete

```bash
$ todo complete 1
Marked task #1 as complete: "Buy groceries"
```

### View Updated List

```bash
$ todo list
ID | Status | Description
---|--------|------------
1  | [✓]    | Buy groceries
```

### Mark Incomplete Again

```bash
$ todo incomplete 1
Marked task #1 as incomplete: "Buy groceries"
```

---

## Task Management

### Updating a Task

Change the description of an existing task:

```bash
$ todo update 1 "Buy organic groceries from Whole Foods"
Updated task #1: "Buy organic groceries from Whole Foods"
```

### Deleting a Task

Remove a task you no longer need:

```bash
$ todo delete 1
Deleted task #1: "Buy organic groceries from Whole Foods"

$ todo list
No tasks yet. Add one with: todo add '<description>'
```

**Note**: Task IDs are never reused. If you delete task #1 and add a new task, it will get ID #2 (or the next available number).

---

## Finding Tasks

### Search by Keyword

Find tasks containing specific text (case-insensitive):

```bash
$ todo add "Buy groceries"
$ todo add "Pay bills"
$ todo add "Buy stamps"

$ todo search "buy"
ID | Status | Description
---|--------|------------
1  | [ ]    | Buy groceries
3  | [ ]    | Buy stamps

$ todo search "bills"
ID | Status | Description
---|--------|------------
2  | [ ]    | Pay bills

$ todo search "vacation"
No tasks found matching "vacation"
```

---

## Help & Troubleshooting

### Get Help

```bash
# Main help - lists all commands
$ todo --help

# Command-specific help
$ todo add --help
$ todo list --help
$ todo complete --help
```

### Common Errors

#### Empty Description
```bash
$ todo add ""
Error: Task description cannot be empty
```

**Solution**: Provide a non-empty description in quotes.

#### Task Not Found
```bash
$ todo complete 999
Error: Task ID 999 not found. Use 'todo list' to see valid IDs.
```

**Solution**: Run `todo list` to see valid task IDs, then use one that exists.

#### Invalid Task ID
```bash
$ todo delete abc
Error: Task ID must be a number
```

**Solution**: Provide a valid integer ID.

### Important Notes

**Session-Based Storage**:
- All tasks are stored in memory only
- Tasks are lost when you exit the program or close your terminal
- This is intentional for Phase 1 (demo purposes)
- Persistence will be added in Phase 2

**Task IDs**:
- IDs are sequential integers starting from 1
- IDs are never reused, even after deletion
- Example: Delete task #2, next task gets #4 (not #2)

**Special Characters**:
- Descriptions support quotes, spaces, and special characters
- Always wrap descriptions in quotes: `todo add "Task description"`

---

## Complete Examples

### Scenario 1: Daily Task Management

```bash
# Morning: Add today's tasks
$ todo add "Check email"
Added task #1: "Check email"

$ todo add "Team meeting at 10am"
Added task #2: "Team meeting at 10am"

$ todo add "Work on project report"
Added task #3: "Work on project report"

$ todo add "Buy lunch"
Added task #4: "Buy lunch"

# View the day's tasks
$ todo list
ID | Status | Description
---|--------|------------
1  | [ ]    | Check email
2  | [ ]    | Team meeting at 10am
3  | [ ]    | Work on project report
4  | [ ]    | Buy lunch

# Complete tasks as you go
$ todo complete 1
Marked task #1 as complete: "Check email"

$ todo complete 2
Marked task #2 as complete: "Team meeting at 10am"

# Check progress
$ todo list
ID | Status | Description
---|--------|------------
1  | [✓]    | Check email
2  | [✓]    | Team meeting at 10am
3  | [ ]    | Work on project report
4  | [ ]    | Buy lunch

# Realize you need to update a task
$ todo update 3 "Finish and submit project report"
Updated task #3: "Finish and submit project report"

# Lunch plans changed
$ todo delete 4
Deleted task #4: "Buy lunch"

# Final list
$ todo list
ID | Status | Description
---|--------|------------
1  | [✓]    | Check email
2  | [✓]    | Team meeting at 10am
3  | [ ]    | Finish and submit project report
```

### Scenario 2: Shopping List

```bash
# Create shopping list
$ todo add "Buy milk"
$ todo add "Buy eggs"
$ todo add "Buy bread"
$ todo add "Buy butter"
$ todo add "Pay utility bill"

# View all
$ todo list
ID | Status | Description
---|--------|------------
1  | [ ]    | Buy milk
2  | [ ]    | Buy eggs
3  | [ ]    | Buy bread
4  | [ ]    | Buy butter
5  | [ ]    | Pay utility bill

# Find all shopping items
$ todo search "buy"
ID | Status | Description
---|--------|------------
1  | [ ]    | Buy milk
2  | [ ]    | Buy eggs
3  | [ ]    | Buy bread
4  | [ ]    | Buy butter

# Mark items as purchased
$ todo complete 1
$ todo complete 2
$ todo complete 3

# Forgot an item
$ todo add "Buy cheese"
Added task #6: "Buy cheese"

# Complete remaining
$ todo complete 4
$ todo complete 5
$ todo complete 6

# All done!
$ todo list
ID | Status | Description
---|--------|------------
1  | [✓]    | Buy milk
2  | [✓]    | Buy eggs
3  | [✓]    | Buy bread
4  | [✓]    | Buy butter
5  | [✓]    | Pay utility bill
6  | [✓]    | Buy cheese
```

### Scenario 3: Project Planning

```bash
# Add project tasks
$ todo add "Research topic"
$ todo add "Create outline"
$ todo add "Write introduction"
$ todo add "Write main sections"
$ todo add "Write conclusion"
$ todo add "Proofread and edit"
$ todo add "Submit assignment"

# Complete first task
$ todo complete 1
$ todo complete 2

# Realize you need to split a big task
$ todo update 4 "Write section 1: Background"
$ todo add "Write section 2: Methods"
$ todo add "Write section 3: Results"

# Check what's writing-related
$ todo search "write"
ID | Status | Description
---|--------|------------
3  | [ ]    | Write introduction
4  | [ ]    | Write section 1: Background
5  | [ ]    | Write conclusion
6  | [ ]    | Proofread and edit
8  | [ ]    | Write section 2: Methods
9  | [ ]    | Write section 3: Results

# Mark sections complete as you finish
$ todo complete 3
$ todo complete 4
$ todo complete 8
$ todo complete 9
$ todo complete 5

# Final steps
$ todo complete 6
$ todo complete 7

# Project complete!
```

---

## Next Steps

- **Experiment**: Try all commands to get comfortable with the interface
- **Provide Feedback**: This is Phase 1 (in-memory demo). Future phases will add:
  - File persistence (tasks survive program exit)
  - Web interface
  - Task priorities and due dates
  - Collaboration features

## Quick Reference Card

| Command | Description | Example |
|---------|-------------|---------|
| `todo add <desc>` | Add new task | `todo add "Buy milk"` |
| `todo list` | Show all tasks | `todo list` |
| `todo complete <id>` | Mark task done | `todo complete 1` |
| `todo incomplete <id>` | Mark task undone | `todo incomplete 1` |
| `todo update <id> <desc>` | Change description | `todo update 1 "New text"` |
| `todo delete <id>` | Remove task | `todo delete 1` |
| `todo search <keyword>` | Find tasks | `todo search "buy"` |
| `todo --help` | Show help | `todo --help` |

---

**Enjoy using the CLI Todo System!** 🎯
