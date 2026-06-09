
Non null asc , null desc:</br>
```
SELECT ename, sal, comm
FROM (
SELECT ename,sal,comm,
	CASE WHEN comm is NULL THEN 0 ELSE 1 
	END AS IS_NULL
FROM sql_cookbook.emp
) x
ORDER BY IS_NULL DESC, comm
```
