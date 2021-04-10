/* First, run the below command to create the database we will use */

CREATE DATABASE group12 WITH OWNER postgres;
\c group12;

/* The below commands are optional and can be used if you need to start over after already creating the tables.
Simply uncomment this section if you need to restart. */

-- DROP TABLE public.hw5;
-- DROP TABLE public.hw5_group1;
-- DROP TABLE public.hw5_group1_USA;
-- DROP TABLE public.hw5_group1_non_USA;
-- DROP TABLE public.hw5_group2;
-- DROP TABLE public.hw5_group2_USA;
-- DROP TABLE public.hw5_group2_non_USA;
-- DROP TABLE public.hw5_group3;
-- DROP TABLE public.hw5_group3_USA;
-- DROP TABLE public.hw5_group3_non_USA;
-- DROP TABLE public.hw5_group4;
-- DROP TABLE public.hw5_group4_USA;
-- DROP TABLE public.hw5_group4_non_USA;

/* Run the below code to create the required tables for this assignment. Note the source file in line 52 below,
this must match the CSV location you will use. */

CREATE TABLE public.hw5

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
	
	
/* Add in info (you would need to change the file path)
copy hw5 FROM '/home/james/hw5/CSCI4710_6710_Group12/hw5/data/project5csv.csv' DELIMITER ',' CSV HEADER; */
copy hw5 FROM '/Users/adunphy/Sites/CSCI4710/CSCI4710_6710_Group12/hw5/data/project5csv.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE public.hw5_group1 as SELECT * FROM public.hw5 where gender = 'Male' and age <= 35;
CREATE TABLE public.hw5_group1_USA as SELECT * FROM public.hw5_group1 where country like 'USA%';
CREATE TABLE public.hw5_group1_non_USA as SELECT * FROM public.hw5_group1 where country not like 'USA%';
CREATE TABLE public.hw5_group2 as SELECT * FROM public.hw5 where gender = 'Male' and age > 35;
CREATE TABLE public.hw5_group2_USA as SELECT * FROM public.hw5_group2 where country like 'USA%';
CREATE TABLE public.hw5_group2_non_USA as SELECT * FROM public.hw5_group2 where country not like 'USA%';
CREATE TABLE public.hw5_group3 as SELECT * FROM public.hw5 where gender = 'Female' and age <= 35;
CREATE TABLE public.hw5_group3_USA as SELECT * FROM public.hw5_group3 where country like 'USA%';
CREATE TABLE public.hw5_group3_non_USA as SELECT * FROM public.hw5_group3 where country not like 'USA%';
CREATE TABLE public.hw5_group4 as SELECT * FROM public.hw5 where gender = 'Female' and age > 35;
CREATE TABLE public.hw5_group4_USA as SELECT * FROM public.hw5_group4 where country like 'USA%';
CREATE TABLE public.hw5_group4_non_USA as SELECT * FROM public.hw5_group4 where country not like 'USA%';
