from string import ascii_uppercase
up_case_letters = ascii_uppercase

morse_letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

dict_morse = {}

for i in range(len(morse_letters)):
    key = morse_letters[i]
    value = ascii_uppercase[i]
    dict_morse[key] = value

coded_message = input().split(" | ")
message = []

for coded_word in coded_message:
    letters = coded_word.split()
    word = ""

    for coded_letter in letters:
        letter = dict_morse[coded_letter]
        word += letter

    message.append(word)

print(" ".join(message))
