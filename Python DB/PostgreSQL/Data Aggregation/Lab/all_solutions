1.	Departments Info (by id)
# counts all employees regardless of whether they have salary or not (null)

SELECT 
	department_id,
	COUNT(id) AS "employee_count" 
FROM employees
GROUP BY department_id
ORDER BY department_id;

2.	Departments Info (by salary)
# counts only number of employees that have salary information 

SELECT
	department_id,
	COUNT(salary) AS "employee_count"
FROM employees
GROUP BY "department_id"
ORDER BY "department_id";

3.	Sum Salaries per Department

SELECT
	department_id,
	SUM(salary) AS "total_salaries"
FROM employees
GROUP BY "department_id"
ORDER BY "department_id";

4.	Maximum Salary per Department

SELECT
	department_id,
	MAX(salary) AS "max_salary"
FROM employees
GROUP BY "department_id"
ORDER BY "department_id";

5.	Minimum Salary per Department

SELECT
	department_id,
	MIN(salary) AS "min_salary"
FROM employees
GROUP BY "department_id"
ORDER BY "department_id";

6.	Average Salary per Department

SELECT
	department_id,
	AVG(salary) AS "avg_salary"
FROM employees
GROUP BY "department_id"
ORDER BY "department_id";

7.	Filter Total Salaries

SELECT
	department_id,
	SUM(salary) AS "Total Salary"
FROM employees
GROUP BY "department_id"
HAVING SUM(salary) < 4200
ORDER BY "department_id";

8.	Department Names

SELECT
	id, first_name, last_name, TRUNC(salary, 2) AS "salary", department_id,
	CASE department_id
		WHEN 1 THEN 'Management'
		WHEN 2 THEN 'Kitchen Staff'
		WHEN 3 THEN 'Service Staff'
	ELSE 'Other'
	END AS "department_name"	
FROM employees
ORDER BY id;



