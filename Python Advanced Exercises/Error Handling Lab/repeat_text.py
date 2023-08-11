try:
    text = input()
    repeat = int(input())
    print(text * repeat)
except ValueError:
    print("Variable times must be an integer")
