-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema empresa_venta_vehiculos_nuevos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema empresa_venta_vehiculos_nuevos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `empresa_venta_vehiculos_nuevos` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `empresa_venta_vehiculos_nuevos` ;

-- -----------------------------------------------------
-- Table `empresa_venta_vehiculos_nuevos`.`vendedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `empresa_venta_vehiculos_nuevos`.`vendedores` (
  `idvendedores` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idvendedores`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `empresa_venta_vehiculos_nuevos`.`comprador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `empresa_venta_vehiculos_nuevos`.`comprador` (
  `idcliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `telefono` INT NOT NULL,
  `correo_electronico` VARCHAR(45) NULL,
  `dirección` VARCHAR(45) NOT NULL,
  `ciudad` VARCHAR(45) NOT NULL,
  `codigo_postal` INT NOT NULL,
  `vendedores_idvendedores` INT NOT NULL,
  PRIMARY KEY (`idcliente`, `vendedores_idvendedores`),
  INDEX `fk_comprador_vendedores1_idx` (`vendedores_idvendedores` ASC) VISIBLE,
  CONSTRAINT `fk_comprador_vendedores1`
    FOREIGN KEY (`vendedores_idvendedores`)
    REFERENCES `empresa_venta_vehiculos_nuevos`.`vendedores` (`idvendedores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `empresa_venta_vehiculos_nuevos`.`factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `empresa_venta_vehiculos_nuevos`.`factura` (
  `idfactura` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATETIME(6) NOT NULL,
  `automovil` VARCHAR(45) NOT NULL,
  `cliente` VARCHAR(45) NOT NULL,
  `vendedor` VARCHAR(45) NOT NULL,
  `vendedores_idvendedores` INT NOT NULL,
  `cliente_idcliente1` INT NOT NULL,
  PRIMARY KEY (`idfactura`),
  INDEX `fk_factura_vendedores1_idx` (`vendedores_idvendedores` ASC) VISIBLE,
  INDEX `fk_factura_cliente2_idx` (`cliente_idcliente1` ASC) VISIBLE,
  CONSTRAINT `fk_factura_vendedores1`
    FOREIGN KEY (`vendedores_idvendedores`)
    REFERENCES `empresa_venta_vehiculos_nuevos`.`vendedores` (`idvendedores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_factura_cliente2`
    FOREIGN KEY (`cliente_idcliente1`)
    REFERENCES `empresa_venta_vehiculos_nuevos`.`comprador` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `empresa_venta_vehiculos_nuevos`.`coche`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `empresa_venta_vehiculos_nuevos`.`coche` (
  `idcoches` INT NOT NULL AUTO_INCREMENT,
  `marca` VARCHAR(45) NOT NULL,
  `modelo` VARCHAR(45) NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `cliente_idcliente` INT NOT NULL,
  `fabricante` VARCHAR(45) NOT NULL,
  `factura_idfactura` INT NOT NULL,
  `vendedores_idvendedores` INT NOT NULL,
  PRIMARY KEY (`idcoches`, `vendedores_idvendedores`),
  INDEX `fk_coche_cliente1_idx` (`cliente_idcliente` ASC) VISIBLE,
  INDEX `fk_coche_factura1_idx` (`factura_idfactura` ASC) VISIBLE,
  INDEX `fk_coche_vendedores1_idx` (`vendedores_idvendedores` ASC) VISIBLE,
  CONSTRAINT `fk_coche_cliente1`
    FOREIGN KEY (`cliente_idcliente`)
    REFERENCES `empresa_venta_vehiculos_nuevos`.`comprador` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_coche_factura1`
    FOREIGN KEY (`factura_idfactura`)
    REFERENCES `empresa_venta_vehiculos_nuevos`.`factura` (`idfactura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_coche_vendedores1`
    FOREIGN KEY (`vendedores_idvendedores`)
    REFERENCES `empresa_venta_vehiculos_nuevos`.`vendedores` (`idvendedores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
