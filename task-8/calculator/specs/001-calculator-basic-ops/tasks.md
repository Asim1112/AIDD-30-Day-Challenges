# Tasks: Simple Calculator Core Logic

**Input**: Design documents from `/specs/001-calculator-basic-ops/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification implies a TDD approach by listing acceptance scenarios. Therefore, tests will be included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Paths shown below assume single project structure as defined in `plan.md`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create root project directories: `src/` and `tests/`
- [x] T002 Create `src/calculator/` directory and `src/calculator/__init__.py`
- [x] T003 Create `tests/unit/` and `tests/integration/` directories
- [x] T004 Install `pytest` for testing
- [x] T005 Configure basic `pytest` setup (e.g., `pytest.ini` if needed)
- [x] T006 Create `src/cli.py` for command-line interface

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Implement a basic parsing function for numbers in `src/calculator/parse.py`
- [x] T008 Implement a basic evaluation function that takes numbers and a single operator in `src/calculator/evaluate.py`
- [x] T009 Create initial unit tests for number parsing in `tests/unit/test_parse.py`
- [x] T010 Create initial unit tests for basic evaluation in `tests/unit/test_evaluate.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform Basic Arithmetic Operations (Priority: P1) 🎯 MVP

**Goal**: Enable users to input simple expressions (+, -, *, /) and get the correct result.

**Independent Test**: Provide various valid basic arithmetic expressions (e.g., "2+2", "5*3", "10-4", "20/5") and verify the output matches expected mathematical results.

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T011 [US1] Add unit tests for parsing basic expressions (numbers and single operators) in `tests/unit/test_parse.py`
- [x] T012 [US1] Add unit tests for evaluating basic expressions (numbers and single operators) in `tests/unit/test_evaluate.py`

### Implementation for User Story 1

- [x] T013 [US1] Refine parsing logic to handle numbers and basic operators (+, -, *, /) in `src/calculator/parse.py`
- [x] T014 [US1] Implement basic evaluation logic for expressions without operator precedence in `src/calculator/evaluate.py`
- [x] T015 [US1] Implement CLI logic to accept a basic expression string and display the result in `src/cli.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Handle Operator Precedence (Priority: P2)

**Goal**: Ensure the calculator applies standard mathematical operator precedence.

**Independent Test**: Provide expressions with mixed operators (e.g., "2+3*4", "10-4/2") and verify the output matches the expected result based on standard precedence rules.

### Tests for User Story 2

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T016 [US2] Add unit tests for parsing expressions with operator precedence in `tests/unit/test_parse.py`
- [x] T017 [US2] Add unit tests for evaluating expressions with operator precedence in `tests/unit/test_evaluate.py`
- [x] T018 [US2] Create integration tests for CLI with operator precedence in `tests/integration/test_cli.py`

### Implementation for User Story 2

- [x] T019 [US2] Refine parsing logic to incorporate operator precedence rules in `src/calculator/parse.py`
- [x] T020 [US2] Refine evaluation logic to apply operator precedence correctly in `src/calculator/evaluate.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Error handling, robustness, and final refinements.

- [x] T021 [P] Implement error handling for division by zero in `src/calculator/evaluate.py`
- [x] T022 [P] Implement error handling for invalid/malformed expressions during parsing in `src/calculator/parse.py`
- [x] T023 [P] Ensure CLI gracefully handles errors and displays clear messages in `src/cli.py`
- [x] T024 Add unit tests for error conditions (division by zero, invalid expressions) in `tests/unit/test_evaluate.py` and `tests/unit/test_parse.py`
- [x] T025 Confirm adherence to standard double-precision floating-point behavior for numerical limits and precision.
- [x] T026 Update `quickstart.md` with examples of error handling.
- [x] T027 Run quickstart.md validation to confirm all examples work as expected.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Integrates with US1 logic, but focused on precedence refinement.

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Parsing logic before evaluation logic
- Core implementation before CLI integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel.
- All Foundational tasks marked [P] can run in parallel (within Phase 2).
- Once Foundational phase completes, User Story 1 and User Story 2 can be worked on by different individuals if care is taken to manage merge conflicts in shared files (e.g., `parse.py`, `evaluate.py`).
- Within each story, tasks modifying different files (e.g., tests vs implementation) can be done in parallel if dependencies are respected.
- Polish tasks marked [P] can run in parallel.

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Add unit tests for parsing basic expressions (numbers and single operators) in tests/unit/test_parse.py"
Task: "Add unit tests for evaluating basic expressions (numbers and single operators) in tests/unit/test_evaluate.py"

# Launch implementation for User Story 1 (after tests are written):
Task: "Refine parsing logic to handle numbers and basic operators (+, -, *, /) in src/calculator/parse.py"
Task: "Implement basic evaluation logic for expressions without operator precedence in src/calculator/evaluate.py"
Task: "Implement CLI logic to accept a basic expression string and display the result in src/cli.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Complete Polish & Cross-Cutting Concerns → Final deployment
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (focus on parsing, basic evaluation, CLI for simple cases)
   - Developer B: User Story 2 (focus on parsing precedence, evaluation with precedence)
3. Both developers collaborate on shared files like `parse.py` and `evaluate.py`.
4. Stories complete and integrate independently.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
