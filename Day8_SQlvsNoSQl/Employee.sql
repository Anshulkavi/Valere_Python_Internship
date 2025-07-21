CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INT,
    department TEXT,
    salary NUMERIC(10, 2),
    email TEXT,
    joining_date DATE,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

ALTER TABLE employees
ADD COLUMN department_id INT REFERENCES departments(id);

ALTER TABLE employees ADD COLUMN is_active BOOLEAN DEFAULT TRUE;
