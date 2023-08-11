class countdown_iterator:
    def __init__(self, count):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration

        self.count -= 1

        return self.count


# class countdown_iterator:
#     def __init__(self, count):
#         self.count = count

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count < 0:
#             raise StopIteration

#         val = self.count
#         self.count -= 1
#         return val
