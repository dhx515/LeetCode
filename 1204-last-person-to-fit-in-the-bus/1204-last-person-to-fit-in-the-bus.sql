/* Write your PL/SQL query statement below */
SELECT
    person_name
FROM
    (SELECT 
        person_name, 
        SUM(weight) OVER (ORDER BY turn) AS sum_weight
      FROM
        queue
      ORDER BY sum_weight DESC)
WHERE 
    sum_weight <= 1000
    AND ROWNUM = 1;