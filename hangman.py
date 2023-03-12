import random


def get_word():  # Returns a random word from the pre-determined list of ten words.
    list_of_words = ['bubble', 'pillow', 'pineapple', 'garbage', 'anticipate',
                     'cards', 'caterpillar', 'console', 'toe', 'chicken']
    return random.choice(list_of_words)


def right_letters_list(word):  # Generates a list of blank spaces equal to the length of the word.
    right_letters = []
    for _ in range(len(word)):
        right_letters.append('_')
    return right_letters


def print_list_as_word(word):  # Takes a list and prints it out letter by letter. Used to print out correct and
    # incorrect guesses.
    for blank in word:
        print(blank, end=' ')
    print()


def make_str_from_list(right_letters):  # Takes a list and turns it into a str.
    # Used to compare the correct guesses to the word since the responses are put into a list.
    str_list = ''
    for letter in right_letters:
        str_list += letter
    return str_list


def game():

    # First, we're getting a random word and creating a list of blank spaces that we will later
    # modify to display the letters the player has guessed correctly.

    word = get_word()
    right_letters = right_letters_list(word)
    wrong_letters = []
    correct_guesses = 0
    incorrect_guesses = 0
    right_letters_str = None

    print(f'The number of letters in the word is {len(word)}')

    while right_letters_str != word:  # We will run this loop until the player figures out the word.
        guess = input('Guess a letter: ')

        if guess in word:
            for letter, index in zip(word, list(range(len(word)))): # Here we make a list of numbers
                # for the length of the word and zip it to the word in order to be able to compare the two
                # and modify the right_letters list at the correct index.
                if guess == letter:
                    right_letters[index] = letter
            correct_guesses += 1
            print_list_as_word(right_letters)

        else: # If the guess isn't in the letter, we update the wrong letter list and print it.
            print(f'{guess} is not in the word. Here are your incorrect guesses so far:')
            wrong_letters.append(guess)
            print_list_as_word(wrong_letters)
            print_list_as_word(right_letters)
            incorrect_guesses += 1

        guesses = correct_guesses + incorrect_guesses
        right_letters_str = make_str_from_list(right_letters) # We update the right_letters_str here so
        # it can be accurately compared in the while statement.
        
        if right_letters_str != word:
            print(f'You have made {guesses} guess(es). You made {correct_guesses} correct guess(es) '
                  f'and {incorrect_guesses} incorrect guess(es).')

    print(f'You guessed the word right! It was {word}. It took you {guesses} guesses.')


def main():
    print("Welcome to Hangman!")
    while True:
        game()
        response = input('Would you like to play again? (y/n): ')
        if response.lower() == 'y':
            continue
        else:
            print('Thanks for playing!')
            break


main()
