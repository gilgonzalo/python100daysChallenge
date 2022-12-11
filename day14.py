# https://www.youtube.com/watch?v=5YP8QIpR1SQ
# day 14 - 2 player rock, paper, scissor

print("Rock (R), Papper (P), Scissors (S) Battle\n\n")

print("Select your move >")
player1=input("Player 1 > ")
print("\nSelect your move >")
player2=input("Player 2 > ")

print("\nResult of the match >\n")
if player1 == 'r' or player1 == 'R':
    if player2== 'r':
        print("\tThat's a tie!")    
    elif player2== 'p' or player2== 'P':
        print("Player 2 Papper will drown Player 1 Rock....\n\tPlayer 2, you're a winner baby")
    elif player2== 's' or player2== 'S':
        print("Player 1 Rock will smash Player 2 Scissors....\n\tPlayer 1, you're a winner baby")
    else :
        print("Player2 --> Incorrect option")
elif player1 == 'p' or player1 == 'P':
    if player2== 'r':
        print("Player 1 Papper will drown Player 2 Rock....\n\tPlayer 1, you're a winner baby")
    elif player2== 'p' or player2== 'P':
        print("\tThat's a tie!")    
    elif player2== 's' or player2== 'S':
        print("Player 2 Scissor will shatter Player 1 Papper....\n\tPlayer 2, you're a winner baby")
    else :
        print("Player2 --> Incorrect option")

elif player1 == 's' or player1 == 'S':
    if player2== 'r':
        print("Player 2 Rock will smash Player 1 Scissors....\n\tPlayer 2, you're a winner baby")
    elif player2== 'p' or player2== 'P':
        print("Player 1 Scissors will shatter Player 2 Papper....\n\tPlayer 1, you're a winner baby")
    elif player2== 's' or player2== 'S':
        print("\tThat's a tie!")    
    else :
        print("Player2 --> Incorrect option")
else:
    print("player1 --> Incorrect option")
