board = [
    [0,0,2,0],
    [2,0,0,4],
    [1,0,0,3],
    [0,3, 0, 0],
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 5):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True;

            bo[row][col] = 0;

    return False


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        k = bo[pos[0]][i]
        if k == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        h = bo[i][pos[1]]
        if h == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 2
    box_y = pos[0] // 2

    for i in range(box_y * 2, box_y * 2 + 2):
        for j in range(box_x * 2, box_x * 2 + 2):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 2 == 0 and i != 0:
            print("---------")

        for j in range(len(bo[0])):
            if j % 2 == 0 and j != 0:
                print(" | ", end="")

            if j == 3:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col


print_board(board)
print(" ")
solve(board)
print(" ")
print_board(board)