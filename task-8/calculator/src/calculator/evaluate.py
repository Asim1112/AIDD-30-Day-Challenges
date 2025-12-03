def evaluate_single_operation(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero")
        return num1 / num2
    else:
        raise ValueError(f"Unknown operator: {operator}")

def evaluate_expression(rpn_tokens):
    """
    Evaluates an expression given in Reverse Polish Notation (RPN).
    """
    if not rpn_tokens:
        return 0.0

    stack = []
    for token in rpn_tokens:
        if isinstance(token, (float, int)):
            stack.append(token)
        else: # It's an operator
            if len(stack) < 2:
                raise ValueError("Invalid RPN expression: not enough operands for operator")
            num2 = stack.pop()
            num1 = stack.pop()
            result = evaluate_single_operation(num1, token, num2)
            stack.append(result)
    
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression: too many operands")
    
    return stack[0]