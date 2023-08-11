import sys
from sys import maxsize
num = str(int(input()))
list_num = list(num)
digits_to_check = len(list_num)
num_max = -sys.maxsize
num_string = ""
index_to_exclude = -1

while digits_to_check > 0:

    for i in range(len(list_num)):
        current_num = int(list_num[i])

        if current_num > num_max:
            num_max = current_num
            index_to_exclude = i

    list_num.pop(index_to_exclude)
    num_string += str(num_max)
    digits_to_check = len(list_num)
    num_max = -sys.maxsize

print(num_string)
