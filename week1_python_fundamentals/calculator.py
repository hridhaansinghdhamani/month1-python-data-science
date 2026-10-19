"""A small command-line calculator for practicing input and conditionals."""

def main():
    print("Basic Calculator")
    try:
        first = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("Division by zero is not defined.")
            return
        result = first / second
    else:
        print("Unsupported operation. Choose +, -, * or /.")
        return

    print(f"Result: {result:g}")

if __name__ == "__main__":
    main()
