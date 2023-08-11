from collections import deque


def check_for_occurrence(collection, char):
    for item in collection:
        if char in item:
            collection[item].add(char)

        if len(set(item).difference(collection[item])) == 0:
            print(f"Word found: {item}")
            return True

    return False


words = {"rose": set(), "tulip": set(), "lotus": set(), "daffodil": set()}
vowels = deque(input().split(" "))
consonants = deque(input().split(" "))

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    if check_for_occurrence(words, current_vowel) or check_for_occurrence(words, current_consonant):
        break


else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

    
    
# from collections import deque


# words = {"rose": set(), "tulip": set(), "lotus": set(), "daffodil": set()}
# vowels = deque(input().split(" "))
# consonants = deque(input().split(" "))

# check_letters = deque()
# found = False

# while vowels and consonants:
#     if vowels:
#         check_letters.append(vowels.popleft())
#     if consonants:
#         check_letters.append(consonants.pop())

#     while check_letters:
#         current = check_letters.popleft()

#         for word in words:
#             if current in word:
#                 words[word].add(current)

#             if len(set(word).difference(words[word])) == 0:
#                 print(f"Word found: {word}")
#                 found = True
#                 break

#     if found:
#         break

# if not found:
#     print("Cannot find any word!")

# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")
