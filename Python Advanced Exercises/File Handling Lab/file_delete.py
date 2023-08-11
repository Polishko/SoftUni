import os


# file_path = "my_first_file.txt" burada gercek path vermeyi oneriyor

# if os.path.exists(file_path):
#     os.remove(file_path)
# else:
#     print("File already deleted!")

# hocanin
path_to_root = os.path.dirname(os.path.abspath(__file__))
file_name = "not_a_file.txt"
file_path = os.path.join(path_to_root, file_name)

if os.path.isfile(file_path):
    os.remove(file_path)

# try:
#     os.remove(file_path)
# except FileNotFoundError:
#     print("File already deleted!")
