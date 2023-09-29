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
