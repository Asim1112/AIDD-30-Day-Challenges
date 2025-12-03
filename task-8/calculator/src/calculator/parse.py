import re

def parse_number(token):
    try:
        return float(token)
    except ValueError:
        return None

# Define operator precedence
# Higher value means higher precedence
OPERATOR_PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

def parse_expression(expression_string):
    """
    Parses a mathematical expression string into a list of tokens in Reverse Polish Notation (RPN).
    Recognizes numbers (integers or floats) and basic arithmetic operators (+, -, *, /).
    Implements the Shunting-yard algorithm.
    """
    token_patterns = r"(\d+\.\d+|\d+|\+|\-|\*|\/)"
    tokens = re.findall(token_patterns, expression_string.replace(" ", ""))

    output_queue = []
    operator_stack = []

    for token in tokens:
        if parse_number(token) is not None: # It's a number
            output_queue.append(parse_number(token))
        elif token in OPERATOR_PRECEDENCE: # It's an operator
            while (operator_stack and operator_stack[-1] in OPERATOR_PRECEDENCE and
                   OPERATOR_PRECEDENCE[operator_stack[-1]] >= OPERATOR_PRECEDENCE[token]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        else:
            # Handle unexpected tokens
            raise ValueError(f"Invalid token: {token}")

    while operator_stack:
        if operator_stack[-1] not in OPERATOR_PRECEDENCE:
            raise ValueError(f"Mismatched parenthesis or invalid operator: {operator_stack[-1]}")
        output_queue.append(operator_stack.pop())
    
    return output_queue
