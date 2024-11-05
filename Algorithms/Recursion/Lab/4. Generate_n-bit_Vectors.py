def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for i in range(2):
        vector[idx] = i
        gen01(idx + 1, vector)

n = int(input())
vector = [0] * n
gen01(0, vector)
