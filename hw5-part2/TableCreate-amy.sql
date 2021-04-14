-- CREATE USER devUser with SUPERUSER;
-- CREATE DATABASE group12 with owner devUser;
-- \c group12;

--create table script

DROP TABLE hw5;
DROP TABLE hw5_group1;
DROP TABLE hw5_group1_USA;
DROP TABLE hw5_group1_non_USA;
DROP TABLE hw5_group2;
DROP TABLE hw5_group2_USA;
DROP TABLE hw5_group2_non_USA;
DROP TABLE hw5_group3;
DROP TABLE hw5_group3_USA;
DROP TABLE hw5_group3_non_USA;
DROP TABLE hw5_group4;
DROP TABLE hw5_group4_USA;
DROP TABLE hw5_group4_non_USA;

CREATE TABLE hw5

(
    "index" bigint PRIMARY KEY,
    "country" character varying(50) COLLATE pg_catalog."default",
    "age" bigint,
    "gender" character varying(50) COLLATE pg_catalog."default",
    "fear" bigint,
    "anxious" bigint,
    "anger" bigint,
    "happy" bigint,
    "sad" bigint,
    "emotion" character varying(5000) COLLATE pg_catalog."default",
    "desc" character varying(5000) COLLATE pg_catalog."default",
    "meaning" character varying(5000) COLLATE pg_catalog."default",
    "occupation" character varying(5000) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE hw5
    OWNER to postgres;
	
	
--Add in info (you would need to change the file path)
-- copy hw5 FROM '/home/james/hw5/CSCI4710_6710_Group12/hw5/data/project5csv.csv' DELIMITER ',' CSV HEADER;
copy hw5 FROM '/Users/adunphy/Sites/CSCI4710/CSCI4710-group12/hw5-part2/data/project5csv.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE hw5_group1 as SELECT * FROM hw5 where gender = 'Male' and age <= 35;
CREATE TABLE hw5_group1_USA as SELECT * FROM hw5_group1 where country like 'USA%';
CREATE TABLE hw5_group1_non_USA as SELECT * FROM hw5_group1 where country not like 'USA%';
CREATE TABLE hw5_group2 as SELECT * FROM hw5 where gender = 'Male' and age > 35;
CREATE TABLE hw5_group2_USA as SELECT * FROM hw5_group2 where country like 'USA%';
CREATE TABLE hw5_group2_non_USA as SELECT * FROM hw5_group2 where country not like 'USA%';
CREATE TABLE hw5_group3 as SELECT * FROM hw5 where gender = 'Female' and age <= 35;
CREATE TABLE hw5_group3_USA as SELECT * FROM hw5_group3 where country like 'USA%';
CREATE TABLE hw5_group3_non_USA as SELECT * FROM hw5_group3 where country not like 'USA%';
CREATE TABLE hw5_group4 as SELECT * FROM hw5 where gender = 'Female' and age > 35;
CREATE TABLE hw5_group4_USA as SELECT * FROM hw5_group4 where country like 'USA%';
CREATE TABLE hw5_group4_non_USA as SELECT * FROM hw5_group4 where country not like 'USA%';
