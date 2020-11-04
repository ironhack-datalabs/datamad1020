-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customer` (
  `idcustomer` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `phone_number` INT NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state/province` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `zip/postal_code_consumer` INT NULL,
  PRIMARY KEY (`idcustomer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`salesperson` (
  `idsalesperson` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  PRIMARY KEY (`idsalesperson`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`car` (
  `idcar` INT NOT NULL AUTO_INCREMENT,
  `vin` INT NOT NULL,
  `manufacturer` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` DATETIME NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `customer_idcustomer` INT NOT NULL,
  PRIMARY KEY (`idcar`, `customer_idcustomer`),
  INDEX `fk_car_customer1_idx` (`customer_idcustomer` ASC) VISIBLE,
  CONSTRAINT `fk_car_customer1`
    FOREIGN KEY (`customer_idcustomer`)
    REFERENCES `mydb`.`customer` (`idcustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`invoce`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`invoce` (
  `idinvoce` INT NOT NULL,
  `date` DATETIME NULL,
  `car` VARCHAR(45) NULL,
  `customer` VARCHAR(45) NULL,
  `salesperson` VARCHAR(45) NULL,
  `customer_idcustomer` INT NOT NULL,
  `car_idcar` INT NOT NULL,
  `car_customer_idcustomer` INT NOT NULL,
  PRIMARY KEY (`idinvoce`, `customer_idcustomer`, `car_idcar`, `car_customer_idcustomer`),
  INDEX `fk_invoce_customer1_idx` (`customer_idcustomer` ASC) VISIBLE,
  INDEX `fk_invoce_car1_idx` (`car_idcar` ASC, `car_customer_idcustomer` ASC) VISIBLE,
  CONSTRAINT `fk_invoce_customer1`
    FOREIGN KEY (`customer_idcustomer`)
    REFERENCES `mydb`.`customer` (`idcustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoce_car1`
    FOREIGN KEY (`car_idcar` , `car_customer_idcustomer`)
    REFERENCES `mydb`.`car` (`idcar` , `customer_idcustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`salesperson_has_invoce`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`salesperson_has_invoce` (
  `salesperson_idsalesperson` INT NOT NULL,
  `invoce_idinvoce` INT NOT NULL,
  PRIMARY KEY (`salesperson_idsalesperson`, `invoce_idinvoce`),
  INDEX `fk_salesperson_has_invoce_invoce1_idx` (`invoce_idinvoce` ASC) VISIBLE,
  INDEX `fk_salesperson_has_invoce_salesperson_idx` (`salesperson_idsalesperson` ASC) VISIBLE,
  CONSTRAINT `fk_salesperson_has_invoce_salesperson`
    FOREIGN KEY (`salesperson_idsalesperson`)
    REFERENCES `mydb`.`salesperson` (`idsalesperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_salesperson_has_invoce_invoce1`
    FOREIGN KEY (`invoce_idinvoce`)
    REFERENCES `mydb`.`invoce` (`idinvoce`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
