```
CREATE SCHEMA professional_notes;

CREATE TABLE professional_notes.person(
    person_id BIGINT NOT NULL,
    last_name VARCHAR(255) NOT NULL
    first_name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (person_id));

```
