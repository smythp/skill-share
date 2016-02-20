DROP TABLE IF EXISTS skill;
DROP TABLE IF EXISTS person;

CREATE TABLE skill (
       id INTEGER primary key,
       skill_name TEXT,
       skill_description TEXT,
       creator_id INTEGER,
       target_date DATETIME
);

CREATE TABLE person (
       id INTEGER primary key,
       first_name TEXT,
       last_name TEXT,
       email TEXT
);       

INSERT INTO skill (id,skill_name,skill_description,creator_id,target_date) VALUES (0,"SQL","I want to learn about databases so I can create a data set based on Byzantine Art",0,"2016-05-10");

INSERT INTO person (id,first_name,last_name,email) VALUES (0,"Patrick","Smyth","pat@smyth.com");
