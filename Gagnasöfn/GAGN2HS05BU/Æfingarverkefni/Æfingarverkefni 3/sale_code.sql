USE 2109012190_sale;

SELECT p_descript, p_qoh, p_price, p_qoh * p_price
FROM product;

SELECT p_descript, p_qoh, p_price, p_qoh * p_price AS totalValue
FROM product;