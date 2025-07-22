# TXT Files (PLain Text)

# READING
with  open("data.txt", "r") as file:
    content = file.read()
    print(content)

# READING LINE-BY-LINE
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# READ AS LIST OF LINES
with open("data.txt", "r") as file:
    lines = file.readlines().strip()
    print(lines)


# #WRITING
with open("data.txt", "w") as file:
    file.write("Hello, this is a text file.\n")
    file.write("This is the second line.")
 
# APPENDING    
with open("data.txt", "a") as file:
    file.write("\nNew line added.")    


# Check if File Exists (before reading)
import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        print(file.read())
else:
    print("File not found.")        
    

#EXAMPLE
filename = "data_1.txt"
tasks = ["Buy groceries", "Read Python book", "Call mom"]

# Write tasks
with open(filename, "w") as file:
    for task in tasks:
        file.write(task + "\n")

#Read tasks        
with open(filename, "r") as file:
    print("Your Tasks:")
    for line in file:
        print("-", line.strip())
       