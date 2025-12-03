# Data Model: Simple Calculator Core Logic

## Entities

### Expression
- Represents a mathematical calculation provided as input by the user.
- **Type**: String
- **Attributes**: The string content itself, which will be parsed.

### Result
- Represents the numerical outcome of evaluating an Expression.
- **Type**: Number (specifically, standard double-precision floating-point as per spec clarification).
- **Attributes**: The numerical value.

## Relationships

- An **Expression** is evaluated to produce a single **Result**.
