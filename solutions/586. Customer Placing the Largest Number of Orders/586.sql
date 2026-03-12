-- FIRST SOLUTION
WITH ordered AS (SELECT customer_number, COUNT(*) AS count
FROM Orders
GROUP BY customer_number
ORDER BY count DESC
    )
SELECT customer_number
FROM ordered LIMIT 1;


-- SECOND SOLUTION
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC LIMIT 1;