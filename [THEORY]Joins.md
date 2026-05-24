INNER JOIN:</BR>
_rows that have a match in the joined tables are retrieved._</BR>
</BR>
OUTER JOIN:</BR>
_An Outer Join retrieves not only rows that have a match in the joined tables, bout also unmatched rows that do not justify the join condition._</BR>
</BR>
LEFT OUTER JOIN:</BR>
_In a LEFT OUTER JOIN, all rows from the first-named table (the left table which appears leftmost in the JOIN clause) are included. Unmatched rows in the right table are ommitted._</BR>
```
SELECT *
FROM staff
LEFT OUTER JOIN branch
ON staff.branchno = branch.branchno;
```
</BR>

RIGHT OUTER JOIN:</BR>
_In a RIGHT OUTER JOIN, all rows in the second-named table (the right table which appears rightmost in the JOIN clause) are included. Unmatch rows ith the left table are omitted._</BR>
```
SELECT *
FROM staff
RIGHT OUTER JOIN branch
ON staff.branchno = branch.branchno;
```

</BR>
CROSS JOIN:</BR>
_Each possible pairing of rows from the 2 tables will result in a row appearing in the result table_</BR>
</BR>
```
```


FULL JOIN:</BR>
_All rows in the joined tables are included, regardless of whether there is a match or not._</BR>
</BR>
```
```
