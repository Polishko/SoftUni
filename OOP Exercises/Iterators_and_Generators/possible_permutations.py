# with recursion

def possible_permutations(my_lst):
    if len(my_lst) == 0:
        yield []

    else:
        for i in range(len(my_lst)):
            for permutation in possible_permutations(my_lst[:i] + my_lst[i + 1:]):
                yield [my_lst[i]] + permutation

# using permutations from library

from itertools import permutations

def possible_permutations(my_lst):
    for permutation in list(permutations(my_list)):
        yield permutation
