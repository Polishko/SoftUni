
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     if command == "SoftUni":
#         continue
#
#     string_to_print = ""
#
#     for letter in range(len(command)): # l in command mesela
#         string_to_print += command[letter] * 2
#
#     print(string_to_print)
# diger cozum print(f"{letter}{letter}, end="")

while True:
    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    for letter in command:
        print(f"{letter}{letter}", end="")
