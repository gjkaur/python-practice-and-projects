import random

print("Welcome to the Number Guessing Game!")
low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

number_to_guess = random.randint(low, high)
attempts = 7
guess_count = 0

print(f"\nGuess the number between {low} and {high}. You have {attempts} attempts.\n")

while guess_count < attempts:
    guess = int(input(f"Attempt {guess_count + 1}: Enter your guess: "))
    guess_count += 1

    if guess == number_to_guess:
        print(f"Correct! The number was {number_to_guess}. You guessed it in {guess_count} attempts.")
        break
    elif guess < number_to_guess:
        print("Too low! Try a higher number.\n")
    else:
        print("Too high! Try a lower number.\n")

if guess != number_to_guess:
    print(f"Out of attempts! The number was {number_to_guess}. Better luck next time.")
