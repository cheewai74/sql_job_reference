psql <Created database> -f "####.sql"</BR>

E.g:</BR>
psql linkedin -f "init.sql"</BR>
psql linkedin -c "\d customers"</BR>

init.sql</BR>
```
-- Drop existing tables to prevent conflicts
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

-- Create Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

```
E.g: insertcustomerrecords.sql</BR>
```
-- Drop existing tables to prevent conflicts
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

-- Create Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

```

insertordersrecords.sql</BR>
```
INSERT INTO Orders (order_id, customer_id, order_date, total_amount, status) 
VALUES 
(101, 1, '2026-05-15', 150.00, 'Shipped'),
(102, 2, '2026-05-16', 85.50, 'Processing'),
(103, 1, '2026-05-18', 210.00, 'Shipped'),
(104, 3, '2026-05-19', 45.00, 'Pending'),
(105, 4, '2026-05-20', 320.00, 'Processing');
```
