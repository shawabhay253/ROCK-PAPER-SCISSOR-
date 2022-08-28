# Rock Paper n Scissors

player1 = input("Enter player 1's choice: ")
player2 = input("Enter player 2's choice: ")

if ((player1 == 'rock' and player2 == 'scissors') 
    or (player1 == 'scissors' and player2 == 'paper') 
    or (player1 == 'paper' and player2 == 'rock')):
    print("Player 1 wins")
elif ((player2 == 'rock' and player1 == 'scissors') 
    or (player2 == 'scissors' and player1 == 'paper') 
    or (player2 == 'paper' and player1 == 'rock')):
    print("Player 2 wins")
elif player1 == player2:
    print("It's a tie")
else:
    print("Something went wromg")
