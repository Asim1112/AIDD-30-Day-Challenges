import streamlit as st
from calculator.operations import add, subtract, multiply, divide

st.title("Simple Calculator")

# Input fields for two numbers
number1 = st.number_input("Enter the first number", value=0.0)
number2 = st.number_input("Enter the second number", value=0.0)

# Operation selection
operation = st.selectbox("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Add":
            result = add(number1, number2)
        elif operation == "Subtract":
            result = subtract(number1, number2)
        elif operation == "Multiply":
            result = multiply(number1, number2)
        elif operation == "Divide":
            result = divide(number1, number2)
        
        st.success(f"The result is: {result}")

    except ValueError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
