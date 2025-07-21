'''Subqueries — Query inside a query
A subquery lets you:

Filter using results from another query

Compare a value to a group

Do powerful conditional logic'''

-- # Show all students who are in a course with the maximum number of credits.

-- SELECT s.name, s.course, c.credits 
-- FROM students s   
-- JOIN courses c ON s.course = c.name
-- WHERE c.credits = (
--     SELECT MAX(credits) FROM courses
-- );

-- # Show all courses where the number of students is above average.
-- Nested subquery gets average students per course; outer filters above it.


-- SELECT course, COUNT(*) AS total_students
-- FROM students
-- GROUP BY course
-- HAVING COUNT(*) > (
--     SELECT AVG(course_count) FROM (
--         SELECT COUNT(*) AS course_count
--         FROM students
--         GROUP BY course
--     ) AS course_totals
-- );

-- # RANK students by age within each course

-- SELECT name, course, age, 
--  RANK() OVER (PARTITION BY course ORDER BY age DESC) AS age_rank
--  FROM students;

-- # RANK students by age within each course
SELECT name, course, COUNT(*) OVER (PARTITION BY course ORDER BY name) AS cumulative_students
FROM students;