from collections import deque

#
# def sum_total(number_array):
#     result = 0
#     step = len(number_array)
#     if len(number_array) == 1:
#         return int(number_array[0])
#     if len(number_array) == 0:
#         return 0
#
#     for i in range(step):
#         part1 = number_array[:i + 1]
#         part2 = number_array[i + 1:]
#         result += sum_total(part1) + sum_total(part2)
#
#
#     return result
#
#
# input_str = input('Enter a number: ')
# input_array = [x for x in input_str]
# length_array = len(input_array)
# print(sum_total(input_array))
#
#

def cut_all_points(s: str):
    # Cut the string at each index and build a zipped list of the cut strings
    zipped = []
    for i in range(1, len(s) + 1):
        zipped.append((s[:i], s[i:]))
    return zipped

def sum_of_all_substrings(s: str) -> int:
    # Cut the string at each index
    zipped = cut_all_points(s)
    total_sum = 0

    for left, right in zipped:
        if len(right) == 0:
            total_sum += int(left)
        else:
            right_sum = sum_of_all_substrings(right)
            left_sum = ((len(right) - 1) * len(right) // 2 + 1) * int(left)
            total_sum += left_sum + right_sum

    return total_sum

# Example usage
print(sum_of_all_substrings("1234"))  # Should output 169
