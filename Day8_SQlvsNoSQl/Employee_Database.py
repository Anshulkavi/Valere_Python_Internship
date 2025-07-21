import psycopg2

# --- PostgreSQL Connection ---
conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",
    password="Anshul@123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# --- Table Setup (Run only once) ---
def setup_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name TEXT,
            age INT,
            department TEXT,
            salary NUMERIC,
            is_active BOOLEAN DEFAULT TRUE
        )
    ''')
    conn.commit()

# --- CREATE ---
def add_employee(name, age, department, salary, is_active=True):
    cursor.execute(
        "INSERT INTO employees (name, age, department, salary, is_active) VALUES (%s, %s, %s, %s, %s)",
        (name, age, department, salary, is_active)
    )
    conn.commit()

# --- READ ---
def list_employees():
    cursor.execute('SELECT * FROM employees ORDER BY id')
    results = cursor.fetchall()
    for emp in results:
        print(emp)

# --- UPDATE ---
def update_salary(name, new_salary):
    cursor.execute(
        "UPDATE employees SET salary = %s WHERE name = %s",
        (new_salary, name)
    )
    conn.commit()

# --- DELETE ---
def delete_employee(name):
    cursor.execute("DELETE FROM employees WHERE name = %s", (name,))
    conn.commit()

# --- SEARCH: Salary Range ---
def search_by_salary_range(min_salary, max_salary):
    cursor.execute("SELECT * FROM employees WHERE salary BETWEEN %s AND %s", (min_salary, max_salary))
    for row in cursor.fetchall():
        print(row)

# --- SEARCH: Active/Inactive ---
def filter_by_active_status(active=True):
    cursor.execute("SELECT * FROM employees WHERE is_active = %s", (active,))
    for row in cursor.fetchall():
        print(row)

# --- SEARCH: Name Pattern ---
def search_by_name_pattern(pattern):
    cursor.execute("SELECT * FROM employees WHERE name ILIKE %s", (f"%{pattern}%",))
    for row in cursor.fetchall():
        print(row)

# --- MENU ---
def menu():
    while True:
        print("\n--- Employee Management ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Salary")
        print("4. Delete Employee")
        print("5. Search by Salary Range")
        print("6. Filter Active/Inactive Employees")
        print("7. Search by Name Pattern")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            dept = input("Department: ")
            salary = float(input("Salary: "))
            active = input("Is Active (y/n)? ").lower() == 'y'
            add_employee(name, age, dept, salary, active)

        elif choice == "2":
            list_employees()

        elif choice == "3":
            name = input("Enter name to update salary: ")
            new_salary = float(input("New Salary: "))
            update_salary(name, new_salary)

        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_employee(name)

        elif choice == "5":
            min_sal = float(input("Min Salary: "))
            max_sal = float(input("Max Salary: "))
            search_by_salary_range(min_sal, max_sal)

        elif choice == "6":
            status = input("Active (y) or Inactive (n)? ").lower() == 'y'
            filter_by_active_status(status)

        elif choice == "7":
            pattern = input("Enter name pattern (e.g. 'an'): ")
            search_by_name_pattern(pattern)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# --- Main ---
if __name__ == "__main__":
    setup_table()
    menu()
    cursor.close()
    conn.close()
