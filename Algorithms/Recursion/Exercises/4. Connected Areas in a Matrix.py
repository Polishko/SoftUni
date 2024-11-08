# Lecturer`s solution
# class Area:
#     def __init__(self, row, col, size):
#         self.row = row
#         self.col = col
#         self.size = size
#
#
# def explore_area(row, col, matrix):
#     if row < 0 or col < 0 or row >= rows or col >= cols:
#         return 0
#     if matrix[row][col] != '-':
#         return 0
#
#     matrix[row][col] = 'v'
#
#     result = 1
#     result += explore_area(row, col + 1, matrix)
#     result += explore_area(row + 1, col, matrix)
#     result += explore_area(row, col - 1, matrix)
#     result += explore_area(row - 1, col, matrix)
#
#     return result
#
#
# rows = int(input())
# cols = int(input())
#
# matrix = []
# for i in range(rows):
#     matrix.append(list(input()))
#
# areas = []
# for row in range(rows):
#     for col in range(cols):
#         size = explore_area(row, col, matrix)
#         if size == 0:
#             continue
#         areas.append(Area(row, col, size))
#
#
# print(f'Total areas found: {len(areas)}')
#
# for i, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
#     print(f'Area #{i + 1} at ({area.row}, {area.col}), size: {area.size}')


def connected_areas(row, col, matrix, areas, area_collection):

        if row < 0 or col < 0 or row >= rows or col >= cols:
            return

        if matrix[row][col] == '*':
            return
        if matrix[row][col] == 'v':
            return

        areas['size'] += 1
        matrix[row][col] = 'v'

        connected_areas(row, col + 1, matrix, areas, area_collection)
        connected_areas(row + 1, col, matrix, areas, area_collection)
        connected_areas(row, col - 1, matrix, areas, area_collection)
        connected_areas(row - 1, col, matrix, areas, area_collection)


def area_search(rows, cols, matrix, area_collection):
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '-':
                areas = {'coordinates': (r, c), 'size': 0}
                connected_areas(r, c, matrix, areas, area_collection)
                area_collection.append(areas)


    print(f'Total areas found: {len(area_collection)}')
    sorted_areas = sorted(area_collection, key=lambda area: (-area['size'], area['coordinates']))
    for i, area in enumerate(sorted_areas, 1):
        print(f"Area #{i} at {area['coordinates']}, size: {area['size']}")


rows = int(input())
cols = int(input())
matrix = [list(input()) for row in range(rows)]

area_collection = []
area_search(rows, cols, matrix, area_collection)
