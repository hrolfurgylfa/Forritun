USE THEMEPARK;

#Slide 5
#1
SELECT DISTINCT(DATE_FORMAT
(SALE_DATE, "%a - %d - %m - %y")) AS "sale_date" 
FROM SALES;

#2
SELECT DISTINCT(DATE_FORMAT
(SALE_DATE, "%d/%m/%Y")) AS "sale_date" 
FROM SALES;

#3
SELECT DISTINCT(DATE_FORMAT
(SALE_DATE, "%W-%D of %M %y")) AS "sale_date" 
FROM SALES;

#Slide 7
#4
SELECT * FROM EMPLOYEE WHERE MONTH(EMP_DOB) = 11;

#Slide 8
#5
SELECT DATEDIFF("2016-12-25","2016-01-01");
SELECT DATEDIFF("2017-12-25","2018-11-8");

#Slide 10
#6
SELECT EMP_HIRE_DATE, DATE_ADD(EMP_HIRE_DATE, INTERVAL 1 YEAR) AS "First Work Appraisal" FROM EMPLOYEE;

#Slide 13
#7
SELECT TRANSACTION_NO, LINE_PRICE, MOD(LINE_PRICE, 10)
FROM SALES_LINE
WHERE LINE_QTY > 2;
#Line price is devided by 10 because it is in MOD with 10 and returns the rest and it only returns anything if the Line Quantity is higher than 2 (3 or more)

#Slide 20
#8
SELECT * FROM EMPLOYEE;

SELECT EMP_NUM, DATE_FORMAT(EMP_DOB, "%d"), UPPER(SUBSTR(EMP_LNAME, 1, 6)) FROM EMPLOYEE;

# Tests
IF PARK_COUNTRY = 'UK' THEN {result := 'United Kingdom'}
[ELSEIF PARK_COUNTRY = 'FR' THEN {result := 'FRANCE'}]
[ELSEIF PARK_COUNTRY = 'NL' THEN result := 'The Netherlands'}]
[ELSEIF PARK_COUNTRY = 'SP' THEN result := 'Spain'}]
[ELSEIF PARK_COUNTRY = 'ZA' THEN result := 'South Africa'}]
[ELSEIF PARK_COUNTRY = 'SW' THEN result := 'Switzerland'}]
[ELSE result := 'Unknown'}]
END IF;

SELECT PARK_CODE, PARK_COUNTRY
FROM THEMEPARK;

# Tests
IF PARK_COUNTRY = 'UK' THEN {result := 'United Kingdom'}
[ELSEIF PARK_COUNTRY = 'FR' THEN {result := 'FRANCE'}]
[ELSEIF PARK_COUNTRY = 'NL' THEN {result := 'The Netherlands'}]
[ELSEIF PARK_COUNTRY = 'SP' THEN {result := 'Spain'}]
[ELSEIF PARK_COUNTRY = 'ZA' THEN {result := 'South Africa'}]
[ELSEIF PARK_COUNTRY = 'SW' THEN {result := 'Switzerland'}]
[ELSE {result := 'Unknown'}]
END IF; 




















