'''
What is JSON?
JSON (JavaScript Object Notation) is a lightweight format used to store and exchange data. It's commonly used in APIs and config files.
{
  "name": "Anshul",
  "age": 22,
  "skills": ["Python", "Django"]
}

Method	        Description
json.dump()	    Writes to a JSON file
json.load()	    Reads from a JSON file
json.dumps()	Converts Python object → string
json.loads()	Converts string → Python object


import json 

users = [
    {"name": "Anshul",
    "age": 22,
    "skills": ["Python", "Django"]},
    {"name": "Kavi",
    "age": 21,
    "skills": ["FastAPI", "Django"]}
]

'''
# Writing to a JSON File
with open("user.json", "w") as file:
    json.dump(users, file, indent=4)

# Reading from a JSON File
with open("user.json", "r") as file:
    data = json.load(file)

for user in data:
    print(user["name"], "-", user["skills"])    



#json.dumps() -- Python -> JSON string

data = {"name": "Anshul", "age": 22}
json_string = json.dumps(data)
print(json_string)


#json.loads() -- JSON string --> Python

json_string = '{"name": "Anshul", "age": 22}'
data = json.loads(json_string)
print(data["name"])
print(type(data))


# Sample Nested JSON
json_string = '''
{
  "name": "Anshul",
  "age": 22,
  "skills": ["Python", "Django", "React"],
  "education": {
    "degree": "B.Tech",
    "year": 2024,
    "college": "ABC Institute"
  }
}

#Parse the string to a Python dict

data = json.loads(json_string)
# print(data)

#Accessing nested data

print(data["name"])
print(data["skills"][1])
print(data["education"]["college"])


#Loop through Keys
# for skill in data["skills"]:
#     print(f"Skill: {skill}")

    # or

for key, value in data["education"].items():
    print(f"{key.title()}: {value}")    