def test_us2_evaluate_operator_precedence():
    # These tests are expected to fail until evaluate.py is updated for precedence
    assert evaluate_expression([2.0, '+', 3.0, '*', 4.0]) == 14.0  # 2 + (3 * 4)
    assert evaluate_expression([10.0, '-', 4.0, '/', 2.0]) == 8.0  # 10 - (4 / 2)
    assert evaluate_expression([2.0, '*', 3.0, '+', 4.0, '/', 2.0]) == 8.0 # (2*3) + (4/2)

import pytest
from src.calculator.evaluate import evaluate_single_operation, evaluate_expression

def test_evaluate_single_operation_addition():
    assert evaluate_single_operation(2, '+', 3) == 5.0

def test_evaluate_single_operation_subtraction():
    assert evaluate_single_operation(5, '-', 2) == 3.0

def test_evaluate_single_operation_multiplication():
    assert evaluate_single_operation(2, '*', 4) == 8.0

def test_evaluate_single_operation_division():
    assert evaluate_single_operation(10, '/', 2) == 5.0

def test_evaluate_single_operation_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        evaluate_single_operation(10, '/', 0)

def test_evaluate_single_operation_unknown_operator():
    with pytest.raises(ValueError, match="Unknown operator"):
        evaluate_single_operation(10, '%', 2)

def test_us1_evaluate_basic_operations():
    assert evaluate_expression([2.0, '+', 3.0]) == 5.0
    assert evaluate_expression([5.0, '-', 2.0]) == 3.0
    assert evaluate_expression([2.0, '*', 4.0]) == 8.0
    assert evaluate_expression([10.0, '/', 2.0]) == 5.0

def test_us1_evaluate_multiple_operations_sequential():
    # Assumes left-to-right evaluation without precedence for now
    assert evaluate_expression([10.0, '+', 5.0, '-', 2.0]) == 13.0
    assert evaluate_expression([2.0, '*', 3.0, '+', 4.0]) == 10.0 # (2*3)+4 = 10 without precedence
    
def test_evaluate_expression_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        evaluate_expression([10.0, '/', 0.0])

def test_evaluate_expression_empty_input():
    assert evaluate_expression([]) == 0.0
