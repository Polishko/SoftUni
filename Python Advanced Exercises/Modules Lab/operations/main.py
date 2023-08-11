from operations.math_calculations import operation

user_input = input().split(" ")
print(f"{operation(*user_input):.2f}")
