--1.	Booked for Nights

SELECT
	CONCAT(a.address, ' ', a.address_2) AS "Apartment Address",
	b.booked_for AS "Nights"
FROM bookings AS b
	JOIN apartments AS a
		ON b.booking_id = a.booking_id
ORDER BY a.apartment_id
;

--2.	First 10 Apartments Booked At

SELECT
	a.name AS "Name",
	a.country AS "Country",
	b.booked_at::DATE AS "Booked at"
FROM apartments AS a
	LEFT JOIN bookings AS b
		ON b.booking_id = a.booking_id
LIMIT
	10
;

--3.	First 10 Customers with Bookings

SELECT
	b.booking_id AS "Booking ID",
	b.starts_at::DATE AS "Start Date",
	b.apartment_id AS "Apartment ID",
	CONCAT(c.first_name, ' ', c.last_name) AS "Customer Name"
FROM bookings AS b
	RIGHT JOIN customers AS c
		ON b.customer_id = c.customer_id
ORDER BY
	"Customer Name"
LIMIT
	10
;

-- 4.	Booking Information

SELECT
	b.booking_id AS "Booking ID",
	a.name AS "Apartment Owner",
	a.apartment_id AS "Apartment ID",
	CONCAT(c.first_name, ' ', c.last_name) AS "Customer Name"
FROM bookings AS b
	FULL JOIN apartments AS a
		ON b.booking_id = a.booking_id
			FULL JOIN customers AS c
				ON b.customer_id = c.customer_id
ORDER BY
	"Booking ID",
	"Apartment Owner",
	"Customer Name"
;

--5. Multiplication of Information**

SELECT
	b.booking_id AS "Booking ID",
	c.first_name AS "Customer Name"
FROM bookings AS b
	CROSS JOIN customers AS c
;

--6. Unassigned Apartments

SELECT
	b.booking_id,
	b.apartment_id,
	c.companion_full_name
FROM bookings AS b
	JOIN customers AS c
		ON b.customer_id = c.customer_id
WHERE b.apartment_id IS NULL
;

--7. Bookings Made by Lead

SELECT
	b.apartment_id,
	b.booked_for,
	c.first_name,
	c.country
FROM bookings AS b
	JOIN customers AS c
		ON b.customer_id = c.customer_id
WHERE c.job_type LIKE '%Lead%'
;

--8. Hahn's Bookings

SELECT
	COUNT(c.customer_id)
FROM bookings AS b
	JOIN customers AS c
		ON b.customer_id = c.customer_id
WHERE c.last_name = 'Hahn'
;

--9. Total Sum of Nights

SELECT
	a.name,
	SUM(b.booked_for)
FROM apartments AS a
	JOIN bookings AS b
		ON b.apartment_id = b.apartment_id
WHERE b.apartment_id = a.apartment_id
GROUP BY
	a.name
ORDER BY
	a.name
;

--OR

SELECT
	a.name,
	SUM(b.booked_for)
FROM apartments AS a, bookings AS b
WHERE b.apartment_id = a.apartment_id
GROUP BY
	a.name
ORDER BY
	a.name
;

--10. Popular Vacation Destination

SELECT
	a.country,
	COUNT(*) AS "booking_count"
FROM apartments AS a
	JOIN bookings AS b
		ON a.apartment_id = b.apartment_id
WHERE b.booked_at > '2021-05-18 07:52:09.904+03' AND b.booked_at < '2021-09-17 19:48:02.147+03'
GROUP BY
	a.country
ORDER BY
	"booking_count" DESC
;

--11. Bulgaria's Peaks Higher than 2835 Meters

SELECT
	mc.country_code,
	m.mountain_range,
	p.peak_name,
	p.elevation
FROM
	mountains_countries AS mc
		JOIN mountains AS m
			ON mc.mountain_id = m.id
				JOIN peaks AS p
					ON m.id = p.mountain_id
WHERE
	p.elevation > 2835 AND mc.country_code = 'BG'
ORDER BY
	p.elevation DESC
;

--12. Count Mountain Ranges

SELECT
	mc.country_code,
	COUNT(m.mountain_range) AS "mountain_range_count"
FROM
	mountains_countries AS mc
		JOIN mountains AS m
			ON mc.mountain_id = m.id
WHERE
	mc.country_code IN ('US', 'RU', 'BG')
GROUP BY
	mc.country_code
ORDER BY
	COUNT(m.mountain_range) DESC
;

--13. Rivers in Africa

SELECT
	c.country_name,
	r.river_name
FROM countries AS c
	LEFT JOIN countries_rivers AS cr
		ON c.country_code = cr.country_code
			LEFT JOIN rivers AS r
				ON cr.river_id = r.id
WHERE
	c.continent_code = 'AF'
ORDER BY
	c.country_name
LIMIT
	5
;

--14. Minimum Average Area Across Continents

SELECT MIN(area) AS "min_average_area"
FROM (
	SELECT
		c.continent_code,
		SUM(c.area_in_sq_km)/COUNT(c.country_code)::NUMERIC AS "area"
	FROM countries as c
	GROUP BY
		c.continent_code		 
	) AS subquery
;

--15. Countries Without Any Mountains

SELECT 
	COUNT(no_mountains) AS "countries_without_mountains"	
	FROM (
		SELECT
			c.country_name
		FROM countries AS c
			LEFT JOIN mountains_countries AS mc
				ON c.country_code = mc.country_code
		WHERE
			mc.mountain_id IS NULL) AS no_mountains
;

--16. Monasteries by Country **

CREATE TABLE monasteries (
	id SERIAL PRIMARY KEY,
	monastery_name VARCHAR(255),
	country_code CHAR(2)
);

INSERT INTO monasteries(monastery_name, country_code)
VALUES
	('Rila Monastery "St. Ivan of Rila"', 'BG'),
	('Bachkovo Monastery "Virgin Mary"', 'BG'),
	('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
	('Kopan Monastery', 'NP'),
	('Thrangu Tashi Yangtse Monastery', 'NP'),
	('Shechen Tennyi Dargyeling Monastery', 'NP'),
	('Benchen Monastery', 'NP'),
	('Southern Shaolin Monastery', 'CN'),
	('Dabei Monastery', 'CN'),
	('Wa Sau Toi', 'CN'),
	('Lhunshigyia Monastery', 'CN'),
	('Rakya Monastery', 'CN'),
	('Monasteries of Meteora', 'GR'),
	('The Holy Monastery of Stavronikita', 'GR'),
	('Taung Kalat Monastery', 'MM'),
	('Pa-Auk Forest Monastery', 'MM'),
	('Taktsang Palphug Monastery', 'BT'),
	('Sümela Monastery', 'TR');

ALTER TABLE countries
ADD COLUMN three_rivers BOOLEAN DEFAULT FALSE;

UPDATE countries AS c
SET three_rivers = 'true'
FROM (
	SELECT
		c.country_code,
		COUNT(cr.river_id) AS river_count
	FROM countries AS c
		LEFT JOIN countries_rivers AS cr
			ON c.country_code = cr.country_code
				GROUP BY
					c.country_code
		) AS rc

WHERE rc.country_code = c.country_code AND rc.river_count > 3
;

SELECT
	m.monastery_name AS "Monastery",
	c.country_name AS "Country"
FROM monasteries AS m
	JOIN countries AS c
		ON m.country_code = c.country_code
WHERE c.three_rivers = 'false'
ORDER BY
	m.monastery_name
;

-- 17. Monasteries by Continents and Countries**

UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar';

INSERT INTO monasteries (monastery_name, country_code)
VALUES
	('Hanga Abbey', (SELECT
				c.country_code
			FROM
				countries AS c
			WHERE
				c.country_name = 'Tanzania'
					)),
	('Myin-Tin-Daik', (SELECT
				c.country_code
			FROM
				countries AS c
			WHERE
				c.country_name = 'Myanmar'
					))
;				

SELECT
	cn.continent_name AS "Continent Name",
	c.country_name AS "Country Name",
	COUNT(m.monastery_name) AS "Monasteries Count"
FROM
	continents AS cn
	LEFT JOIN countries AS c
		ON cn.continent_code = c.continent_code
			LEFT JOIN monasteries AS m
				ON c.country_code = m.country_code
WHERE c.three_rivers = 'false'
GROUP BY
	cn.continent_name,
	c.country_name
ORDER BY
	COUNT(m.monastery_name) DESC,
	c.country_name
;

--18. Retrieving Information about Indexes

SELECT
	tablename,
	indexname,
	indexdef
FROM
	pg_indexes
WHERE
	schemaname = 'public'
ORDER BY
	tablename,
	indexname
;

--19. * Continents and Currencies

CREATE VIEW continent_currency_usage AS
    WITH cte AS (
        SELECT
            co.continent_code,
            c.currency_code,
            COUNT(c.currency_code) AS "currency_usage",
            DENSE_RANK() OVER (PARTITION BY co.continent_code ORDER BY COUNT(c.currency_code) DESC) AS rn
        FROM countries AS c
            JOIN continents AS co
                ON c.continent_code = co.continent_code
        GROUP BY
            co.continent_code,
            c.currency_code
        HAVING
            COUNT(c.currency_code) > 1
        ORDER BY
            currency_usage DESC
        )
    SELECT
        continent_code,
        currency_code,
        currency_usage
    FROM cte
    WHERE rn = 1
;

--20. * The Highest Peak in Each Country

WITH row_number AS(
    SELECT
        c.country_name AS "Country",
        p.peak_name AS "Highest Peak Name",
        p.elevation AS "Highest Peak Elevation",
        m.mountain_range AS "Mountain",
       DENSE_RANK() OVER (PARTITION BY c.country_name ORDER BY p.elevation DESC) AS rn
    FROM countries AS c
        LEFT JOIN mountains_countries AS mc
            ON c.country_code = mc.country_code
                LEFT JOIN mountains AS m
                    ON mc.mountain_id = m.id
                        LEFT JOIN peaks AS p
                            ON m.id = p.mountain_id
)

    SELECT
        "Country",
        COALESCE("Highest Peak Name", '(no highest peak)') AS "Highest Peak Name",
        COALESCE("Highest Peak Elevation", 0) AS "Highest Peak Elevation",
        CASE
            WHEN "Highest Peak Name" IS NULL THEN '(no mountain)'
            ELSE "Mountain"
        END AS "Mountain"
    FROM row_number
    WHERE rn = 1
    ORDER BY
        "Country",
        "Highest Peak Elevation" DESC
;



