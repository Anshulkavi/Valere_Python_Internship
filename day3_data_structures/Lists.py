'''
What is a List?
A list is:

Ordered (items maintain insertion order)

Mutable (you can change, add, or remove items)

Allows duplicates
'''

#fruits = ["apple", "banana", "cherry"] Initialized

#creating Lists
empty_list = []
numbers = [1,2,3,4]
mixed = ['apple', 10, True, 3.14]
chars = list("hello")     # ['h', 'e', 'l', 'l', 'o']
nums = list(range(5))     # [0, 1, 2, 3, 4]


#Accessing List Elements
fruits = ["apple", "banana", "cherry"]
#print(fruits[0]) #apple
#print(fruits[-1]) #cherry (last element)

#Updating and changing Elements
fruits[1] = "orange"
print(fruits) # ['apple', 'orange', 'cherry']

#reversing the list
print(list(reversed(fruits))) # by converting to list
print(fruits[::-1]) # by Slicing

#reverse at in-place
fruits.reverse()
print(fruits)
