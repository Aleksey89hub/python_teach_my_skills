import json
import csv


def json_to_csv(json_data_path: str,
                output_csv_file: str,
                ) -> None:
    try:
        with open(json_data_path, 'r') as json_reader:
            json_data = json.load(json_reader)

        with open(output_csv_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            headers = json_data[0].keys()
            csv_writer.writerow(headers)

            for row in json_data:
                row['languages'] = ', '.join(row['languages'])
                csv_writer.writerow(row.values())

        print(f"Conversion completed. Result written to {output_csv_file}")

    except Exception as e:
        print(f"Error: {e}")


def add_user_to_json_and_csv(json_path: str,
                             csv_path: str, ) -> None:
    try:
        try:
            with open(json_path, 'r') as reader:
                json_data = json.load(reader)

        except FileNotFoundError as e:
            json_data = []

        name = input("Enter the employee's name: ")
        birthday = input("Enter the employee's birthday (DD.MM.YYYY): ")
        height = int(input("Enter the employee's height in centimeters: "))
        weight = float(input("Enter the employee's weight in kilograms: "))
        car = input("Does the employee have a car? (True/False): ").lower() == 'true'
        languages_str = input("Enter the employee's languages separated by commas: ")
        languages = [lang.strip() for lang in languages_str.split(',')]

        new_employee = {
            "name": name,
            "birthday": birthday,
            "height": height,
            "weight": weight,
            "car": car,
            "languages": languages
        }

        json_data.append(new_employee)

        with open(json_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

        with open(csv_path, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=new_employee.keys())

            csv_writer.writerow(new_employee)


    except Exception as e:
        print(f"Error: {e}")


def find_user_from_json_by_name(json_path: str):
    user_name = input("Enter the user name: ").strip()

    try:
        with open(json_path, 'r') as reader:
            json_data = json.load(reader)

        user_data = None
        for user in json_data:
            if user.get('name') == user_name:
                user_data = user
                break

        if user_data:
            print(f"User found:\n{json.dumps({user_name: user_data}, indent=2)}")
        else:
            print(f"User with name '{user_name}' not found.")

    except FileNotFoundError:
        print(f"Error: File '{json_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_path}'.")
    except Exception as e:
        print(f"Error: {e}")


def find_user_by_programming_language(json_path: str) -> None:
    programming_language = str(input("Enter programming language :")).title()
    try:
        with open(json_path, "r") as reader:
            json_data = json.load(reader)
            user_data = []
            for user in json_data:
                if programming_language in user.get("languages", []):
                    user_data.append(user)
            if user_data:
                print(f"User found:\n{json.dumps({programming_language: user_data}, indent=2)}")
            else:
                print(f"User with name '{programming_language}' not found.")

    except FileNotFoundError as e:
        print(e)


def find_avg_height_by_age(json_path: str) -> None:
    birthday_year = int(input("Enter the employee's birthday year: "))
    avg = 0
    try:
        with open(json_path, "r") as reader:
            json_data = json.load(reader)
            filtered_employees = [employee for employee in json_data if
                                  int(employee.get("birthday").split(".")[2]) < birthday_year]

            for user in filtered_employees:
                avg += user.get("height")
        print(avg / len(filtered_employees))
    except FileNotFoundError as e:
        print(e)


def user_application(json_data_path: str,
                     output_csv_file: str,
                     ) -> None:
    text = '''
    1. Convert JSON to CSV
    2. Add a user to JSON to CSV
    3. Find a user by name
    4. Find a user by a programming language
    5. Find users average height by birthday's year
    6. Terminate the application
    '''
    while True:
        print("Choose you action by entering numbers 1-6")
        print(text)
        try:
            number = int(input("Enter the value: "))
            if number == 1:
                json_to_csv(json_data_path, output_csv_file)
            elif number == 2:
                add_user_to_json_and_csv(json_data_path, output_csv_file)
            elif number == 3:
                find_user_from_json_by_name(json_data_path)
            elif number == 4:
                find_user_by_programming_language(json_data_path)
            elif number == 5:
                find_avg_height_by_age(json_data_path)
            elif number == 6:
                break
            else:
                print(f"The entered {number} number is not valid")

        except ValueError as e:
            print(e)


user_application("employees.json", "output_csv.csv")