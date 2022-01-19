# implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function

def get_max(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

if __name__ == '__main__':
    a,b,c = 1, 1, 1
    print(get_max(a,b,c))