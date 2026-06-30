```
CREATE SCHEMA professional_notes;

CREATE TABLE professional_notes.person_from_select (
    person_id BIGINT NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    age INT NOT NULL,
    PRIMARY KEY (person_id));

CREATE TABLE professional_notes.person_over_30 AS SELECT * FROM professional_notes.person_from_select WHERE age > 30;

CREATE TABLE professional_notes.person (
    person_id BIGINT NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    PRIMARY KEY (person_id));

CREATE UNLOGGED TABLE professional_notes.person_unlogged(
    person_id BIGINT NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    PRIMARY KEY (person_id));

```
