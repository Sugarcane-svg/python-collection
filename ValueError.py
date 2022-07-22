# use try/except to catch the Value Error Exception




import random


number = random.randint(1, 9)
number_of_guesses = 0


try:
    while True:
        guess = int(input("Guess a number between 1 and 9: "))
        number_of_guesses += 1
        if guess == number:
            break
    print(f"You needed {number_of_guesses} guesses to guess the number {number}")
except ValueError:
    print("input other than integer is not accepted")


