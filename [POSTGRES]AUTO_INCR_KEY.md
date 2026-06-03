Creating an Auto-Incrementing Surrogate Key Example:
```
 CREATE TABLE practical_sql.surrogate_key_example(
	order_number bigserial,
	product_name VARCHAR(50),
	order_date date,
	CONSTRAINT order_key PRIMARY KEY(order_number)
 );

 INSERT INTO practical_sql.surrogate_key_example(product_name, order_date)
 VALUES
 ('Beachball Polish','2015-03-17'),
 ('Wrinkle De-Atomizer','2017-05-22'),
 ('Flux Capacitor','1985-10-26');

SELECT * FROM practical_sql.surrogate_key_example
```
