import re
from spellchecker import SpellChecker
from word2number import w2n
from num2words import num2words


def check_valid_text(text):
    if text in ["Search", "Remove", "End"]:
        return text

    spell = SpellChecker()

    if not re.fullmatch(num_word_pattern, text):
        print("Input should be text.")
        return check_valid_text(input("Enter text again: "))
    elif len(spell.unknown(text.split())) > 0:
        print("Typo in text.")
        return check_valid_text(input("Enter text again: "))
    elif "minus" in text:
        print("Number should be positive.")
        return check_valid_text(input("Enter text again: "))
    return text


def check_if_text_is_num(text):
    try:
        match = w2n.word_to_num(text)

        if text != num2words(match):
            return check_valid_text(input("Enter valid text: "))

    except ValueError:
        print("The input text does not correspond to a valid number.")
        return check_valid_text(input("Enter text again: "))
    return text


def check_if_num_is_valid(num, text):
    if num.startswith("0") and len(num) > 1:
        return check_if_num_is_valid(input("Enter valid value: "), text)

    try:
        value = int(num)

        if w2n.word_to_num(text) != value:
            print("Value doesn't match text")
            return check_if_num_is_valid(input("Enter value: "), text)

    except ValueError:
        print("The variable number must be an integer.")
        return check_if_num_is_valid(input("Enter value: "), text)
    return num


def search_for_num(text):
    try:
        print(numbers_dictionary[text.lower()])
    except KeyError:
        print("Number does not exist in collection")


def delete_num(text):
    try:
        del numbers_dictionary[text.lower()]
    except KeyError:
        print("Number does not exist in collection")


numbers_dictionary = {}
num_word_pattern = r"[A-Za-z]+[ A-Za-z]*"

print("Enter valid text for positive numbers up to 999,999,999 and a corresponding integer value for the text.\n"
      "When finished Enter 'Search' to search in collection.")

while True:
    line = check_valid_text(input("Enter text: "))

    if line == "Search":
        break

    number_as_string = check_if_text_is_num(line)
    number = check_if_num_is_valid(input("Enter value: "), number_as_string)
    numbers_dictionary[number_as_string.lower()] = number

print("Enter text to search. When finished enter 'Remove' to remove numbers.")
while True:

    line = check_valid_text(input("Enter text: "))

    if line == "Remove":
        break

    search_for_num(line)

print("Enter text to remove. When finished enter 'End' to view collection.")
while True:

    line = check_valid_text(input("Enter text: "))

    if line == "End":
        break

    delete_num(line)

print(numbers_dictionary)
