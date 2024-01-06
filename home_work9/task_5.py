def get_student_grade(file_path: str, score: int) -> None:
    with open(file_path, "r") as reader:
        content = reader.read()
        lines = content.strip().split('\n')

        for line in lines:
            words = line.strip().split()
            if len(words) == 3:
                surname, name, student_grade = words
                grade = int(student_grade)
                if score < grade:
                    print(f"Student {surname}, {name}, {grade}")


get_student_grade("students.txt", 3)