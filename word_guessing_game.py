import random

# Ask the user's name and greet them
name = input("What is your name? ")
print("Good Luck!", name)

# List of possible words to guess
words = [
    'rainbow', 'computer', 'science', 'programming',
    'python', 'mathematics', 'player', 'condition',
    'reverse', 'water', 'board', 'geeks'
]

# Randomly select a word
word = random.choice(words)

print("Guess the characters of the word.")

# Initialize variables
guesses = ''
turns = 12

# Game loop
while turns > 0:
    failed = 0

    # Display word with guessed letters and underscores
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    # Check if player has won
    if failed == 0:
        print("You Win!")
        print("The word is:", word)
        break

    # Get user's next guess
    guess = input("Guess a character: ").lower()

    # Add guess to the guesses string
    guesses += guess

    # Handle incorrect guess
    if guess not in word:
        turns -= 1
        print("Wrong guess.")
        print("You have", turns, "more guesses.")

        if turns == 0:
            print("You Lose!")
            print("The word was:", word)
