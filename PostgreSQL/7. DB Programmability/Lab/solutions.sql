--1.	Count Employees by Town

CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
AS $$
    DECLARE
        count INT;
    BEGIN
        SELECT
	        COUNT(e.employee_id) INTO count
        FROM towns AS t
	        JOIN addresses AS a
		        ON t.town_id = a.town_id
			        JOIN employees AS e
				        ON a.address_id = e.address_id
        WHERE t."name" = town_name;
        RETURN count;
    END;
$$ LANGUAGE plpgsql;

-- OR

CREATE OR REPLACE FUNCTION fn_count_employees_by_town(
IN town_name VARCHAR(20),
OUT count INT)

AS $$

    BEGIN
        SELECT
	        COUNT(e.employee_id) INTO count
        FROM towns AS t
	        JOIN addresses AS a
		        ON t.town_id = a.town_id
			        JOIN employees AS e
				        ON a.address_id = e.address_id
        WHERE t."name" = town_name;

    END;
$$ LANGUAGE plpgsql;

-- OR

CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
AS $$
    DECLARE
    BEGIN
        RETURN
        (SELECT
	        COUNT(e.employee_id)
        FROM towns AS t
	        JOIN addresses AS a
		        ON t.town_id = a.town_id
			        JOIN employees AS e
				        ON a.address_id = e.address_id
        WHERE t."name" = town_name);
    END;
$$ LANGUAGE plpgsql;


-- test:
SELECT fn_count_employees_by_town(NULL)

--2.	Employees Promotion

CREATE PROCEDURE sp_increase_salaries(department_name VARCHAR(50))
AS
$$
    BEGIN
            UPDATE employees AS e
            SET salary = salary * 1.05
            WHERE e.department_id = (
                SELECT
                    d.department_id
                FROM
                    departments as d
                WHERE
                    d.name = department_name
                );
    END;
$$ LANGUAGE plpgsql;

--OR

CREATE PROCEDURE sp_increase_salaries(department_name VARCHAR(50))
AS
$$
    BEGIN
            UPDATE employees AS e
            SET salary = salary * 1.05
            WHERE e.department_id = (
                SELECT
                    d.department_id
                FROM
                    departments as d
                JOIN
                    employees AS e
                ON
                    d.department_id = e.department_id
                WHERE
                    d.name = department_name
                GROUP BY
                    d.department_id
                );
    END;
$$ LANGUAGE plpgsql;



--test

CALL sp_increase_salaries('Finance');

--3.	Employees Promotion by ID

--a) not a very correct query but an invalid/non-existent id returns null values for both the name areas so it works

CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
AS
$$
    DECLARE
        temp_emp_first_name VARCHAR(50);
        temp_emp_last_name VARCHAR(50);
    BEGIN
        temp_emp_first_name = (
        SELECT e.first_name
        FROM employees AS e
        WHERE e.employee_id = id
            );

        temp_emp_last_name = (
        SELECT e.last_name
        FROM employees AS e
        WHERE e.employee_id = id
            );

        IF temp_emp_first_name IS NULL AND temp_emp_last_name IS NULL THEN
            RETURN;
        ELSE
            UPDATE employees AS e
                SET salary = salary * 1.05
                WHERE e.employee_id = id;
        END IF;
        COMMIT;
        RETURN;
    END
$$
    LANGUAGE plpgsql;

--b) better version, directly checking the count of employees that have the given id

CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
AS
$$
    BEGIN
        IF (SELECT COUNT(*) FROM employees AS e WHERE e.employee_id = id) <> 1 THEN
            ROLLBACK; --Here RETURN is better because no change is made yet
        ELSE
            UPDATE employees AS e
                SET salary = salary * 1.05
                WHERE e.employee_id = id;
        END IF;
        COMMIT;
    END
$$
    LANGUAGE plpgsql;

--4.	Triggered

CREATE TABLE deleted_employees(
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	middle_name VARCHAR(20),
	job_title VARCHAR(50),
	department_id INT,
	salary NUMERIC(19,4)
);

CREATE OR REPLACE FUNCTION log_fired_employees()
RETURNS TRIGGER AS
$$
    BEGIN
        INSERT INTO deleted_employees(first_name, last_name, middle_name, job_title, department_id)
        VALUES (old.first_name, old.last_name, old.middle_name, old.job_title, old.department_id);
        RETURN NULL;
    END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER log_fired_employees_trigger
AFTER DELETE
ON employees
FOR EACH ROW
EXECUTE FUNCTION log_fired_employees();






