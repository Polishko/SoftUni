--1.	Database Design

CREATE TABLE IF NOT EXISTS owners(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(50) NOT NULL,
	phone_number VARCHAR(15) NOT NULL,
	address VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS animal_types(
	"id" SERIAL PRIMARY KEY,
	animal_type VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS cages(
	"id" SERIAL PRIMARY KEY,
	animal_type_id INT NOT NULL,
	CONSTRAINT fk_cages_animal_types
		FOREIGN KEY(animal_type_id)
			REFERENCES animal_types("id")
			ON UPDATE CASCADE
			ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS animals(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(30) NOT NULL,
	birthdate DATE NOT NULL,
	owner_id INT,
	animal_type_id INT NOT NULL,
	CONSTRAINT fk_animals_owners
		FOREIGN KEY(owner_id)
			REFERENCES owners("id")
			ON UPDATE CASCADE
			ON DELETE CASCADE,
	CONSTRAINT fk_animals_animal_types
		FOREIGN KEY(animal_type_id)
			REFERENCES animal_types("id")
			ON UPDATE CASCADE
			ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS volunteers_departments(
	"id" SERIAL PRIMARY KEY,
	department_name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS volunteers(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(50) NOT NULL,
	phone_number VARCHAR(15) NOT NULL,
	address VARCHAR(50),
	animal_id INT,
	department_id INT NOT NULL,
	CONSTRAINT fk_volunteers_animals
		FOREIGN KEY(animal_id)
			REFERENCES animals("id")
			ON UPDATE CASCADE
			ON DELETE CASCADE,
	CONSTRAINT fk_volunteers_volunteers_departments
		FOREIGN KEY(department_id)
			REFERENCES volunteers_departments("id")
			ON UPDATE CASCADE
			ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS animals_cages(
	cage_id INT NOT NULL,
	animal_id INT NOT NULL,
	CONSTRAINT fk_animals_cages_cages
		FOREIGN KEY(cage_id)
			REFERENCES cages("id")
			ON UPDATE CASCADE
			ON DELETE CASCADE,
	CONSTRAINT fk_animals_cages_animals
		FOREIGN KEY(animal_id)
			REFERENCES animals("id")
			ON UPDATE CASCADE
			ON DELETE CASCADE
);

--2. Insert

INSERT INTO volunteers("name", phone_number, address, animal_id, department_id)
    VALUES
        ('Anita Kostova', '0896365412',	'Sofia, 5 Rosa str.', 15, 1),
        ('Dimitur Stoev', '0877564223',	NULL,42, 4),
        ('Kalina Evtimova',	'0896321112', 'Silistra, 21 Breza str.', 9,	7),
        ('Stoyan Tomov', '0898564100',	'Montana, 1 Bor str.', 18,	8),
        ('Boryana Mileva', '0888112233', NULL, 31,	5)
;

INSERT INTO animals("name", birthdate, owner_id, animal_type_id)
    VALUES
        ('Giraffe', '2018-09-21',	21,	1),
        ('Harpy Eagle', '2015-04-17', 15, 3),
        ('Hamadryas Baboon', '2017-11-02', NULL, 1),
        ('Tuatara', '2021-06-30', 2, 4)
;

--3. Update

UPDATE animals
SET owner_id = 4
WHERE owner_id IS NULL;

--4. Delete

DELETE FROM volunteers_departments
WHERE department_name = 'Education program assistant';

--5. Volunteers

SELECT
    "name",
    phone_number,
    address,
    animal_id,
    department_id
FROM
    volunteers
ORDER BY
    "name",
    animal_id,
    department_id
;

--6.	Animals Data

SELECT
    a."name",
    at.animal_type,
    TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS "birthdate"
FROM animals AS a
    JOIN animal_types AS at
        ON a.animal_type_id = at.id
ORDER BY
    a."name"
;

--7.	Owners and Their Animals

SELECT
    o."name" AS "owner",
    COUNT(*) AS "count_of_animals"
FROM owners AS o
    LEFT JOIN animals AS a
        ON o.id = a.owner_id
GROUP BY
    o."name"
ORDER BY
    "count_of_animals" DESC,
    "owner"
LIMIT
    5
;

--8. Owners, Animals and Cages

SELECT
    CONCAT(o."name", ' - ', a."name") AS "Owners - Animals",
    o.phone_number AS "Phone Number",
    ac.cage_id AS "Cage ID"
FROM owners AS o
    JOIN animals AS a
        ON o.id = a.owner_id
            JOIN animal_types AS at
                ON a.animal_type_id = at.id
                    JOIN animals_cages AS ac
                        ON a.id = ac.animal_id
WHERE
    at.animal_type = 'Mammals'
ORDER BY
    o."name",
    a."name" DESC
;

--9.	Volunteers in Sofia

SELECT
    v."name" AS "volunteers",
    v.phone_number,
    TRIM(SUBSTRING(v.address, POSITION(',' IN v.address) + 1)) AS "address"
FROM volunteers AS v
    JOIN volunteers_departments AS vd
        ON v.department_id = vd.id
WHERE
    vd.department_name = 'Education program assistant' AND
    v.address LIKE '%Sofia%'
ORDER BY
    v."name"
;

--10.	Animals for Adoption

SELECT
    a."name" AS "animal",
    EXTRACT(YEAR FROM a.birthdate) AS "birth_year",
    at.animal_type
FROM animals AS a
    JOIN animal_types AS at
        ON a.animal_type_id = at.id
WHERE
    a.owner_id IS NULL AND
    EXTRACT(YEAR FROM AGE('01-01-2022', a.birthdate)) < 5 AND
    at.animal_type <> 'Birds'
ORDER BY
    a."name"
;

--11.	All Volunteers in a Department

CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
searched_volunteers_department VARCHAR(30)
)

RETURNS INT AS
$$
    DECLARE
        volunteers_count INT;
    BEGIN
        SELECT COUNT(*) INTO volunteers_count
        FROM volunteers_departments AS vd
                JOIN volunteers AS v
                    ON vd.id = v.department_id
            WHERE
                department_name = searched_volunteers_department;
    RETURN volunteers_count;
    END;
$$
LANGUAGE plpgsql;

--test
SELECT fn_get_volunteers_count_from_department('Zoo events')


--12. Animals with Owner or Not


