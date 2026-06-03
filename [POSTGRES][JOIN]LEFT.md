LEFT JOIN Example:

```
CREATE TABLE practical_sql.school_left(
	id integer CONSTRAINT left_id_key PRIMARY KEY,
	left_school varchar(30)
);

CREATE TABLE practical_sql.school_right(
	id integer CONSTRAINT right_id_key PRIMARY KEY,
	right_school varchar(30)
);

INSERT INTO practical_sql.school_left(id, left_school)
VALUES 
	(1, 'Oak Street School'),
	(2, 'Roosevel High School'),
	(5, 'Washington Middle School'),
	(6, 'Jefferson High School');

INSERT INTO practical_sql.school_right(id, right_school)
VALUES
	(1, 'Oak Street School'),
	(2, 'Roosevel High School'),
	(3, 'Morrison Elementary'),
	(4, 'Chase Magnet Academy'),
	(6, 'Jefferson High School');

SELECT * FROM
practical_sql.school_left AS scl LEFT JOIN practical_sql.school_right AS scr
ON scl.id = scr.id;
```
