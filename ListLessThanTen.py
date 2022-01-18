a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# prints out all elements of the list that are less than 5
for i in a:
    if i <= 5:
        print(i)
    else:
        break

# make a new list that has all the elements less than 5 from the list
temp1 = []
for i in a:
    if i <= 5:
        temp1.append(i)
    else:
        break
print('temp1: %s' % temp1)

# write this in one line
temp2 = [i for i in a if i <= 5]
print('temp2: %s' % temp2)


# ask user for a number and return a list that contains only elements from the original list that are smaller than that number given by the user
user = int(input('enter a upper bound number: '))
temp3 = [i for i in a if i <= user]
print('temp3: %s' % temp3)
