/* 1:
	Smíðið trigger fyrir insert into Restrictors skipunina. 
	Triggernum er ætlað að koma í veg fyrir að einhver áfangi sé undanfari eða samfari síns sjálfs. 
	með öðrum orðum séu courseNumber og restrictorID með sama innihald þá stoppar triggerinn þetta með
	því að kasta villu og birta villuboð.
	Dæmi um insert sem triggerinn á að stoppa: insert into Restrictors values('GSF2B3U','GSF2B3U',1);
*/
DELIMITER $$
DROP TRIGGER IF EXISTS BEFORE_INSERT_Restrictors$$
CREATE TRIGGER BEFORE_INSERT_Restrictors
    BEFORE INSERT
    ON Restrictors FOR EACH ROW
BEGIN
    IF (NEW.restrictorID = NEW.courseNumber) THEN
		signal sqlstate '45000' set message_text = "courseNumber má ekki vera það sama og restrictorID";
	END IF;
END$$
DELIMITER ;

insert into Restrictors(courseNumber,restrictorID,restrictorType)values('GSF2B3U','GSF2B3U',1);


-- 2:
-- Skrifið samskonar trigger fyrir update Restrictors skipunina.
DELIMITER $$
DROP TRIGGER IF EXISTS BEFORE_UPDATE_Restrictors$$
CREATE TRIGGER BEFORE_UPDATE_Restrictors
    BEFORE UPDATE
    ON Restrictors FOR EACH ROW
BEGIN
    IF (NEW.restrictorID = NEW.courseNumber) THEN
		signal sqlstate '45000' set message_text = "courseNumber má ekki vera það sama og restrictorID";
	END IF;
END$$
DELIMITER ;

UPDATE Restrictors
SET restrictorID = 'GSF2B3U'
WHERE courseNumber = 'GSF2B3U';


/*
	3:
	Skrifið stored procedure sem leggur saman allar einingar sem nemandinn hefur lokið.
    Birta skal fullt nafn nemanda, heiti námsbrautar og fjölda lokinna eininga(
	Aðeins skal velja staðinn áfanga. passed = true
*/
delimiter $$
drop procedure if exists KlaradarEiningar $$

create procedure KlaradarEiningar(IN nemendaID INT)
begin
	SELECT SUM(courseCredits)
	FROM Registration r
		JOIN Courses c
		ON r.courseNumber = c.courseNumber
	WHERE r.StudentID = nemendaID AND r.passed = 1;
end $$
delimiter ;
CALL KlaradarEiningar(4);

/*
	4:
	Skrifið 3 stored procedure-a:
    AddStudent()
    AddMandatoryCourses()
    Hugmyndin er að þegar AddStudent hefur insertað í Students töfluna þá kallar hann á AddMandatoryCourses() sem skráir alla
    skylduáfanga á nemandann.
    Að endingu skrifið þið stored procedure-inn StudentRegistration() sem nota skal við sjálfstæða skráningu áfanga nemandans.
*/
DELIMITER $$
DROP PROCEDURE IF EXISTS AddStudent $$

CREATE PROCEDURE AddStudent(IN firstName_IN VARCHAR(55), lastName_IN VARCHAR(55), dob_IN DATE, BrautarID_IN INT)
BEGIN
	INSERT INTO Students
		(firstName,lastName,dob,startSemester)
	VALUES
		(
			firstName_IN,
            lastName_IN,
            dob_IN,
            (SELECT CurrentSemester())
		);
	
	CALL AddMandatoryCourses(LAST_INSERT_ID(), BrautarID_IN);
END $$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS AddMandatoryCourses $$

CREATE PROCEDURE AddMandatoryCourses(IN NemendaID INT, BrautarID INT)
begin
	DECLARE i INT;
    DECLARE n INT;
	
	SET i = 0;
    
	SELECT Count(trackID)
	FROM TrackCourses 
	WHERE mandatory = True AND Semester = 1 AND trackID = BrautarID
    INTO n;

	WHILE n > i
	DO
		INSERT INTO Registration
			(studentID, trackID, courseNumber, registrationDate, passed, semesterID)
		VALUES
			(
				NemendaID,
				BrautarID, 
				(-- Þetta Nær í course number af áfanganum sem er verið að lúppa í gegnum
					SELECT courseNumber
					FROM TrackCourses 
					WHERE mandatory = True AND Semester = 1 AND trackID = BrautarID
					LIMIT i, 1
				),
				CURRENT_DATE(),
				False,
				(SELECT CurrentSemester())
			);
        
        SET i = i + 1;
	END WHILE;
end $$
DELIMITER ;

DELIMITER $$
DROP FUNCTION IF EXISTS CurrentSemester $$
    
CREATE FUNCTION CurrentSemester()
RETURNS INT
NO SQL
BEGIN
    RETURN(
		SELECT semesterID
		FROM Semesters
		WHERE semesterStarts < CURRENT_DATE() AND semesterEnds > CURRENT_DATE()
	);
END $$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS StudentRegistration $$

CREATE PROCEDURE StudentRegistration(IN NemendaID INT, BrautarID INT, AfangaID CHAR(10), annarID INT)
BEGIN
	INSERT INTO Registration
			(studentID, trackID, courseNumber, registrationDate, passed, semesterID)
		VALUES
			(
				NemendaID,
				BrautarID, 
				AfangaID,
                CURRENT_DATE(),
                FALSE,
                annarID
			);
END $$
DELIMITER ;


CALL AddStudent("Jón", "Spæjó", "1642-4-1", 9);
CALL StudentRegistration(3, 9, "GSF2B3U", CurrentSemester());