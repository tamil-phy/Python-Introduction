import random

def play_game():
    moves = ['rock','paper','scissors']
    player_move = input("Choose rock, paper, or scissors: ")
    computer_move = random.choice(moves)
    print(f"Computer chooses {computer_move}")
    if player_move == computer_move:
        print("Tie !")
        return None
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'paper' and computer_move == 'rock') or \
         (player_move == 'scissors' and computer_move == 'paper' ): 
         print("You Win!")
         return "player"
    else:
        print("Computer Wins !")
        return 'computer'