def user_present(field_collection, person):
    for field, person_list in field_collection.items():
        if person in person_list:
            return True
    return False


def field_present(field_collection, field):
    for fields in field_collection.keys():
        if field in field_collection:
            return True
    return False


users_in_force_sides = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        force_side, force_user = command.split(" | ")

        if user_present(users_in_force_sides, force_user):
            continue

        elif not user_present(users_in_force_sides, force_user) and not field_present(users_in_force_sides, force_side):
            users_in_force_sides[force_side] = []

        users_in_force_sides[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        user_found = False

        if user_present(users_in_force_sides, force_user):
            for sides, user_list in users_in_force_sides.items():
                for user in user_list:
                    if user == force_user:
                        user_found = True
                        user_list.remove(user)
                        break
                if user_found:
                    break

        if not field_present(users_in_force_sides, force_side):
            users_in_force_sides[force_side] = []

        users_in_force_sides[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for side, users in users_in_force_sides.items():
    if len(users) == 0:
        continue

    print(f"Side: {side}, Members: {len(users)}")

    for user in users:
        print(f"! {user}")
