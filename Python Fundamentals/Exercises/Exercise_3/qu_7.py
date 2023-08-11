gifts = input()
gifts_list = gifts.split(" ")
last_gift_index = len(gifts_list) - 1

while True:
    command = input()

    if command == "No Money":
        break

    command_list = command.split(" ")

    if "OutOfStock" in command:
        for i in range(len(gifts_list)):
            if gifts_list[i] == command_list[1]:
                gifts_list[i] = "None"

    elif "Required" in command:
        if 0 <= int(command_list[2]) <= last_gift_index:
            replace_index = int(command_list[2])
            gifts_list[replace_index] = command_list[1]

    elif "JustInCase" in command:
        gifts_list[last_gift_index] = command_list[1]

for gift_no in range(len(gifts_list)):
    if gifts_list[gift_no] == "None":
        continue

    print(gifts_list[gift_no], end=" ")
