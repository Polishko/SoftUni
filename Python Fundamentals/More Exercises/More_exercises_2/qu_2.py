num = int(input())
is_prime_number = True

if num == 1 or num == 0:
    is_prime_number = False
else:
    for divide_num in range(2, num + 1):
        if num % divide_num == 0 and divide_num != num:
            is_prime_number = False
            break

print(is_prime_number)
