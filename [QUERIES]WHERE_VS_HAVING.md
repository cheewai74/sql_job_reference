Quick Rule:</BR>
WHERE = Before GROUP BY</BR>
HAVING = AFTER GROUP BY</BR>

| sale_id       | product       | category      | amount        |
| ------------- | ------------- | ------------- | ------------- |
| 1 | laptop |Tech| 900 |
| 2 | Mouse |Tech| 40 |
| 3 | Chair |Office| 120 |
| 4 | Desk|Office| 300 |
| 5 | Keyboard |Tech| 80 |

```
SELECT
  category,
  SUM(amount) AS total_sales
FROM sales
GROUP BY category
HAVING SUM(amount) > 500;
```

Remember:</BR>
* WHERE = filters individual rows before grouping <BR>
* HAVING = filters grouped results after aggregation </BR>
