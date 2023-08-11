class dictionary_iter:
    def __init__(self, my_dict):
        self.items = list(my_dict.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items) - 1:
            raise StopIteration

        self.index += 1
        return list(self.items)[self.index]
        
# class dictionary_iter:
#     def __init__(self, my_dict):
#         self.my_dict = my_dict
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.my_dict) - 1:
#             raise StopIteration
#
#         self.index += 1
#         return list(self.my_dict.items())[self.index - 1]



# class dictionary_iter:
#     def __init__(self, my_dict):
#         self.my_dict = my_dict
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == len(self.my_dict):
#             raise StopIteration

#         val = list(self.my_dict.items())[self.index]
#         self.index += 1
#         return val
