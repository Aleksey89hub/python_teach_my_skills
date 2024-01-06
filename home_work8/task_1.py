class CustomError(Exception):
    def __init__(self, message="Something is wrong with your input data. Please double check your values"):
        self.message = message
        super().__init__(self.message)


class TestHumanWeight:

    @staticmethod
    def calculate_bmi(weight: float, height_cm: float) -> float:
        height_m = height_cm / 100.0
        try:
            if weight <= 0:
                raise CustomError("weight should be positive numbers and not equal to zero.")

            bmi = weight / (height_m ** 2)

            return bmi
        except ZeroDivisionError:
            raise CustomError("Height cannot be zero.")
        except CustomError as ce:
            raise ce

    @staticmethod
    def interpret_bmi(bmi: float) -> str:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = TestHumanWeight.calculate_bmi(weight, height)
interpretation = TestHumanWeight.interpret_bmi(bmi)
print(interpretation)