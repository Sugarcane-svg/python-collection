# be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers and symbols. The passwords should be random, generating a new passwords every time the user asks for a new passwords. Include your run-time code in a main method.
import random


letter_and_number = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'


def generate_passwords(type, digits):
    str = ''
    if type == 'new':
        for i in range(digits):
            str = str + random.choice(letter_and_number)
    elif type == 'digit':
        for i in range(digits):
            str = str + random.choice(numbers)
    elif type == 'letter':
        for i in range(digits):
            str = str + random.choice(letters)
    else:
        return 'you enter a wrong type'

    return str


input_digits = int(input('for your password, how long would you like? '))
input_type = input(
    'if you like combination of letters and numbers, enter "new", if you want only numbers, enter "digit", if you want only letters, enter "letter". Your choice: ')

print('your password is %s ' % generate_passwords(input_type, input_digits))
