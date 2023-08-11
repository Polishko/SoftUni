input_string = input()
queue_list = input_string.split(", ")
queue_list.reverse()
n = len(list(queue_list))

for i in range(n):
    if i == 0 and queue_list[i] == "wolf":
        print(f"Please go away and stop eating my sheep")
    elif i != 0 and queue_list[i] == "wolf":
        print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
