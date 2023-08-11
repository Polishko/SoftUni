
string_one = input()
string_two = input()

for i in range(len(string_two)):
    string = ""
    for k in range(len(string_two)):
        if k == i:
            string += string_two[k]
        else:
            string += string_one[k]
    current = string
    if current != string_one:
        print(current)
    string_one = current
