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

-- test:
SELECT fn_count_employees_by_town(NULL)

--2.	Employees Promotion
