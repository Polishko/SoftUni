import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in file_types:
                file_types[extension] = []

            file_types[extension].append(filename)

        if os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


dir_path = input()
file_types = {}

try:
    save_extensions(dir_path)
except FileNotFoundError:
    print("Not a directory")

sorted_files = sorted(file_types.items())

root_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "report.txt"
file_path = os.path.join(dir_path, file_name)

with open(file_path, "a", encoding='utf-8') as file:

    for item in sorted_files:
        file.write(f"{item[0]}\n")

        for files in sorted(item[1]):
            file.write(f"- - - {files}\n")
