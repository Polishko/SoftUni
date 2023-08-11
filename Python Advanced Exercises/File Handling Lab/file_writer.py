# with open("my_first_file.txt", "w") as file:
#     file.write("I just created my first file!")

# (file.writelines(["sth\n", "else\n"]) linelar yazabilirsin yan bilgi)

# gene os yapti hoca

import os


path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "my_first_file.txt")

with open("my_first_file.txt", "w") as file:
    file.write("I just created my first file!")

