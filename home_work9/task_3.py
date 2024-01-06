from collections import Counter
import re
from typing import Tuple


def most_common_word(line: str) -> Tuple[str, int]:
    words = re.findall(r'\b\w+\b', line)
    word_counts = Counter(words)
    most_common, count = word_counts.most_common(1)[0]
    return most_common, count


def process_file(input_file: str, output_file: str) -> None:
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as output:
        for line in lines:
            most_common, count = most_common_word(line)
            output.write(f"Most common word: {most_common}, Count: {count}\n")


process_file("court.txt", "output_file.txt")