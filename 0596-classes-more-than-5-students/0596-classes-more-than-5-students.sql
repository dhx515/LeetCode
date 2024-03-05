/* Write your PL/SQL query statement below */
SELECT A.class
  FROM (SELECT class, COUNT(student) AS cnt
          FROM Courses
         GROUP BY class) A
 WHERE A.cnt >= 5
;