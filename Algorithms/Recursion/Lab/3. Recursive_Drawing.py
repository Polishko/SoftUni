# initial solution
# def draw_stars(n, result):
#
#     def draw_tags(m, result):
#         if m == counter + 1:
#             return result
#
#         result += '#' * m + '\n'
#         return draw_tags(m + 1, result)
#
#     if n == 0:
#         return draw_tags(1, result)
#
#     result  += '*' * n + '\n'
#     return draw_stars(n-1, result)
#
# counter = int(input('Enter a number: '))
# num = counter
#
# print(draw_stars(num, ''))

# Lecturer's solution
def draw_stars(n):
    if n == 0:
        return

    print('*' * n)
    draw_stars(n-1)
    print('#' * n)

draw_stars(int(input('Enter a number: ')))
