USE 2109013290_sale;

SELECT p_descript, p_qoh, p_price, p_qoh * p_price
FROM PRODUCT;

SELECT p_descript, p_qoh, p_price, p_qoh * p_price AS totalValue
FROM PRODUCT;

SELECT * FROM PRODUCT;

UPDATE PRODUCT
SET	P_INDATE = "2017.01.18",
	P_PRICE = "17.99",
    P_MIN = 10
WHERE P_CODE = "13-Q2/P2";

SET autocommit = 0;
START TRANSACTION;


UPDATE PRODUCT
SET	P_INDATE = "2034.01.18",
	P_PRICE = "99.99",
    P_DISCOUNT = P_PRICE
WHERE P_MIN != 5;


SELECT * FROM PRODUCT;

ROLLBACK;

SELECT * FROM PRODUCT;

SELECT * FROM 2109013290_sale."alphabetical_list_of_products";