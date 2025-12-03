# Function Contracts for Calculator Logic

This document defines the contracts for the core calculator functions that will be implemented in the `calculator/operations.py` module.

## `add(a: float, b: float) -> float`

- **Description**: Adds two numbers.
- **Parameters**:
    - `a` (float): The first number.
    - `b` (float): The second number.
- **Returns**: The sum of `a` and `b`.

## `subtract(a: float, b: float) -> float`

- **Description**: Subtracts the second number from the first.
- **Parameters**:
    - `a` (float): The first number.
    - `b` (float): The second number.
- **Returns**: The result of `a - b`.

## `multiply(a: float, b: float) -> float`

- **Description**: Multiplies two numbers.
- **Parameters**:
    - `a` (float): The first number.
    - `b` (float): The second number.
- **Returns**: The product of `a` and `b`.

## `divide(a: float, b: float) -> float`

- **Description**: Divides the first number by the second.
- **Parameters**:
    - `a` (float): The numerator.
    - `b` (float): The denominator.
- **Returns**: The result of `a / b`.
- **Raises**: `ValueError` if `b` is zero.
