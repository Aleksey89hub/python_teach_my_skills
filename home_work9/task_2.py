import re


def correct_text(path_to_text: str) -> None:
    with open(path_to_text, "r") as reader, open("corrected.txt", "w") as corrected_text:
        content = reader.read()
        fio_pattern = re.compile(
            r'\b(?!Подсудимая\b)([A-ZА-Я][a-zа-я\-?]+?)([?:A-ZА-Я][a-zа-я]+)(?: [A-ZА-Я][a-zа-я]+)?(?: [A-ZА-Я][a-zа-я]+)?\b')
        modified_text = fio_pattern.sub('N', content)
        corrected_text.write(modified_text)


correct_text("court.txt")