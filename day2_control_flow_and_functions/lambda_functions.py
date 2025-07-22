# lambda arguments : expression

#ex1 add two numbers
add = lambda x,y: x + y
print(add(2,3))

#ex2 square of a number
square = lambda x: x ** 2
print(square(4))

#ex3 using with map()
numbers = [1,2,3,4]
squares = list(map(lambda x: x**2, numbers))
print(squares) # Output: [1, 4, 9, 16]

#ex4 Using with filter()
nums = [1,2,3,4,5,6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

#ex5 Using with sorted()
students = [("Anshul", 88), ("Riya", 95), ("Karan", 75)]
sorted_students = sorted(students, key=lambda x : x[1])
print(sorted_students)