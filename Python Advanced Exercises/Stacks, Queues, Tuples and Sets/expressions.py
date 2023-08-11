from collections import deque


def is_operation(a):
    if a in ["*", "+", "-", "/"]:
        return True
    return False


def apply_operation(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    else:
        return a // b


collection = deque(input().split(" "))
operation_list = deque()

result = 0
while collection:
    current_item = collection.popleft()

    if not is_operation(current_item):
        operation_list.append(int(current_item))
    else:
        operator = current_item
        result = operation_list.popleft()

        while operation_list:
            sub_current_item = operation_list.popleft()
            result = apply_operation(result, sub_current_item, operator)

        if not collection:
            break

        collection.appendleft(str(result))

print(result)
