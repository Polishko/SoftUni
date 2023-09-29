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

