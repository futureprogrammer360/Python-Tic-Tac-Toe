import os
import time

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
won = False
turns = 9
input_to_index = {
    "1": (0, 0), "2": (0, 1), "3": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "7": (2, 0), "8": (2, 1), "9": (2, 2)
}

def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("-----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("-----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

def get_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != " ":
                return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != " ":
                return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        if board[1][1] != " ":
            return board[1][1]

while not won and turns > 0:
    if turns % 2 == 1:
        mark = "X"
    else:
        mark = "O"

    os.system("cls")
    print_board(board)

    user_input = input(f"Player {mark}: ")
    row, col = input_to_index[user_input]

    if board[row][col] == " ":
        board[row][col] = mark
        turns -= 1
    else:
        print("Square already occupied. Please try again.")
        time.sleep(1)

    if get_winner(board):
        os.system("cls")
        print_board(board)
        won = True
        print(f"Congratulations, player {get_winner(board)}! You won!")
