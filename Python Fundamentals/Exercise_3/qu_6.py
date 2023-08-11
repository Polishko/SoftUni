integer_string_input = input()
n = int(input())

list_string = integer_string_input.split(" ")
list_integers = list(map(int, list_string))
sorted_int_list = sorted(list_integers)
sorted_string_list = list(map(str, sorted_int_list))

for i in range(n):
    element = sorted_string_list[i]
    list_string.remove(element)

print(", ".join(list_string))
