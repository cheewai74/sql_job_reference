
Syntax:</BR>
```
CREATE VIEW view_name [(column_name[,....n])]
AS
select_statement
```


Example:</BR>
```
CREATE VIEW ManagerView
AS SELECT * FROM staff
WHERE branchno = 1

select * from managerview
```
