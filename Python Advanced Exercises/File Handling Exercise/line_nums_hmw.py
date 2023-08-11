from string import punctuation


with open("text.txt", "r") as file:
    lines = file.readlines()

output_file = open("files/output_mine.txt", "w")

for i in range(len(lines)):
    line = lines[i]

    char_count = len([char for char in line if char in punctuation])
    letters_count = len([char for char in line if char.isalpha()])
    output_file.write(f"Line {i}: {''.join(line[:-1])} ({letters_count})({char_count})\n")

output_file.close()
