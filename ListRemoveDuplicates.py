# take a list and return a new list that contains all the elements of the first list minus all the duplicates

# with function
def remove_duplicates(list):
    temp = []
    for i in list:
        if i not in temp:
            temp.append(i)
    return temp


a = [1, 2, 3, 4, 4, 4, 4, 5, 6]
print(remove_duplicates(a))


# use set
A = set(a)
print(list(A))
