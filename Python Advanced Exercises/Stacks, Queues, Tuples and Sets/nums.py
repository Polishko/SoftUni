seq_1 = set(int(num) for num in input().split(" "))
seq_2 = set(int(num) for num in input().split(" "))

command_count = int(input())

for _ in range(command_count):
    args = input().split(" ") # split everything in one line
    commands = args[0], args[1]
    args_set = set(args)
    command_set = {args[0], args[1]}

    if commands == ("Add", "First"): # put all commands in lambda fnc in dict
        args_set.difference_update(command_set)
        seq_1.update([int(num) for num in args_set])

    elif commands == ("Add", "Second"):
        args_set.difference_update(command_set)
        seq_2.update([int(num) for num in args_set])

    elif commands == ("Remove", "First"):
        args_set.difference_update(command_set)
        seq_1.difference_update([int(num) for num in args_set])

    elif commands == ("Remove", "Second"):
        args_set.difference_update(command_set)
        seq_2.difference_update([int(num) for num in args_set])

    else:
        if seq_1.issubset(seq_2) or seq_2.issubset(seq_1):
            print("True") # put boolean directly in print
        else:
            print("False")

print(", ".join(str(num) for num in sorted(seq_1)))
print(", ".join(str(num) for num in sorted(seq_2)))
