num = int(input())


def tribonacci_seq(a):

    result = None
    current_num = 0

    tribonacci_list = [1]

    for i in range(a):
        if 0 < i < 3:
            current_num = i
            tribonacci_list.append(current_num)
        if i >= 3:
            current_num = sum(tribonacci_list[i - 3:i])
            tribonacci_list.append(current_num)

    tribonacci_string = [str(ele) for ele in tribonacci_list]
    result = " ".join(tribonacci_string)
    print(result)


tribonacci_seq(num)
