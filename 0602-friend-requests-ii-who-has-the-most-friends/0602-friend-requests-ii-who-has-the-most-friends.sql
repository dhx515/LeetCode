/* Write your PL/SQL query statement below */
SELECT 
    * 
FROM
    (SELECT 
         A AS id, 
         SUM(temp) AS num 
     FROM
        (
         SELECT 
             COUNT(requester_id) temp, 
             requester_id AS a 
         FROM 
             RequestAccepted 
         GROUP BY requester_id

         UNION ALL

         SELECT
             COUNT(accepter_id) temp,
             accepter_id AS b 
         FROM 
             RequestAccepted 
         GROUP BY accepter_id
        )
    GROUP BY A ORDER BY num DESC) 
WHERE 
    ROWNUM = 1
;