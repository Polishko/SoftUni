def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for _ in range(n - 2):
        length = len(triangle[-1])
        line = [1] + [triangle[-1][i] + triangle[-1][i + 1] for i in range(length - 1)] + [1]
        triangle.append(line)

    return triangle

