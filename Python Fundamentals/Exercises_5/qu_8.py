def decipher(word):
    final_lst = []

    digit_lst = list(filter(lambda x: x.isdigit(), word))
    digit_part = "".join(digit_lst)
    final_lst.append(digit_part)

    letter_part = list(filter(lambda x: x.isalpha(), word))
    final_lst.extend(letter_part)

    char = chr(int(final_lst[0]))
    final_lst[0] = char

    last_ele = final_lst[len(final_lst) - 1]
    final_lst[len(final_lst) - 1] = final_lst[1]
    final_lst[1] = last_ele

    return "".join(final_lst)


word_lst = input().split(" ")
decipher_lst = list(map(lambda x: decipher(x), word_lst))
print(" ".join(decipher_lst))
