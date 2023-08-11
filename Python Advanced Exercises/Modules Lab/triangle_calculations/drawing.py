def triangle_area(height):
    for i in range(1, height * 2):
        if i <= height:
            print(" ".join(str(x) for x in range(1, i + 1)))
        else:
            print(" ".join(str(x) for x in range(1, height * 2 - i + 1)))
