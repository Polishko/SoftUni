### n, m = input().split(" ")
### set_1_len, set_2_len = int(n), int(m)

# n, m = [int(a) for a in input().split(" ")]
# set_1, set_2 = set(), set()
#
# for _ in range(n):
#     num = int(input())
#     set_1.add(num)
#
# for _ in range(m):
#     num = int(input())
#     set_2.add(num)
#
# common_elements = set_1.intersection(set_2)
### for ele in common_elements:
###     print(ele)

# print(*common_elements, sep="\n")

# n, m = input().split(" ")
# set_1_len, set_2_len = int(n), int(m)

# Dilyan
n, m = [int(a) for a in input().split(" ")]

set_1 = {int(num) for num in range(n)}
set_2 = {int(num) for num in range(m)}

print(*set_1.intersection(set_2), sep="\n")
