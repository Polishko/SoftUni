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
