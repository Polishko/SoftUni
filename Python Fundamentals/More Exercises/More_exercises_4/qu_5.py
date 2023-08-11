num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def identify_mult_result(a, b, c):

    result = ""
    list_nums = [a, b, c]
    count_negative = 0
    zero_present = False
    negative_result = False

    for i in range(len(list_nums)):

        if list_nums[i] == 0:
            zero_present = True
            result = "zero"
            print(result)
            return
        elif list_nums[i] < 0:
            count_negative += 1

    if count_negative == 1 or count_negative == 3:
        negative_result = True
        result = "negative"
        print(result)
        return

    else:
        result = "positive"
        print(result)


identify_mult_result(num_1, num_2, num_3)
