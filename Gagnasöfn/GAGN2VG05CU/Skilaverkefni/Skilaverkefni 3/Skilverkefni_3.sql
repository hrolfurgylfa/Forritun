/*
1:
	Skrifið stored procedure: StudentListJSon() sem notar cursor til að breyta vensluðum gögnum í JSon string.
	JSon-formuð gögnin eru listi af objectum.
	OBS: StudentListJSon skilar texta sem þið hafið formað.

	Niðurstöðurnar ættu að líta einhvern vegin svona út:

	[
		  {"first_name": "Guðrún", "last_name": "Ólafsdóttir", "date_of_birth": "1999-03-31"},
		  {"first_name": "Andri Freyr", "last_name": "Kjartansson", "date_of_birth": "2000-11-01"},
		  {"first_name": "Tinna Líf", "last_name": "Björnsson", "date_of_birth": "1998-08-14"},
		  {"first_name": "Magni Þór", "last_name": "Sigurðsson", "date_of_birth": "2000-05-27"},
		  {"first_name": "Rheza Már", "last_name": "Hamid-Davíðs", "date_of_birth": "2001-09-17"},
		  {"first_name": "Hadría Gná", "last_name": "Schmidt", "date_of_birth": "1999-07-29"},
		  {"first_name": "Jasmín Rós", "last_name": "Stefánsdóttir", "date_of_birth": "1996-02-29"}
	]
*/
delimiter $$
drop procedure if exists JSONStudents $$

create procedure JSONStudents()
begin
	SELECT 
		CONCAT(
			'[{"',
			GROUP_CONCAT(
				CONCAT_WS(
					'", "', 
					CONCAT('first_name": "',firstName), 
					CONCAT('last_name": "',lastName), 
					CONCAT('dob": "',dob)
				)
				SEPARATOR '"},{"'
			),
			'"}]'
		)
		AS "Student JSON"
	FROM
		Students;
end $$
delimiter ;

CALL JSONStudents();


/*
	2:
	Skrifið nú SingleStudentJSon()þannig að nemandinn innihaldi nú lista af þeim áföngum sem hann hefur tekið.
	Śé nemandinn enn við nám þá koma þeir áfangar líka með.
	ATH: setjið nemandann sem object.
	Líkleg niðurstaða:

	{
		"student_id": "1",
		"first_name": "Guðrún",
		"last_name": "Ólafsdóttir",
		"date_of_birth": "1999-03-31",
		"courses" :[
		  {"course_number": "STÆ103","course_credits": "5","status": "pass"},
		  {"course_number": "EÐL103","course_credits": "5","status": "pass"},
		  {"course_number": "STÆ203","course_credits": "5","status": "pass"},
		  {"course_number": "EÐL203","course_credits": "5","status": "pass"},
		  {"course_number": "STÆ303","course_credits": "5","status": "pass"},
		  {"course_number": "GSF2A3U","course_credits": "5","status": "pass"},
		  {"course_number": "FOR3G3U","course_credits": "5","status": "pass"},
		  {"course_number": "GSF2B3U","course_credits": "5","status": "pass"},
		  {"course_number": "GSF3B3U","course_credits": "5","status": "fail"},
		  {"course_number": "FOR3D3U","course_credits": "5","status": "fail"}
		]
	}
*/
delimiter $$
drop procedure if exists SingleStudentJSon $$

create procedure SingleStudentJSon(IN NemendaID INT)
begin
	DECLARE AllirAfangarNemanda LONGTEXT DEFAULT "[";
    DECLARE FjoldiAfanga INT DEFAULT (SELECT COUNT(*) FROM Registration WHERE StudentID = NemendaID);
    DECLARE courseObject TEXT;
    DECLARE i INT DEFAULT 0;
    DECLARE JsonOut LONGTEXT;
    
    -- Þetta keyrir í gegnum alla áfangana sem nemandinn er í og setir þá í JSON Array
    WHILE i < FjoldiAfanga
    DO
		SELECT
			JSON_UNQUOTE(JSON_OBJECT(
				"course_number", r.courseNumber,
                "course_credits", c.courseCredits,
                "status", CASE WHEN r.passed = 1 THEN "pass" ELSE "fail" END
			))
		FROM Registration r
		JOIN Courses c
			ON r.CourseNumber = c.courseNumber
		WHERE r.StudentID = NemendaID
        LIMIT i, 1
		INTO courseObject;
        
		SET AllirAfangarNemanda = CONCAT(AllirAfangarNemanda, courseObject, ",");
        SET i = i + 1;
    END WHILE;
    
    -- Þetta skiptir síðustu kommuni fyrir kassasviga til þess að loka arrayinum
	SET AllirAfangarNemanda = SUBSTRING(AllirAfangarNemanda, 1, CHAR_LENGTH(AllirAfangarNemanda)-1);
    SET AllirAfangarNemanda = CONCAT(AllirAfangarNemanda, "]");
    
    -- Þetta býr til JSONið, fyrir utan courses sem ég geri á eftir
    SELECT
		JSON_OBJECT(
			"student_id", StudentID,
			"first_name", firstName,
			"last_name", lastName,
			"date_of_birth", dob
		) AS "JSON Output"
    FROM Students 
    WHERE StudentID = NemendaID
    INTO JsonOut;
    
    -- Eyða síðasta stafnum, setja arreyinn þar inn og loka objectinum svo aftur
    SET JsonOut = SUBSTRING(JsonOut, 1, CHAR_LENGTH(JsonOut)-1);
    SET JsonOut = CONCAT(
		JsonOut,
			',"courses": ', AllirAfangarNemanda, 
        "}"
	);
    
    -- Skila JSONinu
    SELECT JsonOut;
end $$
delimiter ;

CALL SingleStudentJSon(2);

SELECT * FROM Registration;
SELECT * 
FROM Registration r
JOIN Courses c
	ON r.CourseNumber = c.courseNumber;
SELECT * FROM Students;

SELECT COUNT(*) FROM Registration WHERE StudentID = 3;


/*
	3:
	Skrifið stored procedure: SemesterInfoJSon() sem birtir uplýsingar um ákveðið semester.
	Semestrið inniheldur lista af nemendum sem eru /hafa verið á þessu semestri.
	Og að sjálfsögðu eru gögnin á JSon formi!

	Gæti litið út einhvern veginn svona(hérna var semesterID 8 notað á original gögnin:
	[
		{"student_id": "1", "first_name": "Guðrún", "last_name": "Ólafsdóttir", "courses_taken": "2"},
		{"student_id": "2", "first_name": "Andri Freyr", "last_name": "Kjartansson", "courses_taken": "1"},
		{"student_id": "5", "first_name": "Rheza Már", "last_name": "Hamid-Davíðs", "courses_taken": "2"},
		{"student_id": "6", "first_name": "Hadríra Gná", "last_name": "Schmidt", "courses_taken": "2"}
	]
*/


-- ACHTUNG:  2 og 3 nota líka cursor!

