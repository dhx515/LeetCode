/* Write your PL/SQL query statement below */
SELECT E1.NAME

FROM EMPLOYEE E1
  JOIN (
        SELECT MANAGERID
          FROM EMPLOYEE
         GROUP BY MANAGERID
        HAVING COUNT(*) >= 5
        ) E2
    ON E1.ID = E2.MANAGERID
 ;