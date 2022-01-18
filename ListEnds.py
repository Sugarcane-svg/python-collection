# takes a list of numbers and makes a new list of only the first and last elements if the given list

# generate a list
import numpy as np
np.random.seed(100)
a = np.random.randint(0, 1000, 50)
print(a)


def get_first_last(arr):
    return list([arr[0], arr[-1]])


print(get_first_last(a))
