# input
input_list = [int(num) for num in input().split(", ")]

# filter
positive_num_lst = list(filter(lambda x: x >= 0, input_list))
negative_num_lst = list(filter(lambda x: x < 0, input_list))
even_num_lst = list(filter(lambda x: x % 2 == 0, input_list))
odd_num_lst = list(filter(lambda x: x % 2 != 0, input_list))

# convert to str
positive_str_lst = ", ".join([str(num) for num in positive_num_lst])
negative_str_lst = ", ".join([str(num) for num in negative_num_lst])
even_str_lst = ", ".join([str(num) for num in even_num_lst])
odd_str_lst = ", ".join([str(num) for num in odd_num_lst])

# output
print(f"Positive: {positive_str_lst}")
print(f"Negative: {negative_str_lst}")
print(f"Even: {even_str_lst}")
print(f"Odd: {odd_str_lst}")
