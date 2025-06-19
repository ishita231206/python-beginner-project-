import random

print("Welcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == number_to_guess:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess < number_to_guess:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
