import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname = "testdb",
    user= "postgres",
    password="Anshul@123",
    host= "localhost",
    port= "5432"
)
cursor = conn.cursor()

# CREATE: Insert a student
def create_student(name, age):
    cursor.execute("INSERT INTO STUDENTS (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()

# READ: GET all students
def read_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)    

# UPDATE: update student age by name
def update_student(name,new_age):
    cursor.execute("UPDATE students SET age = %s WHERE name = %s", (new_age, name))  
    conn.commit()  

# DELETE: Remove student by name
def delete_student(name):
    cursor.execute("DELETE FROM students WHERE name = %s", (name,))
    conn.commit()

# --- Example usage ---
create_student("Anshul", 22)
create_student("Riya", 23)
read_students()
update_student("Anshul", 25)
read_students()

# Close connection
cursor.close()
conn.close()