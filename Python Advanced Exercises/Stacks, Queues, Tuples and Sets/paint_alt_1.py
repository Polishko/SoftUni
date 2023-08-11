from collections import deque


def is_item_pair_color(item, color_list):
    for color_element in color_list:
        if item[0] + item[1] == color_element or item[1] + item[0] == color_element:
            return color_element
    return False


def add_to_sub_color_sets(color_element, combination_sets):
    if color_element == "red":
        combination_sets["orange"].append("red")
        combination_sets["purple"].append("red")
    elif color_element == "yellow":
        combination_sets["green"].append("yellow")
        combination_sets["orange"].append("yellow")
    elif color_element == "blue":
        combination_sets["purple"].append("blue")
        combination_sets["green"].append("blue")


def check_color_combination(color_element, combination_sets):
    if color_element in combination_sets:
        if len(combination_sets[color_element]) != 2:
            return False
    return True


strings = deque(input().split())

colors = ["yellow", "blue", "red", "green", "purple", "orange"]
sub_color_sets = {"orange": [], "green": [], "purple": []}

colors_found = []
while strings:
    if len(strings) == 1:
        color = strings.pop()

        if color in colors:
            colors_found.append(color)
            add_to_sub_color_sets(color, sub_color_sets)
        break

    n = len(strings) // 2
    part_1 = deque(strings[:n])
    part_2 = deque(strings[n:])

    ele_1 = part_1.popleft()
    ele_2 = part_2.pop()
    result = (ele_1, ele_2)

    color = is_item_pair_color(result, colors)
    if color:
        colors_found.append(color)
        add_to_sub_color_sets(color, sub_color_sets)

    else:
        ele_1 = ele_1[:-1]
        ele_2 = ele_2[:-1]

        if ele_1:
            part_1.append(ele_1)
        if ele_2:
            part_2.appendleft(ele_2)

    strings = list(part_1 + part_2)

to_print = []
for color in colors_found:
    if check_color_combination(color, sub_color_sets):
        to_print.append(color)

print(to_print)
