def check_prime(num = 2):
    range_between = range(2, int(num**0.5)+1)
    temp = [i for i in range_between if num % i == 0]
    return len(temp) == 0

print(check_prime(7))