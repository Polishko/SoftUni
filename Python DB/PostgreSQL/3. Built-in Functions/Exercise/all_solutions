1. River Info

CREATE VIEW view_river_info AS
SELECT CONCAT(       --Better to use CONCAT_WS here because separator is " " everywhere
	'The river',
	' ',
	"river_name",
	' ',
	'flows into the',
	' ', "outflow",
	' ',
	'and is',
	' ', "length",
	' ',
	'kilometers long.')
	AS "River Information"
FROM rivers
ORDER BY river_name;

2. Concatenate Geography Data

CREATE VIEW view_continents_countries_currencies_details AS
SELECT
	CONCAT(continents.continent_name, ': ', continents.continent_code) AS "Continent Details",
	CONCAT(countries.country_name, ' - ', countries.capital, ' - ', countries.area_in_sq_km, ' - km2') AS "Country Information",
	CONCAT(currencies.description, ' (', currencies.currency_code, ')') AS "Currencies"
FROM 
	continents, countries, currencies
WHERE                                                                   -- Can use JOIN() here
	countries.continent_code = continents.continent_code
	AND currencies.currency_code = countries.currency_code 
ORDER BY "Country Information";

3. Capital Code

ALTER TABLE countries
ADD COLUMN "capital_code" VARCHAR(25);

UPDATE countries
SET "capital_code" = SUBSTRING(capital, 1, 2);

4. (Descr)iption

SELECT SUBSTRING(description, 5) AS substring
FROM currencies;

5. Substring River Length

SELECT SUBSTRING("River Information", '([0-9]{1,4})') AS "river_length"  --with REGEX_MATCHING() [1] also possible
FROM view_river_info;

6. Replace A

SELECT 
	REPLACE(mountain_range, 'a', '@') AS replace_a,
	REPLACE(mountain_range, 'A', '$') AS replace_A		
FROM mountains;

7. Translate

SELECT 
	capital,
	TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou') AS "translated_name"
FROM countries;

8. LEADING

SELECT
	continent_name,
	TRIM(LEADING FROM continent_name) AS "trim"
FROM continents;

9. TRAILING

SELECT
	continent_name,
	TRIM(TRAILING FROM continent_name) AS "trim"                   --Can use LTRIM() as well
FROM continents;

10. LTRIM & RTRIM

SELECT
	TRIM(LEADING 'M' FROM peak_name) AS "Left Trim",    --Can write as LTRIM()
	TRIM(TRAILING 'm' FROM peak_name) AS "Right Trim"   --Can write as RTRIM()
FROM peaks;

11. Character Length and Bits

SELECT 
	CONCAT(mountains.mountain_range, ' ', peaks.peak_name) AS "Mountain Information",
	LENGTH(CONCAT(mountains.mountain_range, ' ', peaks.peak_name)) AS "Characters Length", --CHAR_LENGTH() would be more correct here length gıves bytes
	BIT_LENGTH(CONCAT(mountains.mountain_range, ' ', peaks.peak_name)) AS "Bits of a String"   
FROM mountains, peaks
WHERE mountains.id = peaks.mountain_id;

12. Length of a Number

SELECT
	population,
	LENGTH(CAST(population AS TEXT)) AS "length"
FROM countries;

13. Positive and Negative LEFT

SELECT
	peak_name,
	LEFT(peak_name, 4) AS "Positive Left",
	LEFT(peak_name, -4) AS "Negative Left"
FROM peaks;

14. Positive and Negative RIGHT

SELECT
	peak_name,
	RIGHT(peak_name, 4) AS "Positive Left",
	RIGHT(peak_name, -4) AS "Negative Left"
FROM peaks;

15. Update iso_code

UPDATE countries
SET iso_code = UPPER(LEFT(country_name, 3))
WHERE iso_code IS NULL;

16. REVERSE country_code

UPDATE countries
SET country_code = REVERSE(LOWER(country_code));

17. Elevation --->> Peak Name

SELECT CONCAT(elevation, ' ', REPEAT('-', 3), REPEAT('>', 2), ' ', peak_name) AS "Elevation --->> Peak Name"        --CONCAT_WS() can be also used
FROM peaks
WHERE elevation >= 4884

18. Arithmetical Operators

--All this can be done using CAST() in AS SELECT during table creation

CREATE TABLE bookings_calculation AS
SELECT booked_for
FROM bookings
WHERE bookings.apartment_id = 93;

ALTER TABLE bookings_calculation
ADD COLUMN multiplication NUMERIC,
ADD COLUMN modulo NUMERIC;

UPDATE bookings_calculation
SET 
	multiplication = bookings_calculation.booked_for * 50,
	modulo = bookings_calculation.booked_for % 50;

19. ROUND vs TRUNC

SELECT
	latitude,
	ROUND(latitude, 2) AS "round",
	TRUNC(latitude, 2) AS "trunc"
FROM apartments;

20. Absolute Value

SELECT
	longitude,
	ABS(longitude) AS "abs"
FROM apartments;

21. Billing Day**

ALTER TABLE bookings
ADD COLUMN billing_day TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP;

SELECT
	billing_day,
	TO_CHAR(billing_day, 'DD "Day" MM "Month" YYYY "Year" HH24:MI:SS') AS "Billing Day"
FROM bookings;

22. EXTRACT Booked At

SELECT
	EXTRACT(YEAR FROM (booked_at AT TIME ZONE 'UTC')),
	EXTRACT(MONTH FROM (booked_at AT TIME ZONE 'UTC')),
	EXTRACT(DAY FROM (booked_at AT TIME ZONE 'UTC')),
	EXTRACT(HOUR FROM (booked_at AT TIME ZONE 'UTC')),
	EXTRACT(MINUTE FROM (booked_at AT TIME ZONE 'UTC')),
	CEILING(EXTRACT(SECOND FROM (booked_at AT TIME ZONE 'UTC')))
FROM bookings;

23. Early Birds**

SELECT
	user_id,
	AGE(starts_at, booked_at) AS "Early Birds"
FROM bookings
WHERE AGE(starts_at, booked_at) >= '10 months';   --Or WHERE starts_at - booked_at >= '10 MONTHS'

24. Match or Not

SELECT "companion_full_name", "email"
FROM users
WHERE LOWER("companion_full_name") LIKE '%and%' AND "email" NOT LIKE '%@gmail';  --Or use ILIKE which is case insensitive like

25. * COUNT by Initial

SELECT
	SUBSTRING("first_name", 1, 2) AS "initials",
	COUNT(SUBSTRING("first_name", 1, 2)) AS "user_count"
FROM users
GROUP BY "initials"
ORDER BY "user_count" DESC, "initials";

26. * SUM

SELECT
	SUM(booked_for) AS "total_value"
FROM
	bookings
WHERE apartment_id = 90
GROUP BY
	apartment_id;

27. * Average Value

SELECT
	AVG(multiplication) AS "average_value"
FROM
	bookings_calculation




