import random

# List of words
word_list = [
    "algorithm", "function", "variable", "compile",
    "iterate", "recursion", "binary", "array",
    "syntax", "pointer"
]

def display_hangman(pointer_pos):
    print("HANGMAN")
    print(" " * pointer_pos + "^")

def play_game():
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 0
    max_attempts = len("HANGMAN") - 1
    word_display = ["_"] * len(word)

    print("Welcome to Hangman!")
    display_hangman(attempts)
    print(" ".join(word_display))

    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print("Wrong guess!")
            attempts += 1

        # Display the current status
        display_hangman(attempts)
        print(" ".join(word_display))

        # Check if the player has guessed the word
        if "_" not in word_display:
            print(f"Congratulations! You guessed the word: '{word}'")
            print("Phew... you are saved.")
            return

    # Game over
    print("You are hanged.")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
