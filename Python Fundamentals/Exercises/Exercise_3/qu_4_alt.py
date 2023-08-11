num_list = [int(num) for num in input().split(", ")]
beggar_count = int(input())

beggars = [0] * beggar_count

for idx in range(len(num_list)):
    beggar_idx = idx % beggar_count
    num = num_list[idx]
    beggars[beggar_idx] += num

print(beggars)
