/*
INSERT INTO
	Verkefni_6.kaupandi(kt,nafn_kaupanda)
VALUES
	("2512025640","Óskar Árni Óskarsson"),
    ("2612097390","Guðrún Ragnheiðardóttir"),
    ("0908825649","Helgi Birgirsson"),
    ("2603891479","Unnur Kristjánsdóttir"),
    ("0203942309","Hildur Daníelsdóttir"),
    ("0804841239","Jóhannes Björn Bjarnason"),
    ("1804034210","Guðný Sveinsdóttir"),
    ("1611023440","Erla Magnúsdóttir"),
    ("1011134220","Kristján Jóhansson"),
    ("1311463379","Gísli Sigurður Einarsson");
    
INSERT INTO
	Verkefni_6.seljandi(kt,nafn_seljanda)
VALUES
	("0506073000","Kristófer Óli"),
    ("2212829139","Vilhjálmur"),
    ("0303966459","Steinunn Þóra"),
    ("1301071870","Halldór Ragnar"),
    ("0809734549","Hildur"),
    ("2003017110","Páll"),
    ("2006141970","Guðmundur Sigurður"),
    ("0803118990","Anna"),
    ("0510843159","Kristín"),
    ("0602129500","Björn Þorsteinn");
    
INSERT INTO
	Verkefni_6.solumadur(kt,nafn_solumanns)
VALUES
	("1705601389","Sigrún Jóhanna"),
    ("1210775809","Birgir Pétur"),
    ("1804055380","Hulda"),
    ("2102535759","Bjarni"),
    ("2301058110","Ásta"),
    ("1511836629","Ingibjörg"),
    ("1602075780","Davíð Páll"),
    ("1008818629","Anna Lilja"),
    ("1304799989","Halldór"),
    ("2701417759","Auður");
    
INSERT INTO
	Verkefni_6.bill(fastanumer,tegund,litur,asett_verd_millj,seljandi_kt)
VALUES
	("AB549","Toyota Carolla","Hvítur",1.6,"0506073000"),
    ("IU593","Porsche 911","Ljós grár",9.2,"2212829139"),
    ("FIG46","LEXUS LS 450h","Hvítur",6.2,"0303966459"),
    ("FJ504","BMW M5","Blár",7.5,"1301071870"),
    ("FLD47","TOYOTA RAV4","Dökk grár",3.6,"0809734549"),
    ("OBD05","NISSAN Leaf","Grænn",2.5,"2003017110"),
    ("UV470","Toyota Carolla","Gulur",0.3,"2006141970"),
    ("HVO97","SpaceX Falcon Heavy","Ljós grár",5.4,"0803118990"),
    ("UVS31","TESLA Model 3","Svartur",8.1,"0510843159"),
    ("UG856","Porsche Cayenne","Hvítur",9.6,"0602129500");

INSERT INTO
	Verkefni_6.sala(fastanumer,kaupandi_kt,seljandi_kt,verd,solumadur_kt)
VALUES
	("AB549","2512025640","0506073000",1.6,"1705601389"),
    ("IU593","2612097390","2212829139",9.2,"1210775809"),
    ("FIG46","0908825649","0303966459",6.2,"1804055380"),
    ("FJ504","2603891479","1301071870",7.5,"2102535759"),
    ("FLD47","0203942309","0809734549",3.6,"2301058110"),
    ("OBD05","0804841239","2003017110",2.5,"1511836629"),
    ("UV470","1804034210","2006141970",0.3,"1602075780"),
    ("HVO97","1611023440","0803118990",5.4,"1008818629"),
    ("UVS31","1011134220","0510843159",8.1,"1304799989"),
    ("UG856","1311463379","0602129500",9.6,"2701417759");
*/
#1.
#SELECT tegund, fastanumer FROM Verkefni_6.bill WHERE litur = "blár";

#2.
/*
SELECT 	verd AS "Verð í milljónum", 
	bill.fastanumer AS "Bílnúmer", 
    nafn_kaupanda AS "Kaupandi", 
    nafn_seljanda AS "Seljandi", 
    nafn_solumanns AS "Sölumaður"
    
FROM Verkefni_6.sala
	JOIN Verkefni_6.bill
    ON bill.fastanumer = sala.fastanumer
    JOIN Verkefni_6.kaupandi
    ON sala.kaupandi_kt = kaupandi.kt
    JOIN Verkefni_6.seljandi
    ON sala.seljandi_kt = seljandi.kt
    JOIN Verkefni_6.solumadur
    ON sala.solumadur_kt = solumadur.kt
    
WHERE verd > .5;
*/
#3.
#SELECT * FROM seljandi WHERE kt LIKE "____84%" OR kt LIKE "____85%" AND kt LIKE "%9";

#4
#UPDATE bill SET litur = "Bleikur" WHERE fastanumer = "AB549";

#5
#UPDATE bill SET asett_verd_millj = 1.3 WHERE fastanumer = "AB549";

#6
/*
SELECT nafn_solumanns AS "Nafn",
	solumadur_kt AS "Kennitala",
	bill.fastanumer AS "Bílnúmer",
	tegund AS "Tegund"

FROM Verkefni_6.sala
	JOIN Verkefni_6.bill
    ON bill.fastanumer = sala.fastanumer
    JOIN Verkefni_6.kaupandi
    ON sala.kaupandi_kt = kaupandi.kt
    JOIN Verkefni_6.seljandi
    ON sala.seljandi_kt = seljandi.kt
    JOIN Verkefni_6.solumadur
    ON sala.solumadur_kt = solumadur.kt
*/
