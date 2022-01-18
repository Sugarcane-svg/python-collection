# write one line of python that takes this list and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([i for i in a if i % 2 == 0])