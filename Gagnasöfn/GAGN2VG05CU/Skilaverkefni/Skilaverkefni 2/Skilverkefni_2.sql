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

CREATE PROCEDURE AddStudent(IN firstName_IN VARCHAR(55), lastName_IN VARCHAR(55), dob_IN DATE, startSemester_IN INT)
BEGIN
	INSERT INTO Students
		(firstName,lastName,dob,startSemester)
	VALUES
		(firstName_IN, lastName_IN, dob_IN, startSemester_IN);
	
	CALL AddMandatoryCourses(LAST_INSERT_ID());
END $$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS AddMandatoryCourses $$

CREATE PROCEDURE AddMandatoryCourses(IN StudentID INT)
BEGIN
	INSERT INTO Students
		(firstName,lastName,dob,startSemester)
	VALUES
		(firstName_IN, lastName_IN, dob_IN, startSemester_IN);
END $$
DELIMITER ;


CALL AddStudent("Kalli", "Klikkaði", "2019-11-21", 9);