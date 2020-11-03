-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Car_store
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Car_store
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Car_store` DEFAULT CHARACTER SET utf8 ;
USE `Car_store` ;

-- -----------------------------------------------------
-- Table `Car_store`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Car_store`.`car` (
  `car_id` INT NOT NULL AUTO_INCREMENT,
  `manufacturer` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `vin` INT NOT NULL,
  PRIMARY KEY (`car_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Car_store`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Car_store`.`customer` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `phone` INT NULL,
  `email` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state/province` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `zip/postal code` VARCHAR(45) NOT NULL,
  `id` INT NOT NULL,
  PRIMARY KEY (`customer_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Car_store`.`salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Car_store`.`salesperson` (
  `staff_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `store` VARCHAR(45) NOT NULL,
  `id` INT NOT NULL,
  PRIMARY KEY (`staff_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Car_store`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Car_store`.`invoice` (
  `invoice_number` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `car_car_id` INT NOT NULL,
  `salesperson_staff_id` INT NOT NULL,
  `invoice_number` INT NOT NULL,
  `customer_customer_id` INT NOT NULL,
  PRIMARY KEY (`invoice_number`),
  INDEX `fk_invoice_car_idx` (`car_car_id` ASC) VISIBLE,
  INDEX `fk_invoice_salesperson1_idx` (`salesperson_staff_id` ASC) VISIBLE,
  INDEX `fk_invoice_customer1_idx` (`customer_customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_invoice_car`
    FOREIGN KEY (`car_car_id`)
    REFERENCES `Car_store`.`car` (`car_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_salesperson1`
    FOREIGN KEY (`salesperson_staff_id`)
    REFERENCES `Car_store`.`salesperson` (`staff_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_customer1`
    FOREIGN KEY (`customer_customer_id`)
    REFERENCES `Car_store`.`customer` (`customer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
