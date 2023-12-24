import random


def is_prime_number(number: int) -> bool:
    return True if (number > 1) and (number % 2 != 0) else False


# Task 5
def encrypt_caesar(message: str, shift: int) -> str:
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message


def decrypt_caesar(encrypted_message: str, shift: int) -> str:
    return encrypt_caesar(encrypted_message, -shift)


# Task 7
def create_random_matrix(rows: int, cols: int):
    matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    print(matrix)


# Task 8
def find_min_max_in_matrix(matrix):
    rows = len(matrix)
    column = len(matrix[0])

    min_number = matrix[0][0]
    max_number = matrix[0][0]
    for i in range(rows):
        for j in range(column):
            if matrix[i][j] < min_number:
                min_number = matrix[i][j]
            if matrix[i][j] > max_number:
                max_number = matrix[i][j]

    print(f'The min number is {min_number}')
    print(f'The max number is {max_number}')