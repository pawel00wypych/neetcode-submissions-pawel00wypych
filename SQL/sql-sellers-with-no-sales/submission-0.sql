-- Write your query below
SELECT s.seller_name
FROM seller s
LEFT JOIN orders o 
    ON o.seller_id = s.seller_id
    AND o.sale_date >= '2020-01-01'
    AND o.sale_date < '2021-01-01'
WHERE o.customer_id IS NULL
ORDER BY s.seller_name;