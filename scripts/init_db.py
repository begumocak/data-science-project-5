import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

# Önceki çalıştırmalardan / diğer projelerden kalan tabloları temizle
cur.execute("DROP TABLE IF EXISTS customers, orders, products CASCADE;")

cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    signup_date DATE
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    total_amount NUMERIC(10,2),
    status VARCHAR(20)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price NUMERIC(10,2),
    category VARCHAR(50)
);
""")

cur.execute("""
INSERT INTO customers (full_name, email, signup_date) VALUES
('Ali Veli', 'ali@example.com', '2023-01-01'),
('Ayşe Yılmaz', 'ayse@example.com', '2023-02-15'),
('Mehmet Can', 'mehmet@example.com', '2022-12-10'),
('Zeynep Ak', NULL, '2023-03-01'),
('Deniz Yıldız', 'denizyildiz.com', '2023-04-01');
""")

cur.execute("""
INSERT INTO orders (customer_id, order_date, total_amount, status) VALUES
(1, '2024-01-10', 500.00, 'completed'),
(2, '2024-01-12', 150.00, 'pending'),
(3, '2024-01-15', 300.00, 'completed');
""")

cur.execute("""
INSERT INTO products (product_name, price, category) VALUES
('Laptop', 1500.00, 'Electronics'),
('Tablet', 800.00, 'Electronics'),
('Buzdolabı', 1200.00, 'Appliances'),
('Mouse', 250.00, NULL);
""")

conn.commit()
cur.close()
conn.close()
