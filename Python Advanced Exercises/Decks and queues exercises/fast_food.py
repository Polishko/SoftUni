# from collections import deque
#
# food = int(input())
# orders = deque(input().split(" "))
# n = len(orders)
# orders_left = orders.copy()
# max_order = 0
#
# food_finished = False
# for _ in range(n):
#     current_order = int(orders.popleft())
#
#     if current_order > max_order:
#         max_order = current_order
#
#     if not food_finished:
#         if current_order <= food:
#             food -= current_order
#             orders_left.popleft()
#         else:
#             food_finished = True
#
#     if food == 0:
#         food_finished = True
#
# print(max_order)
# if len(orders_left) == 0:
#     print("Orders complete")
# else:
#     print(f"Orders left: {' '.join(orders_left)}")

### 2. Solution  ###

# from collections import deque
#
# food = int(input())
# orders = deque([int(num) for num in input().split(" ")])
#
# print(max(orders))
#
# while orders:
#     current_order = orders.popleft()
#
#     if current_order <= food:
#         food -= current_order
#     else:
#         orders.appendleft(current_order)
#         break
#
# if not orders:
#     print("Orders complete")
# else:
#     print(f"Orders left: {' '.join([str(num) for num in orders])}")

# Diyan Kalaydjiev
from collections import deque

food = int(input())
orders = deque([int(num) for num in input().split(" ")])

print(max(orders))

for order in orders.copy():

    if order <= food:
        food -= order
        orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(num) for num in orders])}")
        break

else:
    print("Orders complete")
