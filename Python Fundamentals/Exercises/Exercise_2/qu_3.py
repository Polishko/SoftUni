no_people = int(input())
elevator_capacity = int(input())

if no_people % elevator_capacity == 0:
    no_courses = int(no_people / elevator_capacity)
else:
    no_courses = int(no_people // elevator_capacity) + 1

print(no_courses)

# mesela bunda  ceil kullanarak if kosulundan kurtuluyor