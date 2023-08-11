from math import sqrt, floor

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())


def line_length(n_1, m_1, n_2, m_2, n_3, m_3, n_4, m_4):

    result = 0

    a = abs(n_1 - n_2)
    b = abs(m_1 - m_2)
    c = abs(n_3 - n_4)
    d = abs(m_3 - m_4)

    line_1_length = sqrt(a ** 2 + b ** 2)
    line_2_length = sqrt(c ** 2 + d ** 2)

    point_dist_1 = sqrt(n_1 ** 2 + m_1 ** 2)
    point_dist_2 = sqrt(n_2 ** 2 + m_2 ** 2)
    point_dist_3 = sqrt(n_3 ** 2 + m_3 ** 2)
    point_dist_4 = sqrt(n_4 ** 2 + m_4 ** 2)

    if line_1_length >= line_2_length:
        if point_dist_1 <= point_dist_2:
            result = f"({floor(n_1)}, {floor(m_1)})({floor(n_2)}, {floor(m_2)})"
        else:
            result = f"({floor(n_2)}, {floor(m_2)})({floor(n_1)}, {floor(m_1)})"
    else:
        if point_dist_3 <= point_dist_4:
            result = f"({floor(n_3)}, {floor(m_3)})({floor(n_4)}, {floor(m_4)})"
        else:
            result = f"({floor(n_4)}, {floor(m_4)})({floor(n_3)}, {floor(m_3)})"

    print(result)


line_length(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)
