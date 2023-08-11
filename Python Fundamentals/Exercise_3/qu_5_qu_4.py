num_list = [int(num) for num in input().split(", ")]
beggar_count = int(input())
counter = 0
current_order = 1
sum_list = []

while current_order <= beggar_count:
    order = current_order
    sum_nums = 0

    for idx in range(0, len(num_list)):
        counter += 1
        if counter % order == 0:
            sum_nums += num_list[idx]
            order += beggar_count
    sum_list.append(sum_nums)
    current_order += 1
    counter = 0

print(sum_list)
