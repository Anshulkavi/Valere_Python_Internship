import json

# ===== Load Data from File =====
def load_data():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = {}

# ===== Save Data to File =====
def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)

# ===== Student Operations =====
def add_students():
    name = input("Enter a name: ").strip().title()
    if name in students:
        print("Student already exists.")
        return
    try:
        subjects = int(input("How many subjects?: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    marks = {}
    for _ in range(subjects):
        subject = input("Enter subject name: ").strip().title()
        try:
            score = int(input(f"Enter marks in {subject}: "))
        except ValueError:
            print("Marks must be an integer. Aborting student addition.")
            return
        marks[subject] = score

    students[name] = marks
    save_data()
    print("Student added successfully.")


def view_all_students():
    if not students:
        print("No students to show.")
        return
    for name, marks in students.items():
        print(f"\n{name}'s Marks:")
        for subject, score in marks.items():
            print(f" {subject}: {score}")
        total = sum(marks.values())
        avg = total / len(marks)
        print(f" Total: {total}, Average: {avg:.2f}")


def search_student():
    name = input("Enter a name: ").strip().title()
    if name in students:
        print(f"\n{name}'s Marks:")
        for subject, score in students[name].items():
            print(f" {subject}: {score}")
        total = sum(students[name].values())
        avg = total / len(students[name])
        print(f" Total: {total}, Average: {avg:.2f}")
    else:
        print("Student not found.")


def update_marks():
    name = input("Enter student name to update: ").strip().title()
    if name not in students:
        print("Student not found.")
        return

    print("Available subjects:", ', '.join(students[name].keys()))
    subject = input("Enter subject to update: ").strip().title()

    if subject in students[name]:
        try:
            score = int(input(f"Enter new marks for {subject}: "))
        except ValueError:
            print("Invalid input. Marks must be an integer.")
            return
        students[name][subject] = score
        save_data()
        print("Marks updated.")
    else:
        print("Subject not found for this student.")


def delete_students():
    name = input("Enter student name to delete: ").strip().title()
    if name in students:
        confirm = input(f"Are you sure you want to delete {name}? (y/n): ").lower()
        if confirm == 'y':
            students.pop(name)
            save_data()
            print("Student deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("Student not found.")


def show_topper():
    if not students:
        print("No student data available.")
        return

    topper = None
    top_avg = 0
    for name, marks in students.items():
        avg = sum(marks.values()) / len(marks)
        if avg > top_avg:
            top_avg = avg
            topper = name

    print(f"\nTopper: {topper} with average {top_avg:.2f}")


# ===== Main Menu Loop =====
load_data()
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
