# def even_odd_filter(**kwargs):
#     nums = {}
#
#     for key in kwargs.keys():
#
#         if key == "odd":
#             nums[key] = list(filter(lambda x: (x % 2 != 0), kwargs[key]))
#         else:
#             nums[key] = list(filter(lambda x: (x % 2 == 0), kwargs[key]))
#
#     return dict(sorted(nums.items(), key=lambda x: -len(x[1])))
#
#
# print(even_odd_filter(
#  odd=[2, 2, 30, 44, 10, 5],
# ))

# yeni sozluk olusturmadan mevcut sozlugu modify etti

def even_odd_filter(**kwargs):

    for key in kwargs.keys():

        if key == "odd":
            kwargs[key] = list(filter(lambda x: (x % 2 != 0), kwargs[key]))
        else:
            kwargs[key] = list(filter(lambda x: (x % 2 == 0), kwargs[key]))

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
 odd=[1, 2, 3, 4, 10, 5],
 even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))