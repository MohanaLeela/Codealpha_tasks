import random

# List of predefined words
words = ["python", "apple", "tiger", "hello", "train"]

# Select a random word
secret_word = random.choice(words)

# Initialize variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

print("Guess the hidden word!")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the word with guessed letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Attempts remaining:", max_attempts - incorrect_guesses)

    # Check whether the word is completely guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word!")
        print("The word was:", secret_word)
        break

    # Get user input
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter. Try again!\n")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")

else:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")