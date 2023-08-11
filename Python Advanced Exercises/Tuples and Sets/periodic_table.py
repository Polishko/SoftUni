# num_inputs = int(input())
# element = set()
#
# for _ in range(num_inputs):
#     line = input().split()
#
#     for ele in line:
#         element.add(ele)
#
# for ele in element:
#     print(ele)

num_inputs = int(input())
elements = set()

for _ in range(num_inputs):
    elements = elements.union(ele for ele in input().split())

print(*elements, sep="\n")
