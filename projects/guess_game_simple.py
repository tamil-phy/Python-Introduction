import random

secret_number = random.randint(1, 100) # Generate random number between 1 and 100
tries = 0

print("Guess the number between 1 and 100!")

while tries < 5:
    guess = int(input("Enter your guess: "))
    tries += 1

    higher = guess > secret_number
    lower = guess < secret_number

    message = "Your guess is "
    message += "higher" if higher else "lower" if lower else "correct!"

    print(message)

    if guess == secret_number:
        print("Congratulations, you won!")
        break

if tries == 5:
    print("Sorry, you lost. The secret number was", secret_number)

