# def check_match(a, b):
#     if (a == "(" and b == ")") or a == "{" and b == "}" or a == "[" and b == "]":
#         return True
#     return False
#
#
# line = [*input()]
#
# opening = []
# no_match = False
# for char in line:
#     if char in "([{":
#         opening.append(char)
#     elif not opening:
#         no_match = True
#     else:
#         final_ele = opening.pop()
#         if not check_match(final_ele, char):
#             no_match = True
#
#     if no_match:
#         break
#
# if no_match or opening:
#     print("NO")
# else:
#     print("YES")

from collections import deque

matches = {"(": ")", "[": "]", "{": "}"}


line = deque([*input()])
opening_para = []

while line:
    current_ele = line.popleft()

    if current_ele in "([{":
        opening_para.append(current_ele)
    elif not opening_para:
        print("NO")
        break
    else:
        final_taken = opening_para.pop()

        if matches[final_taken] != current_ele: # Dilyan's solution: if not in "()[]{}"
            print("NO")
            break
else:
    print("YES")
