from collections import deque
# kesinlikle reduce cozumune de bak

operations = {"+": lambda a, b: a + b,
              "-": lambda a, b: a - b,
              "*": lambda a, b: a * b,
              "/": lambda a, b: a // b}

collection = deque(input().split(" "))
num_lst = deque() # yeni liste yapmadi item = 0 dedi

result = 0
while collection: # while item < len(collections[item)
    current_item = collection.popleft() # element = collection[item] # gerisi karisik gerekli mi emin degilim 19.30'da cozum

    if current_item not in "*+-/":
        num_lst.append(int(current_item))
    else:
        operator = current_item
        item_1 = num_lst.popleft()

        while num_lst:
            item_2 = num_lst.popleft()
            item_1 = operations[operator](item_1, item_2)

        num_lst.appendleft(item_1)

print(num_lst.pop())
