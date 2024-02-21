
CREATE SCHEMA IF NOT EXISTS DataWarehouse;
USE DataWarehouse;
-- -----------------------------------------------------
-- Table dim_climat
-- -----------------------------------------------------
DROP TABLE IF EXISTS dim_climat;
CREATE TABLE IF NOT EXISTS dim_climat (
  `climat_id` INT NOT NULL AUTO_INCREMENT,
  `average_temperature` DECIMAL(10,3) NULL,
  `average_temperature_uncertainty` DECIMAL(10,3) NULL,
  PRIMARY KEY (`climat_id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table dim_terrorism
-- -----------------------------------------------------
DROP TABLE IF EXISTS dim_terrorism;
CREATE TABLE IF NOT EXISTS dim_terrorism (
  `event_id` INT NOT NULL AUTO_INCREMENT,
  `event_name` VARCHAR(45) NULL,
  `extended` TINYINT(2) NULL,
  PRIMARY KEY (`event_id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table dim_date
-- -----------------------------------------------------
DROP TABLE IF EXISTS dim_date;
CREATE TABLE IF NOT EXISTS dim_date (
  `date_id` INT NOT NULL AUTO_INCREMENT,
  `year` INT NULL,
  `month` INT NULL,
  `day` INT NULL,
  PRIMARY KEY (`date_id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table dim_country
-- -----------------------------------------------------
DROP TABLE IF EXISTS dim_country;
CREATE TABLE IF NOT EXISTS dim_country (
  `country_id` INT NOT NULL AUTO_INCREMENT,
  `country_code` INT NULL,
  `country_name` VARCHAR(45) NULL,
  PRIMARY KEY (`country_id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table fact_hapiness_analysis
-- -----------------------------------------------------
DROP TABLE IF EXISTS fact_hapiness_analysis;
CREATE TABLE IF NOT EXISTS fact_hapiness_analysis (
  `fact_hapiness_analysis_id` INT NOT NULL AUTO_INCREMENT,
  `climat_id` INT NULL,
  `date_id` INT NULL,
  `country_id` INT NULL,
  `event_id` INT NULL,
  `life_ladder` DECIMAL(10,3) NULL,
  `gdp_per_capita` DECIMAL(10,3) NULL,
  `positive_affect` DECIMAL(10,3) NULL,
  `social_support` DECIMAL(10,3) NULL,
  `life_expancy` DECIMAL(10,3) NULL,
  `freedom_choice` DECIMAL(10,3) NULL,
  `generocity` DECIMAL(10,3) NULL,
  `corruption` DECIMAL(10,3) NULL,
  `negative_affect` DECIMAL(10,3) NULL,
  PRIMARY KEY (`fact_hapiness_analysis_id`),
  INDEX `fk1_idx` (`climat_id` ASC) VISIBLE,
  INDEX `fk2_idx` (`date_id` ASC) VISIBLE,
  INDEX `fk3_idx` (`country_id` ASC) VISIBLE,
  INDEX `fk4_idx` (`event_id` ASC) VISIBLE,
  CONSTRAINT `fk1`
    FOREIGN KEY (`climat_id`)
    REFERENCES dim_climat (`climat_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk2`
    FOREIGN KEY (`date_id`)
    REFERENCES dim_date (`date_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk3`
    FOREIGN KEY (`country_id`)
    REFERENCES dim_country (`country_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk4`
    FOREIGN KEY (`event_id`)
    REFERENCES dim_terrorism (`event_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
