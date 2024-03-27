/* Write your PL/SQL query statement below */
DELETE 
FROM
    Person 
WHERE
    id NOT IN (
                SELECT 
                    MIN(p.id) 
                FROM 
                    Person p 
                GROUP BY p.email
              )
;