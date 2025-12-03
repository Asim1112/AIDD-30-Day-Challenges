# Quickstart: Simple Calculator Core Logic

This document provides a brief overview of how to run and interact with the Simple Calculator CLI application once implemented.

## Running the Application

Assuming Python 3.9+ is installed and the project dependencies (if any) are met, the application can be run from the command line.

### Basic Usage

To calculate an expression, you will typically run the `cli.py` script and provide the expression as an argument (exact command line arguments to be defined during implementation).

```bash
python -m src.cli "2 + 2"
# Expected output: 4
```

### Examples

*   **Addition**:
    ```bash
    python src/cli.py "10 + 5"
    # Expected output: 15
    ```

*   **Subtraction**:
    ```bash
    python src/cli.py "10 - 5"
    # Expected output: 5
    ```

*   **Multiplication**:
    ```bash
    python src/cli.py "10 * 5"
    # Expected output: 50
    ```

*   **Division**:
    ```bash
    python src/cli.py "10 / 5"
    # Expected output: 2
    ```

*   **Operator Precedence**:
    ```bash
    python src/cli.py "2 + 3 * 4"
    # Expected output: 14
    ```

*   **Invalid Expression Handling**:
    ```bash
    python src/cli.py "2 + * 3"
    # Expected output: Error: Invalid expression
    ```

*   **Division by Zero Handling**:
    ```bash
    python src/cli.py "5 / 0"
    # Expected output: Error: Division by zero
    ```

## API Contracts

This is a CLI application, so there are no external API contracts to define in the traditional sense (e.g., REST or GraphQL endpoints). The interaction is purely via command-line arguments and standard output/error streams.
