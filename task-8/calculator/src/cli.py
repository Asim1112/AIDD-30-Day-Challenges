import sys
# --- MODIFICATION 1: FIXING THE IMPORT PATH ---
# Changed from 'from src.calculator...' to 'from calculator...'
from calculator.parse import parse_expression
from calculator.evaluate import evaluate_expression

def handle_expression(expression_string):
    """Parses and evaluates a single expression string."""
    if not expression_string:
        return
        
    try:
        # 1. Parse the expression string into RPN tokens
        parsed_expression = parse_expression(expression_string)
        # 2. Evaluate the RPN tokens
        result = evaluate_expression(parsed_expression)
        # 3. Print the result
        print(result)
    except ValueError as e:
        # Handle parsing or evaluation errors gracefully
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Check if a single expression was passed as a command-line argument
    if len(sys.argv) >= 2:
        # Mode A: Single-shot command line execution (original behavior)
        expression_string = sys.argv[1]
        handle_expression(expression_string)
        return # Exit after calculating the single expression

    # --- MODIFICATION 2: IMPLEMENTING THE INTERACTIVE LOOP ---
    # Mode B: Interactive Loop
    print("Welcome to the Interactive Calculator!")
    print("Type 'exit' or 'quit' to close the application.")
    
    while True:
        try:
            # Get input from the user, showing a prompt
            user_input = input("Calc > ").strip()
        except EOFError:
            # Handle Ctrl+D (Unix) or Ctrl+Z (Windows)
            break
        
        # Check for exit commands
        if user_input.lower() in ('quit', 'exit'):
            break

        # Process the input
        handle_expression(user_input)
        
    print("Exiting calculator. Goodbye!")


if __name__ == "__main__":
    main()