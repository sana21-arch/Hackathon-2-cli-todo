# CLI In-Memory Todo System

A clean, professional CLI-based todo application demonstrating spec-driven development with Python 3.13+.

## Overview

This is Phase 1 of "The Evolution of Todo" - a demonstration project showcasing software development best practices with a focus on clarity, simplicity, and professional quality. The system provides essential task management operations through an intuitive command-line interface.

**Target Audience**: Hackathon judges and beginner software engineers

## Features

- ✅ Add tasks with descriptions
- ✅ List all tasks with status indicators
- ✅ Mark tasks as complete/incomplete
- ✅ Delete unwanted tasks
- ✅ Update task descriptions
- ✅ Search tasks by keyword (case-insensitive)

## Requirements

- Python 3.13 or higher
- No external dependencies (uses stdlib only)

## Installation & Setup

1. **Clone or download the project**:
   ```bash
   cd path/to/Hackathon\ 2
   ```

2. **Verify Python version**:
   ```bash
   python --version  # Should be 3.13+
   ```

3. **Run the Todo CLI**:
   ```bash
   python src/cli/main.py --help
   ```

4. **(Optional) Create an alias for convenience**:

   **On Unix/Mac** (add to `~/.bashrc` or `~/.zshrc`):
   ```bash
   alias todo='python /full/path/to/src/cli/main.py'
   ```

   **On Windows PowerShell** (add to `$PROFILE`):
   ```powershell
   function todo { python "C:\full\path\to\src\cli\main.py" $args }
   ```

## Quick Start

### Add your first task
```bash
python src/cli/main.py add "Buy groceries"
# Output: Added task #1: "Buy groceries"
```

### View all tasks
```bash
python src/cli/main.py list
# Output:
# ID | Status | Description
# ---|--------|------------
# 1  | [ ]    | Buy groceries
```

### Mark a task complete
```bash
python src/cli/main.py complete 1
# Output: Marked task #1 as complete: "Buy groceries"
```

### Search for tasks
```bash
python src/cli/main.py search "groceries"
# Output: (filtered list of matching tasks)
```

## Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add <description>` | Add a new task | `python src/cli/main.py add "Buy milk"` |
| `list` | Show all tasks | `python src/cli/main.py list` |
| `complete <id>` | Mark task as done | `python src/cli/main.py complete 1` |
| `incomplete <id>` | Mark task as undone | `python src/cli/main.py incomplete 1` |
| `update <id> <description>` | Change description | `python src/cli/main.py update 1 "New text"` |
| `delete <id>` | Remove a task | `python src/cli/main.py delete 1` |
| `search <keyword>` | Find tasks | `python src/cli/main.py search "buy"` |
| `--help` | Show help | `python src/cli/main.py --help` |

## Important Notes

**Session-Based Storage**:
- All tasks are stored in memory only
- Tasks are lost when the program exits
- This is intentional for Phase 1 (demonstration purposes)
- Persistence will be added in Phase 2

**Task IDs**:
- IDs are sequential integers starting from 1
- IDs are never reused, even after deletion
- Example: Delete task #2, next task gets #4 (not #2)

## Architecture

This project follows a clean three-layer architecture:

```
CLI Layer (argparse, commands)
    ↓
Service Layer (TaskService with CRUD + search)
    ↓
Model Layer (Task dataclass)
```

**Key Design Decisions**:
- Zero external dependencies (stdlib only)
- Dataclass for Task model
- In-memory list storage
- Auto-incrementing IDs starting from 1
- Strict input validation with actionable error messages

## Development

See [quickstart.md](specs/001-cli-todo/quickstart.md) for detailed usage examples and workflows.

See [plan.md](specs/001-cli-todo/plan.md) for comprehensive architecture documentation.

## Project Status

- ✅ Phase 1: CLI In-Memory Todo (Current)
- 🔜 Phase 2: File/Database Persistence
- 🔜 Phase 3: Web Interface
- 🔜 Phase 4: Advanced Features (tags, priorities, due dates)

## License

This is an educational demonstration project for hackathon presentation.

## Contributing

This is Phase 1 of a learning-focused project. Future phases will expand functionality while maintaining the core principles of clarity and simplicity.

---

**Enjoy using the CLI Todo System!** 🎯
