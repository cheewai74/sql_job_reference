```
SELECT date, revenue
  SUM(revenue) OVER (ORDER BY date)
AS
  cumulative
FROM daily_sales;
```
