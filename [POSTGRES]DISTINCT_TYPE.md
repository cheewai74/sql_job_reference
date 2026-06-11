NOTE:</br>
1. In PostgreSQL, there is no CREATE DISTINCT TYPE (DB2) statement.</br>
2. PostgreSQL, uses CREATE DOMAIN to replace CREATE DISTINCT TYPE as work around.</br>

```
CREATE DOMAIN USdollar AS DECIMAL(10,2);

CREATE TABLE retail1.us_invoice(
	invoiceNo	INTEGER		PRIMARY KEY,
	customerID	INTEGER,
	salesID		INTEGER,
	salesTotal	USdollar,
	tax			USdollar,
	shipping	USdollar,
	grandTotal	USdollar
);

```

