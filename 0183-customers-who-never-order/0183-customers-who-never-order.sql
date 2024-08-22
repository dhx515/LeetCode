/* Write your PL/SQL query statement below */
SELECT c.name as Customers
  FROM Customers c
 WHERE c.id NOT IN (SELECT DISTINCT customerId FROM Orders)
;