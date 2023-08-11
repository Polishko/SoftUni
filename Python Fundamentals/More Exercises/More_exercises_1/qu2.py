input_string = list(input())
output_string = []

for index in range(len(input_string)):
    string_item = str(input_string[index])
    if string_item.isupper():
        output_string.append(index)

print(output_string)
