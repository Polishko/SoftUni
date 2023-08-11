class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):

        if self.iterations == self.count - 1:
            raise StopIteration

        return self.iterations * self.step


# class take_skip:
#     def __init__(self, step: int, count: int):
#         self.step = step
#         self.count = count
#         self.value = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         num = self.value

#         if self.count == 0:
#             raise StopIteration

#         self.count -= 1
#         self.value += self.step
#         return num
