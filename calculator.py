# Simple Calculator Program

try:
    # Take two numbers as input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Display the available operations
    print("\nChoose an operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")

    # Take the operation from the user
    operator = input("Enter operator (+, -, *, /): ")

    # Perform the selected operation
    if operator == "+":
        result = num1 + num2
        print("Result:", result)

    elif operator == "-":
        result = num1 - num2
        print("Result:", result)

    elif operator == "*":
        result = num1 * num2
        print("Result:", result)

    elif operator == "/":
        # Check whether the second number is zero
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        # Handle an invalid operator
        print("Error: Invalid operator.")

# Handle invalid number input
except ValueError:
    print("Error: Please enter valid numbers.")