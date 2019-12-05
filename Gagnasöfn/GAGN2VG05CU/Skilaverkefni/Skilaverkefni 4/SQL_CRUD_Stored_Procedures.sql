-- ##########################
-- #      Courses CRUD      #
-- #                        #
-- ##########################
delimiter $$
drop procedure if exists GetCourse $$

create procedure GetCourse(IN brautarNumer CHAR(10))
begin
	SELECT * FROM Courses WHERE courseNumber = brautarNumer;
end $$
delimiter ;
CALL GetCourse("EÐL303");


delimiter $$
drop procedure if exists CreateCourse $$

create procedure CreateCourse(IN brautarNumer CHAR(10), brautarNafn VARCHAR(75), einingar TINYINT)
begin
	INSERT INTO Courses(courseNumber, courseName, courseCredits)
    VALUES (brautarNumer, brautarNafn, einingar);
end $$
delimiter ;
CALL CreateCourse("EÐL603", "Enþá meiri Eðlisfræði!!!", 5);


delimiter $$
drop procedure if exists ChangeCourse $$

create procedure ChangeCourse(IN afangaNumer CHAR(10), nyttBrautarNafn VARCHAR(75))
begin
	UPDATE Courses
	SET courseName = nyttBrautarNafn
    WHERE courseNumber = afangaNumer;
end $$
delimiter ;
CALL ChangeCourse("EÐL603", "EÐLISFRÆÐI!!!");


delimiter $$
drop procedure if exists RemoveCourse $$

create procedure RemoveCourse(IN afangaNumer CHAR(10))
begin
	DELETE FROM Courses WHERE CourseNumber = afangaNumer;
end $$
delimiter ;
CALL RemoveCourse("EÐL603");



-- ##########################
-- #     Students  CRUD     #
-- #                        #
-- ##########################
delimiter $$
drop procedure if exists GetStudent $$

create procedure GetStudent(IN nemendaID INT)
begin
	SELECT * FROM Students WHERE studentID = nemendaID;
end $$
delimiter ;
CALL GetStudent(3);


delimiter $$
drop procedure if exists CreateStudent $$

create procedure CreateStudent(IN fyrstanafn VARCHAR(55), eftirnafn VARCHAR(55), faedingardagur DATE, byrjunarOnn INT)
begin
	INSERT INTO Students(firstName, lastName, dob, startSemester)
    VALUES (fyrstanafn, eftirnafn, faedingardagur, byrjunarOnn);
end $$
delimiter ;
CALL CreateStudent("Kanína", "Gulrótardóttir", "2019-4-8", 11);


delimiter $$
drop procedure if exists ChangeStudent $$

create procedure ChangeStudent(IN nemendaID INT, fyrstanafn VARCHAR(55))
begin
	UPDATE Students
	SET firstName = fyrstanafn
    WHERE studentID = nemendaID;
end $$
delimiter ;
CALL ChangeStudent(3, "Hæna");


delimiter $$
drop procedure if exists RemoveStudent $$

create procedure RemoveStudent(IN nemendaID INT)
begin
	DELETE FROM Students WHERE studentID = nemendaID;
end $$
delimiter ;
CALL RemoveStudent(11);



-- ##########################
-- #     Students  CRUD     #
-- #                        #
-- ##########################
delimiter $$
drop procedure if exists GetSchool $$

create procedure GetSchool(IN skolaID INT)
begin
	SELECT * FROM Schools WHERE schoolID = skolaID;
end $$
delimiter ;
CALL GetSchool(1);


delimiter $$
drop procedure if exists CreateSchool $$

create procedure CreateSchool(IN skolaNafn VARCHAR(75))
begin
	INSERT INTO Schools(schoolName)
    VALUES (skolaNafn);
end $$
delimiter ;
CALL CreateSchool("Menntaskólinn í Kópavogi");


delimiter $$
drop procedure if exists ChangeSchool $$

create procedure ChangeSchool(IN skolaID INT, skolaNafn VARCHAR(75))
begin
	UPDATE Schools	
	SET schoolName = skolaNafn
    WHERE schoolID = skolaID;
end $$
delimiter ;
CALL ChangeSchool(2, "MK");


delimiter $$
drop procedure if exists RemoveSchool $$

create procedure RemoveSchool(IN skolaID INT)
begin
	DELETE FROM Schools WHERE schoolID = skolaID;
end $$
delimiter ;
CALL RemoveSchool(2);