# Simple Calculator Program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot Divide by Zero"
    return a / b

print("Calculation")

# Getting Input from User
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to Numbers
num1 = float(num1)
num2 = float(num2)

op = input("Enter operation (+, -, *, /): ")

# Doing Calculation
if op == "+":
    result = add(num1, num2)
    print("Answer:", result)

elif op == "-":
    result = subtract(num1, num2)
    print("Answer:", result)

elif op == "*":
    result = multiply(num1, num2)
    print("Answer:", result)

elif op == "/":
    result = divide(num1, num2)
    print("Answer:", result)

else:
    print("Invalid Operation")
  
