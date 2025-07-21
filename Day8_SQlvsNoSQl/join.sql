-- -- BASIC INNER JOIN — Student Info + Course Credits

-- SELECT 
--   s.name AS student_name,
--   s.age,
--   s.course,
--   c.credits
-- FROM 
--     students s 
-- JOIN 
--     courses c
-- ON 
--     s.course = c.name  

-- LEFT JOIN - INCLUDE ALL STUDENTS EVEN IF COURSE NOT FOUND

-- SELECT 
--    s.name AS student_name,
--    s.course,
--    c.credits
-- FROM 
--    students s 
-- LEFT JOIN
--    courses c 
-- ON 
--   s.course = c.name;   

-- RIGHT JOIN -- LIST ALL COURSES EVEN IF NO STUDENT IS ENROLLED

-- SELECT
--   s.name AS student_name,
--   c.name AS course_name,
--   c.credits
-- FROM 
--   students s      
-- RIGHT JOIN
--   courses c
-- ON
--   s.course = c.name;   


--#List student names and their course credit hours.
-- SELECT
--    s.name AS student_name,
--    c.name AS course_name,
--    c.credits
-- FROM
--    students s
-- JOIN 
--     courses c
-- ON
--     s.course = c.name;

-- # Find students who are in courses with more than 3 credits
-- SELECT
--    s.name AS student_name,
--    c.name AS course_name,
--    c.credits
-- FROM
--    students s   
-- JOIN 
--     courses c
-- ON
--     s.course = c.name
-- WHERE 
--    c.credits > 3;    

-- # List all courses that do not have any enrolled students.
    SELECT 
       s.name AS student_name,
       c.name AS course_name,
       c.credits
    FROM
       students s
    RIGHT JOIN
       courses c
    ON 
       s.course = c.name
    WHERE
       s.name IS NULL;         