
Non null sorted asc , null last:</br>
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

Non null sorted desc , null desc:</br>
```
SELECT ename, sal, comm
FROM (
SELECT ename,sal,comm,
	CASE WHEN comm is NULL THEN 0 ELSE 1 
	END AS IS_NULL
FROM sql_cookbook.emp
) x
ORDER BY IS_NULL DESC, comm DESC
```

Non null sorted asc , null first:</br>
```
SELECT ename, sal, comm
FROM (
SELECT ename,sal,comm,
	CASE WHEN comm is NULL THEN 0 ELSE 1 
	END AS IS_NULL
FROM sql_cookbook.emp
) x
ORDER BY IS_NULL, comm
```
