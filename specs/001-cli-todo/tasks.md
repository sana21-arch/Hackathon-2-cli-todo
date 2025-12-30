# Tasks: CLI In-Memory Todo System

**Input**: Design documents from `/specs/001-cli-todo/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md

**Tests**: Manual CLI validation is the primary testing approach for Phase 1

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create src/ directory with subdirectories: models/, services/, cli/
- [x] T002 Create tests/ directory (optional for Phase 1)
- [x] T003 [P] Create empty __init__.py in src/cli/
- [x] T004 [P] Create README.md with project description, setup, and usage placeholder
- [x] T005 [P] Create requirements.txt (empty, stdlib only)
- [x] T006 [P] Create pyproject.toml with Python 3.13+ requirement

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Create Task dataclass in src/models/task.py with fields: id (int), description (str), completed (bool), created (datetime)
- [x] T008 Create TaskService class in src/services/task_service.py with module-level _task_store list and _next_id counter
- [x] T009 Create custom exceptions in src/services/task_service.py: TaskNotFoundError, ValidationError
- [x] T010 Create CLI argument parser skeleton in src/cli/main.py with argparse setup and subparsers for commands
- [x] T011 Create command implementations module src/cli/commands.py with function stubs for all 7 commands

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks and view them in a formatted list

**Independent Test**: Run `todo add "Buy groceries"` followed by `todo list` and verify task appears with ID 1

### Implementation for User Story 1

- [x] T012 [P] [US1] Implement add_task(description: str) -> Task method in src/services/task_service.py with validation and ID generation
- [x] T013 [P] [US1] Implement list_tasks() -> list[Task] method in src/services/task_service.py
- [x] T014 [US1] Implement add command handler in src/cli/commands.py that calls task_service.add_task() and formats output
- [x] T015 [US1] Implement list command handler in src/cli/commands.py that calls task_service.list_tasks() and formats table output
- [x] T016 [US1] Wire add and list commands to CLI parser in src/cli/main.py with proper argument handling
- [x] T017 [US1] Add input validation for empty descriptions in src/cli/commands.py add handler
- [x] T018 [US1] Add error handling and stderr output for validation errors in src/cli/commands.py
- [x] T019 [US1] Add exit code handling (0 for success, 1 for errors) in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently (MVP complete!)

---

## Phase 4: User Story 2 - Mark Tasks Complete (Priority: P2)

**Goal**: Enable users to toggle task completion status

**Independent Test**: Add task, run `todo complete <id>`, verify status changes in `todo list`

### Implementation for User Story 2

- [ ] T020 [P] [US2] Implement get_task(task_id: int) -> Task | None method in src/services/task_service.py with ID lookup
- [ ] T021 [P] [US2] Implement toggle_complete(task_id: int, completed: bool) -> Task method in src/services/task_service.py
- [ ] T022 [US2] Implement complete command handler in src/cli/commands.py that calls toggle_complete(id, True)
- [ ] T023 [US2] Implement incomplete command handler in src/cli/commands.py that calls toggle_complete(id, False)
- [ ] T024 [US2] Wire complete and incomplete commands to CLI parser in src/cli/main.py
- [ ] T025 [US2] Add ID validation (integer, exists) in src/cli/commands.py for complete/incomplete handlers
- [ ] T026 [US2] Update list command in src/cli/commands.py to display status indicators: [ ] for incomplete, [✓] for complete
- [ ] T027 [US2] Add error handling for TaskNotFoundError in src/cli/commands.py complete/incomplete handlers

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Delete Unwanted Tasks (Priority: P3)

**Goal**: Enable users to remove tasks from the list

**Independent Test**: Add tasks, run `todo delete <id>`, verify task removed from `todo list`

### Implementation for User Story 3

- [ ] T028 [US3] Implement delete_task(task_id: int) -> Task method in src/services/task_service.py that removes task from _task_store
- [ ] T029 [US3] Implement delete command handler in src/cli/commands.py that calls task_service.delete_task()
- [ ] T030 [US3] Wire delete command to CLI parser in src/cli/main.py
- [ ] T031 [US3] Add ID validation for delete handler in src/cli/commands.py
- [ ] T032 [US3] Add error handling for TaskNotFoundError in src/cli/commands.py delete handler
- [ ] T033 [US3] Verify ID permanence: test that deleted IDs are never reused (manual validation)

**Checkpoint**: User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Descriptions (Priority: P4)

**Goal**: Enable users to modify task descriptions

**Independent Test**: Add task, run `todo update <id> "New description"`, verify change in `todo list`

### Implementation for User Story 4

- [ ] T034 [US4] Implement update_task(task_id: int, description: str) -> Task method in src/services/task_service.py
- [ ] T035 [US4] Implement update command handler in src/cli/commands.py that calls task_service.update_task()
- [ ] T036 [US4] Wire update command to CLI parser in src/cli/main.py with two arguments (id and description)
- [ ] T037 [US4] Add validation for empty descriptions in update handler in src/cli/commands.py
- [ ] T038 [US4] Add ID validation and error handling for update handler in src/cli/commands.py

**Checkpoint**: User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Search Tasks by Keyword (Priority: P5)

**Goal**: Enable users to find tasks by keyword

**Independent Test**: Add multiple tasks, run `todo search "keyword"`, verify only matching tasks appear

### Implementation for User Story 5

- [ ] T039 [US5] Implement search_tasks(keyword: str) -> list[Task] method in src/services/task_service.py with case-insensitive substring matching
- [ ] T040 [US5] Implement search command handler in src/cli/commands.py that calls task_service.search_tasks() and formats results
- [ ] T041 [US5] Wire search command to CLI parser in src/cli/main.py
- [ ] T042 [US5] Add validation for empty search keywords in src/cli/commands.py search handler
- [ ] T043 [US5] Add "no matches found" message when search returns empty results in src/cli/commands.py

**Checkpoint**: All user stories (1-5) should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T044 [P] Add --help text for main command in src/cli/main.py describing all available commands
- [ ] T045 [P] Add --help text for each subcommand (add, list, complete, incomplete, delete, update, search) in src/cli/main.py
- [ ] T046 [P] Add docstrings to all public functions in src/models/task.py
- [ ] T047 [P] Add docstrings to all public methods in src/services/task_service.py
- [ ] T048 [P] Add docstrings to all command handlers in src/cli/commands.py
- [ ] T049 Update README.md with complete setup instructions (< 5 commands), usage examples, and command reference
- [ ] T050 [P] Add empty list message "No tasks yet. Add one with: todo add '<description>'" to list command in src/cli/commands.py
- [ ] T051 [P] Verify all error messages are actionable (state problem + solution) across all commands in src/cli/commands.py
- [ ] T052 Manual validation: Test with 1,000+ tasks to verify performance meets <1s for list (success criteria SC-005)
- [ ] T053 Manual validation: Test all edge cases from spec.md (invalid IDs, empty inputs, special characters, very long descriptions)
- [ ] T054 Manual validation: Verify exit codes are correct (0 for success, 1 for errors) for all commands
- [ ] T055 Manual validation: Run through quickstart.md examples and verify all scenarios work as documented

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Uses get_task() but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Uses get_task() but independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tasks within a story must follow the order shown (service methods before CLI handlers)
- Tasks marked [P] within the same phase can run in parallel
- Validation and error handling tasks depend on core implementation completing first

### Parallel Opportunities

- **Setup (Phase 1)**: Tasks T003-T006 can all run in parallel
- **Foundational (Phase 2)**: Tasks T007-T009 can run in parallel (different files)
- **User Story 1**: Tasks T012-T013 can run in parallel (both in task_service.py, different methods)
- **User Story 2**: Tasks T020-T021 can run in parallel
- **Polish (Phase 8)**: Tasks T044-T045, T046-T048, T050-T051 can run in parallel

- **Cross-Story Parallelism**: Once Foundational phase completes, User Stories 1-5 can ALL start simultaneously if team capacity allows

---

## Parallel Example: User Story 1

```bash
# After Foundational phase complete, launch User Story 1 tasks:

# Parallel: Implement service methods
Task T012: "Implement add_task() in src/services/task_service.py"
Task T013: "Implement list_tasks() in src/services/task_service.py"

# Sequential: Wire CLI (depends on service methods)
Task T014: "Implement add command handler in src/cli/commands.py"
Task T015: "Implement list command handler in src/cli/commands.py"
Task T016: "Wire commands to parser in src/cli/main.py"

# Parallel: Add validation and error handling
Task T017: "Add validation for empty descriptions"
Task T018: "Add error handling and stderr output"
Task T019: "Add exit code handling"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T006)
2. Complete Phase 2: Foundational (T007-T011) - CRITICAL blocker
3. Complete Phase 3: User Story 1 (T012-T019)
4. **STOP and VALIDATE**: Test User Story 1 independently
   - `todo add "Test"` → verifies task added
   - `todo list` → verifies task displayed
   - `todo add ""` → verifies error handling
5. Deploy/demo MVP if ready

### Incremental Delivery

1. **Foundation** (Phases 1-2) → Setup complete, ready for features
2. **Add User Story 1** (Phase 3) → Test independently → Deploy/Demo **(MVP!)**
3. **Add User Story 2** (Phase 4) → Test independently → Deploy/Demo
4. **Add User Story 3** (Phase 5) → Test independently → Deploy/Demo
5. **Add User Story 4** (Phase 6) → Test independently → Deploy/Demo
6. **Add User Story 5** (Phase 7) → Test independently → Deploy/Demo
7. **Polish** (Phase 8) → Final validation → Production ready

Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1. **Team completes Setup + Foundational together** (Phases 1-2)
2. **Once Foundational is done**:
   - Developer A: User Story 1 (Phase 3) - MVP priority
   - Developer B: User Story 2 (Phase 4) - Core functionality
   - Developer C: User Story 3 (Phase 5) - Supporting feature
3. Stories complete and integrate independently
4. Remaining stories (4-5) can be assigned as capacity allows
5. Polish phase done collaboratively after all stories complete

---

## Validation Checklist

Before marking each phase complete, verify:

### User Story 1 (MVP)
- ✅ Can add task with description
- ✅ Can list all tasks with ID, status, description
- ✅ Empty description rejected with clear error
- ✅ Exit codes correct (0 success, 1 error)
- ✅ Task IDs start at 1 and increment sequentially

### User Story 2
- ✅ Can mark task complete (status changes to [✓])
- ✅ Can mark task incomplete (status changes to [ ])
- ✅ Invalid task ID shows actionable error
- ✅ Non-integer ID rejected with clear error

### User Story 3
- ✅ Can delete task (removed from list)
- ✅ Deleted task ID never reused
- ✅ Invalid task ID shows actionable error

### User Story 4
- ✅ Can update task description
- ✅ Empty description rejected with clear error
- ✅ Invalid task ID shows actionable error

### User Story 5
- ✅ Search finds matching tasks (case-insensitive)
- ✅ Search shows "no matches" when appropriate
- ✅ Empty keyword rejected with clear error

### Polish & Performance
- ✅ Help text complete and accurate for all commands
- ✅ All error messages actionable (problem + solution)
- ✅ Empty list shows helpful message
- ✅ Handles 1,000+ tasks in <1s for list
- ✅ All commands respond in <100ms
- ✅ Special characters handled correctly
- ✅ README matches actual behavior

---

## Notes

- [P] tasks = different files, no dependencies within same phase
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- **No tests are generated** - manual CLI validation is the primary approach per plan.md
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Task Count Summary

- **Total Tasks**: 55
- **Setup**: 6 tasks (T001-T006)
- **Foundational**: 5 tasks (T007-T011)
- **User Story 1 (MVP)**: 8 tasks (T012-T019)
- **User Story 2**: 8 tasks (T020-T027)
- **User Story 3**: 6 tasks (T028-T033)
- **User Story 4**: 5 tasks (T034-T038)
- **User Story 5**: 5 tasks (T039-T043)
- **Polish**: 12 tasks (T044-T055)

**Parallel Opportunities**: 15+ tasks marked [P] can run simultaneously if team capacity allows

**MVP Scope**: Phases 1-3 (Tasks T001-T019) = 19 tasks to minimal viable product

**Full Feature Set**: All 55 tasks for complete Phase 1 implementation
