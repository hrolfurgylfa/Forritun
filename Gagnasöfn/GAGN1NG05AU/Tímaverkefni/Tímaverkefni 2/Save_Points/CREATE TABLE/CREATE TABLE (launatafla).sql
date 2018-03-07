DROP TABLE IF EXISTS Timaverkefni2.launatafla;
CREATE TABLE Timaverkefni2.launatafla
(
	Audkenni INT PRIMARY KEY,
    Nafn VARCHAR(40),
    Starfsheiti VARCHAR(20),
    Netfang VARCHAR(50),
    Launaflokkur VARCHAR(1),
    Laun INT
);