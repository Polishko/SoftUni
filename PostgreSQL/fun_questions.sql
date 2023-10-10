--1. Triangular numbers: Adapted from another task from @Codewars

/*A triangular number can be explained as the count of objects that form an equilateral triangle for a given n,
where each side of the triangle consists of n dots (more info: Triangular number - Wikipedia).
For example for n=1 the triangular number is 1, for n=3 the triangular number is 6 and for n = 4 the triangular number is 10.
Write a procedure sp_return_triangular_numbers, which accepts an integer n and outputs all numbers from 0 to n in one column (n)
and their corresponding triangular numbers in another column (res). You can create a table called results for this purpose before you create the procedure.
n will be always >= 0.*/

--Solution 1

CREATE TABLE IF NOT EXISTS results(
    id SERIAL PRIMARY KEY,
    n INT,
    res INT
);

CREATE OR REPLACE PROCEDURE sp_return_nth_triangular_number(num INT)
AS $$
    DECLARE
        triangular_num INT;
        counter INT := 0;
    BEGIN
        TRUNCATE results;

        WHILE counter < num + 1 LOOP

            WITH number_series(num_series) AS(
                SELECT generate_series(0, counter)
            )
                SELECT SUM(num_series)
                FROM
                    number_series INTO triangular_num;

            INSERT INTO results(n, res)
            VALUES (counter, triangular_num);
            counter = counter + 1;

        END LOOP;
    END
$$
LANGUAGE plpgsql;

CALL sp_return_nth_triangular_number(3);
SELECT * FROM results;

--Solution 2

CREATE TABLE IF NOT EXISTS results(
    id SERIAL PRIMARY KEY,
    n INT,
    res INT
);

CREATE OR REPLACE PROCEDURE sp_return_nth_triangular_number(num INT)
AS $$
    DECLARE
        triangular_num INT;
        counter INT := 0;
    BEGIN
        TRUNCATE results;

        WHILE counter < num + 1 LOOP
            triangular_num := counter * (counter + 1) / 2;

            INSERT INTO results(n, res)
            VALUES (counter, triangular_num);
            counter = counter + 1;

        END LOOP;
    END
$$
LANGUAGE plpgsql;

CALL sp_return_nth_triangular_number(6);
SELECT * FROM results;

