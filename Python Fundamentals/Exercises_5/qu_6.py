electron_num = int(input())

shell_lst = []
shell_no = 0

while electron_num > 0:
    shell_no += 1
    e_to_fill = 2 * shell_no ** 2

    if electron_num >= e_to_fill:
        electron_num -= e_to_fill
        shell_lst.append(e_to_fill)
    else:
        shell_lst.append(electron_num)
        electron_num = 0

print(shell_lst)
