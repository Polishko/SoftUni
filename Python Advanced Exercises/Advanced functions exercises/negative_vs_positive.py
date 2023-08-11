# def negatives_vs_positives(args):
#     def sum_negatives():
#         negative_sum = sum(list(filter(lambda x: x < 0, args)))
#         return negative_sum
#
#     def sum_positives():
#         positive_sum = sum(list(filter(lambda x: x >= 0, args)))
#         return positive_sum
#
#     print(sum_negatives(), sum_positives(), sep="\n")
#
#     if abs(sum_negatives()) > abs(sum_positives()):
#         print("The negatives are stronger than the positives")
#     elif abs(sum_negatives()) < abs(sum_positives()):
#         print("The positives are stronger than the negatives")
#
#
# nums = [int(num) for num in input().split()]
# negatives_vs_positives(nums)


# def negatives_vs_positives(args):
#     negative_sum = sum(x for x in args if x < 0)
#     positive_sum = sum(x for x in args if x >= 0)
#
#     print(negative_sum, positive_sum, sep="\n")
#
#     if abs(negative_sum) > abs(positive_sum):
#         print("The negatives are stronger than the positives")
#     elif abs(negative_sum) < abs(positive_sum):
#         print("The positives are stronger than the negatives")
#
#
# nums = [int(num) for num in input().split()]
# negatives_vs_positives(nums)

# daha dogrusu

def negatives_vs_positives(negatives, positives):

    if abs(negative_sum) > abs(positive_sum):
        print("The negatives are stronger than the positives")
    elif abs(negative_sum) < abs(positive_sum):
        print("The positives are stronger than the negatives")


nums = [int(num) for num in input().split()]

negative_sum = sum(x for x in nums if x < 0)
positive_sum = sum(x for x in nums if x >= 0)

print(negative_sum, positive_sum, sep="\n")

negatives_vs_positives(negative_sum, positive_sum)