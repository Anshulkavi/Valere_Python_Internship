'''
.append(), .insert()	
.remove(), .pop()
'''

fruits = ['apple', 'banana', 'kiwi']

# append()
fruits.append('cherry')
print(fruits) # added cherry at last

# remove() - Removes by value, doesn't return
fruits.remove('banana')
print(fruits)

# insert()
fruits.insert(1, 'orange') # list.insert(index, value)
print(fruits)

#pop() - Removes by index, returns the value
fruits.pop() # just pop out the last element
print(fruits)

fruits.pop(0) # pop specific indexed element
print(fruits)