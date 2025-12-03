# Task 8 — SPECKitPlus Simple Calculator

## SPECKit Plus (short note)
SPECKit Plus is a structured five-phase workflow that helps developers define, specify, plan, taskize and implement small AI-native features or apps.

---

## /constitution
Simple calculator with basic operations only

## /specify
Calculator: input expr(string) -> output result(number)

## /plan
Plan: take expression -> validate -> evaluate -> return number

## /tasks
1. Receive input  
2. Validate expression  
3. Evaluate safely  
4. Return result

## /implement
Implemented a Python CLI calculator using AST-based safe evaluator.

---

## Implementation files
- `cli.py` — safe evaluator & CLI

## How to run
```bash
python src\cli.py
