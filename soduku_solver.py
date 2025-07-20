def solver(board,row ,col):
    if row == len(board):
        return True
    next_row = row 
    next_col = col + 1
    if next_col == len(board):
        next_row += 1
        next_col = 0
    if board[row][col] != 0:
        return solver(board, next_row, next_col)
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solver(board, next_row, next_col):
                return True
            board[row][col] = 0
def is_valid(board, row, col, num):
    for i in range(len(board)):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True


def print_board(board):
    for row in board:
        print(row)

# Example usage:
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solver(board, 0, 0):
    print_board(board)
else:
    print("No solution exists")