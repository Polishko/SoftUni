input_string = input()
input_list = input_string.split(" ")
num_list = [int(num) for num in input_list]
step = int(input())
counter = 0
kills_in_order = []

while len(num_list) > 0:
    indexes_to_remove = []

    for i in range(len(num_list)):
        checked_person = num_list[i]
        counter += 1

        if counter % step == 0:
            indexes_to_remove.append(i)
            kills_in_order.append(str(checked_person))

    for m in range(len(indexes_to_remove)):
        for n in range(len(num_list)):
            if n == indexes_to_remove[m]:
                num_list[n] = -1

    for k in range(len(num_list) - 1, -1, -1):
        if num_list[k] == -1:
            num_list.remove(num_list[k])

final_string = ",".join(kills_in_order)
print(f"[{final_string}]")
