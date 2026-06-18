```
CREATE TABLE apress.ttest1(
	ival1	INTEGER,
	sval1 	VARCHAR(64)
);

CREATE TABLE apress.ttest2(
	ival2	INTEGER,
	sval2	VARCHAR(64)
);

INSERT INTO apress.ttest1(ival1, sval1) VALUES(1, 'David')

BEGIN;
UPDATE apress.ttest1 SET sval1='Dave' WHERE ival1=1;

SELECT sval1 FROM apress.ttest1 WHERE ival1=1;

ROLLBACK;

SELECT sval1 FROM apress.ttest1 WHERE ival1=1;
```
