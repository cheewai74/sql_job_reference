Syntax:
```
SELECT select_list
FROM table_source
ORDER BY {column_name [ASC | DESC]}[,..n]]
```

Example:</br>
1. Ordering by one column:</BR>
```
SELECT name, salary
FROM staff
ORDER BY salary DESC;
```

2. Ordering by multiple Columns:</BR>
```
SELECT name, salary
FROM staff
ORDER BY salary, datejoin DESC;
```
