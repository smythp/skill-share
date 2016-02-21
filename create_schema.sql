DROP TABLE IF EXISTS learn_skill;
DROP TABLE IF EXISTS teach_skill;
DROP TABLE IF EXISTS user;

CREATE TABLE learn_skill (
       id INTEGER primary key,
       skill_name TEXT,
       skill_description TEXT,
       creator_id INTEGER,
       target_date DATETIME
);

CREATE TABLE teach_skill (
       id INTEGER primary key,
       skill_name TEXT,
       skill_description TEXT,
       creator_id INTEGER,
       target_date DATETIME
);

CREATE TABLE user (
       id INTEGER primary key,
       first_name TEXT,
       last_name TEXT,
       email TEXT
);       

INSERT INTO learn_skill (id,skill_name,skill_description,creator_id,target_date) VALUES (0,"SQL","I want to learn about databases so I can create a data set based on Byzantine Art",0,"2016-05-10");

INSERT INTO teach_skill (id,skill_name,skill_description,creator_id,target_date) VALUES (0,"Postgres","I'm super duper at Postgres, happy to help!",0,"2016-05-10");

INSERT INTO user (id,first_name,last_name,email) VALUES (0,"Patrick","Smyth","pat@smyth.com");
