/* Write your PL/SQL query statement below */
SELECT TO_CHAR(activity_date, 'YYYY-MM-DD') AS day
      ,COUNT(DISTINCT user_id) AS active_users
  FROM Activity
 WHERE 1=1
   AND activity_date BETWEEN '2019-06-28' AND '2019-07-27'
 GROUP BY TO_CHAR(activity_date, 'YYYY-MM-DD')
;