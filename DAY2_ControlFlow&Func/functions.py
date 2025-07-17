def str_add():
    str1 = "hello"
    str2 = " world"
    print(str1 + str2)

str_add()    

def add(a,b):
    print(a+b)
add(1,2)

#return function
def add1(a,b):
    c = a + b
    return c

ans = add1(10,20) # when ever using return() , printing needs a variable
print(ans)    

def mult(a,b):
    c = a * b
    return c

result = mult(2, 'Mike')
print(result)


#passing arguments to the functions
def add3(a):
    print(a + 1)

add3(2)    

def add2(X,Y):
    print(X + Y)

add2(4,5)

#passing functions as arguments
def add4(x,y):
    return x + y # 6 + 1 = 7
def square(z):
    return z * z # 7 * 7 = 49

result = square(add4(6,1))
print(result)

