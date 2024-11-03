
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
        print(f'Area #{i} at {area['coordinates']}, size: {area['size']}')


rows = int(input())
cols = int(input())
matrix = [list(input()) for row in range(rows)]

area_collection = []
area_search(rows, cols, matrix, area_collection)
