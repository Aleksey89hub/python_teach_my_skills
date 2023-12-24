import time
from functools import reduce


# 1
def convert_numbers_to_string(array: list) -> list[str]:
    return list(map(str, array))


# 2
def get_number_greater_then_zero(array: list) -> list[int]:
    return list((filter(lambda i: i > 0, array)))


# 3
def get_palindrome_list(array: list) -> list[str]:
    return list(filter(lambda i: i == "".join(reversed(i)), array))


# 4
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Execution time of function {func.__name__}: {elapsed_time:.6f} seconds")
        return result

    return wrapper


@timing_decorator
def example_function():
    time.sleep(5)


def calculate_room_area(room):
    return room["length"] * room["width"]


rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

areas = map(calculate_room_area, rooms)

total_area = reduce(lambda x, y: x + y, areas)