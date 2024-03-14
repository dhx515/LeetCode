WITH all_products AS (
    SELECT DISTINCT product_id
    FROM products
),
last_order_date AS (
    SELECT product_id, MAX(change_date) AS change_date
    FROM products
    WHERE change_date <= TO_DATE('2019-08-16', 'YYYY-MM-DD')
    GROUP BY product_id
)
SELECT
    a.product_id,
    NVL(p.new_price, 10) AS price
FROM
    all_products a
LEFT JOIN
    last_order_date l ON a.product_id = l.product_id
LEFT JOIN
    products p ON p.product_id = l.product_id AND p.change_date = l.change_date;