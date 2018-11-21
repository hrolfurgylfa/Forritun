USE 2109013290_COMPANY;

SELECT * FROM dept;
SELECT * FROM employee;
SELECT * FROM deptsal;

#2
DROP TABLE IF EXISTS deptsal;
CREATE TABLE deptsal (
	dept_no INT PRIMARY KEY,
    totalsalary INT
);
INSERT INTO 
	deptsal
VALUES
	(1,0),
    (2,0),
    (3,0),
    (4,0);
    
#3 step 1
DELIMITER //

#3 step 2
DROP PROCEDURE IF EXISTS updateSalary//
CREATE PROCEDURE updateSalary (IN u_dept_no INT)
BEGIN
	UPDATE deptsal
    SET deptsal.totalsalary = (SELECT SUM(salary) FROM employee WHERE dept_no = u_dept_no) 
    WHERE dept_no = u_dept_no;
END; //

#3 step 3
DELIMITER ;

#3 step 4
CALL updateSalary(1);
CALL updateSalary(2);
CALL updateSalary(3);
CALL updateSalary(4);

#3 step 5
SELECT * FROM deptsal;

# 1
SHOW PROCEDURE STATUS;

#2
DROP PROCEDURE updateSalary;

#3
UPDATE deptsal
SET deptsal.totalsalary = 0;

#--------------- 4 ---------------
DELIMITER //

DROP PROCEDURE IF EXISTS updateAllSalary//
CREATE PROCEDURE updateAllSalary ()
BEGIN
	DECLARE tel INT unsigned DEFAULT 1; 
	WHILE tel <= (SELECT COUNT(totalsalary) FROM deptsal) DO
		UPDATE deptsal
		SET deptsal.totalsalary = (SELECT SUM(salary) FROM employee WHERE dept_no = tel) 
		WHERE dept_no = tel;
        SET tel = tel + 1;
	END WHILE;
END; //

DELIMITER ;

CALL updateAllSalary();

#--------------- 5 ---------------
DELIMITER //

DROP PROCEDURE IF EXISTS updateAllSalaryCursor//
CREATE PROCEDURE updateAllSalaryCursor ()
BEGIN
	DEClARE totalsalary_cursor CURSOR FOR 
		SELECT totalsalary FROM deptsal;
        
	OPEN totalsalary_cursor;
    REPEAT
		FETCH totalsalary_cursor INTO tSalary;
        SELECT * FROM tSalary;
    
    /*WHILE tel <= (SELECT COUNT(totalsalary) FROM deptsal) DO
		UPDATE deptsal
		SET deptsal.totalsalary = (SELECT SUM(salary) FROM employee WHERE dept_no = tel) 
		WHERE dept_no = tel;
        SET tel = tel + 1;
	END WHILE;*/
    UNTIL tel = (SELECT COUNT(totalsalary) FROM deptsal)
    END REPEAT;
END; //

DELIMITER ;

CALL updateAllSalaryCursor();