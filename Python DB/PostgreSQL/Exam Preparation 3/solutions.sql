--1.	Database Design

CREATE TABLE categories(
    id	SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE addresses(
    id SERIAL PRIMARY KEY,
    street_name VARCHAR(100) NOT NULL,
    street_number INT NOT NULL CHECK(street_number > 0),
    town VARCHAR(30) NOT NULL,
    country VARCHAR(50) NOT NULL,
    zip_code INT NOT NULL CHECK(zip_code > 0)
);

CREATE TABLE publishers(
    id	SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    address_id	INT NOT NULL,
    website	VARCHAR(40),
    phone	VARCHAR(20),
    CONSTRAINT fk_publishers_addresses
        FOREIGN KEY(address_id)
            REFERENCES addresses(id)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE players_ranges(
    id SERIAL PRIMARY KEY,
    min_players INT NOT NULL CHECK(min_players > 0),
    max_players INT NOT NULL CHECK(max_players > 0)
);

CREATE TABLE creators(
    id	SERIAL PRIMARY KEY,
    first_name	VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL
);

CREATE TABLE board_games(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    release_year INT NOT NULL CHECK(release_year > 0),
    rating NUMERIC(10, 2) NOT NULL,
    category_id INT NOT NULL,
    publisher_id INT NOT NULL,
    players_range_id INT NOT NULL,
    CONSTRAINT fk_board_games_categories
        FOREIGN KEY(category_id)
            REFERENCES categories(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    CONSTRAINT fk_board_games_publishers
        FOREIGN KEY(publisher_id)
            REFERENCES publishers(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    CONSTRAINT fk_board_games_players_ranges
        FOREIGN KEY(players_range_id)
            REFERENCES players_ranges(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
);

CREATE TABLE creators_board_games(
    creator_id INT NOT NULL,
    board_game_id INT NOT NULL,
    CONSTRAINT fk_creators_board_games_creators
        FOREIGN KEY(creator_id)
            REFERENCES creators(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    CONSTRAINT fk_creators_board_games_board_games
        FOREIGN KEY(board_game_id)
            REFERENCES board_games(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
);

--2. Insert

INSERT INTO board_games(name, release_year, rating,	category_id, publisher_id, players_range_id)
    VALUES
        ('Deep Blue', '2019', 5.67,	1, 15, 7),
        ('Paris', '2016', 9.78, 7, 1, 5),
        ('Catan: Starfarers', '2021',	9.87, 7, 13, 6),
        ('Bleeding Kansas',	'2020',	3.25, 3, 7,	4),
        ('One Small Step', '2019', 5.75, 5,	9, 2)
;

INSERT INTO publishers(name, address_id, website, phone)
    VALUES
        ('Agman Games', 5, 'www.agmangames.com', '+16546135542'),
        ('Amethyst Games', 7, 'www.amethystgames.com', '+15558889992'),
        ('BattleBooks',	13,	'www.battlebooks.com', '+12345678907')
;

--3.	Update

UPDATE players_ranges
SET  max_players = max_players + 1
WHERE max_players <= 2 AND min_players >= 2;

UPDATE board_games
SET name = CONCAT(name, ' V2')
WHERE release_year >= 2020;

--4.	Delete

ALTER TABLE board_games
DROP CONSTRAINT fk_board_games_publishers;

ALTER TABLE board_games
ADD CONSTRAINT fk_board_games_addresses
FOREIGN KEY(publisher_id)
REFERENCES publishers(id)
ON DELETE CASCADE ;

DELETE FROM addresses CASCADE
WHERE SUBSTRING(town FROM 1 FOR 1) = 'L';

--5.	Board Games by Release Year

SELECT
    name,
    rating
FROM board_games
ORDER BY release_year, name DESC;

--6.	Board Games by Category

SELECT
    bg.id,
    bg.name,
    bg.release_year,
    c.name
FROM board_games AS bg
    JOIN categories AS c
        ON bg.category_id = c.id
WHERE
    c.name = 'Strategy Games' OR c.name = 'Wargames'
ORDER BY
    bg.release_year DESC
;

--7.	Creators without Board Games

SELECT
    cr.id,
    CONCAT(cr.first_name, ' ', cr.last_name) AS "creator_name",
    cr.email
FROM creators AS cr
    LEFT JOIN creators_board_games AS cbg
        ON cr.id = cbg.creator_id
            LEFT JOIN board_games AS bg
                ON cbg.board_game_id = bg.id
WHERE
    bg.name IS NULL
ORDER BY
    creator_name
;

--8.	First 5 Board Games

SELECT
    bg.name,
    bg.rating,
    ca.name
FROM board_games AS bg
    JOIN players_ranges AS pr
        ON bg.players_range_id = pr.id
            JOIN categories AS ca
                ON bg.category_id = ca.id
WHERE
    (bg.rating > 7.00 AND (LOWER(bg.name) LIKE '%a%' OR bg.rating > 7.50)) AND (pr.min_players >= 2 AND pr.max_players <= 5)
ORDER BY
    bg.name,
    bg.rating DESC
LIMIT
    5
;

--9.	Creators with Emails

SELECT
    CONCAT(cr.first_name, ' ', cr.last_name) AS "full_name",
    cr.email,
    MAX(b.rating)
FROM creators_board_games AS crb
    JOIN creators AS cr
        ON crb.creator_id = cr.id
            JOIN board_games AS b
                ON crb.board_game_id = b.id
WHERE
    cr.email LIKE '%.com'
GROUP BY
    full_name,
    cr.email
ORDER BY
    full_name
;

--10.	Creators by Rating

SELECT
    cr.last_name,
    CEIL(AVG(b.rating)) AS "average_rating",
    p.name
FROM board_games AS b
    JOIN creators_board_games AS crb
        ON b.id = crb.board_game_id
            JOIN creators AS cr
                ON crb.creator_id = cr.id
                    JOIN publishers AS p
                        ON b.publisher_id = p.id
WHERE
    p.name = 'Stonemaier Games'
GROUP BY
    cr.last_name,
    cr.email,
    p.name
ORDER BY
    average_rating DESC
;

--11.	Creator of Board Games

CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
    IN input_first_name VARCHAR(30),
    OUT total_number_of_board_games INT)
AS $$
    BEGIN

        SELECT INTO total_number_of_board_games
            COUNT(cbg.board_game_id)
        FROM creators AS c
            LEFT JOIN creators_board_games AS cbg
                ON c.id = cbg.creator_id
        WHERE
            c.first_name = input_first_name
        ;
    END
$$
LANGUAGE plpgsql;

--12.	Search for Board Games

CREATE TABLE IF NOT EXISTS search_results (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    release_year INT,
    rating FLOAT,
    category_name VARCHAR(50),
    publisher_name VARCHAR(50),
    min_players VARCHAR(50),
    max_players VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE usp_search_by_category(category varchar(50))
AS $$
    DECLARE
    BEGIN
        TRUNCATE TABLE search_results;
        INSERT INTO search_results(
            name,
            release_year,
            rating,
            category_name,
            publisher_name,
            min_players,
            max_players)
        SELECT
            bg.name,
            bg.release_year,
            bg.rating,
            c.name,
            p.name,
            CONCAT(pl.min_players, ' people'),
            CONCAT(pl.max_players, ' people')
        FROM board_games AS bg
            JOIN categories AS c
                ON bg.category_id = c.id
                    JOIN publishers AS p
                        ON bg.publisher_id = p.id
                            JOIN players_ranges AS pl
                                ON bg.players_range_id = pl.id
        WHERE
            c.name = category
        ORDER BY
            p.name,
            bg.release_year DESC
        ;
    END
$$
LANGUAGE plpgsql;

--TEST
CALL usp_search_by_category('Wargames');

SELECT * FROM search_results;
