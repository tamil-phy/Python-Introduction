import rock_paper_scissors

num_rounds = 3
player_score = 0
computer_score = 0

for i in range(num_rounds):
    winner = rock_paper_scissors.play_game()
    if winner == 'player':
        player_score += 1
    elif winner == 'computer':
         computer_score += 1


print(f'Player score: {player_score}')
print(f'Computer score: {computer_score}')
if player_score > computer_score:
    print('Player wins!')
elif player_score < computer_score:
    print('Computer wins!')
else:
    print('Tie!')
