# write a function that takes an ordered list of numbers(a list where the elements are in order from smallest to largetest) and another number. The function decides whether or not the given numer is inside the list and returns an appropriate boolean.

def search(list:list, num):

    return num in list

a = [1,2,3,4,5,6]
print(search(a, 5))

def binary_search(list:list, num) -> bool:
    begin = 0
    end = len(list)-1
    
    while begin < end:

        mid = (begin+end)//2
        
        if num > list[mid]: 
            begin = mid
        elif num < list[mid]:
            end = mid
        else:
            return True

    return False


print(binary_search(a, 0))