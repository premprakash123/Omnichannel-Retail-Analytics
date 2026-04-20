-- Create the sales table
CREATE TABLE sales (
    order_id VARCHAR(50) PRIMARY KEY,
    product VARCHAR(100),
    quantity INTEGER,
    price NUMERIC(10, 2),
    timestamp TIMESTAMP,
    city VARCHAR(50),
    sales NUMERIC(10, 2),
    month VARCHAR(20),
    year INTEGER
);

SELECT COUNT(*) FROM sales;

-- Total Revenue
SELECT SUM(sales) AS total_revenue FROM sales;

-- Total Order Volume
SELECT COUNT(order_id) AS total_orders FROM sales;

-- Average Order Value (AOV)
SELECT ROUND(SUM(sales) / COUNT(order_id), 2) AS average_order_value FROM sales;

-- 1. Best Selling Products (By Volume)
SELECT product, SUM(quantity) as total_qty 
FROM sales 
GROUP BY product 
ORDER BY total_qty DESC LIMIT 5;

-- 2. Geographic Performance
SELECT city, SUM(sales) as city_revenue 
FROM sales 
GROUP BY city 
ORDER BY city_revenue DESC;

-- 3. Peak Hour Analysis 
SELECT EXTRACT(HOUR FROM timestamp) as shopping_hour, COUNT(*) as order_count 
FROM sales 
GROUP BY shopping_hour 
ORDER BY order_count DESC;



