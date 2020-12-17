import random


def guessing_game():
    """Guessing game

    Write a function (guessing_game) that takes no arguments.
    When run, the function chooses a random integer between 0 and 100 (inclusive).

    Not only should you choose a random number, but you should also choose a
    random number base, from 2 to 16, in which the user should submit their input.
    If the user inputs “10” as their guess, you’ll need to interpret it in the
    correct number base; “10” might mean 10 (decimal), or 2 (binary),
    or 16 (hexadecimal).

    Then ask the user to guess what number has been chosen.
    Each time the user enters a guess, the program indicates one of the following:
    - Too high
    - Too low
    - Just right
    If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
    The program only exits after the user guesses correctly.
    """


random_guess = random.randint(0, 100)
random_base = random.randint(2, 16)
print(random_guess)
print(random_base)
print(f"{random_guess**(1/random_base)}")

while user_guess := int(input("Enter a number. ")):
    if user_guess == random_guess:
        print(f"Just right! I had the number {random_guess} in mind.")
        break
    elif user_guess > random_guess:
        print(f"The number {user_guess} is too high! Try again.")
    else:
        print(f"The number {user_guess} is too low. Try again.")
print("Finished!")
