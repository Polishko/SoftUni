import os
import django
from datetime import datetime

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Student

# Create and check models


def add_students():
    student_1 = Student.objects.create(
        student_id="FC5204",
        first_name="John",
        last_name="Doe",
        birth_date=datetime.strptime("15/05/1995", "%d/%m/%Y").strftime("%Y-%m-%d"),
        email="john.doe@university.com"
    )
    student_1.save()

    student_2 = Student.objects.create(
        student_id="FE0054",
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@university.com"
    )
    student_2.save()

    student_3 = Student.objects.create(
        student_id="FH2014",
        first_name="Alice",
        last_name="Johnson",
        birth_date=datetime.strptime("10/02/1998", "%d/%m/%Y").strftime("%Y-%m-%d"),
        email="alice.johnson@university.com"
    )
    student_3.save()

    student_4 = Student.objects.create(
        student_id="FH2015",
        first_name="Bob",
        last_name="Wilson",
        birth_date=datetime.strptime("25/11/1996", "%d/%m/%Y").strftime("%Y-%m-%d"),
        email="bob.wilson@university.com"
    )
    student_4.save()

# Good idea is to create a list containing strudent information as a dictionary with necessary fields for each student, then create the objects using a for cycle on the list (Student.objects.create(**_student))
# Bulk create method is another good option.

def get_students_info():
    students = Student.objects.all()
    info_list = [f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}"
                 for student in students]

    return "\n".join(info_list)


def update_students_emails():
    students = Student.objects.all()

    for student in students:
        student.email = student.email.replace("university.com", "uni-students.com")
        student.save()


def truncate_students():
    Student.objects.all().delete()

# Run and print your queries


# print(add_students())

# print(get_students_info())

# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)

truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")


