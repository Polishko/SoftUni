import sys

# input list
input_list = [int(num) for num in input().split(" ")]

# logic
while True:

    command = input()

    if command == "end":
        break

    command_list = command.split(" ")

# exchange command code

    if command_list[0] == "exchange":
        split_location = int(command_list[1])

        if split_location < 0 or split_location > len(input_list) - 1:
            print(f"Invalid index")
        else:
            part_1 = input_list[0:split_location + 1]
            part_2 = input_list[split_location + 1:len(input_list)]
            part_2.extend(part_1)
            input_list = part_2

# min/max odd/even command code

    elif command_list[0] == "max" and command_list[1] == "even":
        max_num = -sys.maxsize
        stored_idx = -1

        for i in range(len(input_list)):
            if input_list[i] % 2 == 0:
                if input_list[i] >= max_num:
                    max_num = input_list[i]
                    stored_idx = i

        idx_to_print = stored_idx

        if idx_to_print != -1:
            print(idx_to_print)
        else:
            print(f"No matches")

    elif command_list[0] == "max" and command_list[1] == "odd":
        max_num = -sys.maxsize
        stored_idx = -1

        for i in range(len(input_list)):
            if input_list[i] % 2 != 0:
                if input_list[i] >= max_num:
                    max_num = input_list[i]
                    stored_idx = i

        idx_to_print = stored_idx

        if idx_to_print != -1:
            print(idx_to_print)
        else:
            print(f"No matches")

    elif command_list[0] == "min" and command_list[1] == "even":
        min_num = sys.maxsize
        stored_idx = -1

        for i in range(len(input_list)):
            if input_list[i] % 2 == 0:
                if input_list[i] <= min_num:
                    min_num = input_list[i]
                    stored_idx = i

        idx_to_print = stored_idx

        if idx_to_print != -1:
            print(idx_to_print)
        else:
            print(f"No matches")

    elif command_list[0] == "min" and command_list[1] == "odd":
        min_num = sys.maxsize
        stored_idx = -1

        for i in range(len(input_list)):
            if input_list[i] % 2 != 0:
                if input_list[i] <= min_num:
                    min_num = input_list[i]
                    stored_idx = i

        idx_to_print = stored_idx

        if idx_to_print != -1:
            print(idx_to_print)
        else:
            print(f"No matches")

# first/last count odd/even command code

    elif command_list[0] == "first" and command_list[2] == "even":
        count = int(command_list[1])
        even_list = []

        if count > len(input_list):
            print(f"Invalid count")
            continue

        if count == 0:
            print(even_list)
            continue

        for k in range(len(input_list)):
            if input_list[k] % 2 == 0:
                even_list.append(input_list[k])
                count -= 1
                if count == 0:
                    break

        print(even_list)

    elif command_list[0] == "first" and command_list[2] == "odd":
        count = int(command_list[1])
        odd_list = []

        if count > len(input_list):
            print(f"Invalid count")
            continue

        if count == 0:
            print(odd_list)
            continue

        for k in range(len(input_list)):
            if input_list[k] % 2 != 0:
                odd_list.append(input_list[k])
                count -= 1
                if count == 0:
                    break

        print(odd_list)

    elif command_list[0] == "last" and command_list[2] == "even":
        count = int(command_list[1])
        even_list = []

        if count > len(input_list):
            print(f"Invalid count")
            continue

        if count == 0:
            print(even_list)
            continue

        for k in range(len(input_list) - 1, -1, -1):
            if input_list[k] % 2 == 0:
                even_list.append(input_list[k])
                count -= 1
                if count == 0:
                    break

        even_list.reverse()
        print(even_list)

    elif command_list[0] == "last" and command_list[2] == "odd":
        count = int(command_list[1])
        odd_list = []

        if count > len(input_list):
            print(f"Invalid count")
            continue

        if count == 0:
            print(odd_list)
            continue

        for k in range(len(input_list) - 1, -1, -1):
            if input_list[k] % 2 != 0:
                odd_list.append(input_list[k])
                count -= 1
                if count == 0:
                    break

        odd_list.reverse()
        print(odd_list)

print(input_list)
