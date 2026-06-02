```
step 1:
CREATE TABLE char_data_types(
	varchar_column	varchar(10),
	char_column 	char(10),
	text_column		text
);

step 2:
INSERT INTO char_data_types
VALUES
	('abc','abc','abc'),
	('defghi','defghi','defghi');

step 3:
COPY char_data_types TO 'D:\postgres\postgres_sandbox\typetest.txt'
WITH (FORMAT CSV, HEADER, DELIMITER '|');

```
