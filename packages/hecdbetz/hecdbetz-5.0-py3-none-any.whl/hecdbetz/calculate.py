import sys

def calculate(operation, num1, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        print("Invalid operation")
        return

    print(f"The result of {operation} is: {result}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
    else:
        operation = sys.argv[1]
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
        calculate(operation, num1, num2)


if __name__ == "__main__":
    main()
    