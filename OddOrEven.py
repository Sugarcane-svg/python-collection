

def odd_or_even(user_input):
    return user_input % 2 == 1


def multiple_4(user_input):
    return user_input % 4 == 0


def two_nums(user_input1, user_input2):
    return (user_input1 * 1.0 / user_input2).is_integer()


def print_msg(user_input):
    if odd_or_even(user_input):
        print('%d is a odd number' % (user_input))
    else:
        print('%d is a even number' % (user_input))

    if multiple_4(user_input):
        print('%s is a multiple of 4' % (user_input))
    else:
        print('%s is not a multiple of 4' % (user_input))


def print_msg2(user_input1, user_input2):
    if two_nums(user_input1, user_input2):
        print('%d divides %d evenly' % (user_input1, user_input2))
    else:
        print('%d divides %d unevenly' % (user_input1, user_input2))


user_input = input(
    'you can either enter one number or two numbers, one number press 1, two number press 2: ')

if user_input == '1':
    one_number = int(input('Enter a number: '))
    print_msg(one_number)
else:
    two_number1 = int(input('Enter first number: '))
    two_number2 = int(input('Enter second number: '))
    print_msg2(two_number1, two_number2)


