input_string = input()
list_inputs = input_string.split(", ")
zeroes_list = []

for i in range(len(list_inputs) - 1, -1, -1):
    if int(list_inputs[i]) == 0:
        zeroes_list.append(0)
        list_inputs.remove(list_inputs[i])

list_inputs += zeroes_list
list_integers = list(map(int, list_inputs))
print(list_integers)
