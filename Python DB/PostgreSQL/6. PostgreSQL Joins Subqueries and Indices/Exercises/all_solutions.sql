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
	FROM (SELECT
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



