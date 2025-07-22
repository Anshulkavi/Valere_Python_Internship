--books
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    genre TEXT,
    available_copies INT
);

-- members
CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    join_date DATE DEFAULT CURRENT_DATE
);

ALTER TABLE members ADD COLUMN email TEXT;


--borrow_log
CREATE TABLE borrow_log (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    book_id INT REFERENCES books(id),
    borrow_date DATE DEFAULT CURRENT_DATE,
    return_date DATE
);
