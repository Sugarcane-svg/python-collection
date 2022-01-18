
filename = ['prime_under_1000.txt', 'happy_number_1000.txt']
prime = []
happy = []
for i in filename:

    with open(i, 'r') as file:
        if i == 'prime_under_1000.txt':
            prime.append(i)
        else:
            happy.append(i)


def overlap(list1:list, list2:list):
    temp = [i for i in list1 if i in list2]
    return temp


print(overlap(prime, happy))