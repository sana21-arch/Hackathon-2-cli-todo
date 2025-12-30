# Interactive CLI Task App - User Guide

## Quick Start

Run the interactive task app:

```bash
python interactive_todo.py
```

## What This App Does

This is a **completely redesigned** interactive CLI task tracker that:

1. ✅ Greets you with: "Welcome to the CLI Task App!"
2. ✅ Guides you through entering task details step-by-step
3. ✅ Collects three fields per task:
   - **Task Name**
   - **Description**
   - **Due Date**
4. ✅ Automatically moves to the next field after each entry
5. ✅ Shows "✅ Entry completed!" after each task
6. ✅ Asks "Do you want to add another entry? (yes/no):" after each task
7. ✅ Displays all tasks in a numbered list before exiting
8. ✅ Says "Goodbye! 👋" when you exit
9. ✅ Handles errors gracefully with helpful messages

## Example Session

```
============================================================
               Welcome to the CLI Task App!
============================================================

📌 This app helps you organize your tasks with ease.
   Just follow the prompts and we'll guide you through!

------------------------------------------------------------

✏️  Let's create a new task!

Task Name: Buy groceries
   ✓ Task name recorded

Description: Get milk, eggs, and bread from the store
   ✓ Description recorded

Due Date (e.g., 2025-12-31 or 12/31/2025): 2025-12-31
   ✓ Due date recorded

============================================================
✅ Entry completed!
============================================================

------------------------------------------------------------

Do you want to add another entry? (yes/no): yes

------------------------------------------------------------

✏️  Let's create a new task!

Task Name: Write report
   ✓ Task name recorded

Description: Complete quarterly financial report
   ✓ Description recorded

Due Date (e.g., 2025-12-31 or 12/31/2025): 01/15/2026
   ✓ Due date recorded

============================================================
✅ Entry completed!
============================================================

------------------------------------------------------------

Do you want to add another entry? (yes/no): no

============================================================
📋 YOUR TASKS
============================================================

1. 📋 Buy groceries
   Description: Get milk, eggs, and bread from the store
   Due Date: 2025-12-31

2. 📋 Write report
   Description: Complete quarterly financial report
   Due Date: 2026-01-15

============================================================

============================================================
Goodbye! 👋
============================================================
```

## Features

### User-Friendly Design
- Clear welcome message
- Step-by-step guided input
- Visual confirmations after each field
- Professional formatting with separators

### Smart Date Handling
The app accepts dates in multiple formats:
- `2025-12-31` (YYYY-MM-DD)
- `12/31/2025` (MM/DD/YYYY)
- `31/12/2025` (DD/MM/YYYY)
- `12-31-2025` (MM-DD-YYYY)
- Or any text (for flexibility)

Dates are automatically standardized to YYYY-MM-DD format.

### Error Handling
- Empty fields are not allowed (except due date is optional)
- Ctrl+C gracefully exits and shows what you entered
- Invalid yes/no responses prompt for clarification
- Unexpected errors are caught and explained

### Clean Exit
- Always shows your complete task list before exiting
- Friendly goodbye message
- Shows tasks even if interrupted

## Key Differences from Original

| Original CLI | New Interactive App |
|--------------|-------------------|
| Command-based (add, list, etc.) | Guided conversation flow |
| Separate commands per operation | Single continuous session |
| Task ID required for operations | Automatic numbering |
| Technical command syntax | Natural language prompts |
| No welcome/goodbye | Friendly messages |
| Task only has description | Name + Description + Due Date |

## Usage Tips

1. **Just run the app** - No commands to remember!
2. **Follow the prompts** - The app guides you through everything
3. **Press Enter** - Automatically moves to next field
4. **Type yes/no** - Simple continuation prompt
5. **Press Ctrl+C anytime** - Gracefully exits with your data

## Technical Details

- **Pure Python** - No external dependencies
- **Cross-platform** - Works on Windows, Mac, Linux
- **Python 3.6+** - Uses modern Python features
- **Graceful errors** - Handles all edge cases
- **Input validation** - Prevents empty required fields
- **Date validation** - Flexible date format parsing

## Running the App

### Simple Method:
```bash
python interactive_todo.py
```

### With Python 3 explicitly:
```bash
python3 interactive_todo.py
```

### Make it executable (Unix/Mac):
```bash
chmod +x interactive_todo.py
./interactive_todo.py
```

## Complete Workflow

1. **Start the app**
   ```bash
   python interactive_todo.py
   ```

2. **See welcome message**
   - Friendly greeting
   - Clear instructions

3. **Enter first task**
   - Type task name → Enter
   - Type description → Enter
   - Type due date → Enter
   - See "✅ Entry completed!"

4. **Decide to continue**
   - Type "yes" to add more tasks
   - Type "no" to finish

5. **View all tasks**
   - See numbered list of all entries
   - Each task shows name, description, and due date

6. **Exit gracefully**
   - See "Goodbye! 👋"
   - Your session is complete

## Why This Design?

This interactive design is:
- **Beginner-friendly** - No commands to memorize
- **Conversational** - Feels like a guided interview
- **Forgiving** - Handles mistakes gracefully
- **Visual** - Clear feedback at every step
- **Complete** - Captures all task information
- **Simple** - Works in any Python environment

## Perfect For

- ✅ Hackathon demonstrations
- ✅ Educational projects
- ✅ Quick task capture
- ✅ Learning Python CLI development
- ✅ Non-technical users
- ✅ Prototypes and MVPs

---

**Enjoy your new interactive task app!** 🎉
