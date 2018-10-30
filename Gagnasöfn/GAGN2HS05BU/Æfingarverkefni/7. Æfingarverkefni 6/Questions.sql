USE 2109013290_HumanResources;
SELECT * FROM employees;
SELECT * FROM jobs;
SELECT * FROM departments;
SELECT * FROM locations;

# SUB-QUERIES:
#1
SELECT first_name, last_name, salary FROM employees WHERE salary > (SELECT salary FROM employees WHERE last_name = "Bull");

#2
SELECT first_name, last_name FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE department_name = "IT");

#3
SELECT first_name, last_name FROM employees WHERE manager_id != 0 AND department_id IN (SELECT department_id FROM departments WHERE location_id IN (SELECT location_id FROM locations WHERE country_id = "US"));

#4
SELECT first_name, last_name FROM employees WHERE employee_id IN (SELECT manager_id FROM employees);

#5
SELECT first_name, last_name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);


# JOIN:
#1
SELECT location_id, street_address, city, state_province, country_name 
FROM departments 
	NATURAL JOIN locations 
	NATURAL JOIN countries;

#2
SELECT first_name, last_name, DEPARTMENT_ID, DEPARTMENT_NAME
FROM employees 
	NATURAL JOIN departments;
    
#3
SELECT *
FROM employees 
	NATURAL JOIN jobs 
	NATURAL JOIN departments
    NATURAL JOIN locations
WHERE CITY = "London";

#4
