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

# --- CREATE BOOK ---
def add_book(title, author, genre, available_copies):
    cursor.execute(
        "INSERT INTO books (title, author, genre, available_copies) VALUES (%s, %s, %s, %s)",
        (title, author, genre, available_copies)
    )
    conn.commit()
    print("✅ Book added!")

# --- VIEW BOOKS ---
def view_books():
    cursor.execute("SELECT * FROM books")
    for book in cursor.fetchall():
        print(book)

# --- ADD MEMBER ---
def add_member(name, email):
    cursor.execute(
        "INSERT INTO members (name, email) VALUES (%s, %s)",
        (name, email)
    )
    conn.commit()
    print("✅ Member added!")

# --- VIEW MEMBERS ---
def view_members():
    cursor.execute("SELECT * FROM members")
    for member in cursor.fetchall():
        print(member)

# --- BORROW BOOK ---
def borrow_book(member_id, book_id):
    cursor.execute("SELECT available_copies FROM books WHERE id = %s", (book_id,))
    result = cursor.fetchone()

    if not result:
        print("❌ Book not found.")
        return

    available_copies = result[0]
    if available_copies <= 0:
        print("❌ No copies available.")
        return

    cursor.execute(
        "INSERT INTO borrow_log (member_id, book_id) VALUES (%s, %s)",
        (member_id, book_id)
    )
    cursor.execute(
        "UPDATE books SET available_copies = available_copies - 1 WHERE id = %s",
        (book_id,)
    )
    conn.commit()
    print("✅ Book borrowed successfully.")

# --- RETURN BOOK ---
def return_book(member_id, book_id):
    cursor.execute("""
        SELECT id FROM borrow_log
        WHERE member_id = %s AND book_id = %s AND return_date IS NULL
        ORDER BY borrow_date DESC LIMIT 1
    """, (member_id, book_id))
    result = cursor.fetchone()

    if not result:
        print("❌ No active borrow record found.")
        return

    borrow_log_id = result[0]

    cursor.execute("""
        UPDATE borrow_log SET return_date = CURRENT_DATE WHERE id = %s
    """, (borrow_log_id,))
    cursor.execute("""
        UPDATE books SET available_copies = available_copies + 1 WHERE id = %s
    """, (book_id,))
    conn.commit()
    print("✅ Book returned successfully.")

# --- CLI MENU ---
def menu():
    while True:
        print("\n--- Library Management ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Member")
        print("4. View Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            copies = int(input("Available Copies: "))
            add_book(title, author, genre, copies)

        elif choice == '2':
            view_books()

        elif choice == '3':
            name = input("Member Name: ")
            email = input("Email: ")
            add_member(name, email)

        elif choice == '4':
            view_members()

        elif choice == '5':
            member_id = int(input("Member ID: "))
            book_id = int(input("Book ID: "))
            borrow_book(member_id, book_id)

        elif choice == '6':
            member_id = int(input("Member ID: "))
            book_id = int(input("Book ID: "))
            return_book(member_id, book_id)

        elif choice == '7':
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice.")

    cursor.close()
    conn.close()

if __name__ == '__main__':
    menu()
