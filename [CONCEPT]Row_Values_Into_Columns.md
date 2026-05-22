GENERAL:</BR>
* Only Microsoft SQL Server support PIVOT</BR>

Microsoft SQL Server SQL Code Snippet:</BR>
```
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


POSTGRES SQL Code Snippet:</BR>
```
SELECT
    region,
    SUM(CASE WHEN quater = 'Q1' THEN amount END) AS Q1,
    SUM(CASE WHEN quater = 'Q2' THEN amount END) AS Q2
FROM sales_mock_facebook
GROUP BY region;
```
