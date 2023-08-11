str_lst = input().split(" ")

while True:
    command = input()

    if command == "3:1":
        break

    command_lst = command.split(" ") # command, arg_1, arg_2 = command.split(" ")

    # merging command
    if command_lst[0] == "merge":
        merged_element = ""
        start_idx = int(command_lst[1])
        end_idx = int(command_lst[2])

        # revert to positive indices
        if start_idx < 0 and end_idx < 0:
            start_idx += len(str_lst)
            end_idx += len(str_lst)

        # correct out of limit indices
        if start_idx < 0:  # max(0, start_idx)
            start_idx = 0

        if end_idx > len(str_lst) - 1: # min(0, start_idx)
            end_idx = len(str_lst) - 1

        # merge elements replace with spaces
        for idx in range(start_idx, end_idx + 1):   # put in function
            merged_element += str_lst[idx]
            str_lst[idx] = " "

        # filter spaces in list  # or for cycle remove with pop(start index) the n  elements  in the range
        str_lst = list(filter(lambda x: x != " ", str_lst))

        # add merge element
        str_lst.insert(start_idx, merged_element)

    # division command
    if command_lst[0] == "divide":
        divide_idx = int(command_lst[1])
        divider = int(command_lst[2])    # remainder yerine for c. ile divider kadar divisor aliyor, son parcada kalan her seyi aliyor
        divisor = len(str_lst[divide_idx]) // divider  #alolala div 0 3, range(partition - 1) * part_size) son kismi almiyor, slice yerine
        remainder = len(str_lst[divide_idx]) % divider

        # revert to positive indices
        if divide_idx < 0:
            divide_idx += len(str_lst)

        # take element to manipulate and divide list
        remove_ele = list(str_lst[divide_idx])
        str_lst_1 = str_lst[0:divide_idx]
        str_lst_2 = str_lst[divide_idx + 1: len(str_lst)]

        # find element to divide and manipulate
        divided_lst = []

        while len(remove_ele) > 0: # for c. ile eklenecek parca donuyor, her idx elemani ana liste giriyor ve girdigi indeks
            part_lst = remove_ele[0:divisor] # cycle idx'i ile artiyor
            part_str = "".join(part_lst)
            divided_lst.append(part_str)
            del remove_ele[0:divisor]

            if len(remove_ele) == remainder:
                last_ele = str(divided_lst[-1])
                add_piece = "".join(remove_ele)
                last_ele += add_piece
                divided_lst[-1] = last_ele
                remove_ele.clear()

        # add to list
        str_lst = str_lst_1 + divided_lst + str_lst_2

print(" ".join(str_lst))
