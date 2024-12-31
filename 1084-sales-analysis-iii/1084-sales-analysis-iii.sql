/* Write your PL/SQL query statement below */
SELECT DISTINCT P.product_id, P.product_name
FROM Product P
JOIN Sales S ON P.product_id = S.product_id
WHERE S.product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date < DATE '2019-01-01' OR sale_date > DATE '2019-03-31'
)
AND S.sale_date BETWEEN DATE '2019-01-01' AND DATE '2019-03-31';