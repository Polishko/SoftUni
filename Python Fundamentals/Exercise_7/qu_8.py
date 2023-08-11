courses_students = {}
students = []

while True:
    command = input()

    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses_students:
        courses_students[course_name] = []

    courses_students[course_name].append(student_name)

for course, students in courses_students.items():
    print(f"{course}: {len(students)}")

    for student in students:
        print(f"-- {student}")
