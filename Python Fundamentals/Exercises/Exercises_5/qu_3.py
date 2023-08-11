text_lst = list(filter(lambda x: len(x) % 2 == 0, input().split(" ")))
print(*text_lst, sep='\n')
