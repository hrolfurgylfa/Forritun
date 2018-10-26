USE 2109013290_northwind;

#11
SELECT * FROM Orders;
SELECT * FROM `Order Details`;

#12
SELECT COUNT(*)
FROM Customers 
WHERE Country = "USA" AND Region = "WA" 
	OR Country = "USA" AND Region = "MA" 
	OR Country = "USA" AND Region = "IL" 
	OR Country = "USA" AND Region = "FL";

#13
SELECT * FROM Customers;

#14
SELECT * FROM Orders;

#15
#No Column with Shipping Fees

#16
SELECT OrderID, COUNT(*) AS "number of order details" FROM `Order Details` Group BY OrderID;

#17
SELECT CustomerID, COUNT(*) FROM Orders GROUP BY CustomerID;

#18
#NOT POSSIBLE

#19