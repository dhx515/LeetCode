/* Write your PL/SQL query statement below */
SELECT NAME,
       POPULATION,
       AREA
  FROM WORLD
 WHERE 1=1
   AND AREA >= 3000000
    OR POPULATION >= 25000000