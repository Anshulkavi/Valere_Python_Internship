'''
A dictionary is:

A collection of key-value pairs

Unordered (until Python 3.7+ where insertion order is preserved)

Mutable

Keys must be unique and immutable
'''
#Syntax
my_dict = {
    "name": "Anshul",
    "age": 21,
    "city": "Nashik"
}

#Accessing Values
# print(my_dict["name"])
# print(my_dict.get("age"))

#Adding & Updating Values
my_dict["email"] = "anshul@example.com" #Add
my_dict["age"] = 22 #update

#Removing Items
my_dict.pop("city") # removes by key
# del my_dict["name"] # another way
# my_dict.clear() #removes everything

# Looping through Dictionary
'''
for key in my_dict:
    print(key, my_dict[key])
# or
for key, value in my_dict.items():
    print(f"{key} => {value}") 
'''
'''
# dict.keys() → Get all keys
print(my_dict.keys())     # dict_keys(['name', 'age', 'email'])

# dict.values() -> Get all values
print(my_dict.values()) # dict_values(['Anshul', 22, 'anshul@example.com'])

# dict.items() -> Get all key-value pairs
for key, value in my_dict.items():
    print(key, "->", value)


# dict.get(key) -> Safe value access
print(my_dict.get("name"))
print(my_dict.get("email"))



# dict.pop(key) -> remove key and return value
my_dict.pop("age")
print(my_dict)


# dict.update(other_dict) -> Add or update multiple items
my_dict.update({"email": "anshul1@example.com", "course": "Advanced Python"})
print(my_dict)

my_dict.clear()
print(my_dict)
'''