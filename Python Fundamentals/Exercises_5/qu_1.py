input_lst_1 = input().split(", ")
input_lst_2 = input().split(", ")

final_lst = []

for word_1 in input_lst_1:
    for word_2 in input_lst_2:
        if word_1 in word_2 and word_1 not in final_lst:
            final_lst.append(word_1)

print(final_lst)
