-- SQL Analysis #1
-- Inventory revenue and profit by category

SELECT
    "Category",
    COUNT(*) AS products,
    ROUND(SUM("Revenue")::numeric, 2) AS total_revenue,
    ROUND(SUM("Profit")::numeric, 2) AS total_profit
FROM inventory
GROUP BY "Category"
ORDER BY total_revenue DESC;