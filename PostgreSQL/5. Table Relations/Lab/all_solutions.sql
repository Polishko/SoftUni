1. 1. Mountains and Peaks

CREATE TABLE mountains (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE peaks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	mountain_id INT,
	CONSTRAINT fk_peaks_mountains
		FOREIGN KEY(mountain_id)
			REFERENCES mountains(id)
	
);

2. Trip Organization

SELECT
	v.driver_id,
	v.vehicle_type,
	CONCAT(c.first_name, ' ', c.last_name) AS driver_name
FROM vehicles AS v JOIN
	campers AS c ON
		v.driver_id = c.id
;

3. SoftUni Hiking

SELECT
	r.start_point,
	r.end_point,
	r.leader_id,
	CONCAT(c.first_name, ' ', c.last_name) AS leader_name
FROM routes AS r JOIN
	campers AS c ON
		r.leader_id = c.id
;

4. Delete Mountains

--to drop existing tables
DROP CONSTRAINT fk_peaks_mountains;

DROP TABLE peaks;
DROP TABLE mountains;

--or use
DROP TABLE mountains CASCADE;
DROP TABLE peaks;

-- for Judge

CREATE TABLE mountains (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE peaks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	mountain_id INT,
	CONSTRAINT fk_mountain_id
		FOREIGN KEY(mountain_id)
			REFERENCES mountains(id)
				ON DELETE CASCADE
);

5. Project Management DB*

CREATE DATABASE project_management_db;

CREATE TABLE clients (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE projects (
	id SERIAL PRIMARY KEY,
	client_id INT,
	project_lead_id INT,
	CONSTRAINT fk_projects_clients
		FOREIGN KEY(client_id)
			REFERENCES clients(id)
);

CREATE TABLE employees (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	project_id INT,
	CONSTRAINT fk_employees_projects
		FOREIGN KEY(project_id)
			REFERENCES projects(id)
);

ALTER TABLE projects
ADD CONSTRAINT fk_projects_employees
	FOREIGN KEY(project_lead_id)
		REFERENCES employees(id)
;

