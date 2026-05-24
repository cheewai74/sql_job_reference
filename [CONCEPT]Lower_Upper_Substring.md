
Note:</br>
Select all the books that belong to the 'C' category and show the first 20 characters of the title in lowercase and uppercase</br>
```
LOWER(character expression)
UPPER(character expression)
SUBSTRING(expression, start, length)
```

SQL Eg:</BR>
```
SELECT 
LOWER(SUBSTRING(title, 1, 20)) AS LOWER, 
UPPER(SUBSTRING(title, 1, 20)) AS UPPER
FROM book
WHERE bookcat = 'C';
```
