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
FROM
    drivers AS d
JOIN
    cars_drivers AS cd
ON
    d.id = cd.driver_id
JOIN
        cars AS c
ON
    cd.car_id = c.id
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


