# CLI Todo Tracker - Quick Start Guide

## 🚀 Fast Start

### Run the Interactive Demo (Recommended)
```bash
python todo.py demo
```

This runs a complete demonstration of all features in a single session!

### Run the Test Suite
```bash
python manual_test.py
```

This validates that all functionality is working correctly.

---

## 📋 Usage Options

### Option 1: Interactive Demo Mode (Best for showing features)
```bash
python todo.py demo
```

**What it does:**
- Demonstrates all 7 commands (add, list, complete, incomplete, update, delete, search)
- Runs in a single session so you can see tasks persist
- Shows error handling
- Perfect for presentations and demos

---

### Option 2: CLI Commands (Individual commands)

```bash
# Show help
python todo.py --help

# Add a task
python todo.py add "Buy groceries"

# List all tasks
python todo.py list

# Mark task complete
python todo.py complete 1

# Mark task incomplete
python todo.py incomplete 1

# Update task description
python todo.py update 1 "Buy organic groceries"

# Search for tasks
python todo.py search "groceries"

# Delete a task
python todo.py delete 1
```

**Note:** Each CLI command runs as a separate process, so tasks won't persist between commands (in-memory limitation).

---

### Option 3: Python Script (Best for development/testing)

Create a Python script:

```python
from src.services import task_service

# Add tasks
task1 = task_service.add_task("Buy groceries")
task2 = task_service.add_task("Write report")
task3 = task_service.add_task("Call dentist")

# List tasks
tasks = task_service.list_tasks()
for task in tasks:
    status = "[X]" if task.completed else "[ ]"
    print(f"{task.id} {status} {task.description}")

# Mark complete
task_service.toggle_complete(1, True)

# Update
task_service.update_task(2, "Write monthly report")

# Search
results = task_service.search_tasks("report")

# Delete
task_service.delete_task(3)
```

---

## 🎯 Feature Checklist

- ✅ **Add tasks** - Create new tasks with descriptions
- ✅ **List tasks** - View all tasks with status indicators `[ ]` or `[X]`
- ✅ **Complete tasks** - Mark tasks as done
- ✅ **Incomplete tasks** - Unmark completed tasks
- ✅ **Update tasks** - Modify task descriptions
- ✅ **Search tasks** - Find tasks by keyword (case-insensitive)
- ✅ **Delete tasks** - Remove tasks (IDs never reused)
- ✅ **Error handling** - Clear, actionable error messages
- ✅ **Input validation** - Empty descriptions and invalid IDs rejected

---

## 📊 Project Status

**Phase 1: Complete ✅**

All 5 user stories implemented:
1. ✅ Add and view tasks (MVP)
2. ✅ Mark tasks complete/incomplete
3. ✅ Delete tasks
4. ✅ Update task descriptions
5. ✅ Search tasks by keyword

---

## 🔧 Requirements

- Python 3.13+ (uses modern type hints and features)
- No external dependencies (stdlib only)

---

## 📖 Additional Resources

- **README.md** - Full project overview
- **USAGE.md** - Detailed usage guide with examples
- **specs/001-cli-todo/** - Complete specifications and architecture
- **manual_test.py** - Automated test suite
- **demo.py** - Alternative demo script

---

## 💡 Tips

1. **For demos**: Use `python todo.py demo` - it shows everything in one go
2. **For testing**: Use `python manual_test.py` - validates all features
3. **For development**: Import the service layer directly in Python scripts
4. **For CLI usage**: Remember each command is a separate process (in-memory limitation)

---

## 🎓 Architecture

```
┌─────────────────────────────────────┐
│  CLI Layer (commands.py, main.py)  │
└─────────────┬───────────────────────┘
              │
┌─────────────▼───────────────────────┐
│  Service Layer (task_service.py)   │
│  - CRUD operations                  │
│  - Search functionality             │
│  - Validation & error handling      │
└─────────────┬───────────────────────┘
              │
┌─────────────▼───────────────────────┐
│  Model Layer (task.py)              │
│  - Task dataclass                   │
│  - id, description, completed, date │
└─────────────────────────────────────┘
```

---

## 🚦 What's Next?

**Phase 2 (Future):**
- File persistence (JSON/SQLite)
- Web interface (REST API)
- Advanced features (tags, priorities, due dates)
- Multi-user support

---

**Happy task tracking! 🎉**
