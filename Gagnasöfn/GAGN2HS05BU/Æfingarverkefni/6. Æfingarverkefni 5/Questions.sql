SELECT * FROM Products;

#1
SELECT ProductName, QuantityPerUnit FROM Products;

#2
SELECT ProductID, ProductName FROM Products;

#3
SELECT ProductID, ProductName FROM Products WHERE Discontinued = 1;

#4
SELECT ProductName, UnitPrice FROM Products ORDER BY UnitPrice;

#5
SELECT ProductID, ProductName, UnitPrice FROM Products WHERE UnitPrice < 20;

#6
SELECT ProductID, ProductName, UnitPrice FROM Products WHERE UnitPrice < 25 AND UnitPrice > 15;

#7

SELECT ProductID, ProductName, UnitPrice FROM Products WHERE UnitPrice > (SELECT SUM(UnitPrice)/COUNT(UnitPrice) FROM Products);

#8


#9
SELECT COUNT(SELECT ProductID, ProductName FROM Products WHERE Discontinued = 0), 
		COUNT(SELECT ProductID, ProductName FROM Products WHERE Discontinued = 1)
FROM Products;