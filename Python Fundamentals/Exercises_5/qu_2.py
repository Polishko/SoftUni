def find_next_version(a):

    a[2] += 1

    if a[2] > 9:
        a[2] = 0
        a[1] += 1

    if a[1] > 9:
        a[1] = 0
        a[0] += 1

    return a


current_version_lst = [int(num) for num in input().split(".")]
next_version = find_next_version(current_version_lst)
next_version_formatted = list(map(lambda ele: str(ele), next_version))
print(".".join(next_version_formatted))
