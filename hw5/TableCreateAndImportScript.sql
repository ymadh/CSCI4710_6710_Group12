CREATE USER devUser with SUPERUSER;
CREATE DATABASE group12 with owner devUser;
\c group12;

--create table script

CREATE TABLE hw5
(
    index bigint,
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
copy hw5 FROM '/Users/adunphy/Sites/CSCI4710/CSCI4710-group12/hw5/data/project5csv.csv' DELIMITER ',' CSV HEADER;
