/* Write your PL/SQL query statement below */
/*
SELECT e.name AS Employee
  FROM Employee e
 WHERE e.salary > (SELECT salary
                     FROM Employee
                    WHERE id = e.managerId)
;
*/
SELECT A.name AS Employee
FROM Employee A, Employee B
WHERE A.managerId = B.id AND A.salary > B.salary