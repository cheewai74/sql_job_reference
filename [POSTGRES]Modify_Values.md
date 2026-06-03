```
UPDATE TABLE
SET column =
    (SELECT column
     FROM table_b
     WHERE table.column = table_b.column
WHERE EXITS
    (SELECT column
     FROM table_b
     WHERE table.column = table_b.column;)
```
