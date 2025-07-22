students = {
    "Anshul": {"Math": 90, "Science": 85},
    "Dhaval": {"Math": 78, "Science": 82}
}

# print(students)  # Full dictionary

# students["Virat"] = {"Math": 90, "Science": 84}  #added new students

# print(students)  # After adding Virat

# print(students.keys())    # View all student names
# print(students.values())  # View all marks dictionaries

# print(students["Dhaval"]["Science"]) #Access a Specific Student's Marks

# #marks of all students by looping
# for name, marks in students.items():
#     print(f"{name}:")
#     for subject, score in marks.items():
#         print(f' {subject}: {score}')


#Enter name and get student marks 
name = input("Enter name:")
if name in students:
    print(f"{name}'s marks:")
    for subject, score in students[name].items():
        print(f" {subject}: {score}")
else:
    print("Student not found")        