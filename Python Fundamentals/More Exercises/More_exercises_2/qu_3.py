key = int(input())
n = int(input())
message_list = []

for _ in range(1, n + 1):
    letter = input()
    to_add = chr(ord(letter) + key)
    message_list.append(to_add)

final_message = ""
for i in range(len(message_list)):
    final_message += message_list[i]

print(final_message)
