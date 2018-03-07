DROP TABLE IF EXISTS Timaverkefni2.teams;
CREATE TABLE Timaverkefni2.teams
(
	id INTEGER NOT NULL PRIMARY KEY,
	name VARCHAR(37) NOT NULL,
	conference VARCHAR(2) NULL
);