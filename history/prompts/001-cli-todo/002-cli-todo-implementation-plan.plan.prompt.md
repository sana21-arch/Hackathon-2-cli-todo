---
id: 002
title: CLI Todo Implementation Plan
stage: plan
date: 2025-12-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-cli-todo
branch: 001-cli-todo
user: Sana Mushtaque
command: /sp.plan
labels: ["plan", "architecture", "design", "cli", "todo"]
links:
  spec: specs/001-cli-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-cli-todo/plan.md
  - specs/001-cli-todo/data-model.md
  - specs/001-cli-todo/quickstart.md
  - specs/001-cli-todo/contracts/README.md
  - CLAUDE.md
tests:
  - (none - planning artifact)
---

## Prompt

```text
Create:
- High-level architecture sketch (components + responsibilities)
- CLI flow structure
- In-memory data handling approach
- Error handling and UX consistency rules

Decisions Needing Documentation:
- Task data model fields (required vs optional)
- Task ID generation strategy
- Separation between CLI and business logic
- Scope of optional enhancements (priority, timestamp)
- Error handling vs strict input rejection

Testing Strategy:
- Manual CLI validation against success criteria
- Add/View/Update/Delete/Toggle workflows tested
- Invalid input and invalid ID handling checks
- State consistency after each operation

Development Approach:
- Spec-driven, task-by-task implementation
- One feature implemented and validated at a time
- No premature optimization or abstraction

Phases:
- Design → Specification Alignment → Implementation → Validation
```

## Response snapshot

Created comprehensive implementation plan for CLI In-Memory Todo System with complete architecture design, research decisions, data model, CLI contracts, and testing strategy.

**Key Deliverables**:

1. **Architecture Design** (3-layer):
   - **CLI Layer**: argparse parser, command dispatcher, stdout/stderr formatting, exit codes
   - **Service Layer**: TaskService with CRUD operations, validation, ID generation, in-memory store
   - **Model Layer**: Task dataclass (id, description, completed, created)

2. **Research & Design Decisions** (7 key decisions):
   - CLI Framework: argparse (stdlib, zero dependencies) over typer
   - Task IDs: Auto-increment from 1 (never reused, permanent)
   - Storage: Python list (preserves order, supports deletion without gaps)
   - Task Model: Dataclass with type hints (constitution requirement)
   - Error Handling: Exceptions in service + formatting in CLI (Pythonic)
   - Optional Fields: Include `created` timestamp, defer priority (spec-driven)
   - Validation: Strict rejection with actionable errors (better UX)

3. **Data Model** (Entity: Task):
   - `id` (int): Sequential from 1, auto-assigned, unique, permanent
   - `description` (str): Non-empty, any printable chars
   - `completed` (bool): Defaults False
   - `created` (datetime): Auto-assigned, UTC
   - Validation rules: Non-empty description (FR-009), valid ID before ops (FR-010)

4. **CLI Contracts** (7 commands):
   - `add <desc>` → "Added task #<id>: ..."
   - `list` → Formatted table with ID | Status | Description
   - `complete/incomplete <id>` → "Marked task #<id> as ..."
   - `delete <id>` → "Deleted task #<id>: ..."
   - `update <id> <desc>` → "Updated task #<id>: ..."
   - `search <keyword>` → Filtered list (case-insensitive substring match)
   - `--help` → Full command reference

5. **Testing Strategy**:
   - **Primary**: Manual CLI validation against 8 success criteria (SC-001 to SC-008)
   - **Workflows**: Basic CRUD, multiple tasks, search, invalid inputs
   - **State Consistency**: ID uniqueness, no reuse, creation order, status updates
   - **Optional**: pytest unit tests for TaskService methods

6. **Development Phases** (aligned with user stories P1-P5):
   - Phase 1: Foundation (P1 - Add/View) - Task model + TaskService + CLI basics
   - Phase 2: Completion (P2 - Complete/Incomplete) - Toggle operations
   - Phase 3: Removal (P3 - Delete) - Delete with ID preservation
   - Phase 4: Updates (P4 - Update) - Description changes
   - Phase 5: Search (P5 - Search) - Keyword filtering
   - Phase 6: Polish - Help text, error validation, README, quickstart

7. **Constitution Gates**: ✅ ALL PASSED
   - Accuracy: All features map to spec requirements (FR-001 to FR-017)
   - Clarity: Natural language commands, self-documenting code, actionable errors
   - Simplicity: No design patterns, direct implementations, YAGNI enforced
   - Reproducibility: Zero dependencies (stdlib only), Python 3.13+
   - Python Standards: Type hints, dataclasses, PEP 8, clear separation
   - CLI Behavior: Exit codes 0/1, stdout/stderr, help text, validation

**Technical Highlights**:
- **Zero dependencies**: argparse, dataclasses, sys, datetime (all stdlib)
- **In-memory store**: Module-level list + next_id counter
- **Performance**: O(1) add, O(n) lookup/search (acceptable for 1,000+ tasks)
- **Cross-platform**: Windows, macOS, Linux compatible
- **Clean architecture**: CLI → Service → Model (clear separation of concerns)

## Outcome

- ✅ Impact: Complete implementation plan ready for task breakdown and coding
- 🧪 Tests: Planning artifact - manual CLI testing strategy defined for validation
- 📁 Files: Created plan.md (933 lines), data-model.md, quickstart.md, contracts/README.md
- 🔁 Next prompts: `/sp.tasks` to generate actionable task breakdown aligned with user stories P1-P5
- 🧠 Reflection: Architecture balances simplicity (stdlib only, direct implementations) with professionalism (type hints, error handling, clean structure). All constitution gates passed. Design ready for incremental implementation starting with P1 MVP (add/view).

## Evaluation notes (flywheel)

- Failure modes observed: None - planning completed successfully with zero constitution violations
- Graders run and results (PASS/FAIL): Constitution Check PASS (all 6 principles + all technical constraints), Post-Design Check PASS (no violations introduced)
- Prompt variant (if applicable): Standard /sp.plan with user-requested focus areas (architecture, data model, testing, development approach)
- Next experiment (smallest change to try): Test /sp.tasks workflow to validate that task breakdown aligns with user story priorities (P1-P5) and generates testable, atomic tasks
