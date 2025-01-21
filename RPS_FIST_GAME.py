while True:
    player1 = input("P1 enter choice:(rock,paper,scissor) ")
    player2 = input("P2 enter choice:(rock,paper,scissor) ")
    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock" and player2 == "scissor" or player1 == "paper" and player2 == "rock" or player1 == "scissor" and player2 == "paper":
            print("Player1 wins!")
    elif player2 == "rock" and player1 == "scissor" or player2 == "paper" and player1 == "rock" or player2 == "scissor" and player1 == "paper":
        print("Player2 wins!")
    else:
        print("Invalid input! You have not entered rock, paper or scissor, try again.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "no":
        print("thank you for playing")
        break