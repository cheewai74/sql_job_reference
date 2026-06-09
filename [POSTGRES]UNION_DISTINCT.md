```
SELECT DISTINCT deptno
FROM (
	SELECT deptno
	FROM sql_cookbook.emp
	UNION ALL
	Select deptno
	FROM sql_cookbook.dept)
	ORDER BY deptno DESC
```
