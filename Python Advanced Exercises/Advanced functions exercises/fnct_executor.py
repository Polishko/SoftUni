def func_executor(*args):

    return "\n".join([f"{funct_name.__name__} - {funct_name(*values)}" for funct_name, values in args])

    # results = []
    # for arg in args: # bu iki satir tek olabilir for name, vals in args hatta comprehension sonra join \n
    #     funct_name, values = arg[0], arg[1]
    #     results.append(f"{funct_name.__name__} - {funct_name(*values)}")
    #
    # return "\n".join(results)



# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result
#
#
# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result
#
#
# print(func_executor(
#  (make_upper, ("Python", "softUni")),
#  (make_lower, ("PyThOn",)),
# ))

# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor(
#  (sum_numbers, (1, 2)),
#  (multiply_numbers, (2, 4))
# ))