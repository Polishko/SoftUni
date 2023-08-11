start = ord(input())
end = ord(input())
line = input()
output = ""

for char in line:

    if start < ord(char) < end:
        output += char

print(sum([ord(ele) for ele in output]))
