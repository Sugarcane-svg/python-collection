# ask user fro a number then print out a list of all the dividors of that number. (example: 13 is a divisor of 26 because 26/13 has no remainder)

user = int(input('Enter a number: '))

x = range(2, user+1)
smallest_divisor = 0
for i in x:
    if user % i == 0:
        smallest_divisor = i
        break

del x 
x = range(int(smallest_divisor), int(user/smallest_divisor)+1)
temp = [i for i in x if user % i == 0]
temp.append(user)
print(temp)