Use the function COALESCE  to substitue real  values for null.</BR>

```
SELECT COALESCE(comm, 0)
FROM sql_cookbook.emp
```

Equivalent</BR>

```
SELECT 
CASE WHEN comm IS NOT NULL THEN comm
ELSE 0
END
FROM sql_cookbook.emp
```
