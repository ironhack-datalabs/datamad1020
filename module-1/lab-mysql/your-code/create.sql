-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema sakila
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sakila
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sakila` ;
USE `sakila` ;

-- -----------------------------------------------------
-- Table `sakila`.`actor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`actor` (
  `actor_id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`actor_id`),
  INDEX `idx_actor_last_name` (`last_name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`country` (
  `country_id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `country` VARCHAR(50) NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`country_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`city` (
  `city_id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `city` VARCHAR(50) NOT NULL,
  `country_id` SMALLINT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`city_id`),
  INDEX `idx_fk_country_id` (`country_id` ASC),
  CONSTRAINT `fk_city_country`
    FOREIGN KEY (`country_id`)
    REFERENCES `sakila`.`country` (`country_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`address` (
  `address_id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(50) NOT NULL,
  `address2` VARCHAR(50) NULL DEFAULT NULL,
  `district` VARCHAR(20) NOT NULL,
  `city_id` SMALLINT UNSIGNED NOT NULL,
  `postal_code` VARCHAR(10) NULL DEFAULT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`address_id`),
  INDEX `idx_fk_city_id` (`city_id` ASC),
  CONSTRAINT `fk_address_city`
    FOREIGN KEY (`city_id`)
    REFERENCES `sakila`.`city` (`city_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`category` (
  `category_id` TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(25) NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`staff` (
  `staff_id` TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `address_id` SMALLINT UNSIGNED NOT NULL,
  `picture` BLOB NULL,
  `email` VARCHAR(50) NULL DEFAULT NULL,
  `store_id` TINYINT UNSIGNED NOT NULL,
  `active` TINYINT(1) NOT NULL DEFAULT TRUE,
  `username` VARCHAR(16) NOT NULL,
  `password` VARCHAR(40) BINARY NULL DEFAULT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`staff_id`),
  INDEX `idx_fk_store_id` (`store_id` ASC),
  INDEX `idx_fk_address_id` (`address_id` ASC),
  CONSTRAINT `fk_staff_store`
    FOREIGN KEY (`store_id`)
    REFERENCES `sakila`.`store` (`store_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_staff_address`
    FOREIGN KEY (`address_id`)
    REFERENCES `sakila`.`address` (`address_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`store` (
  `store_id` TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `manager_staff_id` TINYINT UNSIGNED NOT NULL,
  `address_id` SMALLINT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`store_id`),
  UNIQUE INDEX `idx_unique_manager` (`manager_staff_id` ASC),
  INDEX `idx_fk_address_id` (`address_id` ASC),
  CONSTRAINT `fk_store_staff`
    FOREIGN KEY (`manager_staff_id`)
    REFERENCES `sakila`.`staff` (`staff_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_store_address`
    FOREIGN KEY (`address_id`)
    REFERENCES `sakila`.`address` (`address_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`customer` (
  `id_customer` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `phone number` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state/province` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `zip/postal code` INT NOT NULL,
  PRIMARY KEY (`id_customer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakila`.`language`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`language` (
  `language_id` TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` CHAR(20) NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`language_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`film`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`film` (
  `film_id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT NULL,
  `release_year` YEAR NULL,
  `language_id` TINYINT UNSIGNED NOT NULL,
  `original_language_id` TINYINT UNSIGNED NULL DEFAULT NULL,
  `rental_duration` TINYINT UNSIGNED NOT NULL DEFAULT 3,
  `rental_rate` DECIMAL(4,2) NOT NULL DEFAULT 4.99,
  `length` SMALLINT UNSIGNED NULL DEFAULT NULL,
  `replacement_cost` DECIMAL(5,2) NOT NULL DEFAULT 19.99,
  `rating` ENUM('G','PG','PG-13','R','NC-17') NULL DEFAULT 'G',
  `special_features` SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes') NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_title` (`title` ASC),
  INDEX `idx_fk_language_id` (`language_id` ASC),
  INDEX `idx_fk_original_language_id` (`original_language_id` ASC),
  PRIMARY KEY (`film_id`),
  CONSTRAINT `fk_film_language`
    FOREIGN KEY (`language_id`)
    REFERENCES `sakila`.`language` (`language_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_film_language_original`
    FOREIGN KEY (`original_language_id`)
    REFERENCES `sakila`.`language` (`language_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`film_actor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`film_actor` (
  `actor_id` SMALLINT UNSIGNED NOT NULL,
  `film_id` SMALLINT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`actor_id`, `film_id`),
  INDEX `idx_fk_film_id` (`film_id` ASC),
  INDEX `fk_film_actor_actor_idx` (`actor_id` ASC),
  CONSTRAINT `fk_film_actor_actor`
    FOREIGN KEY (`actor_id`)
    REFERENCES `sakila`.`actor` (`actor_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_film_actor_film`
    FOREIGN KEY (`film_id`)
    REFERENCES `sakila`.`film` (`film_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`film_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`film_category` (
  `film_id` SMALLINT UNSIGNED NOT NULL,
  `category_id` TINYINT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`film_id`, `category_id`),
  INDEX `fk_film_category_category_idx` (`category_id` ASC),
  INDEX `fk_film_category_film_idx` (`film_id` ASC),
  CONSTRAINT `fk_film_category_film`
    FOREIGN KEY (`film_id`)
    REFERENCES `sakila`.`film` (`film_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_film_category_category`
    FOREIGN KEY (`category_id`)
    REFERENCES `sakila`.`category` (`category_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`film_text`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`film_text` (
  `film_id` SMALLINT UNSIGNED NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`film_id`),
  FULLTEXT INDEX `idx_title_description` (`title`, `description`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakila`.`inventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`inventory` (
  `inventory_id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `film_id` SMALLINT UNSIGNED NOT NULL,
  `store_id` TINYINT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`inventory_id`),
  INDEX `idx_fk_film_id` (`film_id` ASC),
  INDEX `idx_store_id_film_id` (`store_id` ASC, `film_id` ASC),
  INDEX `fk_inventory_store_idx` (`store_id` ASC),
  CONSTRAINT `fk_inventory_store`
    FOREIGN KEY (`store_id`)
    REFERENCES `sakila`.`store` (`store_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_inventory_film`
    FOREIGN KEY (`film_id`)
    REFERENCES `sakila`.`film` (`film_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`rental`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`rental` (
  `rental_id` INT NOT NULL AUTO_INCREMENT,
  `rental_date` DATETIME NOT NULL,
  `inventory_id` MEDIUMINT UNSIGNED NOT NULL,
  `customer_id` SMALLINT UNSIGNED NOT NULL,
  `return_date` DATETIME NULL,
  `staff_id` TINYINT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`rental_id`),
  UNIQUE INDEX `idx_rental` (`rental_date` ASC, `inventory_id` ASC, `customer_id` ASC),
  INDEX `idx_fk_inventory_id` (`inventory_id` ASC),
  INDEX `idx_fk_customer_id` (`customer_id` ASC),
  INDEX `idx_fk_staff_id` (`staff_id` ASC),
  CONSTRAINT `fk_rental_staff`
    FOREIGN KEY (`staff_id`)
    REFERENCES `sakila`.`staff` (`staff_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_rental_inventory`
    FOREIGN KEY (`inventory_id`)
    REFERENCES `sakila`.`inventory` (`inventory_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_rental_customer`
    FOREIGN KEY (`customer_id`)
    REFERENCES `sakila`.`customer` (`customer_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`payment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`payment` (
  `payment_id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `customer_id` SMALLINT UNSIGNED NOT NULL,
  `staff_id` TINYINT UNSIGNED NOT NULL,
  `rental_id` INT NULL DEFAULT NULL,
  `amount` DECIMAL(5,2) NOT NULL,
  `payment_date` DATETIME NOT NULL,
  `last_update` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`payment_id`),
  INDEX `idx_fk_staff_id` (`staff_id` ASC),
  INDEX `idx_fk_customer_id` (`customer_id` ASC),
  INDEX `fk_payment_rental_idx` (`rental_id` ASC),
  CONSTRAINT `fk_payment_rental`
    FOREIGN KEY (`rental_id`)
    REFERENCES `sakila`.`rental` (`rental_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_payment_customer`
    FOREIGN KEY (`customer_id`)
    REFERENCES `sakila`.`customer` (`customer_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_payment_staff`
    FOREIGN KEY (`staff_id`)
    REFERENCES `sakila`.`staff` (`staff_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sakila`.`pelicula`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`pelicula` (
  `peliculas_id` INT NOT NULL AUTO_INCREMENT,
  `name films` VARCHAR(45) NOT NULL,
  `peliculascol` VARCHAR(45) NULL,
  PRIMARY KEY (`peliculas_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakila`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`car` (
  `id_car` INT NOT NULL AUTO_INCREMENT,
  `vin` VARCHAR(45) NOT NULL,
  `manufacturer` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` VARCHAR(45) NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_car`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakila`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`customer` (
  `id_customer` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `phone number` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state/province` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `zip/postal code` INT NOT NULL,
  PRIMARY KEY (`id_customer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakila`.`salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`salesperson` (
  `id_salesperson` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `store` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_salesperson`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakila`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`invoice` (
  `id_invoices` INT NOT NULL AUTO_INCREMENT,
  `date` VARCHAR(45) NOT NULL,
  `car` VARCHAR(45) NOT NULL,
  `customer_id_customer` INT NOT NULL,
  `salesperson_id_salesperson` INT NOT NULL,
  PRIMARY KEY (`id_invoices`),
  INDEX `fk_invoices_customer1_idx` (`customer_id_customer` ASC),
  INDEX `fk_invoice_salesperson1_idx` (`salesperson_id_salesperson` ASC),
  CONSTRAINT `fk_invoices_customer1`
    FOREIGN KEY (`customer_id_customer`)
    REFERENCES `sakila`.`customer` (`id_customer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_salesperson1`
    FOREIGN KEY (`salesperson_id_salesperson`)
    REFERENCES `sakila`.`salesperson` (`id_salesperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sakila`.`invoice_car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`invoice_car` (
  `car_id_car` INT NOT NULL,
  `invoice_id_invoices` INT NOT NULL,
  PRIMARY KEY (`car_id_car`, `invoice_id_invoices`),
  INDEX `fk_invoice_car_invoice1_idx` (`invoice_id_invoices` ASC),
  CONSTRAINT `fk_invoice_car_car1`
    FOREIGN KEY (`car_id_car`)
    REFERENCES `sakila`.`car` (`id_car`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_car_invoice1`
    FOREIGN KEY (`invoice_id_invoices`)
    REFERENCES `sakila`.`invoice` (`id_invoices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `sakila` ;

-- -----------------------------------------------------
-- Placeholder table for view `sakila`.`customer_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`customer_list` (`ID` INT, `name` INT, `address` INT, `zip code` INT, `phone` INT, `city` INT, `country` INT, `notes` INT, `SID` INT);

-- -----------------------------------------------------
-- Placeholder table for view `sakila`.`film_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`film_list` (`FID` INT, `title` INT, `description` INT, `category` INT, `price` INT, `length` INT, `rating` INT, `actors` INT);

-- -----------------------------------------------------
-- Placeholder table for view `sakila`.`nicer_but_slower_film_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`nicer_but_slower_film_list` (`FID` INT, `title` INT, `description` INT, `category` INT, `price` INT, `length` INT, `rating` INT, `actors` INT);

-- -----------------------------------------------------
-- Placeholder table for view `sakila`.`staff_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`staff_list` (`ID` INT, `name` INT, `address` INT, `zip code` INT, `phone` INT, `city` INT, `country` INT, `SID` INT);

-- -----------------------------------------------------
-- Placeholder table for view `sakila`.`sales_by_store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`sales_by_store` (`store` INT, `manager` INT, `total_sales` INT);

-- -----------------------------------------------------
-- Placeholder table for view `sakila`.`sales_by_film_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`sales_by_film_category` (`category` INT, `total_sales` INT);

-- -----------------------------------------------------
-- Placeholder table for view `sakila`.`actor_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sakila`.`actor_info` (`actor_id` INT, `first_name` INT, `last_name` INT, `film_info` INT);

-- -----------------------------------------------------
-- procedure rewards_report
-- -----------------------------------------------------

DELIMITER $$
USE `sakila`$$


CREATE PROCEDURE `sakila`.`rewards_report` (
    IN min_monthly_purchases TINYINT UNSIGNED
    , IN min_dollar_amount_purchased DECIMAL(10,2) UNSIGNED
    , OUT count_rewardees INT
)
LANGUAGE SQL
NOT DETERMINISTIC 
READS SQL DATA
SQL SECURITY DEFINER
COMMENT 'Provides a customizable report on best customers'
proc: BEGIN
    
    DECLARE last_month_start DATE;
    DECLARE last_month_end DATE;

    /* Some sanity checks... */
    IF min_monthly_purchases = 0 THEN
        SELECT 'Minimum monthly purchases parameter must be > 0';
        LEAVE proc;
    END IF;
    IF min_dollar_amount_purchased = 0.00 THEN
        SELECT 'Minimum monthly dollar amount purchased parameter must be > $0.00';
        LEAVE proc;
    END IF;

    /* Determine start and end time periods */
    SET last_month_start = DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH);
    SET last_month_start = STR_TO_DATE(CONCAT(YEAR(last_month_start),'-',MONTH(last_month_start),'-01'),'%Y-%m-%d');
    SET last_month_end = LAST_DAY(last_month_start);

    /* 
        Create a temporary storage area for 
        Customer IDs.  
    */
    CREATE TEMPORARY TABLE tmpCustomer (customer_id SMALLINT UNSIGNED NOT NULL PRIMARY KEY);

    /* 
        Find all customers meeting the 
        monthly purchase requirements
    */
    INSERT INTO tmpCustomer (customer_id)
    SELECT p.customer_id 
    FROM payment AS p
    WHERE DATE(p.payment_date) BETWEEN last_month_start AND last_month_end
    GROUP BY customer_id
    HAVING SUM(p.amount) > min_dollar_amount_purchased
    AND COUNT(customer_id) > min_monthly_purchases;

    /* Populate OUT parameter with count of found customers */
    SELECT COUNT(*) FROM tmpCustomer INTO count_rewardees;

    /* 
        Output ALL customer information of matching rewardees.
        Customize output as needed.
    */
    SELECT c.* 
    FROM tmpCustomer AS t   
    INNER JOIN customer AS c ON t.customer_id = c.customer_id;

    /* Clean up */
    DROP TABLE tmpCustomer;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function get_customer_balance
-- -----------------------------------------------------

DELIMITER $$
USE `sakila`$$


CREATE FUNCTION `sakila`.`get_customer_balance`(p_customer_id INT, p_effective_date DATETIME) RETURNS DECIMAL(5,2)
    DETERMINISTIC
    READS SQL DATA
BEGIN

       #OK, WE NEED TO CALCULATE THE CURRENT BALANCE GIVEN A CUSTOMER_ID AND A DATE
       #THAT WE WANT THE BALANCE TO BE EFFECTIVE FOR. THE BALANCE IS:
       #   1) RENTAL FEES FOR ALL PREVIOUS RENTALS
       #   2) ONE DOLLAR FOR EVERY DAY THE PREVIOUS RENTALS ARE OVERDUE
       #   3) IF A FILM IS MORE THAN RENTAL_DURATION * 2 OVERDUE, CHARGE THE REPLACEMENT_COST
       #   4) SUBTRACT ALL PAYMENTS MADE BEFORE THE DATE SPECIFIED

  DECLARE v_rentfees DECIMAL(5,2); #FEES PAID TO RENT THE VIDEOS INITIALLY
  DECLARE v_overfees INTEGER;      #LATE FEES FOR PRIOR RENTALS
  DECLARE v_payments DECIMAL(5,2); #SUM OF PAYMENTS MADE PREVIOUSLY

  SELECT IFNULL(SUM(film.rental_rate),0) INTO v_rentfees
    FROM film, inventory, rental
    WHERE film.film_id = inventory.film_id
      AND inventory.inventory_id = rental.inventory_id
      AND rental.rental_date <= p_effective_date
      AND rental.customer_id = p_customer_id;

  SELECT IFNULL(SUM(IF((TO_DAYS(rental.return_date) - TO_DAYS(rental.rental_date)) > film.rental_duration,
        ((TO_DAYS(rental.return_date) - TO_DAYS(rental.rental_date)) - film.rental_duration),0)),0) INTO v_overfees
    FROM rental, inventory, film
    WHERE film.film_id = inventory.film_id
      AND inventory.inventory_id = rental.inventory_id
      AND rental.rental_date <= p_effective_date
      AND rental.customer_id = p_customer_id;


  SELECT IFNULL(SUM(payment.amount),0) INTO v_payments
    FROM payment

    WHERE payment.payment_date <= p_effective_date
    AND payment.customer_id = p_customer_id;

  RETURN v_rentfees + v_overfees - v_payments;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure film_in_stock
-- -----------------------------------------------------

DELIMITER $$
USE `sakila`$$


CREATE PROCEDURE `sakila`.`film_in_stock`(IN p_film_id INT, IN p_store_id INT, OUT p_film_count INT)
READS SQL DATA
BEGIN
     SELECT inventory_id
     FROM inventory
     WHERE film_id = p_film_id
     AND store_id = p_store_id
     AND inventory_in_stock(inventory_id);

     SELECT FOUND_ROWS() INTO p_film_count;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure film_not_in_stock
-- -----------------------------------------------------

DELIMITER $$
USE `sakila`$$


CREATE PROCEDURE `sakila`.`film_not_in_stock`(IN p_film_id INT, IN p_store_id INT, OUT p_film_count INT)
READS SQL DATA
BEGIN
     SELECT inventory_id
     FROM inventory
     WHERE film_id = p_film_id
     AND store_id = p_store_id
     AND NOT inventory_in_stock(inventory_id);

     SELECT FOUND_ROWS() INTO p_film_count;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function inventory_held_by_customer
-- -----------------------------------------------------

DELIMITER $$
USE `sakila`$$


CREATE FUNCTION `sakila`.`inventory_held_by_customer`(p_inventory_id INT) RETURNS INT
READS SQL DATA
BEGIN
  DECLARE v_customer_id INT;
  DECLARE EXIT HANDLER FOR NOT FOUND RETURN NULL;

  SELECT customer_id INTO v_customer_id
  FROM rental
  WHERE return_date IS NULL
  AND inventory_id = p_inventory_id;

  RETURN v_customer_id;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function inventory_in_stock
-- -----------------------------------------------------

DELIMITER $$
USE `sakila`$$


CREATE FUNCTION `sakila`.`inventory_in_stock`(p_inventory_id INT) RETURNS BOOLEAN
READS SQL DATA
BEGIN
    DECLARE v_rentals INT;
    DECLARE v_out     INT;

    #AN ITEM IS IN-STOCK IF THERE ARE EITHER NO ROWS IN THE rental TABLE
    #FOR THE ITEM OR ALL ROWS HAVE return_date POPULATED

    SELECT COUNT(*) INTO v_rentals
    FROM rental
    WHERE inventory_id = p_inventory_id;

    IF v_rentals = 0 THEN
      RETURN TRUE;
    END IF;

    SELECT COUNT(rental_id) INTO v_out
    FROM inventory LEFT JOIN rental USING(inventory_id)
    WHERE inventory.inventory_id = p_inventory_id
    AND rental.return_date IS NULL;

    IF v_out > 0 THEN
      RETURN FALSE;
    ELSE
      RETURN TRUE;
    END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- View `sakila`.`customer_list`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sakila`.`customer_list`;
USE `sakila`;
--
-- View structure for view `customer_list`
--

CREATE  OR REPLACE VIEW customer_list 
AS 
SELECT cu.customer_id AS ID, CONCAT(cu.first_name, _utf8' ', cu.last_name) AS name, a.address AS address, a.postal_code AS `zip code`,
	a.phone AS phone, city.city AS city, country.country AS country, IF(cu.active, _utf8'active',_utf8'') AS notes, cu.store_id AS SID 
FROM customer AS cu JOIN address AS a ON cu.address_id = a.address_id JOIN city ON a.city_id = city.city_id 
	JOIN country ON city.country_id = country.country_id;

-- -----------------------------------------------------
-- View `sakila`.`film_list`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sakila`.`film_list`;
USE `sakila`;
--
-- View structure for view `film_list`
--

CREATE  OR REPLACE VIEW film_list 
AS 
SELECT film.film_id AS FID, film.title AS title, film.description AS description, category.name AS category, film.rental_rate AS price,
	film.length AS length, film.rating AS rating, GROUP_CONCAT(CONCAT(actor.first_name, _utf8' ', actor.last_name) SEPARATOR ', ') AS actors 
FROM category LEFT JOIN film_category ON category.category_id = film_category.category_id LEFT JOIN film ON film_category.film_id = film.film_id
        JOIN film_actor ON film.film_id = film_actor.film_id 
	JOIN actor ON film_actor.actor_id = actor.actor_id 
GROUP BY film.film_id, category.name;

-- -----------------------------------------------------
-- View `sakila`.`nicer_but_slower_film_list`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sakila`.`nicer_but_slower_film_list`;
USE `sakila`;
--
-- View structure for view `nicer_but_slower_film_list`
--

CREATE  OR REPLACE VIEW nicer_but_slower_film_list 
AS 
SELECT film.film_id AS FID, film.title AS title, film.description AS description, category.name AS category, film.rental_rate AS price, 
	film.length AS length, film.rating AS rating, GROUP_CONCAT(CONCAT(CONCAT(UCASE(SUBSTR(actor.first_name,1,1)),
	LCASE(SUBSTR(actor.first_name,2,LENGTH(actor.first_name))),_utf8' ',CONCAT(UCASE(SUBSTR(actor.last_name,1,1)),
	LCASE(SUBSTR(actor.last_name,2,LENGTH(actor.last_name)))))) SEPARATOR ', ') AS actors 
FROM category LEFT JOIN film_category ON category.category_id = film_category.category_id LEFT JOIN film ON film_category.film_id = film.film_id
        JOIN film_actor ON film.film_id = film_actor.film_id
	JOIN actor ON film_actor.actor_id = actor.actor_id 
GROUP BY film.film_id, category.name;

-- -----------------------------------------------------
-- View `sakila`.`staff_list`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sakila`.`staff_list`;
USE `sakila`;
--
-- View structure for view `staff_list`
--

CREATE  OR REPLACE VIEW staff_list 
AS 
SELECT s.staff_id AS ID, CONCAT(s.first_name, _utf8' ', s.last_name) AS name, a.address AS address, a.postal_code AS `zip code`, a.phone AS phone,
	city.city AS city, country.country AS country, s.store_id AS SID 
FROM staff AS s JOIN address AS a ON s.address_id = a.address_id JOIN city ON a.city_id = city.city_id 
	JOIN country ON city.country_id = country.country_id;

-- -----------------------------------------------------
-- View `sakila`.`sales_by_store`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sakila`.`sales_by_store`;
USE `sakila`;
--
-- View structure for view `sales_by_store`
--

CREATE  OR REPLACE VIEW sales_by_store
AS 
SELECT 
CONCAT(c.city, _utf8',', cy.country) AS store
, CONCAT(m.first_name, _utf8' ', m.last_name) AS manager
, SUM(p.amount) AS total_sales
FROM payment AS p
INNER JOIN rental AS r ON p.rental_id = r.rental_id
INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN store AS s ON i.store_id = s.store_id
INNER JOIN address AS a ON s.address_id = a.address_id
INNER JOIN city AS c ON a.city_id = c.city_id
INNER JOIN country AS cy ON c.country_id = cy.country_id
INNER JOIN staff AS m ON s.manager_staff_id = m.staff_id
GROUP BY s.store_id
ORDER BY cy.country, c.city;

-- -----------------------------------------------------
-- View `sakila`.`sales_by_film_category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sakila`.`sales_by_film_category`;
USE `sakila`;
--
-- View structure for view `sales_by_film_category`
--
-- Note that total sales will add up to >100% because
-- some titles belong to more than 1 category
--

CREATE  OR REPLACE VIEW sales_by_film_category
AS 
SELECT 
c.name AS category
, SUM(p.amount) AS total_sales
FROM payment AS p
INNER JOIN rental AS r ON p.rental_id = r.rental_id
INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN film AS f ON i.film_id = f.film_id
INNER JOIN film_category AS fc ON f.film_id = fc.film_id
INNER JOIN category AS c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY total_sales DESC;

-- -----------------------------------------------------
-- View `sakila`.`actor_info`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sakila`.`actor_info`;
USE `sakila`;
--
-- View structure for view `actor_info`
--

CREATE  OR REPLACE DEFINER=CURRENT_USER SQL SECURITY INVOKER VIEW actor_info 
AS
SELECT      
a.actor_id,
a.first_name,
a.last_name,
GROUP_CONCAT(DISTINCT CONCAT(c.name, ': ',
		(SELECT GROUP_CONCAT(f.title ORDER BY f.title SEPARATOR ', ')
                    FROM sakila.film f
                    INNER JOIN sakila.film_category fc
                      ON f.film_id = fc.film_id
                    INNER JOIN sakila.film_actor fa
                      ON f.film_id = fa.film_id
                    WHERE fc.category_id = c.category_id
                    AND fa.actor_id = a.actor_id
                 )
             )
             ORDER BY c.name SEPARATOR '; ')
AS film_info
FROM sakila.actor a
LEFT JOIN sakila.film_actor fa
  ON a.actor_id = fa.actor_id
LEFT JOIN sakila.film_category fc
  ON fa.film_id = fc.film_id
LEFT JOIN sakila.category c
  ON fc.category_id = c.category_id
GROUP BY a.actor_id, a.first_name, a.last_name;
USE `sakila`;

DELIMITER $$
USE `sakila`$$

CREATE TRIGGER `ins_film` AFTER INSERT ON `film` FOR EACH ROW BEGIN
    INSERT INTO film_text (film_id, title, description)
        VALUES (new.film_id, new.title, new.description);
  END$$

USE `sakila`$$

CREATE TRIGGER `upd_film` AFTER UPDATE ON `film` FOR EACH ROW BEGIN
    IF (old.title != new.title) or (old.description != new.description)
    THEN
        UPDATE film_text
            SET title=new.title,
                description=new.description,
                film_id=new.film_id
        WHERE film_id=old.film_id;
    END IF;
  END$$

USE `sakila`$$

CREATE TRIGGER `del_film` AFTER DELETE ON `film` FOR EACH ROW BEGIN
    DELETE FROM film_text WHERE film_id = old.film_id;
  END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
