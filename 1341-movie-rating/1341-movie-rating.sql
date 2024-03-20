/* Write your PL/SQL query statement below */
SELECT
    name as results 
FROM
    (
    SELECT 
        name,
        user_id, 
        COUNT(movie_id) 
    FROM
        MovieRating
        LEFT JOIN Users using(user_id)
    GROUP BY name, user_id
    ORDER BY COUNT(movie_id) DESC, name ASC
    )
WHERE ROWNUM =1


UNION ALL


SELECT 
    title as results 
FROM
    (
    SELECT 
        title, 
        AVG(rating)
    FROM 
        MovieRating
        LEFT JOIN Movies USING(movie_id)
    WHERE 
        created_at >= '2020-02-01' 
        AND created_at <= '2020-02-28'
    GROUP BY title 
    ORDER BY AVG(rating) DESC, title ASC
    ) 
WHERE ROWNUM =1
;