DROP DATABASE IF EXISTS 2109013290_Verkefni_6;

CREATE DATABASE 2109013290_Verkefni_6;
USE 2109013290_Verkefni_6;

#Kaupandi
CREATE TABLE kaupandi(
	kt CHAR(10) PRIMARY KEY NOT NULL,
    nafn_kaupanda VARCHAR(50)
);

#Seljandi
CREATE TABLE seljandi(
	kt CHAR(10) PRIMARY KEY NOT NULL,
    nafn_seljanda VARCHAR(50)
);

#Sölumaður
CREATE TABLE solumadur(
	kt CHAR(10) PRIMARY KEY NOT NULL,
    nafn_solumanns VARCHAR(50)
);

#bílinn
CREATE TABLE bill(
	fastanumer CHAR(5) PRIMARY KEY NOT NULL,
	tegund VARCHAR(255),
	litur VARCHAR(255),
	asett_verd_millj DOUBLE(2,1),
	seljandi_kt CHAR(10),
	#Aðkomulyklar
	CONSTRAINT bill_seljandi_FK FOREIGN KEY (seljandi_kt) REFERENCES seljandi(kt)
);

#Söluferlið
CREATE TABLE sala(
	numer INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	fastanumer CHAR(5),
    kaupandi_kt CHAR(10),
    seljandi_kt CHAR(10),
    solumadur_kt CHAR(10),
    verd DOUBLE(2,1),
    #Aðkomulyklar
	CONSTRAINT fastanumer_FK FOREIGN KEY (fastanumer) REFERENCES bill(fastanumer),
    CONSTRAINT kaupandi_FK FOREIGN KEY (kaupandi_kt) REFERENCES kaupandi(kt),
    CONSTRAINT seljandi_FK FOREIGN KEY (seljandi_kt) REFERENCES bill(seljandi_kt),
    CONSTRAINT solumadur_FK FOREIGN KEY (solumadur_kt) REFERENCES solumadur(kt)
);