MSSQL:</BR>
```
Select staffid, name,
  DATEDIFF(Year, datejoin, getdate()), salary * 12
from staff; 
```

Postgres:</BR>
```
SELECT 
    staffid,
    name,
    EXTRACT(YEAR FROM AGE(CURRENT_DATE, datejoin)) AS years_worked,
    salary * 12 AS annual_salary
FROM staff;
```

* CURRENT_DATE → PostgreSQL equivalent of GETDATE()</BR>
* AGE() → calculates date difference</BR>
* EXTRACT(YEAR FROM ...) → gets the year portion</BR>
* AS years_worked → gives the column a readable name</BR>
