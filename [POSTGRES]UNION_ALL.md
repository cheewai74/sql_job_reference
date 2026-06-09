UNION ALL combines rows from multiple row sources into one result set.</BR>
UNION ALL will include duplicates if they exist.</BR>
```
SELECT  ename AS ename_and_dname, deptno
FROM sql_cookbook.emp
WHERE deptno=10
UNION ALL
SELECT '----------', null
FROM sql_cookbook.t1
UNION ALL 
SELECT dname, deptno
FROM 
sql_cookbook.dept
```
