# ask user for a string and print out whether this string is a palindrome or not. (a lalindorme is a string that reads the same forwards and backwards)

user_input = input('Enter a string: ')

def ispalindrome(user_input):
    temp = user_input[::-1]
    return temp == user_input

print(ispalindrome(user_input))