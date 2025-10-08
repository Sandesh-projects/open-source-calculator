# A simple command-line calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")

    choice = input("Enter operation: ").lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "add":
        print("Result:", add(a, b))
    elif choice == "subtract":
        print("Result:", subtract(a, b))
    elif choice == "multiply":
        print("Result:", multiply(a, b))
    elif choice == "divide":
        print("Result:", divide(a, b))
    else:
        print("Invalid operation")
