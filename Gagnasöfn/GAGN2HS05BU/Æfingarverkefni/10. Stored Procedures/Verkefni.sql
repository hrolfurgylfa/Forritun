USE 2109013290_COMPANY;
/*
SELECT * FROM dept;
SELECT * FROM employee;
SELECT * FROM deptsal;
*/
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
    

DELIMITER //

DROP PROCEDURE IF EXISTS updateSalary//
CREATE PROCEDURE updateSalary (IN u_dept_no INT)
BEGIN
	UPDATE deptsal
    SET totalsalery = (SELECT SUM(salary) FROM employee WHERE dept_no = u_dept_no) 
    WHERE dept_no = u_dept_no;
END; //

DELIMITER ;

CALL updateSalary(1);