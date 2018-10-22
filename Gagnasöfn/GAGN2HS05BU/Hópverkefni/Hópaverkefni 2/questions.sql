DROP TABLE IF EXISTS 2109013290_Review.EMP_1;
DROP TABLE IF EXISTS 2109013290_Review.EMP_2;
DROP TABLE IF EXISTS 2109013290_Review.TEMP_1;
USE 2109013290_Review;

#Slökkva á autocommit
START TRANSACTION;
SET autocommit = 0;

#1
CREATE TABLE EMP_1 (
	EMP_NUM CHAR(3),
	EMP_LNAME VARCHAR(15),
	EMP_FNAME VARCHAR(15),
	EMP_INITIAL CHAR(1),
	EMP_HIREDATE DATE,
	JOB_CODE INT(3),
    
    #Aðkomulyklar
	CONSTRAINT JOB_CODE_EMP_1_FK FOREIGN KEY (JOB_CODE) REFERENCES JOB(JOB_CODE)
);

#2
INSERT INTO
	EMP_1(EMP_NUM, EMP_LNAME, EMP_FNAME, EMP_INITIAL, EMP_HIREDATE, JOB_CODE)
VALUES
	(101, "News", "John", "G", "2000-11-08", 502),
    (102, "Senior", "David", "H", "1989-07-12", 501),
    (103, "Arbough", "June", "E", "1996-12-01", 503),
    (104, "Ramoras", "Anne", "K", "1987-11-15", 501),
    (105, "Johnson", "Alice", "K", "1993-02-01", 502),
    (106, "Smithfield", "William", "", "2004-06-22", 500),
    (107, "Alonzo", "Maria", "D", "1993-10-10", 500),
    (108, "Washington", "Ralph", "B", "1991-08-22", 501),
    (109, "Smith", "Larry", "W", "1997-07-18", 501);

#3
SELECT * FROM EMP_1 WHERE JOB_CODE = 502;

#4
COMMIT;
#5
UPDATE EMP_1 SET JOB_CODE = 501 WHERE EMP_NUM = 107;
SELECT * FROM EMP_1;
ROLLBACK;

#6
DELETE FROM EMP_1 WHERE EMP_LNAME = "Smithfield" AND EMP_FNAME = "William" AND EMP_HIREDATE = "2004-06-22" AND JOB_CODE = 500;
SELECT * FROM EMP_1;

#7
ROLLBACK;

#8
CREATE TABLE EMP_2 LIKE EMP_1;
ALTER TABLE EMP_2 ADD EMP_PCT DECIMAL(4,2);
ALTER TABLE EMP_2 ADD PROJ_NUM CHAR(3);

#Insert Into new table
INSERT INTO
	EMP_2(EMP_NUM, EMP_LNAME, EMP_FNAME, EMP_INITIAL, EMP_HIREDATE, JOB_CODE, EMP_PCT)
VALUES
	(101, "News", "John", "G", "2000-11-08", 502, 5.00),
    (102, "Senior", "David", "H", "1989-07-12", 501, 8.00),
    (103, "Arbough", "June", "E", "1996-12-01", 503, 5.00),
    (104, "Ramoras", "Anne", "K", "1987-11-15", 501, 10.00),
    (105, "Johnson", "Alice", "K", "1993-02-01", 502, 5.00),
    (106, "Smithfield", "William", "", "2004-06-22", 500, 6.00),
    (107, "Alonzo", "Maria", "D", "1993-10-10", 500, 5.00),
    (108, "Washington", "Ralph", "B", "1991-08-22", 501, 9.00),
    (109, "Smith", "Larry", "W", "1997-07-18", 501, 1.00);
    
#9
UPDATE EMP_2 SET EMP_PCT = 3.85 WHERE EMP_NUM = 103;
SELECT * FROM EMP_2;

UPDATE EMP_2 SET EMP_PCT = 6.20 WHERE EMP_NUM = 106;
UPDATE EMP_2 SET EMP_PCT = 5.15 WHERE EMP_NUM = 107;
UPDATE EMP_2 SET EMP_PCT = 10.00 WHERE EMP_NUM = 108;
UPDATE EMP_2 SET EMP_PCT = 2.00 WHERE EMP_NUM = 109;
SELECT * FROM EMP_2;

#10
UPDATE EMP_2 SET PROJ_NUM = "18" WHERE JOB_CODE = 500;
SELECT * FROM EMP_2;

#11
UPDATE EMP_2 SET PROJ_NUM = "25" WHERE JOB_CODE >= 502;
SELECT * FROM EMP_2;
COMMIT;

#12
UPDATE EMP_2 SET PROJ_NUM = "14" WHERE EMP_HIREDATE < "1994-1-1" AND JOB_CODE >= 501;
SELECT * FROM EMP_2;
COMMIT;

#13-A
CREATE TABLE TEMP_1 (
    EMP_NUM CHAR(3),
    EMP_PCT DECIMAL(4,2)
);

#13-B
SET SQL_SAFE_UPDATES = 0;

# INSERT INTO
# 	TEMP_1(EMP_NUM, EMP_PCT)
# VALUES
# 	((SELECT EMP_NUM FROM EMP_2), (SELECT EMP_PCT FROM EMP_2));
# SELECT * FROM TEMP_1;    

#14
DROP TABLE TEST_1;

#15
SELECT * FROM EMPLOYEE WHERE EMP_LNAME LIKE BINARY "Smith%";

#16
SELECT PROJECT.PROJ_NAME, 
	PROJECT.PROJ_VALUE, 
    PROJECT.PROJ_BALANCE, 
    EMPLOYEE.EMP_LNAME, 
    EMPLOYEE.EMP_FNAME, 
    EMPLOYEE.EMP_INITIAL, 
    JOB.JOB_CODE, 
    JOB.JOB_DESCRIPTION, 
    JOB.JOB_CHG_HOUR
    
FROM EMPLOYEE
    JOIN JOB
    ON EMPLOYEE.JOB_CODE = JOB.JOB_CODE
    JOIN PROJECT
    ON EMPLOYEE.EMP_NUM = PROJECT.EMP_NUM;

#17
