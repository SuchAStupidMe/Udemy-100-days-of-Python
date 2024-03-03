# Calculator
def add(f_value, s_value):
    return f_value + s_value


def subtract(f_value, s_value):
    return f_value - s_value


def multiply(f_value, s_value):
    return f_value * s_value


def divide(f_value, s_value):
    return f_value / s_value


first_value = float(input("What's the first number?: "))

while True:
    print("+\n-\n*\n/")
    operator = input("Pick an operation: ")

    second_value = float(input("What's the next number?: "))

    if operator == "+":
        result = add(first_value, second_value)
    elif operator == "-":
        result = subtract(first_value, second_value)
    elif operator == "*":
        result = multiply(first_value, second_value)
    elif operator == "/":
        result = divide(first_value, second_value)
    print(f"{first_value} {operator} {second_value} = {result}")

    continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")
    if continue_calculating == "y":
        first_value = result
    elif continue_calculating == "n":
        first_value = float(input("What's the first number?: "))

