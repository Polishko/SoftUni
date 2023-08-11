from collections import deque


orders = deque(int(x) for x in input().split(", "))
employees = deque(int(x) for x in input().split(", "))

total_orders = 0
while employees:
    if not orders:
        print("All orders are successfully completed!")
        print(f"Total pizzas made: {total_orders}")
        if employees:
            print(f"Employees: {', '.join(str(x) for x in employees)}")
        break

    order = orders.popleft()

    if order > 10 or order <= 0:
        continue

    while True:
        if not employees:
            orders.appendleft(order)
            break

        employee = employees.pop()
        completed = min(order, employee)
        order -= completed
        total_orders += completed

        if order == 0:
            break

if orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
