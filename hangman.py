from random import choice

words = ["hope", "courage", "wisdom", "freedom", "justice", "kindness", "compassion", "integrity",
    "patience", "gratitude", "harmony", "creativity", "curiosity", "knowledge", "respect",
    "empathy", "loyalty", "honesty", "perseverance", "balance", "unity", "diversity",
    "growth", "purpose", "passion", "inspiration", "determination", "confidence", "trust"]

def run_game():
    word: str = choice(words)

    username: str = input('What is your name?  ')
    print(f'Welcome to hangman, {username}!')

    guessed: str = ''
    tries: int = 3

    # The game
    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()  # Add a blank line

        # If there are no blanks left, that means the user won the game!
        if blanks == 0:
            print('You got it!')
            break

        # Get user input
        guess: str = input('Enter a letter: ')

        # Check that the user isn't just guessing the same letter again
        if guess in guessed:
            print(f'You already used: "{guess}". Please try with another letter!')
            continue

        # Add the guess to the guessed string
        guessed += guess

        # Check that the guess is in the word
        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong... ({tries} tries remaining)')

            # Game-over if tries reaches 0
            if tries == 0:
                print('No more tries remaining... You lose.')
                break


if __name__ == '__main__':
    run_game()