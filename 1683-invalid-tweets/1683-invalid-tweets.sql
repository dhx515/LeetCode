/* Write your PL/SQL query statement below */
SELECT TWEET_ID
  FROM TWEETS
 WHERE 1=1
   AND LENGTH(CONTENT) > 15