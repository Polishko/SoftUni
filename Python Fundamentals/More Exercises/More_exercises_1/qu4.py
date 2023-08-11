input_string = input()
input_string = input_string.lower()
count = 0

for char_no in range(len(input_string)):

    if input_string[char_no] == "s":
        if char_no + 4 > len(input_string):
            break

        check_string = ""

        for word_char in range(char_no, char_no + 4):
            check_string += input_string[word_char]
        if check_string == "sand":
            count += 1

    if input_string[char_no] == "s":
        if char_no + 3 > len(input_string):
            break

        check_string = ""

        for word_char in range(char_no, char_no + 3):
            check_string += input_string[word_char]
        if check_string == "sun":
            count += 1

    if input_string[char_no] == "w":
        if char_no + 5 > len(input_string):
            break

        check_string = ""

        for word_char in range(char_no, char_no + 5):
            check_string += input_string[word_char]
        if check_string == "water":
            count += 1

    if input_string[char_no] == "f":
        if char_no + 4 > len(input_string):
            break

        check_string = ""

        for word_char in range(char_no, char_no + 4):
            check_string += input_string[word_char]
        if check_string == "fish":
            count += 1

print(count)
