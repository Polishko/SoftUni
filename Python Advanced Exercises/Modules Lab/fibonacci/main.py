from fibonacci.fibionacci import give_fibonacci, locate_number


seq = []
while True:
    line = input()

    if line == "Stop":
        break

    args = line.split(" ")

    if args[0] == "Create":
        seq = give_fibonacci(int(args[2]))
    else:
        num = int(args[1])
        locate_number(num, seq)
