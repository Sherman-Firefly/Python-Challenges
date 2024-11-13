

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 9)

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
        
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-1] == player for i in range(3)]):
        return True
    return False

def draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X" 

    while True:
        row = int(input(f"{current_player}, enter a row (0,1,2)"))
        col = int(input(f"{current_player}, enter a column (0,1,2)"))

        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break

            if draw(board):
                print("Draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Spot taken. Pick another one")


tic_tac_toe()


