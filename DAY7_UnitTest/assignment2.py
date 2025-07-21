
def Prime(num):
    if num <= 1:
        return f'{num} is not a prime number'
    elif num == 2:
        return '2 is a prime number' 
    elif num % 2 == 0:
        return f'{num} is not a prime number'
    else:
        for i in range(3, int(num ** 0.5)+1, 2):
            if num % i == 0:
                return f'{num} is not a prime number'
                
        return f'{num} is a prime number'      


# print(Prime(1))   # 1 is not a prime number
# print(Prime(2))   # 2 is a prime number
# print(Prime(11))  # 11 is a prime number
# print(Prime(9))   # 9 is not a prime number        