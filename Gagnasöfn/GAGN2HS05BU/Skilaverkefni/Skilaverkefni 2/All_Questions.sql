#   //////////////////////////////
#       Northwind DATABASE
#   //////////////////////////////
USE 2109013290_northwind;

#1
SELECT 
    ProductName, 
    QuantityPerUnit
FROM 
    Products;

#2
SELECT 
    ProductID, 
    ProductName
FROM 
    Products;

#3
SELECT 
    ProductID, 
    ProductName
FROM 
    Products
WHERE 
    Discontinued = 1;

#4
SELECT 
    ProductName, 
    UnitPrice
FROM 
    Products
ORDER BY UnitPrice;

#5
SELECT 
    ProductID, 
    ProductName, 
    UnitPrice
FROM 
    Products
WHERE 
    UnitPrice < 20;

#6
SELECT 
    ProductID, 
    ProductName, 
    UnitPrice
FROM 
    Products
WHERE
    UnitPrice < 25 AND 
    UnitPrice > 15;

#7
SELECT 
    ProductID, 
    ProductName, 
    UnitPrice
FROM
    Products
WHERE
    UnitPrice > (SELECT SUM(UnitPrice) / COUNT(UnitPrice) FROM Products);

#8
SELECT 
    ProductID, 
    ProductName, 
    UnitPrice
FROM
    Products
ORDER BY UnitPrice DESC
LIMIT 10;

#9
SELECT 
    Discontinued,
    COUNT(Discontinued)
FROM
    Products
GROUP BY Discontinued;

#10
SELECT 
    ProductName, 
    UnitsOnOrder, 
    UnitsInStock
FROM
    Products
WHERE
    UnitsOnOrder > UnitsInStock;


#   //////////////////////////////
#     Human Resources DATABASE
#   //////////////////////////////
USE 2109013290_HumanResources;

# SUB-QUERIES:
#1
SELECT 
	first_name, 
	last_name, 
	salary 
FROM 
	employees 
WHERE 
	salary > (
		SELECT salary 
        FROM employees 
        WHERE last_name = "Bull");

#2
SELECT 
	first_name, 
    last_name 
FROM 
	employees 
WHERE 
	department_id IN (
		SELECT department_id 
        FROM departments 
        WHERE department_name = "IT");

#3
SELECT 
	first_name, 
	last_name 
FROM 
	employees 
WHERE
	manager_id != 0 AND 
    department_id IN (
		SELECT department_id 
        FROM departments 
        WHERE location_id IN (
			SELECT location_id 
            FROM locations 
            WHERE country_id = "US"));

#4
SELECT 
	first_name, 
	last_name 
FROM 
	employees 
WHERE 
	employee_id IN (
		SELECT manager_id 
        FROM employees);

#5
SELECT 
	first_name, 
	last_name, 
	salary 
FROM 
	employees 
WHERE 
	salary > (
		SELECT AVG(salary) 
		FROM employees);


# JOIN:
#1
SELECT 
	location_id, 
	street_address, 
	city, 
    state_province, 
    country_name 
FROM departments 
	NATURAL JOIN locations 
	NATURAL JOIN countries;

#2
SELECT 
	first_name, 
    last_name, 
    DEPARTMENT_ID, 
    DEPARTMENT_NAME
FROM employees 
	NATURAL JOIN departments;
    
#3
SELECT 
	employees.FIRST_NAME,
    employees.LAST_NAME,
    jobs.JOB_TITLE,
    departments.DEPARTMENT_ID,
    departments.DEPARTMENT_NAME
FROM employees 
	NATURAL JOIN jobs 
	NATURAL JOIN departments
    NATURAL JOIN locations
WHERE CITY = "London";

#4
SELECT
    e.EMPLOYEE_ID,
    e.LAST_NAME,
    m.EMPLOYEE_ID,
    m.LAST_NAME
FROM employees e
	JOIN employees m
	ON e.MANAGER_ID = m.EMPLOYEE_ID;
    
#5
SELECT 
	e.FIRST_NAME,
    e.LAST_NAME,
    e.HIRE_DATE
FROM employees e
	JOIN employees j
    ON e.HIRE_DATE > j.HIRE_DATE 
WHERE j.LAST_NAME = "Jones";

#6
SELECT 
	e.EMPLOYEE_ID, 
    e.LAST_NAME, 
    d.DEPARTMENT_ID, 
    d.DEPARTMENT_NAME
FROM employees e
	JOIN departments d
    ON e.DEPARTMENT_ID = d.DEPARTMENT_ID;