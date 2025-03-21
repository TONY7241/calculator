def calculator():
    # Ask the user to input two numbers and an operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation based on user input
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation."

    # Print the result
    return f"{num1} {operation} {num2} = {result}"

# Run the calculator function
print(calculator())