from collections import deque

string_lst = deque(lst.split() for lst in input().split("|"))

to_print = []
while string_lst:
    element = string_lst.pop()

    if element:
        print(" ".join(element), end=" ")

# Dilyan

# line = input().split("|")  # прочитаме реда като го разделяме по черта
#
# sub_lists = []  # създаваме списък, в които ще пазим резултата
#
# for sub_string in line[::-1]:  # развъртаме цикъл, който обхожда всеки подтекст в инпута
#     sub_lists.extend(sub_string.split())
#     # удължаваме списъка с резултата със списък от числата от конзолата след като сме махнали всички спейсове
#
# print(*sub_lists)  # ънпакваме списъка
#
# # solution 2
# numbers = [string.split() for string in input().split("|")]
# print(*[' '.join(sub_list) for sub_list in numbers[::-1] if sub_list])