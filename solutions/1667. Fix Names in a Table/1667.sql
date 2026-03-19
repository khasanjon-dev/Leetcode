-- Write your PostgreSQL query statement below
SELECT user_id, INITCAP(name) AS name
FROM Users
ORDER BY user_id
;1667. Fix Names in a Table