num = str(int(input()))
list_str_num = list(num)
num_list = [eval(i) for i in list_str_num]
num_list.sort(reverse=True)
new_num = ""

for i in range(len(num_list)):
    new_num += str(num_list[i])

print(new_num)
