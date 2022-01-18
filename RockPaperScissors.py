# make a rock-paper-scissor game(Hint: ask for player plays, compare them, print out a message of congratulations to the winnier, and ask if the players want to start a new game)

from os import replace
import numpy as np
promt = input(
    'play rock-paper-scissor with computer or other player? computer press 1, other player press 2: ')

options = ['rock', 'paper', 'scissor']


def play_game(input1, input2):
    if input1 == 'rock' and input2 == 'scissor':
        return 'you win'
    elif input1 == 'scissor' and input2 == 'papper':
        return 'you win'
    elif input1 == 'papper' and input2 == 'papper':
        return 'you win'
    elif input1 == input2:
        return 'even'
    elif input1 or input2 not in options:
        return "enter a correct option"
    else:
        return 'you lose'


if promt == '1':
    userinput = input("enter yours in lower case: ")
    computer = np.random.choice(options, size = 1, replace = True)
    print(play_game(userinput, computer))
elif promt == '2':
    player1 = input('enter option for you: ')
    player2 = input('enter option for the other: ')
    print(play_game(player1, player2))
else:
    print('you must enter a correct number to start a game')
