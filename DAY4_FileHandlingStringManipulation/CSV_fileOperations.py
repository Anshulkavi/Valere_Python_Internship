# Writing to a CSV file - Each row is a list (manual header + rows)
import csv 
'''
with open("Students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    #Writing header
    writer.writerow(["Name", "Age", "Marks"])

    #Writing data
    writer.writerow(["Anshul", 20, 88])
    writer.writerow(["Virat", 22, 91])
'''

# Reading from a CSV file - Read row by row
'''
with open("students.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''

#Writing CSV using DictWriter (easier with column names) 
'''
with open("students.csv", "w", newline="")  as file:
    fieldnames = ["Name", "Age", "Marks"]
    writer = csv.DictWriter(file,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"Name": "Anshul", "Age": 20, "Marks": 88})
    writer.writerow({"Name": "Rohit", "Age": 20, "Marks": 85})

'''

#Reading CSV using DictReader
'''
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], "-", row["Marks"])
'''        

# Appending to a CSV file
'''
with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(["Virat", 23, 86])
'''    

#Example
'''
with open("books.csv", "w", newline="") as file:
    fieldnames = ["Title", "Author", "Year"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Title":"Atomic Habits", "Author":"James Clear", "Year": 2018})
    writer.writerow({"Title": "A Song of Ice and Fire", "Author": "George Martin", "Year": 1991})
    writer.writerow({"Title": "Rich Dad Poor Dad", "Author": "Robert-Sharon","Year": 1997})

with open("books.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row["Title"]} by {row["Author"]} ({row["Year"]})")
'''
