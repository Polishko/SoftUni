from collections import deque


customers = deque(int(x) for x in input().split(", "))
taxis = deque(int(x) for x in input().split(", "))
total_time = 0

while taxis:
    customer, taxi = customers[0], taxis.pop()

    if taxi >= customer:
        total_time += customer
        customers.popleft()

    if not customers:
        print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
        break

else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
