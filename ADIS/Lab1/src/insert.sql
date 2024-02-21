-- ----------------------------------------------------
-- Table dim_climat
-- -----------------------------------------------------
INSERT INTO DataWarehouse.dim_climat (average_temperature, average_temperature_uncertainty)
SELECT 
  ROUND(average_temperature, 3) as average_temperature,
  ROUND(average_temperature_uncertainty, 3) as average_temperature_uncertainty
FROM StageZone.Climat;
-- ----------------------------------------------------
-- Table dim_terrorism
-- -----------------------------------------------------
INSERT INTO DataWarehouse.dim_terrorism (event_name, extended)
SELECT event_name, extended
FROM StageZone.Terrorism;

-- ----------------------------------------------------
-- Table dim_country
-- -----------------------------------------------------
INSERT INTO DataWarehouse.dim_country (country_code, country_name)
SELECT country_id, country_name FROM StageZone.Terrorism
UNION
SELECT NULL, country_name FROM StageZone.Hapiness
UNION
SELECT NULL, country_name FROM StageZone.Climat
WHERE NOT EXISTS (
  SELECT * FROM DataWarehouse.dim_country
  WHERE DataWarehouse.dim_country.country_name = StageZone.Hapiness.country_name
  OR DataWarehouse.dim_country.country_name = country_name
);

-- ----------------------------------------------------
-- Table dim_date
-- -----------------------------------------------------
INSERT IGNORE INTO DataWarehouse.dim_date (year, month, day)
SELECT DISTINCT YEAR(date) AS year, MONTH(date) AS month, DAY(date) AS day
FROM StageZone.Climat
UNION
SELECT DISTINCT year, NULL, NULL FROM StageZone.Hapiness
UNION
SELECT DISTINCT year, month, day FROM StageZone.Terrorism
WHERE NOT EXISTS (
  SELECT * FROM DataWarehouse.dim_date
  WHERE (DataWarehouse.dim_date.year = year AND DataWarehouse.dim_date.month = month AND DataWarehouse.dim_date.day = day)
);
-- ----------------------------------------------------
-- Table fact_hapiness_analysis
-- -----------------------------------------------------
USE DataWarehouse;
INSERT INTO fact_hapiness_analysis 
(climat_id, date_id, country_id, event_id, life_ladder, gdp_per_capita, positive_affect, social_support, life_expancy, freedom_choice, generocity, corruption, negative_affect)
SELECT 
  CL.climat_id,
  D.date_id,
  C.country_id,
  T.event_id,
  SH.life_ladder,
  SH.gdp_per_capita,
  SH.positive_affect,
  SH.social_support,
  SH.life_expancy,
  SH.freedom_choice,
  SH.generocity,
  SH.corruption,
  SH.negative_affect
FROM StageZone.Hapiness SH 
LEFT JOIN StageZone.Terrorism ST ON ST.country_name = SH.country_name 
LEFT JOIN StageZone.Climat SCL ON SCL.country_name = ST.country_name 
LEFT JOIN dim_country C ON C.country_name = SH.country_name 
LEFT JOIN dim_date D ON ST.year = SH.year 
	AND ST.year = YEAR(SCL.date) 
    AND ST.month = MONTH(SCL.date) 
    AND ST.day = DAY(SCL.date) 
LEFT JOIN dim_terrorism T ON T.extended = ST.extended 
	AND T.event_name = ST.event_name
LEFT JOIN dim_climat CL ON CL.average_temperature = SCL.average_temperature 
	AND CL.average_temperature_uncertainty = SCL.average_temperature_uncertainty 
WHERE CONCAT(SH.hapiness_id, CL.climat_id, D.date_id, C.country_id, T.event_id) 
NOT IN (SELECT CONCAT(hapiness_id, climat_id, date_id, country_id, event_id) 
        FROM fact_hapiness_analysis);






