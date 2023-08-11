# def even_odd(*args):
#     *nums, command = args
#
#     if command == "even":
#         return list(filter(lambda x: (x % 2 == 0), nums))
#     else:
#         return list(filter(lambda x: (x % 2 != 0), nums))
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# *nums hic almadi command = args[-1] boylece iflerde boldu args[:-1] bundaki evenlari ve oddlari aldi boyle optimize ediyor
# yukarida ayrica nums olusturmamis oluyor

def even_odd(*args):

    if args[-1] == "even":
        return list(filter(lambda x: (x % 2 == 0), args[:-1]))
    else:
        return list(filter(lambda x: (x % 2 != 0), args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))