<!--
Sync Impact Report:
- Version change: 0.0.0 (assumed initial) → 0.1.0
- Modified principles:
    - Simplicity and Readability (New)
    - Correctness and Accuracy (New)
    - Modularity (New)
    - Robustness (New)
- Added sections: Technology Stack, Development Workflow
- Removed sections: None
- Templates requiring updates:
    - .specify/templates/plan-template.md (⚠ pending review)
    - .specify/templates/spec-template.md (⚠ pending review)
    - .specify/templates/tasks-template.md (⚠ pending review)
    - .gemini/commands/sp.adr.toml (⚠ pending review)
    - .gemini/commands/sp.analyze.toml (⚠ pending review)
    - .gemini/commands/sp.checklist.toml (⚠ pending review)
    - .gemini/commands/sp.clarify.toml (⚠ pending review)
    - .gemini/commands/sp.constitution.toml (⚠ pending review)
    - .gemini/commands/sp.git.commit_pr.toml (⚠ pending review)
    - .gemini/commands/sp.implement.toml (⚠ pending review)
    - .gemini/commands/sp.phr.toml (⚠ pending review)
    - .gemini/commands/sp.plan.toml (⚠ pending review)
    - .gemini/commands/sp.specify.toml (⚠ pending review)
    - .gemini/commands/sp.tasks.toml (⚠ pending review)
- Follow-up TODOs: None
-->
# Simple Calculator Constitution

## Core Principles

### I. Simplicity and Readability
Code must be clear, concise, and easy to understand. Prioritize simple algorithms and direct implementations for basic operations. Avoid unnecessary complexity or premature optimization.

### II. Correctness and Accuracy
All calculations must yield accurate results for specified operations. Unit tests must cover all core arithmetic functions to ensure numerical precision and functional correctness.

### III. Modularity
Components should be loosely coupled and highly cohesive. Separate concerns, such as user input, calculation logic, and output display, into distinct modules or functions.

### IV. Robustness
The calculator should gracefully handle invalid inputs (e.g., non-numeric input, division by zero) and provide clear error messages without crashing.

## Technology Stack
This project will use standard programming language features suitable for CLI applications. External dependencies should be minimal and thoroughly vetted.

## Development Workflow
Adhere to a test-driven development (TDD) approach where appropriate. All features and bug fixes must be accompanied by relevant unit tests. Code reviews are encouraged for quality assurance.

## Governance
This constitution defines the core principles guiding the development of the Simple Calculator project. Amendments require consensus from project contributors and will result in a version increment. Compliance with these rules is expected in all contributions.

**Version**: 0.1.0 | **Ratified**: 2025-12-03 | **Last Amended**: 2025-12-03