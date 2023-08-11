string_input = input()
original_list = string_input.split(" ")
new_list = []

for i in range(len(original_list)):
    element = int(original_list[i]) * -1
    new_list.append(element)

print(new_list)
