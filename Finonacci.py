# ask the user how many Fibonnaci numbers to generate and then generates them.

def generate_fibonnaci(num):

    base1 = 0
    base2 = 1
    temp = [base2]
    for i in range(num-1):
        sum = base1+base2
        temp.append(sum)
        base1 = base2
        base2 = sum

    return temp


user_input = int(input('how many Fibonnaci number you want to see? '))

print(generate_fibonnaci(user_input))
