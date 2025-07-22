'''
What is a Set?
A set is:

Unordered

Unindexed

Mutable

Automatically removes duplicates
'''
'''
# Syntax 
my_set = {1, 2, 3}
# or
# my_set = set([1,2,2,3])

#eg
fruits = {"apple", "banana", "apple", "orange"}
# print(fruits) # remove duplicates automatically

#Methods
s = {1, 2, 3}
s.add(4) # add X to set
s.remove(4) # removed 4
# print(4 in s) # false when 4 not found
s.discard(3) # discard 3 in set 
s.clear() 
# print(len(s))

#Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
union = a.union(b) # or union = a | b
# print(union)

Intersection = a.intersection(b) # or Intersection = a & b
# print(Intersection)

Difference = a.difference(b) # Diff = a - b (Elements in a but not in b)
# print(Difference)

sym_difference = a.symmetric_difference(b) # or a ^ b
# print(sym_difference)

#convert list to set
my_list = [ 1, 2, 3, 4]
my_set = set(my_list)
# p rint(my_set)

#sets remove duplicates 
# new_set = set([1,1,2]) 
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))

# Looping through Sets
fruits = {"apple", "banana", "apple", "orange"}
# for fruit in fruits: 
    # print(fruit)


# Real-World Use Cases of Sets

#Remove Duplicates From a List
# nums = [1, 2, 2, 3, 3, 4]
# unique = list(set(nums))
# print(unique) #[1,2,3,4]

#Check if two lists have common Elements
a = [1, 2, 3]
b = [3, 4, 5]

if set(a) & set(b): #intersection
    # print("They have common elements")

#Compare User Tags or Interests (intersection & difference)

user1_tags = {"python", "django", "web"}
user2_tags = {"python", "flask", "ai"}
common = user1_tags & user2_tags
only_user1 = user1_tags - user2_tags

print('Common:', common)
print("Only user1:", only_user1)


#Detect duplicate Emails or Entries
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
if len(emails) != len(set(emails)):
    # print("Duplicates found")


'''

#Fast membership testing
names = {"alice", "bob", "charlie"}
print("bob" in names) #true
print("daniel" in names) #False    

