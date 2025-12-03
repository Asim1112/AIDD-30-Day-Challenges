# Tasks: Calculator UI

**Input**: Design documents from `/specs/001-calculator-ui/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---
## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create the project directory structure as defined in `specs/001-calculator-ui/plan.md`.
- [X] T002 Create a `requirements.txt` file with `streamlit` and `pytest`.

---

## Phase 2: User Story 1 - Basic Calculation (Priority: P1) 🎯 MVP

**Goal**: Implement the core calculator logic and a basic UI to perform addition, subtraction, multiplication, and division.

**Independent Test**: The UI can be launched, and a user can enter two numbers, select an operation, and see the correct result.

### Implementation for User Story 1

- [X] T003 [P] [US1] Implement the `add` function in `src/calculator/operations.py`.
- [X] T004 [P] [US1] Implement the `subtract` function in `src/calculator/operations.py`.
- [X] T005 [P] [US1] Implement the `multiply` function in `src/calculator/operations.py`.
- [X] T006 [P] [US1] Implement the `divide` function in `src/calculator/operations.py`.
- [X] T007 [US1] Create `tests/unit/test_operations.py` and write unit tests for the basic arithmetic functions.
- [X] T008 [US1] Create the basic Streamlit UI in `src/app.py` with number inputs, operation selection, and a button.
- [X] T009 [US1] Connect the UI elements in `src/app.py` to the calculator functions and display the result.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 3: User Story 2 - Input Validation (Priority: P2)

**Goal**: Prevent the application from crashing due to non-numeric input.

**Independent Test**: Entering a non-numeric value in either input field and clicking "Calculate" displays a user-friendly error message.

### Implementation for User Story 2

- [X] T010 [US2] In `src/app.py`, add logic to validate that both inputs are numerical before performing calculations.
- [X] T011 [US2] If validation fails in `src/app.py`, display a clear error message to the user using `st.error`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 4: User Story 3 - Division by Zero (Priority: P3)

**Goal**: Handle division by zero gracefully.

**Independent Test**: Attempting to divide a number by zero displays a user-friendly error message.

### Implementation for User Story 3

- [X] T012 [US3] In `src/calculator/operations.py`, modify the `divide` function to raise a `ValueError` if the denominator is zero.
- [X] T013 [US3] In `tests/unit/test_operations.py`, add a test case to verify that `divide` raises a `ValueError` when the denominator is zero.
- [X] T014 [US3] In `src/app.py`, add a try-except block to catch the `ValueError` from the `divide` function and display an error message.

**Checkpoint**: All user stories should now be independently functional

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T015 Review all code for clarity, comments, and adherence to the project constitution.
- [X] T016 Update the main `README.md` file with instructions from `specs/001-calculator-ui/quickstart.md`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately.
- **User Story 1 (Phase 2)**: Depends on Setup completion.
- **User Story 2 (Phase 3)**: Depends on User Story 1 completion.
- **User Story 3 (Phase 4)**: Depends on User Story 1 completion.
- **Polish (Phase 5)**: Depends on all user stories being complete.

### Parallel Opportunities

- Within User Story 1, tasks T003, T004, T005, and T006 can be done in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: User Story 1
3. **STOP and VALIDATE**: Test User Story 1 independently.

### Incremental Delivery

1. Complete Setup + User Story 1 → Test independently (MVP!).
2. Add User Story 2 → Test independently.
3. Add User Story 3 → Test independently.
4. Complete Polish phase.
