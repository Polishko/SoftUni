# with trial division method applied:

from math import sqrt
from collections import deque

def get_primes(my_list):
    my_deck = deque(my_list)

    while my_deck:
        num = my_deck.popleft()

        if num <= 1:
            continue

        if len([n for n in range(2, int(sqrt(num)) + 1) if num % n == 0]) >= 1:
            continue

        yield num
        
# def get_primes(my_list):
#     idx = 0

#     while idx < len(my_list):
#         num = my_list[idx]

#         if len([n for n in range(1, num + 1) if num % n == 0]) > 2 or num <= 1:
#             idx += 1
#             continue

#         idx += 1
#         yield num
