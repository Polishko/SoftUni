themes_lst = input().split(", ")

while True:

    command = input()

    if command == "course start":
        break

    command_lst = command.split(":")

    if command_lst[0] == "Add" and command_lst[1] not in themes_lst:
        lesson = command_lst[1]
        themes_lst.append(lesson)

    elif command_lst[0] == "Insert" and command_lst[1] not in themes_lst:
        lesson = command_lst[1]
        insert_idx = int(command_lst[2])
        themes_lst.insert(insert_idx, lesson)

    elif command_lst[0] == "Remove" and command_lst[1] in themes_lst:
        lesson = command_lst[1]
        themes_lst.remove(lesson)
        remove_exercise = f"{lesson}-Exercise"
        if remove_exercise in themes_lst:
            themes_lst.remove(remove_exercise)

    elif command_lst[0] == "Swap" and command_lst[1] in themes_lst and command_lst[2] in themes_lst:
        lesson_1 = command_lst[1]
        lesson_2 = command_lst[2]
        idx_lesson_1 = themes_lst.index(lesson_1)
        idx_lesson_2 = themes_lst.index(lesson_2)
        exer_1 = f"{lesson_1}-Exercise"
        exer_2 = f"{lesson_2}-Exercise"
        themes_lst[idx_lesson_1], themes_lst[idx_lesson_2] = themes_lst[idx_lesson_2], themes_lst[idx_lesson_1]

        if exer_1 in themes_lst and exer_2 not in themes_lst:
            to_add = exer_1
            themes_lst.remove(exer_1)
            add_idx_1 = themes_lst.index(lesson_1) + 1
            themes_lst.insert(add_idx_1, to_add)

        elif exer_2 in themes_lst and exer_1 not in themes_lst:
            to_add = exer_2
            themes_lst.remove(exer_2)
            add_idx_2 = themes_lst.index(lesson_2) + 1
            themes_lst.insert(add_idx_2, to_add)

    elif command_lst[0] == "Exercise":
        lesson = command_lst[1]
        check_exercise = f"{lesson}-Exercise"

        if lesson in themes_lst and check_exercise in themes_lst:
            continue

        if lesson not in themes_lst:
            themes_lst.append(lesson)

        exercise_idx = themes_lst.index(lesson) + 1
        themes_lst.insert(exercise_idx, check_exercise)

for i in range(1, len(themes_lst) + 1):
    print(f"{i}.{themes_lst[i - 1]}")
