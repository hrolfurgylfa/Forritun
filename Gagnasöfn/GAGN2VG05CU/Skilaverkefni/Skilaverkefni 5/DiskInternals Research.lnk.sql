-- 1:
-- Skrifið Stored Procedure ElectedCourses
-- Kalla skal á ElectedCourses með nemendanúmeri og hann skilar til baka vali fyrir næstu önn.

delimiter $$
drop procedure if exists ElectedCourses $$

create procedure ElectedCourses(IN NemendaID INT)
begin
    DECLARE n INT DEFAULT (SELECT COUNT(*) FROM Courses);
    DECLARE i INT DEFAULT 0;
    DECLARE JsonOut LONGTEXT;
    DECLARE brautarNumer CHAR(10);
    
    DECLARE n2 INT;
	DECLARE i2 INT DEFAULT 0;
	DECLARE courseDone BOOL DEFAULT False;
    
    
    DROP TABLE IF EXISTS PossibleCourses;
    CREATE TEMPORARY TABLE PossibleCourses LIKE Courses;
    INSERT INTO PossibleCourses SELECT * FROM Courses;
    
    DROP TABLE IF EXISTS Print;
    CREATE TEMPORARY TABLE Print
    (
		course VARCHAR(10),
        msg LONGTEXT
    );

    
    WHILE i < n
    DO
		-- Kóði sem keyrir í lúppunni kemur hérna fyrir neðan
        
        SET brautarNumer = (SELECT courseNumber FROM Courses LIMIT i, 1);
        INSERT INTO Print (course, msg) VALUES (brautarNumer, "Ég er að keyra í gegnum áfanga.");
        
        
        -- Þetta keyrir í gegnum alla Registrationirnar sem nemandinn hefur fyrir þennan áfanga og tékka hvort að þessi áfangi sé búinn
        SET courseDone = False;
        SET i2 = 0;
        SET n2 = (SELECT COUNT(*) FROM Registration WHERE StudentID = NemendaID AND courseNumber = brautarNumer);
        WHILE i2 < n2
        DO
			IF
				(SELECT passed FROM Registration WHERE StudentID = NemendaID AND courseNumber = brautarNumer LIMIT i2, 1) = True OR 
                (SELECT semesterID FROM Registration WHERE StudentID = NemendaID AND courseNumber = brautarNumer LIMIT i2, 1) = CurrentSemester()
			THEN
				SET courseDone = True;
            END IF;
            SET i2 = i2 + 1;
        END WHILE;
        -- Eyða brautinni úr PossibleCourses ef hún er búin í Registration töfluni af nemendanum sem ég er að fara í gegnum
        IF courseDone = True THEN
			DELETE FROM PossibleCourses WHERE courseNumber = brautarNumer;
		END IF;
        
        
        -- Finna áfanga sem nemandinn kemst ekki í vegna þess að það er restrictor á honum
        
        
        -- Hækka teljarann til þess að skoða næstu braut
		SET i = i + 1;
    END WHILE;
    
    SELECT * FROM Print;
    SELECT * FROM PossibleCourses ORDER BY RAND() LIMIT 5;
end $$
delimiter ;

CALL ElectedCourses(2);

SELECT * FROM AllCoursesForStudent;
SELECT * FROM Registration;
SELECT * FROM Registration WHERE StudentID = 2;



-- ATHUGIÐ:
-- Það má alveg takmarka fjölda áfanga sem kerfið velur við t.d. 5 eða einhvern fjölda sem hentar ykkar hönnun.

-- ATTENTION:
-- ElectedCourses þarf að finna þessa áfanga útfrá óloknum áföngum. Skoða þarf hvaða áfangar koma
-- næst. Ef ekki er hægt með góðu móti að finna út hvaða áfangi kemru næst í röðinni þá er bara hægt
-- að velja random 

-- ACHTUNG:
-- Ekki þarf að kanna fall í núverandi áföngum(þeir áfangar sem nemandinn er í en hefur ekki klárað
-- þegar val fer fram).

-- ATTENZIONE:
-- Málið er eiginlega þetta:  Nemandinn er í X áföngum og búinn með Y áfanga.  Hvað getur hann tekið næst



-- 2:
-- Bætið við eða aðlagið klasasafnið ykkar(library) úr verkefni 4 þannig að þig getið prófað þessa virkni úr forriti
-- í viðbót við að testa þetta í grunninum sjálfum!

-- Þetta er núna í Verkefni 4/Classes/SchoolManager.py