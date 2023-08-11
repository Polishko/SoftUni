def students_credits(*args):
    courses = {}
    result = []

    for arg in args:
        tokens = arg.split("-")
        name, creds, max_points, points = tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3])
        courses[name] = creds * (points / max_points)

    total_credits = sum(value for value in courses.values())

    if total_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma.")

    sorted_courses = sorted(courses.items(), key=lambda x: -x[1])
    for course_info in sorted_courses:
        result.append(f"{course_info[0]} - {course_info[1]:.1f}")

    return "\n".join(result)
