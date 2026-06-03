Syntax:
```
SELECT *
FROM
  table_a JOIN table_b
ON
  table_a.key_column = table_b.foreign_key_column
```

SQL Code Example 1:
```
CREATE TABLE practical_sql.departments(
	dept_id BIGSERIAL,
	dept varchar(100),
	city varchar(100),
	CONSTRAINT dept_key PRIMARY KEY (dept_id),
	CONSTRAINT dept_city_unique UNIQUE (dept, city)
);

CREATE TABLE practical_sql.employees(
	emp_id BIGSERIAL,
	first_name varchar(100),
	last_name varchar(100),
	salary integer,
	dept_id integer REFERENCES practical_sql.departments(dept_id),
	CONSTRAINT emp_key PRIMARY KEY(emp_id),
	CONSTRAINT emp_dept_unique UNIQUE(emp_id, dept_id)
);

INSERT INTO practical_sql.departments(dept, city)
VALUES
	('Tax','Atlanta'),
	('IT','Boston');

INSERT INTO practical_sql.employees(first_name, last_name, salary, dept_id)
VALUES
	('Nancy','Jones',62500,1),
	('Lee','Smith',59300,1),
	('Soo','Nguyen',83000,2),
	('Janet','King',95000,2);


SELECT * FROM practical_sql.departments;
SELECT * FROM practical_sql.employees;

SELECT * FROM
practical_sql.employees AS emp JOIN practical_sql.departments AS dept

ON emp.dept_id = dept.dept_id;
```

SQL Code Example 2:
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
practical_sql.school_left AS scl JOIN practical_sql.school_right AS scr
ON scl.id = scr.id;
```

