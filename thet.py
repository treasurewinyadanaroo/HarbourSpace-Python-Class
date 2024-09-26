import os
def play_game(best_of_n):
    choices = ['rock', 'paper', 'scissors']
    player1_score = 0
    player2_score = 0
    
    
    rounds_needed_to_win = (best_of_n // 2) + 1
    
    round_number = 1
    while player1_score < rounds_needed_to_win and player2_score < rounds_needed_to_win:
        print(f"\nRound {round_number}:")
        
        
        player1_choice = input("Player 1, enter rock, paper, or scissors: ").lower()
        
        if player1_choice not in choices:
            print("Invalid choice for Player 1! Please enter rock, paper, or scissors.")
            continue
        
        os.system("cls")
        player2_choice = input("Player 2, enter rock, paper, or scissors: ").lower()
        
        if player2_choice not in choices:
            print("Invalid choice for Player 2! Please enter rock, paper, or scissors.")
            continue
        
        
        if player1_choice == player2_choice:
            print("It's a tie this round!")
        elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
             (player1_choice == 'scissors' and player2_choice == 'paper') or \
             (player1_choice == 'paper' and player2_choice == 'rock'):
            print("Player 1 wins this round!")
            player1_score += 1
        else:
            print("Player 2 wins this round!")
            player2_score += 1

        round_number += 1

    
    print("\nFinal Score:")
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")
    
    if player1_score > player2_score:
        print("Player 1 is the overall winner!")
    else:
        print("Player 2 is the overall winner!")


best_of_n = int(input("Enter the total number of rounds (Best of N): "))
play_game(best_of_n)