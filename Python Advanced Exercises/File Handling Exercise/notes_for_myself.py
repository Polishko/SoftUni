# terminale girdiginde yazan path absolute path yani bulundugun directory, burada file handle exe 6.
# relative path ise ilgili kodu yuruttugun dosya (baska bilg veya sistem de olabilir)

file_path = "files/example.txt"

# file = open(file_path, "w")
# file.close()
#
# ya da bunun yerine write daha guvenli

with open(file_path, "w") as file:
    file.write("This is nice\n")

with open(file_path, "a") as file:
    file.write("This is also nice")

# file.read() --> tum dosyayi okuyor ve string olarak veriyor
# file.readlines() --> liste veriyor her line eleman
# bunlarda cursor surekli ilerliyor

# bilgi okuma olusturma tarihi alma:
import os
from datetime import datetime


file_info = os.stat(file_path)
print(f"File size is {file_info.st_size} bytes")
print(f"Last modified at {datetime.fromtimestamp(file_info.st_mtime)}")
print(f"Last modified at {datetime.fromtimestamp(int(file_info.st_mtime))}")

os.rename(file_path, "files/new_name.txt")  #slash'in yonunun farkli olduguna dikkat et, escape gerektirmiyor

# mesela birkac klasor yukari cikmak istiyorsun
file_path_other = "../../some_file.txt" # kac kez ../ varsa o kadar dir yukarida

# directory levels -- niva

# dir_1
# ---dir_1a level:0 (relative to dir1)
# ---dir_1b level:0
# ---dir_1b level:0
# ---dir_2 level:0
# ------dir_2a level:1 relative to dir_1
# ------dir_2b
# ------dir_2c


