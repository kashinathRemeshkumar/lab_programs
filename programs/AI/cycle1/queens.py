def attack(i, j):
    # Check for queens in the same row or column
    for k in range(n):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # Check for queens in the diagonals
    for k in range(n):
        for l in range(n):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def n_queens(n):
    if n == 0:
        return True
    for i in range(len(board)):
        for j in range(len(board)):
            if (not attack(i, j)) and (board[i][j] != 1):
                board[i][j] = 1
                if n_queens(n - 1):
                    return True
                board[i][j] = 0
    return False

print("Enter the number of queens:")
n = int(input())
board = [[0] * n for _ in range(n)]
if n_queens(n):
    for row in board:
        print(row)
else:
    print("No solution found")
