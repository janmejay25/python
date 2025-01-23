def printboard():
    print("  1 2 3")
    for i in range(3):
        print(i+1, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()
def checkwin():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False
def checkdraw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True
def play():
    player = "X"
    while True:
        printboard()
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if board[row-1][col-1] == " ":
            board[row-1][col-1] = player
            if checkwin():
                printboard()
                print(player + " wins!")
                break
            if checkdraw():
                printboard()
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move! Try again.")
board = [[" "]*3 for i in range(3)]
play()
# Output: