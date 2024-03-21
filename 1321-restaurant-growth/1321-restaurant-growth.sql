/* Write your PL/SQL query statement below */
WITH
    Interval AS
        (
            SELECT
                DISTINCT A.visited_on AS d1,
                B.visited_on AS d2
            FROM
                Customer A
                JOIN Customer B ON (A.visited_on + 6 = B.visited_on)
        )
SELECT
    TO_CHAR(d2,'YYYY-MM-DD') AS visited_on,
    SUM(amount) AS amount,
    ROUND(SUM(amount) / 7, 2) AS average_amount
FROM
    Interval I
    JOIN Customer C ON (visited_on BETWEEN d1 AND d2)
GROUP BY
    d1,d2
ORDER BY
    visited_on
;