def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return take, halves, integers


# def solution():
#     def integers():
#         i = 1
#         while True:
#             yield i
#             i += 1

#     def halves():
#         for i in integers():
#             yield i / 2

#     def take(n, seq):
#         idx = 0
#         result = []

#         for ele in seq:
#             if idx == n:
#                 break
#             result.append(ele)
#             idx += 1

#         return result

#     return take, halves, integers

