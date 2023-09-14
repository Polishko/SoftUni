1.	Create a Table

CREATE TABLE minions (
	id SERIAL PRIMARY KEY,
	name VARCHAR (30),
	age INT
);

2.	Rename the Table

ALTER TABLE minions
RENAME TO minions_info;

3.	Alter the Table

ALTER TABLE minions_info
ADD COLUMN code CHAR (4),
ADD COLUMN task TEXT,
ADD COLUMN salary NUMERIC (8, 3);

4.	Rename Column

ALTER TABLE minions_info
RENAME salary TO banana;

5.	Add New Columns

ALTER TABLE minions_info
ADD COLUMN email VARCHAR (20),
ADD COLUMN equipped BOOLEAN NOT NULL; -- ADD COLUMN equipped BOOLEAN DEFAULT FALSE NOT NULL

6.	Create ENUM Type

CREATE TYPE type_mood
AS ENUM (
  'happy',
  'relaxed', 
  'stressed', 
  'sad'
);

ALTER TABLE minions_info
ADD COLUMN mood type_mood;

7.	Set Default

ALTER TABLE minions_info
ALTER COLUMN age SET DEFAULT 0,
ALTER COLUMN name SET DEFAULT '',
ALTER COLUMN code SET DEFAULT '';

8.	Add Constraints

ALTER TABLE minions_info
ADD CONSTRAINT unique_containt UNIQUE
(id, email),                          --Correct way to add constraint as standard is UQ_id_and_email
ADD CONSTRAINT banana_check
CHECK (banana > 0);                   --Corret is CK banan_is_positive_number

9.	Change Column’s Data Type

ALTER TABLE minions_info
ALTER COLUMN task
TYPE VARCHAR (150);

10.	Drop Constraint

ALTER TABLE minions_info
ALTER COLUMN equipped
DROP NOT NULL;

11.	Remove Column

ALTER TABLE minions_info
DROP COLUMN age;

12.	Table Birthdays

CREATE TABLE minions_birthdays (
	id SERIAL NOT NULL UNIQUE,  -- id INTEGER NOT NULL UNIQUE (according to qu conditions)
	name VARCHAR (50),
	date_of_birth DATE,
	age INTEGER,
	present VARCHAR (100),
	party TIMESTAMPTZ
);

13.	* Insert Into

INSERT INTO minions_info (
	id,
	name,
	code,
	task,
	banana,
	email,
	equipped,
	mood
	
)
VALUES 
	(1, 'Mark', 'GKYA', 'Graphing Points', 3265.265, 'mark@minion.com', FALSE, 'happy'),
	(2, 'Mel', 'HSK', 'Science Investigation',	54784.996, 'mel@minion.com', TRUE, 'stressed'),
	(3, 'Bob', 'HF', 'Painting', 35.652, 'bob@minion.com',	TRUE, 'happy'),
	(4, 'Darwin', 'EHND', 'Create a Digital Greeting',	321.958, 'darwin@minion.com', FALSE, 'relaxed'),
	(5, 'Kevin', 'KMHD', 'Construct with Virtual Blocks', 35214.789, 'kevin@minion.com', FALSE, 'happy'),
	(6, 'Norbert',	'FEWB',	'Testing', 3265.500, 'norbert@minion.com', TRUE, 'sad'),
	(7, 'Donny', 'L', 'Make a Map', 8.452,	'donny@minion.com',	TRUE, 'happy');
	
14.	* Select

SELECT 
	name, 
	task, 
	email, 
	banana
FROM minions_info;

15.	Truncate the Table

TRUNCATE TABLE minions_info;

16.	Drop the Table

DROP TABLE minions_birthdays;
