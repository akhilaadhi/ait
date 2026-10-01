# Tic Tac Toe using Mini-Max Algorithm

import math

# Display the board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()


# Check if a player has won
def check_winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Check whether the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)


# Mini-Max algorithm
def minimax(board, is_maximizing):

    # AI wins
    if check_winner(board, "O"):
        return 1

    # Human wins
    if check_winner(board, "X"):
        return -1

    # Draw
    if is_full(board):
        return 0

    # Maximizing player - AI
    if is_maximizing:
        best_score = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"

                    score = minimax(board, False)

                    board[i][j] = " "

                    best_score = max(best_score, score)

        return best_score

    # Minimizing player - Human
    else:
        best_score = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"

                    score = minimax(board, True)

                    board[i][j] = " "

                    best_score = min(best_score, score)

        return best_score


# Find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"

                score = minimax(board, False)

                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move


# Main game
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("TIC TAC TOE")
print("You = X   Computer = O")

while True:

    print_board(board)

    # Human move
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1

    if board[row][col] != " ":
        print("Position already occupied!")
        continue

    board[row][col] = "X"

    if check_winner(board, "X"):
        print_board(board)
        print("You Win!")
        break

    if is_full(board):
        print_board(board)
        print("Game Draw!")
        break

    # Computer move
    move = best_move(board)

    board[move[0]][move[1]] = "O"

    print("Computer played:", move[0] + 1, move[1] + 1)

    if check_winner(board, "O"):
        print_board(board)
        print("Computer Wins!")
        break

    if is_full(board):
        print_board(board)
        print("Game Draw!")
        break