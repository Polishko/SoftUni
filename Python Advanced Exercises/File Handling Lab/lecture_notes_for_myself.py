import os

absolute_path = os.path.abspath(".")
absolute_path_2 = os.path.abspath(__file__) #means here
absolute_path_3 = os.path.abspath(__file__), "..", "search.txt" # ".."2 directories back ".." koydukca yukari cikmaya devam
file_path = os.path.join()
absolute_path_4 = os.path.dirname(os.path.abspath(__file__)) # sistemden bagimsiz gecerli yolu bulma cok faydali
path = os.path.join(absolute_path, "dir_name", "file_name") # boyle join ile baskasinin bilgisayarinda da dogru path oluyo
# dir yanlissa erisim izni alamadim diyo                       # sistem farkli olunca oncemli
print(os.path.isfile(path)) # bu dosya mi kontrolu

try:
    # file open and do smth
except FileNotFoundError:
    #print sth
finally:
    # file.close dersen file yoksa patlar
    # else: daha uygun
    # ama file her durumda aciliyor ve baska turlu bir hata varsa orn valueerror o zaman finally close sart ki kapatsin


# open with r -- serverin belleginde aciyor ama dosya buyukse ve bellek kucukse cok yavaslatiyor
# os.rename(file_path, renamed_file_path) file rename

# cursor reset
file_name.seek(0) --- # cursor'i basa tasiyor

# file.read().split("\n") burada yine liste readlines gibi ama sonlarinda \n olmuyor
# print(content, end="") sonundaki bosluk kaldiriliyor
