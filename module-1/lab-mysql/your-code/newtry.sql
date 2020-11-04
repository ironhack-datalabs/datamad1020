-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema newtry
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema newtry
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `newtry` ;
USE `newtry` ;

-- -----------------------------------------------------
-- Table `newtry`.`Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `newtry`.`Salesperson` (
  `idSalesperson` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `store` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSalesperson`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `newtry`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `newtry`.`Customers` (
  `idCustomers` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `phone_number` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(45) NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `zip_code` INT NOT NULL,
  `Salesperson_idSalesperson` INT NOT NULL,
  PRIMARY KEY (`idCustomers`),
  INDEX `fk_Customers_Salesperson_idx` (`Salesperson_idSalesperson` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_Salesperson`
    FOREIGN KEY (`Salesperson_idSalesperson`)
    REFERENCES `newtry`.`Salesperson` (`idSalesperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `newtry`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `newtry`.`Invoices` (
  `invoice_number` INT NOT NULL,
  `date` INT NOT NULL,
  `car` INT NOT NULL,
  `customer` INT NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  PRIMARY KEY (`invoice_number`),
  INDEX `fk_Invoices_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `newtry`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `newtry`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `newtry`.`Cars` (
  `VIN` VARCHAR(45) NOT NULL,
  `manufacturer` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  `Invoices_invoice_number` INT NOT NULL,
  PRIMARY KEY (`VIN`),
  INDEX `fk_Cars_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  INDEX `fk_Cars_Invoices1_idx` (`Invoices_invoice_number` ASC) VISIBLE)
ENGINE = FEDERATED;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
