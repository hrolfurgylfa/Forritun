DROP DATABASE IF EXISTS 2109013290_bus_db;

CREATE DATABASE 2109013290_bus_db;
USE 2109013290_bus_db;

#Route
CREATE TABLE route (
    route_number INT PRIMARY KEY NOT NULL,
    average_passengers INT
);

#Stage
CREATE TABLE stage(
	stage_ID INT PRIMARY KEY NOT NULL,
    route_number INT NOT NULL,
    
    #Aðkomulyklar
	CONSTRAINT route_number_FK FOREIGN KEY (route_number) REFERENCES route(route_number)
);

#Towns
CREATE TABLE towns(
	town_ID INT PRIMARY KEY NOT NULL,
    town_name VARCHAR(40) NOT NULL
);

#Go Through
CREATE TABLE go_through (
    stage_ID INT NOT NULL,
    town_ID INT NOT NULL,
    
    #Aðkomulyklar
    CONSTRAINT stage_ID_FK FOREIGN KEY (stage_ID) REFERENCES stage (stage_ID),
    CONSTRAINT town_ID_FK FOREIGN KEY (town_ID) REFERENCES towns (town_ID)
);

#Garage
CREATE TABLE garage(
	garage_ID INT PRIMARY KEY NOT NULL,
    town_ID INT NOT NULL,
    
    #Aðkomulyklar
    CONSTRAINT town_ID_FK2 FOREIGN KEY (town_ID) REFERENCES towns(town_ID)
);

#Buses
CREATE TABLE buses(
	registration_number INT PRIMARY KEY NOT NULL,
    number_of_passengers INT,
    decks INT(1),
    route_number INT NOT NULL,
    garage_ID INT NOT NULL,
    
	#Aðkomulyklar
	CONSTRAINT route_number_FK2 FOREIGN KEY (route_number) REFERENCES route(route_number),
    CONSTRAINT garage_ID_FK FOREIGN KEY (garage_ID) REFERENCES garage(garage_ID)
);

#Drivers
CREATE TABLE drivers(
	employee_number INT PRIMARY KEY NOT NULL,
    first_name varchar(20) NOT NULL,
    last_name varchar(20) NOT NULL,
    phone_number INT,
    stage_ID INT NOT NULL,
    
    #Aðkomulyklar
    CONSTRAINT stage_ID_FK2 FOREIGN KEY (stage_ID) REFERENCES stage(stage_ID)
);

#Adressess
CREATE TABLE adressess(
	employee_number INT NOT NULL,
	city varchar(40) NOT NULL,
    street varchar(50) NOT NULL,
    zipcode INT NOT NULL,
    
    #Aðkomulyklar
    CONSTRAINT employee_number_FK FOREIGN KEY (employee_number) REFERENCES drivers(employee_number)
);