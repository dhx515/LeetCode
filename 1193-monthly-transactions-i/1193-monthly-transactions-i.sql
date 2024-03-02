/* Write your PL/SQL query statement below */
SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month,
       country,
       COUNT(id) AS trans_count,
       SUM(CASE WHEN state='approved' THEN 1 ELSE 0 END) AS approved_count,
       SUM(amount) AS trans_total_amount,
       SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) as approved_total_amount
  FROM Transactions
 GROUP BY TO_CHAR(trans_date, 'YYYY-MM'), country
;