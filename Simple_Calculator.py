def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'q' to quit\n")

    while True:
        expression = input("Enter operation (e.g. 5 + 3): ").strip()
        if expression.lower() == "q":
            print("Goodbye!")
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Invalid input. Use the format: number operator number\n")
            continue

        a_str, op, b_str = parts
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Please enter valid numbers.\n")
            continue

        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        elif op == "/":
            result = divide(a, b)
        else:
            print("Unknown operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

if __name__ == "__main__":
    calculator()