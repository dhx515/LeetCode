/* Write your PL/SQL query statement below */
SELECT R.contest_id,
       ROUND(100 * COUNT(R.contest_id) / (SELECT COUNT(*) FROM Users), 2) AS percentage
  FROM Register R
 GROUP BY R.contest_id
 ORDER BY percentage DESC, contest_id ASC
;