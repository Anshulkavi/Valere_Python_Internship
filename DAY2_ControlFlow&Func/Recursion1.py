# n = int(input("nter a number: "))
'''
#Factorial of N
n = int(input("Enter a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)    

result = factorial(n)
print(f'factorial of {n} is:', result)

#Fibonacci

def Fibonacci(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    return Fibonacci(n-1)+ Fibonacci(n-2)

for i in range(10):
    res = Fibonacci(i)
    print(res)

'''

#sum_of_digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 +    