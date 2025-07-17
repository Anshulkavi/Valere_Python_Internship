#===== Student Marks Management System =====

students = { 
    "Anshul": {"Math": 90, "Science": 85},
    "Dhaval": {"Math": 78, "Science": 82},
    }


def add_students():
    name = input("Enter a name:").strip().title()
    if name in students:
        print("Student Already Exists.")
        return
    marks = {}
    subjects = int(input("How many subjects?: "))
    for _ in range(subjects):
        subject = input("Enter subject name: ")
        score = int(input(f"Enter marks in {subject}: "))
        marks[subject] = score
    students[name] = marks
    print("Student added successfully")        


def view_all_students():
    if not students:
        print("No students to show.")
        return
    for name, marks in students.items():
        print(f"\n{name}'s Marks:")
        for subject, score in marks.items():
            print(f" {subject}: {score}")
        avg = sum(marks.values()) / len(marks)
        print(f" Average: {avg:.2f}")           


def search_student():
    name = input("Enter a name:").strip().title()
    if name in students:
        print(f"{name}'s Marks:")
        for subject, score in students[name].items():
            print(f" {subject}: {score}")
    else:
        print("Student not found")


def update_marks():
    name = input("Enter student name to update: ")
    if name not in students:
        print("Student not found")
        return
    subject = input("Enter subject to update: ")
    if subject in students[name]:
        score = int(input(f"Enter new marks for {subject}: "))
        students[name][subject] = score
        print("Marks Updated")
    else:
        print("Subject not found for this student")


def delete_students():
    name = input("Enter student name to delete: ")
    if name in students:
        students.pop(name)
        print("Student deleted.")
    else:
        print("Student not found.")    


def show_topper():
    if not students:
        print("No student data available")
        return
    topper = None
    top_avg = 0  
    for name, marks in students.items():
        avg = sum(marks.values()) / len(marks)  
        if avg > top_avg:
           top_avg = avg
           topper = name
    print(f"\nTopper: {topper} with average {top_avg:.2f}")    


while True:
    print("\n===== Student Marks Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Students")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_students()
    elif choice == "2":
        view_all_students()   
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_students()
    elif choice == "6":
        show_topper()        
    elif choice == "7":    
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
                 