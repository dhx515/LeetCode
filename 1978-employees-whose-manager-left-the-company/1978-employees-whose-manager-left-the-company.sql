/* Write your PL/SQL query statement below */
SELECT
    employee_id 
FROM
    Employees
WHERE
    salary<30000 
    AND manager_id NOT in (SELECT employee_id from employees )
ORDER BY 
    employee_id
;