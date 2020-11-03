INSERT INTO cars VALUES (DEFAULT,"3K096I98581DHSNUP","Volkswagen","Tiguan",2019,"Blue"),
(DEFAULT,"ZM8G7BEUQZ97IH46V","Peugeot","Rifter",2019,"Red"),
(DEFAULT,"RKXVNNIHLVVZOUB4M","Ford","Fusion",2018,"White"),
(DEFAULT,"HKNDGS7CU31E9Z7JW","Toyota","RAV4",2018,"Silver"),
(DEFAULT,"DAM41UDN3CHU2WVF6","Volvo","V60",2019,"Gray"),
(DEFAULT,"DAM41UDN3CHU2WVF6","Volvo","V60 Cross Country",2019,"Gray");

INSERT INTO customer (idc,customer_id,name,surname,phone,adress,city,state,country,zip) VALUES 
(DEFAULT,10001,"Pablo","Picasso","+34 636 17 63 82"  ,"Paseo de la Chopera, 14","Madrid","Madrid","Spain",28045),
(DEFAULT,20001,"Abraham","Lincoln","+1 305 907 7086"  ,"120 SW 8th St","Miami","Florida","United States",33130),
(DEFAULT,30001,"Napoléon","Bonaparte","+33 1 79 75 40 00"  ,"40 Rue du Colisée","Paris","Île-de-France","France",75000);

INSERT INTO salesperson VALUES 
(DEFAULT,00001,"Petey", "Cruiser","Madrid"),
(DEFAULT,00002,"Anna" ,"Sthesia","Barcelona"),
(DEFAULT,00003,"Paul", "Molive","Berlin"),
(DEFAULT,00004,"Gail", "Forcewind","Paris"),
(DEFAULT,00005,"Paige", "Turner","Mimia"),
(DEFAULT,00006,"Bob", "Frapples","Mexico CPRIMARYinvoice_numberity"),
(DEFAULT,00007,"Walter", "Melon","Amsterdam"),
(DEFAULT,00008,"Shonda", "Leer","São Paulo" );

INSERT INTO invoices VALUES 
(DEFAULT,852399038,'2018-08-22',0,1,3),
(DEFAULT,731166526,'2018-12-31',3,0,5),
(DEFAULT,271135104,'2019-01-22',2,2,7);