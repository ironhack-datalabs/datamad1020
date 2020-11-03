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
-- Table `mydb`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`clientes` (
  `id_clientes` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `num telefono` INT NOT NULL,
  `correo electronico` VARCHAR(45) NOT NULL,
  `dirección` VARCHAR(45) NOT NULL,
  `ciudad` VARCHAR(45) NOT NULL,
  `estado/provincia` VARCHAR(45) NOT NULL,
  `país` VARCHAR(45) NOT NULL,
  `código postal clientes` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_clientes`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`vendedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`vendedores` (
  `id_personal` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `tienda de la empresa` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_personal`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`facturas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`facturas` (
  `id_facturas` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATETIME NOT NULL,
  `automovil` VARCHAR(45) NOT NULL,
  `cliente` VARCHAR(45) NOT NULL,
  `vendedor relacionado con venta` VARCHAR(45) NOT NULL,
  `clientes_id_clientes` INT NOT NULL,
  `vendedores_id_personal` INT NOT NULL,
  PRIMARY KEY (`id_facturas`, `vendedores_id_personal`),
  INDEX `fk_facturas_clientes_idx` (`clientes_id_clientes` ASC) VISIBLE,
  INDEX `fk_facturas_vendedores1_idx` (`vendedores_id_personal` ASC) VISIBLE,
  CONSTRAINT `fk_facturas_clientes`
    FOREIGN KEY (`clientes_id_clientes`)
    REFERENCES `mydb`.`clientes` (`id_clientes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturas_vendedores1`
    FOREIGN KEY (`vendedores_id_personal`)
    REFERENCES `mydb`.`vendedores` (`id_personal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`automoviles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`automoviles` (
  `id_identificación vahiculo` INT NOT NULL AUTO_INCREMENT,
  `nº identificacion del vehiculo(VIN)` INT NOT NULL,
  `fabricante` VARCHAR(45) NOT NULL,
  `modelo` VARCHAR(45) NOT NULL,
  `año` DATETIME NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `facturas_id_facturas` INT NOT NULL,
  `facturas_vendedores_id_personal` INT NOT NULL,
  PRIMARY KEY (`id_identificación vahiculo`, `facturas_id_facturas`, `facturas_vendedores_id_personal`),
  INDEX `fk_automoviles_facturas1_idx` (`facturas_id_facturas` ASC, `facturas_vendedores_id_personal` ASC) VISIBLE,
  CONSTRAINT `fk_automoviles_facturas1`
    FOREIGN KEY (`facturas_id_facturas` , `facturas_vendedores_id_personal`)
    REFERENCES `mydb`.`facturas` (`id_facturas` , `vendedores_id_personal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`clientes_has_automoviles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`clientes_has_automoviles` (
  `clientes_id_clientes` INT NOT NULL,
  `automoviles_id_identificación vahiculo` INT NOT NULL,
  `automoviles_facturas_id_facturas` INT NOT NULL,
  `automoviles_facturas_vendedores_id_personal` INT NOT NULL,
  PRIMARY KEY (`clientes_id_clientes`, `automoviles_id_identificación vahiculo`, `automoviles_facturas_id_facturas`, `automoviles_facturas_vendedores_id_personal`),
  INDEX `fk_clientes_has_automoviles_automoviles1_idx` (`automoviles_id_identificación vahiculo` ASC, `automoviles_facturas_id_facturas` ASC, `automoviles_facturas_vendedores_id_personal` ASC) VISIBLE,
  INDEX `fk_clientes_has_automoviles_clientes1_idx` (`clientes_id_clientes` ASC) VISIBLE,
  CONSTRAINT `fk_clientes_has_automoviles_clientes1`
    FOREIGN KEY (`clientes_id_clientes`)
    REFERENCES `mydb`.`clientes` (`id_clientes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_clientes_has_automoviles_automoviles1`
    FOREIGN KEY (`automoviles_id_identificación vahiculo` , `automoviles_facturas_id_facturas` , `automoviles_facturas_vendedores_id_personal`)
    REFERENCES `mydb`.`automoviles` (`id_identificación vahiculo` , `facturas_id_facturas` , `facturas_vendedores_id_personal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`automoviles_has_vendedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`automoviles_has_vendedores` (
  `automoviles_id_identificación vahiculo` INT NOT NULL,
  `automoviles_facturas_id_facturas` INT NOT NULL,
  `automoviles_facturas_vendedores_id_personal` INT NOT NULL,
  `vendedores_id_personal` INT NOT NULL,
  PRIMARY KEY (`automoviles_id_identificación vahiculo`, `automoviles_facturas_id_facturas`, `automoviles_facturas_vendedores_id_personal`, `vendedores_id_personal`),
  INDEX `fk_automoviles_has_vendedores_vendedores1_idx` (`vendedores_id_personal` ASC) VISIBLE,
  INDEX `fk_automoviles_has_vendedores_automoviles1_idx` (`automoviles_id_identificación vahiculo` ASC, `automoviles_facturas_id_facturas` ASC, `automoviles_facturas_vendedores_id_personal` ASC) VISIBLE,
  CONSTRAINT `fk_automoviles_has_vendedores_automoviles1`
    FOREIGN KEY (`automoviles_id_identificación vahiculo` , `automoviles_facturas_id_facturas` , `automoviles_facturas_vendedores_id_personal`)
    REFERENCES `mydb`.`automoviles` (`id_identificación vahiculo` , `facturas_id_facturas` , `facturas_vendedores_id_personal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_automoviles_has_vendedores_vendedores1`
    FOREIGN KEY (`vendedores_id_personal`)
    REFERENCES `mydb`.`vendedores` (`id_personal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
