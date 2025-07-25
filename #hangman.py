import random

# Word pool
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split()

# Randomly choose a word
word = random.choice(someWords)

# Game starts here
if __name__ == '__main__':
    print('Guess the word! Hint: it is a fruit name.')
    print('_ ' * len(word))  # Hide the word

    playing = True
    guessed_letters = ''
    chances = len(word) + 2
    flag = 0

    while chances > 0 and flag == 0:
        guess = input('\nEnter a letter to guess: ').lower()

        # Input validations
        if not guess.isalpha():
            print('Enter letters only.')
            continue
        elif len(guess) > 1:
            print('Enter only a single letter.')
            continue
        elif guess in guessed_letters:
            print('You already guessed that letter.')
            continue

        # Add guess to guessed_letters
        guessed_letters += guess

        if guess in word:
            print("Nice! You guessed correctly.")
        else:
            chances -= 1
            print("Wrong guess.")
            print("You have", chances, "chances left.")

        # Display current progress
        current_status = ''
        for char in word:
            if char in guessed_letters:
                current_status += char + ' '
            else:
                current_status += '_ '

        print("\n" + current_status)

        # Win condition
        if all(char in guessed_letters for char in word):
            print("Congratulations! You guessed the word:", word)
            flag = 1
            break

    if not flag:
        print("\nYou lost! The word was:", word)
