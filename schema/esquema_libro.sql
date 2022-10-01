-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_libros
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_libros` ;

-- -----------------------------------------------------
-- Schema esquema_libros
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_libros` DEFAULT CHARACTER SET utf8 ;
USE `esquema_libros` ;

-- -----------------------------------------------------
-- Table `esquema_libros`.`autores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros`.`autores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `autor` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_libros`.`libros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros`.`libros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(255) NULL,
  `num_pag` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_libros`.`libros_favoritos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros`.`libros_favoritos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `autor_id` INT NOT NULL,
  `libro_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favoritos_usuarios_idx` (`autor_id` ASC) VISIBLE,
  INDEX `fk_favoritos_libros1_idx` (`libro_id` ASC) VISIBLE,
  CONSTRAINT `fk_favoritos_usuarios`
    FOREIGN KEY (`autor_id`)
    REFERENCES `esquema_libros`.`autores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favoritos_libros1`
    FOREIGN KEY (`libro_id`)
    REFERENCES `esquema_libros`.`libros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
