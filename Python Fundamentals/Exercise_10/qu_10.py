def best_count(line):
    line_1 = line[:10]
    line_2 = line[10:]
    target_sym = ""
    count, max_count_1, max_count_2 = 0, 0, 0

    for idx_1 in range(10):
        a = line_1[idx_1]
        if a == "@" or a == "#" or a == "$" or a == "^":
            target_sym = a

            for i_1 in range(idx_1, 10):
                if line[i_1] != target_sym:
                    break
                count += 1

            max_count_1 = max(max_count_1, count)
            count = 0

        if max_count_1 >= 6:
            break

    for idx_2 in range(10):
        b = line_2[idx_2]
        if b == target_sym:

            for i_2 in range(idx_2, 10):
                if line_2[i_2] != target_sym:
                    break
                count += 1

            max_count_2 = max(max_count_2, count)
            count = 0

        if max_count_2 >= 6:
            break

    result = target_sym, min(max_count_1, max_count_2), line
    return result


ticket_lst = [ticket.strip() for ticket in input().split(", ")]
count_lst = []

for ticket in ticket_lst:

    if len(ticket) != 20:
        count_lst.append(None)
        continue

    check = best_count(ticket)
    count_lst.append(check)

for item in count_lst:

    if item is None:
        print(f"invalid ticket")
    elif 10 <= item[1]:
        print(f"ticket \"{item[2]}\" - {item[1]}{item[0]} Jackpot!")
    elif 6 <= item[1] < 10:
        print(f"ticket \"{item[2]}\" - {item[1]}{item[0]}")
    else:
        print(f"ticket \"{item[2]}\" - no match")
