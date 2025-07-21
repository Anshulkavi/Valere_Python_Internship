-- Create students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
);

-- Create courses table
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    credits INT
);

-- Insert data into courses
INSERT INTO courses (name, credits) VALUES
('Math', 3),
('Physics', 4),
('Chemistry', 5),
('History', 3),
('CS', 4);

-- Insert data into students
INSERT INTO students (name, age, course) VALUES
('Anshul', 22, 'Math'),
('Priya', 23, 'Math'),
('Riya', 21, 'Physics'),
('Neha', 25, 'Physics'),
('Aman', 24, 'CS'),
('Ravi', 22, 'CS'),
('Kiran', 20, 'Chemistry'),
('Divya', 21, 'Chemistry'),
('Mohit', 23, 'Chemistry'),
('Aarti', 22, 'History');

-- Challenge 1: Students in course with max credits
SELECT s.name, s.course, c.credits
FROM students s
JOIN courses c ON s.course = c.name
WHERE c.credits = (
  SELECT MAX(credits) FROM courses
);

-- Challenge 2: Courses with student count above average
SELECT course, COUNT(*) AS total_students
FROM students
GROUP BY course
HAVING COUNT(*) > (
  SELECT AVG(course_count) FROM (
    SELECT COUNT(*) AS course_count
    FROM students
    GROUP BY course
  ) AS course_totals
);

-- Challenge 3: Rank students by age within course
SELECT
  name,
  course,
  age,
  RANK() OVER (PARTITION BY course ORDER BY age DESC) AS age_rank
FROM students;

-- Challenge 4: Cumulative count of students by course
SELECT
  name,
  course,
  COUNT(*) OVER (PARTITION BY course ORDER BY name) AS cumulative_students
FROM students;

-- Challenge 5: Youngest student per course
SELECT *
FROM (
  SELECT
    name,
    course,
    age,
    RANK() OVER (PARTITION BY course ORDER BY age ASC) AS rank_in_course
  FROM students
) AS ranked_students
WHERE rank_in_course = 1;
