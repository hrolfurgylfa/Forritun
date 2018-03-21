SELECT * FROM skilaverkefni_5.CountryLanguage;

-- 1.
-- SELECT * FROM skilaverkefni_5.CountryLanguage WHERE CountryCode = "ARG";

-- 2.
-- SELECT Language AS "Opinber tungumál í Argentínu" FROM skilaverkefni_5.CountryLanguage WHERE CountryCode = "ARG" AND IsOfficial = "T";

-- 3.
-- SELECT Language AS "Óopinber tungumál í Argentínu" FROM skilaverkefni_5.CountryLanguage WHERE CountryCode = "ARG" AND IsOfficial = "F";

-- 4.
-- SELECT CountryCode, Language, Percentage FROM skilaverkefni_5.CountryLanguage WHERE Percentage < 50

-- 5.
-- GROUP BY CountryCode;

-- 6.
-- SELECT * FROM skilaverkefni_5.CountryLanguage WHERE Percentage > 90;

-- 7.
-- SELECT * FROM skilaverkefni_5.CountryLanguage WHERE Percentage < 5;

-- 8.
-- SELECT * FROM skilaverkefni_5.CountryLanguage WHERE Language = "English" AND IsOfficial = "T";

-- 9.
-- SELECT Language, Count(CountryCode) AS "Fjöldi landa sem tala þetta mál" FROM skilaverkefni_5.CountryLanguage GROUP BY Language;

-- 10.
SELECT Language FROM skilaverkefni_5.CountryLanguage WHERE Count(CountryCode) > 5;



