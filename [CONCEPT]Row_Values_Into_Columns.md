GENERAL:</BR>
* Only Microsoft SQL Server support PIVOT</BR>

Microsoft SQL Server SQL Code Snippet:</BR>
```
PIVOT = turns row values into columns.
SUM(amount) = aggregates the values.
FOR quater IN ([Q1],[Q2]) = creates quater columns

SELECT
	region,
	[Q1],
	[Q2]
FROM (
	SELECT
		region,
		quater,
		amount
	FROM sales_mock_facebook
) AS souce_data
PIVOT(
	SUM(amount)
	FOR quater IN ([Q1], [Q2])
)AS pivot_table
ORDER BY region;
```


Postgres SQL Code Snippet:</BR>
```
SELECT
    region,
    SUM(CASE WHEN quater = 'Q1' THEN amount END) AS Q1,
    SUM(CASE WHEN quater = 'Q2' THEN amount END) AS Q2
FROM sales_mock_facebook
GROUP BY region;
```

SQL DATA:<\BR>
```
INSERT INTO sales_mock_facebook(sale_id, region, quater, amount)
VALUES(1, 'North', 'Q1', 120.00);
INSERT INTO sales_mock_facebook(sale_id, region, quater, amount)
VALUES(2, 'North', 'Q2', 180.00);
INSERT INTO sales_mock_facebook(sale_id, region, quater, amount)
VALUES(3, 'South', 'Q1', 90.00);
INSERT INTO sales_mock_facebook(sale_id, region, quater, amount)
VALUES(4, 'South', 'Q2', 150.00);
INSERT INTO sales_mock_facebook(sale_id, region, quater, amount)
VALUES(5, 'East', 'Q1', 200.00);
INSERT INTO sales_mock_facebook(sale_id, region, quater, amount)
VALUES(6, 'East', 'Q2', 160.00);
```
