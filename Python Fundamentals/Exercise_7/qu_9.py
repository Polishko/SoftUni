num_rows = int(input())

all_students = {}
for _ in range(1, num_rows + 1):
    name = input()
    grade = float(input())

    if name not in all_students:
        all_students[name] = []

    all_students[name].append(grade)

for student, grades in all_students.items():
    ave_grade = sum(grades) / len(grades)
    if ave_grade >= 4.50:
        print(f"{student} -> {ave_grade:.2f}")
