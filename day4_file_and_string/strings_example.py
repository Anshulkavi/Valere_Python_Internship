# String Creation

s1 = "Hello"
s2 = "World"
s3 = """ Multi-Line
String"""

# Indexing and Slicing
text = "Python"
'''
print(text[0]) #P
print(text[-1]) #n
print(text[1:4]) #yth
'''
#Common Methods


string = "HELLO virat"
# print(string.lower()) #lower()
# print(string.upper()) #upper()
# print(string.strip()) #strip() - remove leading whitespace
# print(string.replace("E", "I")) #replace()

# print(string.split()) # ['HELLO', 'virat']

# letters = ['h','e','l','l','o']
# print(''.join(letters))

# print(string.count("L")) # -> 2
# print(string.find("v")) # -> 6

# print(string.startswith("H")) # -> True
# print(string.endswith("T")) # false , it is 't'

#String Checking Methods
# print("123".isdigit()) #true
# print("abc".isalpha()) #true
# print("abc123".isalnum()) #alphanumeric
# print("HELLO".isupper()) #true
# print("hello".islower()) #true

# in keyword for substrings
# if "py" in "python":
#     print("Found!")

#f-strings
# name = "anshul"
# score = 95
# print(f"{name} scored {score} marks!")


text = "  Hello, Python!  "

# Clean + convert to uppercase + count letters
clean = text.strip().upper()
print(clean)
print("L count:", clean.count("L"))
