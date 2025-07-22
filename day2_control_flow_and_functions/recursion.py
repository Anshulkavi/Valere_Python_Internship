# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)

# n = 0

# def python():
#     global n
#     n = n + 1
#     print("Python")
#     python()
    
# python()    

'''
0! = 1
1! = 1 * 0! = 1
2! = 2 * 1! = 2
.
4! = 4 * 3! = 24
'''

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))    

result = factorial(5)
print(result)        