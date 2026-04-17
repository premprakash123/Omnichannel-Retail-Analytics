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