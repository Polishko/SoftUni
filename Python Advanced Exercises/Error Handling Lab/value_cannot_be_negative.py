
class ValueCannotBeNegative(Exception):
    """Number is below zero"""


for i in range(5):
    num = int(input())

    if num < 0:
        raise ValueCannotBeNegative
