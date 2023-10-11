import os

logo = '''
___________.__         ___________                 __                 
\__    ___/|__| ____   \__    ___/____    ____   _/  |_  ____   ____  
  |    |   |  |/ ___\    |    |  \__  \ _/ ___\  \   __\/  _ \_/ __ \ 
  |    |   |  \  \___    |    |   / __ \\  \___   |  | (  <_> )  ___/ 
  |____|   |__|\___  >   |____|  (____  /\___  >  |__|  \____/ \___  >
                   \/                 \/     \/                    \/ 
'''


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

key = {
    "Player-1": "X",
    "Player-2": "0"
}


def print_board(board):
    print()
    for j in range(len(board)):
        for i in range(len(board[j])):
            if i < (len(board[j]) - 1):
                print(f" {board[j][i]} |", end="")
            else:
                print(f" {board[j][i]}")

        if j < (len(board) - 1):
            print("-----------")

    print()


def player_has_won(board, value):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == value:
                return True
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[i][0] == value:
                return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == value:
            return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[1][1] == value:
            return True
    else:
        return False


def board_is_full(board):
    for row in board:
        for item in row:
            if item == "X" or item == "0":
                pass
            else:
                return False

    return True


def game(player):
    if player_has_won(board, key["Player-1"]):
        print("Yaay Player-1 has won the match!!!")
        return
    elif player_has_won(board, key["Player-2"]):
        print("Yaay Player-2 has won the match!!!")
        return
    elif board_is_full(board):
        print("The match is drawn")
        return
    if player % 2 == 0:
        turn = 2
    else:
        turn = 1

    print(f"It is player-{turn}'s turn")
    row = int(input("Enter the row (1/2/3): "))
    col = int(input("Enter the column (1/2/3):"))

    if board[row - 1][col -1] == " ":
        board[row - 1][col - 1] = "X" if turn == 1 else "0"
    else:
        print("You are not allowed to overwrite, Please try again")
        game(player)


    print_board(board)

    game(player + 1)


os.system("cls")
print(logo)
print("Player-1: X")
print("Player-2: 0")
print_board(board)
game(1)