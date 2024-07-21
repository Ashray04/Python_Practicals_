def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
  print(f"{num1} + {num2} = {add(num1, num2)}")
  print(f"{num1} - {num2} = {subtract(num1, num2)}")
  print(f"{num1} * {num2} = {multiply(num1, num2)}")
  print(f"{num1} / {num2} = {divide(num1, num2)}")
