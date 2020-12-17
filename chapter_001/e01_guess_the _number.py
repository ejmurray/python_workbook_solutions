import random


def guessing_game_number():
    """Guessing game

    Write a function (guessing_game) that takes no arguments.
    When run, the function chooses a random integer between 0 and 100 (inclusive).
    Then ask the user to guess what number has been chosen.
    Each time the user enters a guess, the program indicates one of the following:
    - Too high
    - Too low
    - Just right
    If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
    The program only exits after the user guesses correctly.
    """


random_guess = random.randint(0, 100)

while user_guess := int(input("Enter a number: ")):
    if user_guess == random_guess:
        print(f"Just right! I had the number {random_guess} in mind.")
        break
    elif user_guess > random_guess:
        print(f"The number {user_guess} is too high! Try again.")
    else:
        print(f"The number {user_guess} is too low. Try again.")
print("Finished!")
