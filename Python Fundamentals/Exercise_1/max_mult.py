divisor_num = int(input())
boundary_num = int(input())
current_max = 1

# for num in range(1, boundary_num + 1):
#     if num % divisor_num == 0:
#         if num >= current_max:  # gerek yok, kosula uyan son buyuk sayiyi store edip print et ya da tersten cyle yap
#             current_max = num
# print(current_max)

for num in range(boundary_num, 0, -1):
    if num % divisor_num == 0:
        print(num)
        break

