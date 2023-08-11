# import re
#
#
# with open("words.txt", "r") as main_file:
#     search_words = main_file.read().lower().split()
    # can also use set

# with open("input.txt", "w") as input_file:
#
#     line = " ".join(x.lower() for x in input().split())
#     while line:
#         input_file.write(f"{line}\n")
#         line = " ".join(x.lower() for x in input().split())
#

# benimki
# import re
#
#
# with open("words.txt", "r") as main_file:
#     search_words = main_file.read().lower().split()
#
# with open("input.txt", "r") as input_file:
#     input_data = input_file.read().lower()
#
# collection = {}
#
# for word in search_words:
#     pattern = r"\b" + re.escape(word) + r"\b"
#     matches = re.findall(pattern, input_data)
#     collection[word] = len(matches)
#
# sorted_collection = sorted(collection.items(), key=lambda x: -x[1])
#
# with open("output.txt", "w") as output_file:
#     for item in sorted_collection:
#         output_file.write(f"{item[0]}-{item[1]}\n")

# hoca

import os
import re

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_name = "words.txt"
file_path = os.path.join(path_to_root, file_name)

# burada try except exit yapti file yoksa cik falan

with open("words.txt", "r") as main_file: # yani bu iki satir try icinde sonra hepsini read content
    # funct koyup sonucunu split etti
    search_words = main_file.read().lower().split()

with open("input.txt", "r") as input_file:
    input_data = input_file.read().lower()

collection = {}

for word in search_words:
    pattern = r"\b" + re.escape(word) + r"\b"
    matches = re.findall(pattern, input_data)
    collection[word] = len(matches)

sorted_collection = sorted(collection.items(), key=lambda x: -x[1])

with open("output.txt", "w") as output_file:
    for item in sorted_collection:
        output_file.write(f"{item[0]}-{item[1]}\n")
