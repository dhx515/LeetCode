/* Write your PL/SQL query statement below */
SELECT U.NAME AS NAME
     , SUM(T.AMOUNT) AS BALANCE
  FROM TRANSACTIONS T
       JOIN USERS U ON T.ACCOUNT = U.ACCOUNT
 GROUP BY U.NAME
HAVING SUM(T.AMOUNT) > 10000
;