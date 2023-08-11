def check_if_number(a):
    for a in range(len(lst)):
        if a == 0 or a == 1:
            return lst[a]
        elif a == 2:
            if lst[2].isdigit():
                return int(lst[2])
            else:
                return 45
        elif a == 3:
            if lst[3].isdigit():
                return int(lst[3])
            else:
                return 250
        elif a == 4:
            if lst[4].isdigit():
                return int(lst[4])
            else:
                return 10

arg_lst = []
line = input().split(" ")
for ele in range(len(line)):
    arg_lst.append(check_if_number(line[ele]))

print(arg_lst)