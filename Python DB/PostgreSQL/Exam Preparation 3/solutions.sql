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
