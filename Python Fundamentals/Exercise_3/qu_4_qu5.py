card_string = input()
shuffle_time = int(input())
card_list = card_string.split(" ")

while shuffle_time > 0:
    length = len(card_list)
    half_length = int(len(card_list) * 0.5)
    part_1 = card_list[0:half_length]
    part_2 = card_list[half_length:length]
    shuffled_list = []

    for i in range(len(part_1)):
        shuffled_list.append(part_1[i])
        shuffled_list.append(part_2[i])

    card_list = shuffled_list
    shuffle_time -= 1

print(card_list)
