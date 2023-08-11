# num_users = int(input())
# users = set()
#
# for _ in range(num_users):
#     user = input()
#     users.add(user)
#
# for user in users:
#     print(user)
#
#

# num_users = int(input())
# users = set()
#
# for _ in range(num_users):
#     users.add(input())
#
# print(*users, sep="\n")

# Dilyan's solution
print(*{input() for _ in range(int(input()))}, sep="\n")
