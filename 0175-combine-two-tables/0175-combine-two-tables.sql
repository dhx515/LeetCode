/* Write your PL/SQL query statement below */
SELECT p.firstName
     , p.lastName
     , a.city
     , a.state 
  FROM Person p 
  LEFT JOIN Address a on p.personId  = a.personId 
;