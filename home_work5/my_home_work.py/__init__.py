# Task 2

def calculate_days_to_save(total_sum_for_phone: int, money_to_put_aside: int):
    days = 0
    current_saving = 0

    while current_saving < total_sum_for_phone:
        days += 1

        if days % 7 != 0:
            current_saving += money_to_put_aside

    print(f"It takes {days} days to save the sum {total_sum_for_phone}")


# Task 3

def calculate_fibonacci_number(n: int):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci_number(n - 1) + calculate_fibonacci_number(n - 2)


print(calculate_fibonacci_number(3))


# Task 4

def find_min_max_avg_in_list(array: list):
    minimal_value = array[0]
    maximal_value = array[0]
    avg = 0

    if len(array) == 0:
        print(f"The {array} is empty")

    for i in array:
        avg += i

        if minimal_value < i:
            minimal_value = i

        if maximal_value > i:
            maximal_value = i

    print(f"The average sum is {avg}, the max element is {maximal_value} and the min element is {minimal_value}")


# Task 5

def check_uniqueness_and_duplicates(numbers):
    seen_numbers = {}
    duplicates = {}

    for number in numbers:
        if number not in seen_numbers:
            seen_numbers[number] = 1
        else:
            seen_numbers[number] += 1
            if number not in duplicates:
                duplicates[number] = seen_numbers[number]

    if not duplicates:
        print("All numbers are unique")
    else:
        print("No all numbers are unique")
        for number, count in duplicates.items():
            print(f"Number {number} repeats {count} times.")


print(check_uniqueness_and_duplicates(list([5, 4, 12, 2, 4, 9])))


# Task 6

def binary_search(array: list, target: int):
    sorted_numbers = sorted(array)
    left, right = 0, len(sorted_numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_numbers[mid] == target:
            return mid
        elif sorted_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1