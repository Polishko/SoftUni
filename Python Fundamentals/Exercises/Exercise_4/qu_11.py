int_num = int(input())


def loading_bar(a):
    count_percentile = a // 10
    count_dots = 10 - count_percentile
    percentile = "%"
    dot = "."

    if a == 100:
        return f"{a}% Complete!\n[{count_percentile * percentile}]"
    else:
        return f"{a}% [{count_percentile * percentile}{count_dots * dot}]\nStill loading..."


print(loading_bar(int_num))
