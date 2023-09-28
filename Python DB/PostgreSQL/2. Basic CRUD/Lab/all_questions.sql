1.	Select and Display Employee Information by Concatenating Columns

SELECT 
	id,
	first_name || ' ' || last_name AS "Full Name",
	job_title AS "Job Title"
FROM employees;

2.	Select Employees by Filtering and Ordering

SELECT id,
	first_name || ' ' || last_name as "full_name",
	job_title,
	salary
FROM employees
WHERE salary > 1000.00
ORDER BY id;

3.	Select Employees by Multiple Filters

SELECT *
FROM employees
WHERE department_id = 4 AND salary >= 1000
ORDER BY id;

4.	Insert Data into Employees Table

INSERT INTO employees 
	(first_name, last_name, job_title, department_id, salary)
VALUES
	('Samantha', 'Young', 'Housekeeping', 4, 900),
	('Roger', 'Palmer', 'Waiter', 3, 928.33);

SELECT *
FROM employees;

5.	Update Employees Salary

UPDATE employees
SET salary = salary + 100
WHERE job_title = 'Manager';

SELECT *
FROM employees
WHERE job_title = 'Manager';

6.	Delete from Table

DELETE FROM employees
WHERE department_id = 1 OR department_id = 2;

SELECT *
FROM employees
ORDER BY id;

7.	Create a View for Top Paid Employee

CREATE VIEW top_paid_empl AS
SELECT * FROM employees
ORDER BY salary DESC LIMIT 1;

SELECT *
FROM top_paid_empl;
