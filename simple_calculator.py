def simple_calculator():

    print("Simple Arithmetic Calculator")
    print("Choose an Operator: +(add), -(subtract), *(multiply) /(division)")

    try:
        num1 = float(input("Enter First Number: "))
        operator = input("Enter an Operator: ")
        num2 = float(input("Enter Second Number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError("Invalid Operator!")

        print(f"Result: {result} ")

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

        if __name__ == "__main__":
            simple_calculator()
