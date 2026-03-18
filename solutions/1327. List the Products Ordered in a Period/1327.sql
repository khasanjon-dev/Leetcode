SELECT p.product_name, SUM(o.unit)
FROM Products p
         LEFT JOIN Orders o
                   ON p.product_id = o.product_id
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100
;