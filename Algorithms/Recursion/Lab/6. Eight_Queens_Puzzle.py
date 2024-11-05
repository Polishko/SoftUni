def print_board(board):
    [print(' '.join(row)) for row in board]

def can_place_queen(row, column, rows, columns, left_diagonals, right_diagonal):
    if row in rows:
        return False
    if column in columns:
        return False
    if (row + column) in right_diagonal:
        return False
    if (row - column) in left_diagonals:
        return False
    return True

def set_queen(row, column, board, rows, columns, left_diagonals, right_diagonals):
    board[row][column] = '*'
    rows.add(row)
    columns.add(column)
    left_diagonals.add(row - column)
    right_diagonals.add(row + column)

def remove_queen(row, column, board, rows, columns, left_diagonals, right_diagonals):
    board[row][column] = '-'
    rows.remove(row)
    columns.remove(column)
    left_diagonals.remove(row - column)
    right_diagonals.remove(row + column)


def put_queens(row, board, rows, columns, left_diagonals, right_diagonals):
    if row == 8:
        print_board(board)
        print()
        return

    for column in range(8):
        if can_place_queen(row, column, rows, columns, left_diagonals, right_diagonals):
            set_queen(row, column, board, rows, columns, left_diagonals, right_diagonals)
            put_queens(row + 1, board, rows, columns, left_diagonals, right_diagonals)
            remove_queen(row, column, board, rows, columns, left_diagonals, right_diagonals)


board = list(['-'] * 8 for x in range(8))
put_queens(0, board, set(), set(), set(), set())
