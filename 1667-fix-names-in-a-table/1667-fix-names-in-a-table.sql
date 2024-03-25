/* Write your PL/SQL query statement below */
SELECT
    user_id,
    CONCAT(UPPER(SUBSTR(NAME,1,1)),LOWER(SUBSTR(NAME,2))) AS name
FROM
    Users
ORDER BY user_id
;