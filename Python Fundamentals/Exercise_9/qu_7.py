num_commands = int(input())
registered_users = {}

for num in range(num_commands): # for _
    command = input().split(" ")

    if command[0] == "register":
        user = command[1]
        plate = command[2]

        if user not in registered_users: # bu maddeyi alttaki if'in else'i olarak yapti daha iyi
            registered_users[user] = ""

        current_plate = registered_users[user]

        if plate == current_plate:
            print(f"ERROR: already registered with plate number {registered_users[user]}")

        else:
            registered_users[user] = plate
            print(f"{user} registered {plate} successfully")

    elif command[0] == "unregister":
        user = command[1]

        if user not in registered_users:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            del registered_users[user] # pop ile de oluyor yapti

for key, value in registered_users.items():
    print(f"{key} => {value}")
