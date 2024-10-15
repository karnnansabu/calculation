# Simple Python program to subtract two numbers

# Function to subtract two numbers
def subtract_numbers(num1, num2):
    return num1 - num2

# Input: asking user to enter two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Subtracting the numbers
result = subtract_numbers(number1, number2)

# Output: displaying the result
print(f"The result of subtracting {number2} from {number1} is: {result}")
