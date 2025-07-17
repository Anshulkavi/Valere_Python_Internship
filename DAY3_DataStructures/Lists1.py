# .sort() - List method - modifies original list
# sorted() - Built-in function -  returns new list - sorted

# .sort()
numbers = [4,1,3,2]
# numbers.sort()
# print(numbers)


# sorted()
# new_list = sorted(numbers)
# print(new_list)   # [1, 2, 3, 4]
# print(numbers)    # [4, 1, 3, 2] → original unchanged

# Sorting in Descending Order  -> [4, 3, 2, 1]
numbers.sort(reverse=True)
# print(numbers)
#or
new_list = sorted(numbers, reverse=True)
# print(new_list)

# Sort by length of Elements

words = ["apple", "kiwi","banana"]
words.sort(key=len)
print(words) # ['kiwi', 'apple', 'banana']

words.sort()
print(words)