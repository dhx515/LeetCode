/* Write your PL/SQL query statement below */
SELECT
    DEP_NAME "Department",
    EMP_NAME "Employee",
    SALARY   "Salary"
FROM
    (
        SELECT
            SALARY,
            D.NAME AS DEP_NAME,
            E.NAME AS EMP_NAME,
            DENSE_RANK() OVER(
                                PARTITION BY D.NAME 
                                ORDER BY E.SALARY DESC
                             ) AS RANKED
        FROM
            EMPLOYEE E
            JOIN DEPARTMENT D ON (E.DEPARTMENTID = D.ID)
    )
WHERE
    RANKED <= 3
ORDER BY 3 DESC
;