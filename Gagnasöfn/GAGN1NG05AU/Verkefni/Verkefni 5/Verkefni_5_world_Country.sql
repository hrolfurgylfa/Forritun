SELECT * FROM skilaverkefni_5.Country;

-- 1. 
-- SELECT * FROM skilaverkefni_5.Country WHERE Continent LIKE "%Europe%";

-- 2.
-- SELECT SUM(Population) FROM skilaverkefni_5.Country;

-- 3.
-- SELECT * FROM skilaverkefni_5.Country WHERE SurfaceArea > 600000;

-- 4. 
-- SELECT * FROM skilaverkefni_5.Country WHERE IndepYear > 1920;

-- 5. 
-- SELECT * FROM skilaverkefni_5.Country WHERE Population BETWEEN 10000000 and 20000000;

-- 6. 
-- SELECT * FROM skilaverkefni_5.Country WHERE GNPOld != 0;

-- 7. 
-- SELECT * FROM skilaverkefni_5.Country WHERE Name != LocalName

-- 8. 
-- SELECT Continent,count(*) FROM skilaverkefni_5.Country GROUP BY Continent;

-- 9. 
-- SELECT AVG(LifeExpectancy) AS "Meðallífstími" FROM skilaverkefni_5.Country

-- 10. 
-- SELECT SUM(GNP) AS "Summa GNP" FROM skilaverkefni_5.Country

-- 11. 
-- SELECT Continent,count(*) FROM skilaverkefni_5.Country WHERE Continent = "Asia";

-- 12. 
-- SELECT * FROM skilaverkefni_5.Country WHERE Continent = "Asia" AND Population  >= 10000000;

-- 13. 
-- SELECT * FROM skilaverkefni_5.Country WHERE GovernmentForm = "Constitutional Monarchy"

-- 14. 
-- SELECT * FROM skilaverkefni_5.Country WHERE GNPOld > GNP;

-- 15. 
-- SELECT GovernmentForm,COUNT(*) FROM skilaverkefni_5.Country GROUP BY GovernmentForm;

-- 16. 
-- SELECT * FROM skilaverkefni_5.Country WHERE Continent = "Europe" or Continent = "Asia" ORDER BY Continent;

-- 17. 
-- SELECT Continent,count(*) FROM skilaverkefni_5.Country GROUP BY Continent;

-- 18. 
-- SELECT Continent,COUNT(*) FROM skilaverkefni_5.Country GROUP BY Continent HAVING COUNT(*) > 20;