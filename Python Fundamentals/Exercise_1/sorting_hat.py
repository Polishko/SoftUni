while True:
    name = input()
    sorting_successful = True

    if name == "Welcome!":
        break

    if name == "Voldemort":
        print(f"You must not speak of that name!")
        sorting_successful = False
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

if sorting_successful:
    print(f"Welcome to Hogwarts.")
