# CLI Todo Tracker - Usage Guide

## Quick Start

The CLI Todo Tracker is a simple, in-memory task management system built with Python. Since tasks are stored in memory, they persist only during a single Python session.

## Running the Application

### Method 1: Using the Service Layer (Recommended for Testing)

The best way to test all features is to use the service layer directly in a Python script or interactive session:

```python
from src.services import task_service

# Add tasks
task1 = task_service.add_task("Buy groceries")
task2 = task_service.add_task("Write report")
task3 = task_service.add_task("Call dentist")

# List all tasks
tasks = task_service.list_tasks()
for task in tasks:
    status = "[X]" if task.completed else "[ ]"
    print(f"{task.id} {status} {task.description}")

# Mark task complete
task_service.toggle_complete(1, True)

# Update a task
task_service.update_task(2, "Write monthly report")

# Search for tasks
results = task_service.search_tasks("report")
for task in results:
    print(f"Found: {task.id} - {task.description}")

# Delete a task
task_service.delete_task(3)

# List remaining tasks
tasks = task_service.list_tasks()
print(f"Remaining tasks: {len(tasks)}")
```

### Method 2: Using the CLI

You can also use the command-line interface:

```bash
# Show help
python todo.py --help

# Add a task
python todo.py add "Buy groceries"

# List tasks (Note: will be empty because each command is a separate process)
python todo.py list

# Mark task complete
python todo.py complete 1

# Mark task incomplete
python todo.py incomplete 1

# Update a task
python todo.py update 1 "Buy organic groceries"

# Search for tasks
python todo.py search "groceries"

# Delete a task
python todo.py delete 1
```

**Important Note**: When using the CLI directly (Method 2), each command runs as a separate process, so tasks won't persist between commands. This is a limitation of the in-memory storage model.

## Running the Tests

### Manual Test Suite

Run the comprehensive manual test to verify all functionality:

```bash
python manual_test.py
```

This will test:
- Adding tasks
- Listing tasks
- Marking tasks complete/incomplete
- Updating tasks
- Searching tasks
- Deleting tasks
- Error handling

### Interactive Demo

Run the demo to see examples of all commands:

```bash
python demo.py
```

## Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add <description>` | Add a new task | `todo.py add "Buy milk"` |
| `list` | Show all tasks | `todo.py list` |
| `complete <id>` | Mark task as done | `todo.py complete 1` |
| `incomplete <id>` | Mark task as not done | `todo.py incomplete 1` |
| `update <id> <description>` | Change task description | `todo.py update 1 "Buy organic milk"` |
| `delete <id>` | Remove a task | `todo.py delete 1` |
| `search <keyword>` | Find tasks by keyword | `todo.py search "milk"` |
| `--help` | Show help | `todo.py --help` |

## Features

- ✅ **Add tasks** with descriptions
- ✅ **List all tasks** with status indicators
- ✅ **Mark tasks complete/incomplete** to track progress
- ✅ **Update task descriptions** to keep tasks current
- ✅ **Search tasks** by keyword (case-insensitive)
- ✅ **Delete tasks** when no longer needed
- ✅ **Error handling** with clear, actionable messages
- ✅ **Input validation** for empty descriptions and invalid IDs

## Architecture

```
CLI Layer (commands.py, main.py)
    ↓
Service Layer (task_service.py)
    ↓
Model Layer (task.py)
```

- **Model**: Task dataclass with id, description, completed, created fields
- **Service**: TaskService with CRUD operations and search
- **CLI**: Command handlers and argument parsing

## Project Status

- ✅ **User Story 1**: Add and view tasks (MVP)
- ✅ **User Story 2**: Mark tasks complete/incomplete
- ✅ **User Story 3**: Delete tasks
- ✅ **User Story 4**: Update task descriptions
- ✅ **User Story 5**: Search tasks by keyword

All Phase 1 features are now implemented and tested!

## Next Steps (Phase 2)

Future enhancements could include:
- 📁 File persistence (JSON, SQLite)
- 🌐 Web interface (REST API, frontend)
- 🏷️ Tags and categories
- 📅 Due dates and priorities
- 👥 Multi-user support

## Troubleshooting

**Q: Why don't my tasks persist between commands?**
A: Tasks are stored in memory only. Each CLI command runs as a separate process, so tasks are lost. Use the Python service layer directly (Method 1 above) to maintain state during a session.

**Q: How do I test all features together?**
A: Run `python manual_test.py` to see all features working in a single session.

**Q: Can I use this for real task management?**
A: This is Phase 1 (in-memory only). For real use, you would need Phase 2 with file/database persistence.

## License

This is an educational demonstration project for hackathon presentation.
