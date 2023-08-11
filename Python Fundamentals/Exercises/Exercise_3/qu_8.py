first_string = input()
water = float(input())

first_list = first_string.split("#")
values_list = []

for i in range(len(first_list)):
    second_string = first_list[i]
    second_list = second_string.split(" = ")
    for n in range(1):
        if "High" in second_list and not (81 <= int(second_list[1]) <= 125):
            continue
        elif "Medium" in second_list and not (51 <= int(second_list[1]) <= 80):
            continue
        elif "Low" in second_list and not (1 <= int(second_list[1]) <= 50):
            continue
        values_list.append(int(second_list[1]))

total_fire = 0
to_print = []

for k in range(len(values_list)):
    if values_list[k] > water:
        continue
    water -= values_list[k]
    total_fire += values_list[k]
    string_value = f"- {values_list[k]}"
    to_print.append(string_value)

effort = total_fire * 0.25
print("Cells:")

for m in range(len(to_print)):
    print(to_print[m])

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
