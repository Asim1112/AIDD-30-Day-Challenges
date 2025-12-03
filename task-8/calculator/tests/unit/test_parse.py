import pytest

from src.calculator.parse import parse_number, parse_expression

def test_us2_parse_expressions_without_spaces_and_mixed_operators():
    assert parse_expression("2+3*4") == [2.0, '+', 3.0, '*', 4.0]
    assert parse_expression("10-4/2") == [10.0, '-', 4.0, '/', 2.0]
    assert parse_expression("1+2-3*4/5") == [1.0, '+', 2.0, '-', 3.0, '*', 4.0, '/', 5.0]

def test_parse_number():
    assert parse_number("123") == 123.0
    assert parse_number("123.45") == 123.45
    assert parse_number("-10") == -10.0
    assert parse_number("0") == 0.0
    assert parse_number("abc") is None
    assert parse_number("") is None

def test_us1_parse_basic_expressions():
    assert parse_expression("1 2 3") == [1.0, 2.0, 3.0]
    assert parse_expression("1.0 + 2.0") == [1.0, '+', 2.0]
    assert parse_expression("10 - 5") == [10.0, '-', 5.0]
    assert parse_expression("2 * 3") == [2.0, '*', 3.0]
    assert parse_expression("20 / 4") == [20.0, '/', 4.0]
    assert parse_expression("  10   +   5  ") == [10.0, '+', 5.0]

def test_parse_expression_invalid_token():
    with pytest.raises(ValueError, match="Invalid token: a"):
        parse_expression("1+a*2")
