1.	Create New Database

CREATE DATABASE gamebar;

2.	Create Tables	

CREATE TABLE employees (
	id SERIAL PRIMARY KEY NOT NULL,
	first_name VARCHAR (30),
	last_name VARCHAR (50),
	hiring_date DATE DEFAULT '2023-01-01',
	salary NUMERIC(10, 2),
	devices_number INT
);
CREATE TABLE departments (
	id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR (50),
	code CHAR (3),
	description TEXT
	
);
CREATE TABLE issues (
	id SERIAL PRIMARY KEY NOT NULL,
	description VARCHAR (150),
	date DATE,
	start TIMESTAMP
);

3.	Insert Data in Tables

INSERT INTO employees (
	id,
	first_name,
	last_name,
	hiring_date,
	salary,
	devices_number
)

VALUES 
	(1, 'Susan', 'Powell', '08-08-2020', 1000, 3),
	(2, 'Adam', 'White', '07-21-2021', 800, 2),
	(3, 'Myriam', 'Jhones', '04-23-2022', 1500, 4);

4.	Alter Tables

ALTER TABLE employees
ADD COLUMN middle_name VARCHAR (50);

5.	Add Constraints

ALTER TABLE employees
ALTER COLUMN salary SET NOT NULL,
ALTER COLUMN salary SET DEFAULT 0,
ALTER COLUMN hiring_date SET NOT NULL;

6.	Modify Columns

ALTER TABLE employees
ALTER COLUMN middle_name TYPE VARCHAR (100);

7.	Truncate Tables

TRUNCATE TABLE issues;

8.	Drop Tables

DROP TABLE departments;

