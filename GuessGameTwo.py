import numpy as np

# the actual number from user
actual_number = int(input('pick a number from 0 to 100(include both end): '))

# computer make a initial guess
initial_guess = np.random.randint(0, 101)

# compare initial guess and actual number, if it does not match. make another guess between initial guess and one of ends.
start = 0
end = 100
n = 0
while True:

    if actual_number > initial_guess:
        n += 1
        print('%d too low' % initial_guess)
        start = initial_guess
        initial_guess = np.random.randint(start, end+1)
    elif actual_number < initial_guess:
        n += 1
        print('%d too high' % initial_guess)
        end = initial_guess
        initial_guess = np.random.randint(start, end)
    else:
        break


print('computer has made %d time to guess number %d correct' % (n, initial_guess))
