USE 2109013290_COMPANY;

SELECT * FROM dept;
SELECT * FROM employee;

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
    
SELECT * FROM deptsal;
    
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
  DECLARE b INT;
  DECLARE tel INT UNSIGNED DEFAULT 1;
  DEClARE totalsalary_cursor CURSOR FOR 
		SELECT dept_no FROM deptsal;
  DECLARE CONTINUE HANDLER FOR NOT FOUND
     SET b = 1;
  OPEN totalsalary_cursor;
  REPEAT
     UPDATE deptsal
     SET totalsalary = (SELECT SUM(salary) FROM employee WHERE dept_no = tel);
     SET tel = tel + 1;
     UNTIL b
  END REPEAT;
  CLOSE totalsalary_cursor;
END;//

DELIMITER ;

CALL updateAllSalary();

#--------------- 6 ---------------
DELIMITER //

DROP PROCEDURE IF EXISTS updateSalery10p//
CREATE PROCEDURE updateSalery10p ()
BEGIN
  DECLARE b INT;
  DEClARE updateSalery10p_cursor CURSOR FOR 
		SELECT emp_id FROM employee;
  DECLARE CONTINUE HANDLER FOR NOT FOUND
     SET b = 1;
  OPEN updateSalery10p_cursor;
  REPEAT
     UPDATE employee
     SET salary = (salary/100)*110;
     UNTIL b
  END REPEAT;
  CLOSE updateSalery10p_cursor;
END;//

DELIMITER ;

CALL updateSalery10p();

#--------------- 7 ---------------
DELIMITER //
#-----A-----
DROP TRIGGER IF EXISTS after_employee_insert//
CREATE TRIGGER after_employee_insert 
    AFTER INSERT ON employee
    FOR EACH ROW 
BEGIN
    CALL updateAllSalary();
END//

#-----B-----
DROP TRIGGER IF EXISTS after_employee_delete//
CREATE TRIGGER after_employee_delete 
    AFTER DELETE ON employee
    FOR EACH ROW 
BEGIN
    CALL updateAllSalary();
END//
DELIMITER ;

#A - test
INSERT INTO
	employee(emp_id, emp_name, dept_no, salary)
VALUES
	(9, "Hrólfur Gylfason", 2, 3);

#B - test
DELETE FROM employee WHERE emp_name = "Hrólfur Gylfason";



