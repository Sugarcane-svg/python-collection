# generate a random number between 1 and 9(including 1 and 9). ask the user to guess the number, then tell the, whether they guessed too low, too high, or exactly right.

import numpy as np

number = np.random.randint(1, 10, size=1)

user_input = int(
    input('guess what number is generated from 1 to 9 inclusive? type "exit" to quit. '))

n = 1
while user_input != 'exit':
    if number > user_input:
        print('too low')
    elif number < user_input:
        print('too high')
    else:
        print("congras, you've tried %d times and get it right." % n)
        break

    
    user_input = int(
        input('guess what number is generated from 1 to 9 inclusive? '))
    n+=1

print('game finished.')
