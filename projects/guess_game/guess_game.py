import random

def play_game():
    secret_num = random.randint(1, 100)
    num_guesses = 0
    while True:
        guess = int(input('Guess the secret number between 1 and 100: '))
        num_guesses += 1
        if guess == secret_num:
            print(f'Congratulations! You guessed the number in {num_guesses} guesses.')
            return num_guesses
        elif guess < secret_num:
            print('Too low. Try again.')
        else:
            print('Too high. Try again.')

