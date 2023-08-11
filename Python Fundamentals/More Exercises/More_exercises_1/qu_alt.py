num = str(int(input()))
list_str_num = list(num)
num_list = [eval(i) for i in list_str_num]
num_string = ""

for i in range(len(num_list)):
    num_max = max(num_list)
    num_string += str(num_max)
    index_to_remove = num_list.index(num_max)
    num_list.pop(index_to_remove)

print(num_string)
