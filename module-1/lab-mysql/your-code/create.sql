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
-- Table `mydb`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`address` (
  `id_address` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `zip_code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_address`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`salesperson` (
  `id_salesperson` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `store` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_salesperson`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customer` (
  `id_customer` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `phone_number` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NULL,
  `id_address` INT NOT NULL,
  `id_salesperson` INT NOT NULL,
  PRIMARY KEY (`id_customer`, `id_address`),
  INDEX `fk_customer_address1_idx` (`id_address` ASC) VISIBLE,
  INDEX `fk_customer_salesperson1_idx` (`id_salesperson` ASC) VISIBLE,
  CONSTRAINT `fk_customer_address1`
    FOREIGN KEY (`id_address`)
    REFERENCES `mydb`.`address` (`id_address`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_customer_salesperson1`
    FOREIGN KEY (`id_salesperson`)
    REFERENCES `mydb`.`salesperson` (`id_salesperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`car` (
  `id_car` INT NOT NULL AUTO_INCREMENT,
  `VIN` INT NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `customer_id_customer` INT NOT NULL,
  PRIMARY KEY (`id_car`),
  INDEX `fk_car_customer1_idx` (`customer_id_customer` ASC) VISIBLE,
  CONSTRAINT `fk_car_customer1`
    FOREIGN KEY (`customer_id_customer`)
    REFERENCES `mydb`.`customer` (`id_customer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`manufacturer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`manufacturer` (
  `id_manufacturer` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_manufacturer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`car_has_manufacturer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`car_has_manufacturer` (
  `id_manufacturer` INT NOT NULL,
  `id_car` INT NOT NULL,
  `contract_manufacturer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_manufacturer`, `id_car`),
  INDEX `fk_manufacturer_has_car_car1_idx` (`id_car` ASC) VISIBLE,
  INDEX `fk_manufacturer_has_car_manufacturer_idx` (`id_manufacturer` ASC) VISIBLE,
  CONSTRAINT `fk_manufacturer_has_car_manufacturer`
    FOREIGN KEY (`id_manufacturer`)
    REFERENCES `mydb`.`manufacturer` (`id_manufacturer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_manufacturer_has_car_car1`
    FOREIGN KEY (`id_car`)
    REFERENCES `mydb`.`car` (`id_car`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`invoice` (
  `id_invoice` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `id_car_vin` INT NOT NULL,
  `id_customer` INT NOT NULL,
  `id_address` INT NOT NULL,
  `id_salesperson` INT NOT NULL,
  PRIMARY KEY (`id_invoice`),
  INDEX `fk_invoice_car1_idx` (`id_car_vin` ASC) VISIBLE,
  INDEX `fk_invoice_customer1_idx` (`id_customer` ASC, `id_address` ASC) VISIBLE,
  INDEX `fk_invoice_salesperson1_idx` (`id_salesperson` ASC) VISIBLE,
  CONSTRAINT `fk_invoice_car1`
    FOREIGN KEY (`id_car_vin`)
    REFERENCES `mydb`.`car` (`id_car`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_customer1`
    FOREIGN KEY (`id_customer` , `id_address`)
    REFERENCES `mydb`.`customer` (`id_customer` , `id_address`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_salesperson1`
    FOREIGN KEY (`id_salesperson`)
    REFERENCES `mydb`.`salesperson` (`id_salesperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
