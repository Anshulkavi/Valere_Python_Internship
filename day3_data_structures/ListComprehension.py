''' What is List Comprehension?
It’s a shorter way to write a for loop that builds a list. '''

# Using Loop
squares = []
for x in range(5):
    squares.append(x * x)
# print(squares)    

# Using List Comprehension
squares = [x * x for x in range(5)]
# print(squares)

# Basic Syntax : [expression for item in iterable]
twice =[x * 2 for x in [1, 2, 3]]  # [2, 4, 6]
# print(twice)

# With if condition:
#Syntax : [expression for item in iterable if condition]
# Get even Numbers
evens = [x for x in range(10) if x % 2 == 0]
# print(evens)

# With if-else Condition
odd_even= ['even' if x % 2 == 0 else 'odd' for x in range(5)]  # ['even', 'odd', 'even', 'odd', 'even']
# print(odd_even)

#EXAMPLES 
#  Square of each element:
nums = [1,2,3]
squares = [n**2 for n in nums]
# print(squares)

# Remove vowels from a string
text = 'hello'
no_vowels = [ch for ch in text if ch not in 'aeiou'] # ['h', 'l', 'l']
# print(no_vowels)

#Covert list of strings tp integers
str_nums = ['1','2','3']
int_nums = [int(x) for x in str_nums]
# print(int_nums)

# cubes from 1 to 10
cube = [x**3 for x in range(1,11)]
# print(cube) #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# Extract only odd number from a list
odd = [x for x in range(1,11) if x % 2 != 0]
# print(odd)

#covert to uppercase with .upper()
names = ["alice","amy",'bob', 'charlie']
upper_names = [name.upper() for name in names]
# print(upper_names)

# only convert names starting with 'a'
a_names = [name.upper() for name in names if name.startswith('a')]
# print(a_names)

#lower()
a_names = [name.lower() for name in names]
# print(a_names)

#title()
names = ["john doe", "alice", "charlie brown"]
titled_names = [name.title() for name in names]
# print(titled_names)

#filter names by length
names = ["Amy", "Jonathan", "Bob", "Alice", "Max"]
long_names = [name for name in names if len(name) > 4]
# print(long_names)

#combining both title and length
names = ["amy", "jonathan", "bob", "alice", "max"]
filtered = [name.title() for name in names if len(name) > 4]
# print(filtered)

# Nested List - A nested list is a list inside another list.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[0]) #[1, 2, 3] row access
# print(matrix[0][1]) # 2-> row 0, col 1 Accessing element

# for row in matrix: # Loop to print all elements
#     for item in row:
        # print(item, end=' ') # 1 2 3 4 5 6 7 8 9

#Safe List Copying (copy())
a = [1, 2, 3]
b = a.copy() 
 # or
# b = list(a)
# # or
# b = a[:]

b.append(4)
# print("a: ",a) 
# print("b: ",b)


# enumerate() - Get index and value while looping

fruits = ['apple', 'banana', 'cherry']
for i,fruit in enumerate(fruits):
    print(i, fruit)


# max(), min(), sum()

nums = [5,2,9,1]
print("Max: ", max(nums))
print("Min:", min(nums))
print("Sum: ", sum(nums))