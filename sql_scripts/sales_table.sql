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

-- 1. Total Revenue
SELECT SUM(sales) AS total_revenue FROM sales;

-- 2. Total Order Volume
SELECT COUNT(order_id) AS total_orders FROM sales;

-- 3. Average Order Value (AOV)
SELECT ROUND(SUM(sales) / COUNT(order_id), 2) AS average_order_value FROM sales;

