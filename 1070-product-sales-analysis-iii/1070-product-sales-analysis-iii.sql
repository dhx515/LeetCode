/* Write your PL/SQL query statement below */
SELECT S.product_id
      ,S.year AS first_year
      ,S.quantity
      ,S.price
  FROM Sales S
  JOIN (
        SELECT product_id
              ,MIN(year) AS year
          FROM Sales
         GROUP BY product_id
        ) SS
        ON (S.product_id = SS.product_id and S.year = SS.year)
;