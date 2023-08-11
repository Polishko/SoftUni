

# try:
#     file = open("text.txt", "r")
#     print("File found")
#     file.close()
# except FileNotFoundError:
#     print("File not found")

import os


path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "text.txt")

if os.path.isfile(file_path):
    pass
else:
    pass

# bu daha safe cunku olusturun dememisler, hocanin tercihi

