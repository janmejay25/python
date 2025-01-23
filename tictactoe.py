def printboard():
    print("  1 2 3")
    for i in range(3):
        print(i+1, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        # This print() is used to print a newline character.
        print()
def checkwin():
    for i in range(3):
            #The reason the condition checks only board[i][0] != " " is because if board[i][0] is not empty and all three cells in the row are equal (board[i][0] == board[i][1] == board[i][2]), then it is guaranteed that board[i][1] and board[i][2] are also not empty.

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