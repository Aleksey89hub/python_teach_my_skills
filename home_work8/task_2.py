from enum import Enum


class Operation(Enum):
    ADD = "+"
    SUBTRACTION = "-"
    DIVISION = "/"
    MULTIPLICATION = "*"


class OperationMethods:
    def __init__(self):
        pass

    def add(self, x, y):
        print(x + y)

    def subtract(self, x, y):
        print(x - y)

    def multiply(self, x, y):
        print(x * y)

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Error: division by zero is not allowed.")
        print(x / y)


class Calculator:
    def calculate(self):
        operation_methods_instance = OperationMethods()
        try:
            number1 = float(input("Enter the first number: "))
            sign = str(input("Enter the math sign number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError as e:
            print(f"Error: {e}")
            return

        if sign == Operation.ADD.value:
            operation_methods_instance.add(number1, number2)
        elif sign == Operation.SUBTRACTION.value:
            operation_methods_instance.subtract(number1, number2)
        elif sign == Operation.DIVISION.value:
            operation_methods_instance.divide(number1, number2)
        elif sign == Operation.MULTIPLICATION.value:
            operation_methods_instance.multiply(number1, number2)
        else:
            print(f"Error: Unknown operation {sign}")


calculator_instance = Calculator()
calculator_instance.calculate()