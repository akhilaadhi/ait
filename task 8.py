# N-Queens Problem using Backtracking
# 4 Queens Problem

N = 4
board = [-1] * N


def is_safe(row, col):
    for i in range(row):
        # Same column
        if board[i] == col:
            return False

        # Same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            # Backtracking
            board[row] = -1

    return False


# Solve the problem
if solve(0):
    print("Solution for 4-Queens Problem:\n")

    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists.")