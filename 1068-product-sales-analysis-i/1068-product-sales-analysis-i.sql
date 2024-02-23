/* Write your PL/SQL query statement below */
SELECT PRODUCT_NAME,
       YEAR,
       PRICE
  FROM Sales S
  JOIN Product P 
    ON S.product_id = P.product_id