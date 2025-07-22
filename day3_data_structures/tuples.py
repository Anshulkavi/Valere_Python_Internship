''' 
What is a Tuple?
A tuple is:

Ordered

Immutable (cannot be changed after creation)

Can contain duplicate values

Written using parentheses ( )
'''

# Creating Tuples
t1 = (1, 2, 3)
t2 = ("apple",) #  For a single-element tuple, use a comma:
t3 = tuple([4,5,6])  # using tuple() function

#Accessing Elements
t = (10, 20, 30)
print(t[1]) #20
print(t[2]) #30

# Tuple Unpacking
person = ("Anshul", 21)
name, age = person
print(name) #Anshul
print(age) #21

# Tuple Methods
t = (1,2,2,3)
print(t.count(2)) #2
print(t.index(3)) #3

# Tuple with Loops
fruits = ("apple", "banana", "cherry", "grapes")
for  fruit in fruits:
    print(fruit)

# Named Tuples
from collections import namedtuple

# Define a named tuple type
student = namedtuple("Student", ["name", "age", "grade"])

#Create a student
s1 = student("Anshul", 21, "A")

print(s1.name)
print(s1.age)
print(s1.grade)

# Returning Multiple Values from a function
def get_user():
    name = "anshul"
    age = 21
    return name, age # returns a tuple

n, a = get_user()
print(n, a)