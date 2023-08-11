def fibonacci():
    val_1, val_2 = 0, 1

    while True:
        yield val_1
        val_1, val_2 = val_2, val_1 + val_2


# def fibonacci():
#     idx = 0
#     val_1, val_2 = 0, 0

#     while True:
#         if idx == 0:
#             val_1 = idx
#             yield val_1
#         elif idx == 1:
#             val_2 = idx
#             yield val_2
#         else:
#             val_3 = val_1 + val_2
#             val_1 = val_2
#             val_2 = val_3
#             yield val_3

#         idx += 1
