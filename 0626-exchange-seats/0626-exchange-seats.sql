/* Write your PL/SQL query statement below */
SELECT
    CASE
        WHEN MOD(id, 2) = 0 
            THEN LAG(id, 1) OVER (ORDER BY id)
        ELSE LEAD(id, 1, id) OVER (ORDER BY id)
    END AS id,
    student
FROM
    seat
ORDER BY id
;