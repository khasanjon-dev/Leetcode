def calculator():
    print("=== Python Calculator ===")
    print("Operations: +, -, *, /")
    print("Type 'q' to quit")

    while True:
        first = input("\nEnter first number: ")

        if first.lower() == "q":
            break

        try:
            a = float(first)
            operator = input("Enter operator (+, -, *, /): ")
            b = float(input("Enter second number: "))

            if operator == "+":
                result = a + b
            elif operator == "-":
                result = a - b
            elif operator == "*":
                result = a * b
            elif operator == "/":
                if b == 0:
                    print("Error: Division by zero!")
                    continue
                result = a / b
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {result:g}")

        except ValueError:
            print("Error: Please enter valid numbers.")

    print("Calculator closed.")


if __name__ == "__main__":
    calculator()
