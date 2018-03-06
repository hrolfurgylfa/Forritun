CREATE TABLE skuld_lanabok
(
	Kennitala VARCHAR(11) PRIMARY KEY NOT NULL,
    Nafn VARCHAR(40) NOT NULL,
    Heimilisfang VARCHAR(40),
    Pósnúmer INTEGER,
    Netfang VARCHAR(50) NOT NULL,
    Skuld INTEGER,
    Lán DECIMAL(7,2)
)