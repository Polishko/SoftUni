# a = input()
# b = a.split("\\")
# last_ele = b[-1]
# file_name, file_extension = last_ele.split(".")
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")

# bu ustteki iyi bir yanit degil isimde nokta olabilir
# bu yuzden . ile split edince lst.pop() = extension yapmali
# file name icin de kalan lst icin "."join


a = input()
b = a.split("\\")
last_ele = b[-1].split(".")
file_extension = last_ele.pop()
file_name = ".".join(last_ele)
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
