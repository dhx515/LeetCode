WITH 
    cte AS (
            SELECT 
                tiv_2016,
                COUNT(tiv_2015) over(PARTITION BY tiv_2015 ORDER BY NULL) same_2015,
                COUNT(lat||lon) over(PARTITION BY lat||lon ORDER BY NULL) same_loc
            FROM 
                insurance
            )
SELECT 
    SUM(tiv_2016) tiv_2016 
FROM 
    cte 
WHERE 
    same_loc = 1 
    AND same_2015 > 1
;