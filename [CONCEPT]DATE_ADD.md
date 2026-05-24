Note:</BR>
DATEADD() is a Microsoft SQL Server function, not a PostgreSQL function</BR>

POSTRGRES</BR>
```
SELECT staffid, 
       name, 
       datejoin,
       datejoin + INTERVAL '6 months' AS "Confirmation Date"
FROM staff;
```

Mircrosoft SQL</BR>
```
SELECT staffid, name, datejoin,
DATEADD(month, 6, datejoin)
AS "Confirmation Date"
FROM staff;
```
