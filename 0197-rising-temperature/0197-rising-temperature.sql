/* Write your PL/SQL query statement below */
SELECT W.ID

 FROM Weather W
 JOIN Weather X
   ON W.recordDate = X.recordDate + INTERVAL '1' DAY

WHERE W.temperature > X.temperature
;