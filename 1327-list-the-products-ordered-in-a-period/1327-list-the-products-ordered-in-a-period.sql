/* Write your PL/SQL query statement below */
SELECT
    Products.product_name,
    SUM(Orders.unit) AS unit

FROM
    Orders,
    Products

WHERE
        Orders.product_id = Products.product_id
    AND TO_DATE(Orders.order_date, 'YYYY-MM-DD') >= TO_DATE('2020-02-01', 'YYYY-MM-DD')
    AND TO_DATE(Orders.order_date, 'YYYY-MM-DD') <= TO_DATE('2020-02-29', 'YYYY-MM-DD')

GROUP BY 
    Products.product_name

HAVING
    SUM(Orders.unit) >= 100
;