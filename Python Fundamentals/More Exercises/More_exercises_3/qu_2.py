num_string = input()
num_str_list = num_string.split(" ")
text_string = input()
text_list = list(text_string)

sums_list = []

for num_no in num_str_list:
    sum_digits = 0
    for index, digit in enumerate(num_no):
        sum_digits += int(digit)
    sums_list.append(sum_digits)

final_message = ""
char_to_remove = ""

for i in range(len(sums_list)):
    sum_to_check = sums_list[i]
    current_list = text_list

    while sum_to_check > len(current_list) - 1:
        current_list += text_list

    for char_no in range(len(current_list)):
        if char_no == int(sum_to_check):
            final_message += current_list[char_no]
            char_to_remove = current_list[char_no]
            break

    for k in range(len(text_list)): # bu da gereksiz gibi remove yeterli, dene bunu
        if text_list[k] == char_to_remove:
            text_list.remove(char_to_remove)
            break # bu gereksiz muhtemelen

print(final_message)
