DROP DATABASE IF EXISTS TEST;
CREATE DATABASE TEST;
USE TEST;

CREATE TABLE t (
	ID INT,
    s1 INT
);

DELIMITER = //

CREATE PROCEDURE p7 ()
BEGIN
	SET @a = 5;
    SET @b = 5;
    INSERT INTO t VALUES (@a);
END; //

CREATE PROCEDURE p12 (IN parameter1 INT)
BEGIN
	DECLARE variable1 INT;
    SET variable1 = parameter1 + 1;
    IF variable1 = 0 THEN
		INSERT INTO t VALUES (17);
	END IF;
    IF parameter1 = 0 THEN
		UPDATE t SET s1 = s1 +1;
	ELSE
		UPDATE t SET s1 = s1 +1;
	END IF;
END; //

CREATE PROCEDURE p14()
BEGIN
	DECLARE v INT;
    SET v = 0;
    WHILE v < 5 DO
		INSERT INTO t VALUES (v);
        SET v = v + 1;
	END;
END; //


DELIMITER = ;



