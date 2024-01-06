import re


def sum_numbers_in_file(file_path: str):
    with open(file_path, "r") as reader:
        content = reader.read()
        numeric_sequences = re.findall(r'\d+', content)
        total_sum = sum(map(int, numeric_sequences))
        print(f"The sum is {total_sum}")


sum_numbers_in_file("total_sum.txt")