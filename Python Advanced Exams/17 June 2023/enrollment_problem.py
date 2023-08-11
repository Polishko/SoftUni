def gather_credits(needed_credits, *courses):
    result, enrolled = [], []
    gathered = 0

    for course_info in courses:
        course_name, no_credits = course_info[0], course_info[1]

        if needed_credits > 0:
            if course_name in enrolled:
                continue

            needed_credits = max(0, needed_credits - no_credits)
            gathered += no_credits
            enrolled.append(course_name)

    if needed_credits == 0:
        result.append(f"Enrollment finished! Maximum credits: {gathered}.")
        result.append(f"Courses: {', '.join(sorted(enrolled))}")
        return "\n".join(result)

    return f"You need to enroll in more courses! You have to gather {needed_credits} credits more."
