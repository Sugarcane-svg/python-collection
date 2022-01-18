# ask the user for a long string containing multiple words. print back to the user the same string with the words in backwards order.

def print_backwards(name):
    l = name.split()
    return l[::-1]


user_input = input('enter a long string: ')
print(' '.join(print_backwards(user_input)))
