input_string = input()
current_element = ""
que_list = []

for char_no in range(len(input_string)):
    if input_string[char_no] == ",":
        que_list.append(current_element)
        current_element = ""
        continue
    if input_string[char_no] == " ":
        continue
    current_element += input_string[char_no]
    if char_no == len(input_string) - 1:
        que_list.append(current_element)

que_list.reverse()
n = len(list(que_list))

for i in range(n):
    if i == 0 and que_list[i] == "wolf":
        print(f"Please go away and stop eating my sheep")
    elif i != 0 and que_list[i] == "wolf":
        print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
