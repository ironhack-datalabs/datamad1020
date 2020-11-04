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
-- Table `mydb`.`sales person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`sales person` (
  `idsales person` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `store at you company` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsales person`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customers` (
  `idcustomers` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `phone number` INT NULL,
  `email` VARCHAR(45) NOT NULL,
  `sales person_idsales person` INT NOT NULL,
  PRIMARY KEY (`idcustomers`),
  INDEX `fk_customers_sales person1_idx` (`sales person_idsales person` ASC) VISIBLE,
  CONSTRAINT `fk_customers_sales person1`
    FOREIGN KEY (`sales person_idsales person`)
    REFERENCES `mydb`.`sales person` (`idsales person`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Invoices` (
  `idInvoices` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `car` INT NOT NULL,
  `customer` VARCHAR(45) NULL,
  `customers_idcustomers` INT NOT NULL,
  PRIMARY KEY (`idInvoices`),
  INDEX `fk_Invoices_customers1_idx` (`customers_idcustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_customers1`
    FOREIGN KEY (`customers_idcustomers`)
    REFERENCES `mydb`.`customers` (`idcustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cars` (
  `idcars` VARCHAR(45) NOT NULL,
  `manufacturer` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  `colour` VARCHAR(45) NULL,
  `customers_idcustomers` INT NOT NULL,
  `Invoices_idInvoices` INT NOT NULL,
  PRIMARY KEY (`idcars`),
  INDEX `fk_cars_customers_idx` (`customers_idcustomers` ASC) VISIBLE,
  INDEX `fk_cars_Invoices1_idx` (`Invoices_idInvoices` ASC) VISIBLE,
  CONSTRAINT `fk_cars_customers`
    FOREIGN KEY (`customers_idcustomers`)
    REFERENCES `mydb`.`customers` (`idcustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cars_Invoices1`
    FOREIGN KEY (`Invoices_idInvoices`)
    REFERENCES `mydb`.`Invoices` (`idInvoices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`sales person_has_cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`sales person_has_cars` (
  `sales person_idsales person` INT NOT NULL,
  `cars_idcars` INT NOT NULL,
  PRIMARY KEY (`sales person_idsales person`, `cars_idcars`),
  INDEX `fk_sales person_has_cars_cars1_idx` (`cars_idcars` ASC) VISIBLE,
  INDEX `fk_sales person_has_cars_sales person1_idx` (`sales person_idsales person` ASC) VISIBLE,
  CONSTRAINT `fk_sales person_has_cars_sales person1`
    FOREIGN KEY (`sales person_idsales person`)
    REFERENCES `mydb`.`sales person` (`idsales person`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sales person_has_cars_cars1`
    FOREIGN KEY (`cars_idcars`)
    REFERENCES `mydb`.`cars` (`idcars`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`adress`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`adress` (
  `idadress` INT NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `zip code` INT NOT NULL,
  `customers_idcustomers` INT NOT NULL,
  PRIMARY KEY (`idadress`),
  INDEX `fk_adress_customers1_idx` (`customers_idcustomers` ASC) VISIBLE,
  CONSTRAINT `fk_adress_customers1`
    FOREIGN KEY (`customers_idcustomers`)
    REFERENCES `mydb`.`customers` (`idcustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
