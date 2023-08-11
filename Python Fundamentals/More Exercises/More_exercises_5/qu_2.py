input_lst = [ele for ele in input()]

num_str_lst = list(filter(lambda x: x.isdigit(), input_lst))
num_lst = [int(num) for num in num_str_lst]
non_num_lst = list(filter(lambda x: not x.isdigit(), input_lst))

take_lst = []
skip_lst = []

for idx in range(len(num_lst)):
    if idx % 2 == 0:
        take_lst.append(num_lst[idx])
    elif idx % 2 != 0:
        skip_lst.append(num_lst[idx])

result_lst = []

while len(take_lst) > 0:
    m = take_lst.pop(0)
    n = skip_lst.pop(0)

    for _ in range(m):

        if len(non_num_lst) == 0:
            break

        take_ele = non_num_lst.pop(0)
        result_lst.append(take_ele)

    for _ in range(n):

        if len(non_num_lst) == 0:
            break

        non_num_lst.pop(0)

    if len(non_num_lst) == 0:
        break

if result_lst[-1] == " ":
    del result_lst[-1]

print("".join(result_lst))
