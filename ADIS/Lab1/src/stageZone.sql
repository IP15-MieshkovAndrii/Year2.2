DROP SCHEMA IF EXISTS StageZone;
CREATE SCHEMA IF NOT EXISTS StageZone;
USE StageZone;

CREATE TABLE IF NOT EXISTS Hapiness (
  `hapiness_id` INT NOT NULL AUTO_INCREMENT,
  `country_name` VARCHAR(45) NULL,
  `year` INT NULL,
  `life_ladder` DECIMAL(10,3) NULL,
  `gdp_per_capita` DECIMAL(10,3) NULL,
  `positive_affect` DECIMAL(10,3) NULL,
  `social_support` DECIMAL(10,3) NULL,
  `life_expancy` DECIMAL(10,3) NULL,
  `freedom_choice` DECIMAL(10,3) NULL,
  `generocity` DECIMAL(10,3) NULL,
  `corruption` DECIMAL(10,3) NULL,
  `negative_affect` DECIMAL(10,3) NULL,
  PRIMARY KEY (`hapiness_id`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS Climat (
  `climat_id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NULL,
  `average_temperature` DECIMAL(10,3) NULL,
  `average_temperature_uncertainty` DECIMAL(10,3) NULL,
  `country_name` VARCHAR(45) NULL,
  PRIMARY KEY (`climat_id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Terrorism (
  `event_id` INT NOT NULL AUTO_INCREMENT,
  `event_name` VARCHAR(45) NULL,
  `year` INT NULL,
  `month` INT NULL,
  `day` INT NULL,
  `extended` TINYINT(2) NULL,
  `country_id` INT NULL,
  `country_name` VARCHAR(45) NULL,
  PRIMARY KEY (`event_id`))
ENGINE = InnoDB;

