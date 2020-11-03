
SELECT * FROM lab_mysql.customers;
UPDATE `lab_mysql`.`customers` SET `email` = '-	ppicasso@gmail.com' WHERE (`customer ID` = '10001');
UPDATE `lab_mysql`.`customers` SET `email` = 'lincoln@us.gov' WHERE (`customer ID` = '20001');
UPDATE `lab_mysql`.`customers` SET `email` = '	hello@napoleon.me' WHERE (`customer ID` = '30001');


SELECT * FROM lab_mysql.salesperons;
UPDATE `lab_mysql`.`salesperons` SET `store` = 'Miami' WHERE (` staff ID` = '5');