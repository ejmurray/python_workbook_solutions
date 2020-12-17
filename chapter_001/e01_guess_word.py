import random


def guessing_game():
    """Guessing game

    Write a function (guessing_game) that takes no arguments.
    When run, the function chooses a random word between 2 and 5 letters long.
    Then ask the user to guess what word has been chosen.
    Each time the user enters a guess, the program indicates one of the following:
    - Too early in the dictionary
    - Too late in the dictionary
    - Correct match
    If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
    The program only exits after the user guesses correctly.
    """


dict_words = sorted(["cream", "to", "tea", "fast", "panel", "an", "pasta", "pop"])
# print(dict_words)
random_guess = random.choice(dict_words)
# print(random_guess)
word_index = dict_words.index(random_guess)
# print(f"Word index: {word_index}")

while user_guess := input("Enter a word that has between 2 and 5 letters: "):
    if len(user_guess) > 6:
        print(f"The word '{user_guess}' is too long. Try again.")
    if user_guess not in dict_words:
        print(f"The word '{user_guess}' is not in the dictionary. Try again.")
    elif user_guess == random_guess:
        print(f"Just right! I had the word '{random_guess}' in mind.")
        break
    elif user_guess != random_guess:
        user_guess_index = dict_words.index(user_guess)
        if word_index > user_guess_index:
            print(
                f"The word '{user_guess}' is incorrect. Try something a bit after that in the dict."
            )
        else:
            print(
                f"The word '{user_guess}' is incorrect. Try something a bit before that in the dict."
            )
print("Finished!")
