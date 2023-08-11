num_lines = int(input())

max_range = 0 # gereksiz
inters_with_max_range = "" # bu set() olmali daha mantikli
for _ in range(num_lines):
    values_first, values_second = input().split("-")
    first_start, first_end = values_first.split(",")
    second_start, second_end = values_second.split(",")
    set_1 = set(int(num) for num in range(int(first_start), int(first_end) + 1))
    set_2 = set(int(num) for num in range(int(second_start), int(second_end) + 1))
    intersection = list(set_1.intersection(set_2))

    if len(intersection) > max_range:
        max_range = len(intersection) # bunu printte yap
        inters_with_max_range = intersection

print(f"Longest intersection is {inters_with_max_range} with length {max_range}")

#
# num_lines = int(input())
#
# max_range = 0
# intersection = ""
#
# for _ in range(num_lines):
#     nums_1, nums_2 = input().split("-")
#     set_1, set_2 = set(nums_1.split(",")), set(nums_2.split(","))
#     set_nums = set(nums_1.split(",")).union(set(nums_2.split(",")))
#     length = abs(sorted(set_nums)[-1] - sorted(set_nums)[0])
#
#     if length > max_range:
#         max_range = length
#         intersection =
