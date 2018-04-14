DROP DATABASE IF EXISTS verk51;

-- 1.
CREATE DATABASE verk51;

-- 2.
CREATE TABLE verk51.staff
(
 	ID INT PRIMARY KEY AUTO_INCREMENT,
	nafn VARCHAR(255),
	heimili VARCHAR(255),
	laun DOUBLE,
	bonus DOUBLE
);

-- 3.
INSERT INTO 
	verk51.staff(nafn,heimili,laun,bonus)
VALUES
	('Jónas','Kristuvík',250000,10),
	('Guðmundur','Helguvík',195000,10),
	('Kormákur','Reykjavík',260000,10),
	('Skjöldur','Dritvík',550000,20),
	('Hallur','Akurvík',345000,20),
	('Konráð','Stökustað',150000,20),
	('Stefán','Útstað',350000,15),
	('Sigurður','Þorbrandsstað',350000,15),
	('Hallgrímur','Akurgerði',550000,15),
	('Sigurður','Hveragerði',540000,25);
    
-- 4.
SELECT * FROM verk51.staff;

-- A
-- SELECT SUM(laun) AS 'Heildarlaun' FROM verk51.staff;

-- B
-- SELECT nafn,laun
-- FROM verk51.staff
-- WHERE laun = 550000;

-- C
-- SELECT nafn,laun
-- FROM verk51.staff
-- WHERE nafn = 'jónas';

-- D
-- SELECT nafn,laun
-- FROM verk51.staff
-- WHERE laun BETWEEN 250000 AND 350000;

-- E
-- SELECT nafn,(laun * bonus / 100) AS 'Bónusgreiðslur'
-- FROM verk51.staff
-- WHERE laun BETWEEN 250000 AND 500000;

-- F
-- SELECT AVG(laun + (laun * bonus / 100)) AS 'Meðallaun með bónus'
-- FROM verk51.staff;

-- G
-- SELECT nafn,heimili
-- FROM verk51.staff
-- WHERE heimili LIKE '%vík';

-- H
-- SELECT nafn,laun
-- FROM verk51.staff
-- WHERE nafn LIKE '%Sigurður%';

-- I
-- SELECT nafn,(laun + (laun * bonus / 100)) * 12 AS 'Árslaun með bónus'
-- FROM verk51.staff;

-- J
-- SELECT nafn,laun + (laun * bonus / 100) AS 'Mánaðarlaun með bónus'
-- FROM verk51.staff;