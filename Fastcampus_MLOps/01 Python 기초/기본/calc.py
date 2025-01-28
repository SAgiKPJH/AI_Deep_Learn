def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def mod(a, b):
    return a % b

def pow(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Error: Cannot take the square root of a negative number"
    return a ** 0.5

def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == "__main__":
    print("Welcome to the Calculator!")
    while True:
        operation = input("\nEnter an operation (+, -, *, /, %, **, sqrt, factorial): ")
        if operation not in ['+', '-', '*', '/', '%', '**', 'sqrt', 'factorial']:
            print("Error: Invalid operation. Please try again.")
            continue
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == '+':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = sub(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = mul(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            result = div(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif operation == '%':
            result = mod(num1, num2)
            print(f"{num1} % {num2} = {result}")
        elif operation == '**':
            result = pow(num1, num2)
            print(f"{num1} ** {num2} = {result}")
        elif operation == 'sqrt':
            result = sqrt(num1)
            print(f"The square root of {num1} is {result}")
        elif operation == 'factorial':
            result = factorial(num1)
            print(f"The factorial of {num1} is {result}")