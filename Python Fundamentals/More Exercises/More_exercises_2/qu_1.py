int_1 = int(input())
int_2 = int(input())
print(f"Before:")
print(f"a = {int_1}")
print(f"b = {int_2}")

int_1 = int_1 + int_2
int_2 = int_1 - int_2
int_1 = int_1 - int_2
print(f"After:")
print(f"a = {int_1}")
print(f"b = {int_2}")
