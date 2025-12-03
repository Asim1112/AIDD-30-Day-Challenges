# Research for Calculator UI

This document outlines the decisions made during the planning phase for the Calculator UI feature.

## Python Version

- **Decision**: Use Python 3.9.
- **Rationale**: Python 3.9 provides a good balance of modern language features and wide compatibility with libraries, including the latest versions of Streamlit and pytest.
- **Alternatives considered**:
    - **Python 3.10/3.11**: While newer, using a slightly older version like 3.9 can sometimes provide more stability and fewer surprise dependency issues. For this project, the features of 3.10+ are not critical.

## Streamlit Application Structure

- **Decision**: The application will be structured with a main `app.py` file for the UI and a separate `calculator` module for the business logic.
- **Rationale**: This separation of concerns makes the code easier to understand, test, and maintain. The `app.py` handles all the UI-related code, while the `calculator` module contains the pure-python mathematical functions.
- **Alternatives considered**:
    - **Single file app**: Putting all logic into `app.py`. This is simpler for very small scripts but becomes unmanageable as the application grows. Separating the logic is a better practice even for this small project.

## Testing Strategy

- **Decision**: Unit tests will be written using `pytest` to test the functions in the `calculator` module.
- **Rationale**: The core logic of the calculator is the most critical part to test. `pytest` is a simple and powerful tool for this. End-to-end testing of the Streamlit UI is more complex and considered out of scope for this simple project, as the UI is very thin.
- **Alternatives considered**:
    - **Selenium/Playwright**: These tools could be used for end-to-end UI testing. However, they add significant complexity and are overkill for this project's requirements.
