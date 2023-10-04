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


