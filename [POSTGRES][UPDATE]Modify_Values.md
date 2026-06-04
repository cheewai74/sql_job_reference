```
UPDATE table
SET column = value;

UPDATE table
SET column_a = value,
    column_b = value;

UPDATE table
SET column = value
WHERE criteria;

UPDATE table
SET column = (SELECT column
              FROM table_b
              WHERE table.column = table_b.column)
WHERE EXISTS (SELECT column
              FROM table_b
              WHERE table.column = table_b.column)

UPDATE table
SET column = table_b.column
FROM table_b
WHERE table.column = table_b.column;
```

```
SELECT
    (SELECT COUNT(*) FROM <table>) AS original,
    (SELECT COUNT(*) FROM <table>_backup) AS backup

E.g:
SELECT 
	(SELECT COUNT(*) FROM practical_sql.meat_poultry_egg_inspect) AS original,
	(SELECT COUNT(*) FROM practical_sql.meat_poultry_egg_inspect_backup) AS backup
```



