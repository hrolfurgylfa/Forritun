USE ProgressTracker;

-- 1:
-- Birtið lista af öllum áföngum sem geymdir eru í gagnagrunninum.
-- Áfangarnir eru birtir í stafrófsröð
delimiter $$
drop procedure if exists CourseList $$

create procedure CourseList()
begin
	SELECT courseName FROM Courses ORDER BY courseName ASC;
end $$
delimiter ;
-- CALL CourseList();


-- 2:
-- Birtið upplýsingar um einn ákveðin áfanga.
delimiter $$
drop procedure if exists SingleCourse $$

create procedure SingleCourse(IN brautarNumer CHAR(10))
begin
	SELECT * FROM Courses WHERE courseNumber = brautarNumer;
end $$
delimiter ;
CALL SingleCourse("EÐL603");


-- 3:
-- Nýskráið áfanga í gagnagrunninn.
-- Það þarf að skrá áfanganúmerið, áfangaheitið og einingafjöldann
delimiter $$
drop procedure if exists NewCourse $$

create procedure NewCourse(IN brautarNumer CHAR(10), brautarNafn VARCHAR(75), einingar TINYINT)
begin
	INSERT INTO Courses(courseNumber, courseName, courseCredits)
    VALUES (brautarNumer, brautarNafn, einingar);
end $$
delimiter ;
CALL NewCourse("EÐL603", "Enþá meiri Eðlisfræði!!!", 5);

-- 4:
-- Uppfærið réttan kúrs.
-- row_count() fallið er hér notað til að birta fjölda raða sem voru uppfærðar.
delimiter $$
drop procedure if exists UpdateCourse $$

create procedure UpdateCourse(IN afangaNumer CHAR(10), nyttBrautarNafn VARCHAR(75))
begin
	UPDATE Courses
	SET courseName = nyttBrautarNafn
    WHERE courseNumber = afangaNumer;
end $$
delimiter ;
CALL UpdateCourse("EÐL603", "EÐLISFRÆÐI!!!");


-- 5:
-- ATH: Ef verið er að nota áfangann einhversstaðar(sé hann skráður á TrackCourses töfluna) þá má EKKI eyða honum.
-- Sé hins vegar hvergi verið að nota hann má eyða honum úr bæði Courses og Restrictor töflunum.
delimiter $$
drop procedure if exists DeleteCourse $$

create procedure DeleteCourse(IN afangaNumer CHAR(10))
begin
	DELETE FROM Courses WHERE CourseNumber = afangaNumer;
end $$
delimiter ;
CALL DeleteCourse("EÐL603");


-- 6:
-- fallið skilar heildarfjölda allra áfanga í grunninum
delimiter $$
drop function if exists NumberOfCourses $$
    
create function NumberOfCourses()
returns int
no sql
begin
    RETURN(
		SELECT COUNT(*) FROM Courses
	);
end $$
delimiter ;
SELECT NumberOfCourses();


-- 7:
-- Fallið skilar heildar einingafjölda ákveðinnar námsleiðar(Track)
-- Senda þarf brautarNumer inn sem færibreytu
delimiter $$
drop function if exists TotalTrackCredits $$
    
create function TotalTrackCredits(brautarNumer INT)
returns int
no sql
begin
    RETURN(
		SELECT SUM(courseCredits)
		FROM TrackCourses tc
			JOIN courses c
			ON tc.courseNumber = c.courseNumber
		WHERE trackID = brautarNumer
	);
end $$
delimiter ;
SELECT TotalTrackCredits(9);

SELECT *
FROM Courses c
	JOIN trackcourses tc
    ON c.courseNumber = tc.courseNumber
    JOIN tracks t
    ON tc.trackID = t.trackID;


-- 8: 
-- Fallið skilar heildarfjölda áfanga sem eru í boði á ákveðinni námsleið
delimiter $$
drop function if exists TotalNumberOfTrackCourses $$
    
create function TotalNumberOfTrackCourses(brautarNumer INT)
returns int
no sql
begin
    RETURN(
		SELECT COUNT(courseCredits)
		FROM TrackCourses tc
			JOIN courses c
			ON tc.courseNumber = c.courseNumber
		WHERE trackID = brautarNumer
	);
end $$
delimiter ;
SELECT TotalNumberOfTrackCourses(9);


-- 9:
-- Fallið skilar true ef áfanginn finnst í töflunni TrackCourses
delimiter $$
drop function if exists CourseInUse $$
    
create function CourseInUse(afangaNumer CHAR(10))
returns boolean
no sql
begin
	return(
		IF((SELECT count(courseNumber) FROM TrackCourses WHERE courseNumber = afangaNumer), true, false)
    );
end $$
delimiter ;
SELECT CourseInUse("GSF2A3U");
SELECT CourseInUse("GSF2A3");


-- 10:
-- Fallið skilar true ef árið er hlaupár annars false
delimiter $$
drop function if exists IsLeapyear $$

create function IsLeapYear(ar INT)
returns boolean
no sql
begin
	CASE 
		WHEN ar % 400 = 0 THEN return(true);
		WHEN ar % 100 = 0 THEN return(false);
        WHEN ar % 4 = 0 THEN return(true);
		ELSE return(false);
	END CASE;
end $$
delimiter ;
SELECT IsLeapyear(2011);

-- 11:
-- Fallið reiknar út og skilar aldri ákveðins nemanda
delimiter $$
drop function if exists StudentAge $$
    
create function StudentAge(nemandaID INT)
returns int
no sql
begin
	RETURN(
		YEAR(CURRENT_DATE) - YEAR((SELECT dob FROM Students WHERE studentID = nemandaID))
    );
end $$
delimiter ;
SELECT StudentAge(5);
SELECT * FROM Students;
SELECT dob FROM Students WHERE studentID = 2;
SELECT CURRENT_DATE - (SELECT dob FROM Students WHERE studentID = 2);

-- 12:
-- Fallið skilar fjölda þeirra eininga sem nemandinn hefur tekið(lokið)
delimiter $$
drop function if exists StudentCredits $$
    
create function StudentCredits()
returns int
begin
	-- kóði hér...
end $$
delimiter ;


-- 14:
-- Hér þarf skila lista af öllum áföngum ásamt restrictorum og tegund þeirra.
-- Hafi áfangi enga undanfara eða samfara þá birtast þeir samt í listanum.
delimiter $$
drop procedure if exists CourseRestrictorList $$

create procedure CourseRestrictorList()
begin
	-- kóði hér...
end $$
delimiter ;


-- 15:
-- RestrictorList birtir upplýsingar um alla restrictora ásamt áföngum.
-- Með öðrum orðum: Gemmér alla restrictora(undanfara, samfara) og þá áfanga sem þeir hafa áhrif á.
delimiter $$
drop procedure if exists RestrictorList $$

create procedure RestrictorList()
begin
	-- kóði hér...
end $$
delimiter ;