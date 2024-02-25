/* Write your PL/SQL query statement below */
SELECT E.NAME,
       B.BONUS
  FROM Employee E
  LEFT OUTER JOIN BONUS B ON (E.EMPID = B.EMPID)
 WHERE 1=1
   AND (B.BONUS < 1000 OR B.BONUS IS NULL)
;