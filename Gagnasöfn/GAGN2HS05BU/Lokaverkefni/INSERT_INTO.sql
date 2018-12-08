USE 2109013290_MovieCo;

INSERT INTO 
	MEMBERSHIP(MEM_NUM, MEM_FNAME, MEM_LNAME, MEM_STREET, MEM_CITY, MEM_STATE, MEM_ZIP, MEM_BALANCE)
VALUES
	(102, "Tami", "Dawson", "2632 Takli Circle", "Norene", "TN", 37136, 11),
    (103, "Curt", "Knight", "4025 Cornell Court", "Flatgap", "KY", 41219, 6),
    (104, "Jamal", "Melendez", "788 East 145th Avenue", "Quebeck", "TN", 38579, 0),
    (105, "Iva", "Mcclain", "6045 Musket Ball Circle", "Summit", "KY", 42783, 15),
    (106, "Miranda", "Parks", "4469 Maxwell Place", "Germantown", "TN", 38183, 0),
    (107, "Rosario", "Elliott", "7578 Danner Avenue", "Columbia", "TN", 38402, 5),
    (108, "Mattie", "Guy", "4390 Evergreen Street", "Lily", "KY", 40740, 0),
    (109, "Clint", "Ochoa", "1711 Elm Street", "Greeneville", "TN", 37745, 10),
    (110, "Lewis", "Rosales", "4524 Southwind Circle", "Gounce", "TN", 38326, 0),
    (111, "Stacky", "Mann", "2789 East Cook Avenue", "Murfreesboro", "TN", 37132, 8),
    (112, "Luis", "Trujillo", "7267 Melvin Avenue", "Heiskell", "TN", 37754, 3),
    (113, "Minnie", "Gonzales", "6430 Vasili Drive", "Williston", "TN", 38076, 0);
    
INSERT INTO 
	RENTAL(RENT_NUM, RENT_DATE, MEM_NUM)
VALUES
	(1001, "09-03-01", 103),
    (1002, "09-03-01", 105),
    (1003, "09-03-02", 102),
    (1004, "09-03-02", 110),
    (1005, "09-03-02", 111),
    (1006, "09-03-02", 107),
    (1007, "09-03-02", 104),
    (1008, "09-03-03", 105),
    (1009, "09-03-03", 111);
    
INSERT INTO 
	PRICE(PRICE_CODE, PRICE_DESCRIPTION, PRICE_RENTFEE, PRICE_DAILYLATEFEE)
VALUES
	(1, "Standard", 2.0, 1.0),
    (2, "New Relese", 3.5, 3.0),
    (3, "Discount", 1.5, 1.0),
    (4, "Weekly Special", 1.0, 0.5);

INSERT INTO 
	MOVIE(MOVIE_NUM, MOVIE_NAME, MOVIE_YEAR, MOVIE_COST, MOVIE_GENRE, PRICE_CODE)
VALUES
	(1234, "The Cesar Family Christmas", 2007, 39.95, "FAMILY", 2),
    (1235, "Smokey Mountain Wildlife", 2004, 59.95, "ACTION", 1),
    (1236, "Richard Goodhope", 2008, 59.95, "DRAMA", 2),
    (1237, "Beatnik Fever", 2007, 29.95, "COMEDY", 2),
    (1238, "Constant Companion", 2008, 89.95, "DRAMA", 2),
    (1239, "Where Hope Dies", 1998, 25.49, "DRAMA", 3),
    (1245, "Time to Burn", 2005, 45.49, "ACTION", 1),
    (1246, "What He Doesn't Know", 2006, 58.29, "COMEDY", 1);

INSERT INTO 
	VIDEO(VID_NUM, VID_INDATE, MOVIE_NUM)
VALUES
	(54321, "18-06-08", 1234),
    (54324, "18-06-08", 1234),
    (54325, "18-06-08", 1234),
    (34341, "22-01-07", 1235),
    (34342, "22-01-07", 1235),
    (34366, "02-06-09", 1236),
    (34367, "02-06-09", 1236),
    (34368, "02-06-09", 1236),
    (34369, "02-06-09", 1236),
    (44392, "21-10-08", 1237),
    (44397, "21-10-08", 1237),
    (59237, "14-02-09", 1237),
    (61388, "25-01-07", 1239),
    (61353, "28-01-06", 1245),
    (61354, "28-01-06", 1245),
    (61367, "30-07-08", 1246),
    (61369, "30-07-08", 1246);

INSERT INTO 
	DETAILRENTAL(RENT_NUM, VID_NUM, DETAIL_FEE, DETAIL_DUEDATE, DETAIL_RETURNDATE, DETAIL_DAILYLATEFEE)
VALUES
	(1001, 34342, 2.0, "09-03-04", "09-03-02", 1),
	(1001, 61353, 2.0, "09-03-04", "09-03-03", 1),
	(1002, 59237, 3.5, "09-03-04", "09-03-04", 3),
	(1003, 54325, 3.5, "09-03-04", "09-03-09", 3),
	(1003, 61369, 2.0, "09-03-06", "09-03-09", 1),
	(1003, 61388, 0.0, "09-03-06", "09-03-09", 1),
	(1004, 44392, 3.5, "09-03-05", "09-03-07", 3),
	(1004, 34367, 3.5, "09-03-05", "09-03-07", 3),
	(1004, 34341, 2.0, "09-03-07", "09-03-07", 1),
	(1005, 34342, 2.0, "09-03-07", "09-03-05", 1),
	(1005, 44397, 3.5, "09-03-05", "09-03-05", 3),
	(1006, 34366, 3.5, "09-03-05", "09-03-04", 3),
	(1006, 61367, 2.0, "09-03-07", NULL, 1),
	(1007, 34368, 3.5, "09-03-05", NULL, 3),
	(1008, 34369, 3.5, "09-03-05", "09-03-05", 3),
	(1009, 54324, 3.5, "09-03-05", NULL, 3),
	(1001, 34366, 3.5, "09-03-04", "09-03-02", 3);
	
