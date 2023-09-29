-- 1.	Towns Addresses

SELECT
	t.town_id,
	t.name AS "town_name",
	a.address_text
FROM towns AS t
JOIN addresses AS a
ON t.town_id = a.town_id
WHERE t.name IN ('San Francisco', 'Sofia', 'Carnation')
ORDER BY t.town_id, a.address_id
;

-- 2.	Managers

SELECT
	e.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	d.department_id,
	d.name AS "department_name"
FROM employees AS e
	RIGHT JOIN departments AS d
		ON d.manager_id = e.employee_id
ORDER BY
	e.employee_id
LIMIT
	5
;

--or

SELECT
	e.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	d.department_id,
	d.name AS "department_name"
FROM departments AS d
	LEFT JOIN employees AS e
		ON e.employee_id = d.manager_id
ORDER BY
	e.employee_id
LIMIT 5
;

--3.	Employees’ Projects

SELECT
	ep.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS "full_name",
	ep.project_id,
	p.name AS "project_name"	
FROM employees_projects AS ep
	JOIN employees AS e
		ON ep.employee_id = e.employee_id
			JOIN projects AS p
				ON ep.project_id = p.project_id
WHERE ep.project_id = 1	
;

-- 4.	Higher Salary

SELECT
COUNT(employee_id) AS "count"
FROM employees
WHERE salary > (SELECT AVG(salary) as "ave_salary"
				        FROM employees
			          HAVING AVG(salary) IS NOT NULL)
;



