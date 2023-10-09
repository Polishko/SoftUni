--1. Database Design

CREATE TABLE IF NOT EXISTS addresses(
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(100) NOT NULL
    );

CREATE TABLE IF NOT EXISTS categories(
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS clients(
  "id" SERIAL PRIMARY KEY,
   full_name VARCHAR(50) NOT NULL,
   phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS drivers(
   "id" SERIAL PRIMARY KEY,
   first_name VARCHAR(30) NOT NULL,
   last_name VARCHAR(30) NOT NULL,
   age INT NOT NULL CHECK(age > 0),
   rating NUMERIC(10, 2) DEFAULT 5.5
);

CREATE TABLE IF NOT EXISTS cars(
    "id" SERIAL PRIMARY KEY,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20),
    year INT DEFAULT 0 NOT NULL CHECK(year > 0),
    mileage INT DEFAULT 0 CHECK(mileage > 0),
    condition CHAR(1) NOT NULL,
    category_id INT NOT NULL,
    CONSTRAINT fk_cars_categories
        FOREIGN KEY(category_id)
            REFERENCES categories(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS courses(
   "id" SERIAL PRIMARY KEY,
   from_address_id INT NOT NULL,
   start TIMESTAMP NOT NULL,
   bill NUMERIC(10, 2) DEFAULT 10 CHECK (bill > 0),
   car_id INT NOT NULL,
   client_id INT NOT NULL,
   CONSTRAINT fk_courses_addresses
        FOREIGN KEY(from_address_id)
            REFERENCES addresses(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    CONSTRAINT fk_courses_cars
        FOREIGN KEY(car_id)
            REFERENCES cars(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    CONSTRAINT fk_courses_clients
        FOREIGN KEY(client_id)
            REFERENCES clients(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS cars_drivers(
    car_id INT NOT NULL,
    driver_id INT NOT NULL,
    CONSTRAINT fk_cars_drivers_cars
        FOREIGN KEY(car_id)
            REFERENCES cars(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    CONSTRAINT fk_cars_drivers_drivers
        FOREIGN KEY(driver_id)
            REFERENCES drivers(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

--2. Insert

INSERT INTO clients(full_name, phone_number)
SELECT
    CONCAT(first_name, ' ', last_name) AS "full_name", CONCAT('(088) 9999', (id * 2)::VARCHAR)
FROM
    drivers
WHERE
    id BETWEEN 10 AND 20;

--3. Update

UPDATE cars
SET
    condition = 'C'
WHERE
    (mileage >= 800000 OR mileage IS NULL) AND
    year <= 2010 AND
    make <> 'Mercedes-Benz';

--4. Delete

DELETE FROM clients
WHERE
    id IN
    (SELECT
        cl.id
    FROM
        clients AS cl
    LEFT JOIN
        courses AS c
    ON
        cl.id = c.client_id
    WHERE
        c.id IS NULL)
;

--5. Cars

SELECT
    make,
    model,
    condition
FROM cars
ORDER BY id
;

--6.	Drivers and Cars

SELECT
    d.first_name,
    d.last_name,
    c.make,
    c.model,
    c.mileage
FROM  drivers AS d
  JOIN cars_drivers AS cd
    ON d.id = cd.driver_id
      JOIN cars AS c
        ON cd.car_id = c.id
WHERE
    c.mileage IS NOT NULL
ORDER BY
    c.mileage DESC,
    d.first_name
;

--7. Number of Courses for Each Car

SELECT
    c.id AS "car_id",
    C.make AS "make",
    c.mileage AS "mileage",
    COUNT(cr.id) AS "count_of_courses",
    CASE
        WHEN COUNT(cr.id) > 0 THEN ROUND(AVG(cr.bill), 2)
    END
        AS "average_bill"
FROM cars AS c
    LEFT JOIN courses AS cr
        ON c.id = cr.car_id
GROUP BY
    c.id,
    c.make,
    c.mileage
HAVING
    COUNT(cr.id) <> 2
ORDER BY
    count_of_courses DESC,
    c.id
;

--8.	Regular Clients

WITH clients_with_a AS
    (SELECT
         cl.id,
         cl.full_name
        FROM clients AS cl
            WHERE SUBSTRING(cl.full_name FROM 2 FOR 1) = 'a')

SELECT
    cwa.full_name,
    COUNT(co.car_id) AS "count_of_cars",
    SUM(co.bill)
FROM clients_with_a AS cwa
    JOIN courses AS co
        ON cwa.id = co.client_id
GROUP BY
    cwa.full_name
HAVING
    COUNT(co.car_id) > 1
ORDER BY
    cwa.full_name
;

--better

SELECT
    cl.full_name,
    COUNT(co.car_id) AS "count_of_cars",
    SUM(co.bill) AS "total_sum"
FROM clients AS cl
    JOIN courses AS co
        ON cl.id = co.client_id
WHERE
    SUBSTRING(cl.full_name FROM 2 FOR 1) = 'a'
GROUP BY
    cl.full_name
HAVING
    COUNT(co.car_id) > 1
ORDER BY
    cl.full_name
;

--9.	Full Information of Courses

SELECT
    a.name,
    CASE
        WHEN EXTRACT(HOUR FROM co.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE
            'Night'
    END AS "day_time",
    co.bill,
    cl.full_name,
    c.make,
    c.model,
    ca.name
FROM courses AS co
    JOIN addresses AS a
        ON co.from_address_id = a.id
            JOIN clients AS cl
                ON co.client_id = cl.id
                    JOIN cars AS c
                        ON co.car_id = c.id
                            JOIN categories AS ca
                                ON c.category_id = ca.id
ORDER BY
    co.id
;

--10.	Find all Courses by Client’s Phone Number

CREATE OR REPLACE FUNCTION fn_courses_by_client(
    IN phone_num VARCHAR(20),
    OUT number_of_courses INT
)
AS $$
    BEGIN
        SELECT
            COUNT(co.id)
        FROM clients AS cl
            JOIN courses AS co
                ON cl.id = co.client_id
        WHERE
            cl.phone_number = phone_num
        INTO number_of_courses;
    END
$$
LANGUAGE plpgsql;

--test
SELECT fn_courses_by_client('(803) 6386812')

--11.	Full Info for Address

CREATE TABLE search_results (
            id SERIAL PRIMARY KEY,
            address_name VARCHAR(50),
            full_name VARCHAR(100),
            level_of_bill VARCHAR(20),
            make VARCHAR(30),
            condition CHAR(1),
            category_name VARCHAR(50)
        );

CREATE OR REPLACE PROCEDURE sp_courses_by_address(address_name VARCHAR(100))
LANGUAGE plpgsql
AS $$
    BEGIN
        TRUNCATE search_results;

        INSERT INTO search_results (address_name, full_name, level_of_bill, make, condition, category_name)
        SELECT
            a.name,
            cl.full_name,
            CASE
                WHEN co.bill <= 20 THEN 'Low'
                WHEN co.bill <= 30 THEN 'Medium'
                ELSE 'High'
            END,
            c.make,
            c.condition,
            ca.name
        FROM courses AS co
            RIGHT JOIN addresses AS a
                ON a.id = co.from_address_id
                    JOIN clients AS cl
                        ON co.client_id = cl.id
                            JOIN cars AS c
                                ON co.car_id = c.id
                                    JOIN categories AS ca
                                        ON c.category_id = ca.id
        WHERE
            a.name = address_name
        ORDER BY
            c.make,
            cl.full_name;
    END
$$;
