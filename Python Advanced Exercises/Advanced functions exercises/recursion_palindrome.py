# def palindrome(word, index=0):
#
#     if len(word) % 2 != 0:
#         n = len(word) // 2 + 1 # buna ihtiyacin yok aslinda yarisi yeter ki zaten bi harf kalir
#     else:
#         n = len(word) // 2 # if idx bu oldugunda not palindrone
#
#     first = word[index]
#     last = word[len(word) - index - 1]  # word[-idx] != word[-idx-1]
#
#     if first != last:
#         return f"{word} is not a palindrome"
#
#     if index == n:
#         return f"{word} is a palindrome"
#
#     return palindrome(word, index + 1)


def palindrome(word, index=0):

    if word[index] != word[-index - 1]:
        return f"{word} is not a palindrome"

    if index == len(word) // 2:
        return f"{word} is a palindrome"

    return palindrome(word, index + 1)

print(palindrome("peter", 0))