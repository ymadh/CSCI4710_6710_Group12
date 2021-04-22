-- CREATE USER devUser with SUPERUSER;
-- CREATE DATABASE group12 with owner devUser;
-- \c group12;

--create table script

DROP TABLE IF EXISTS public.scooter_rent;
DROP TABLE IF EXISTS public.scooter_user;

CREATE TABLE public.scooter_rent

(
    "scooter_id" bigint GENERATED ALWAYS AS IDENTITY,
    "scooter_brand" character varying(50) COLLATE pg_catalog."default",
    "available" boolean,
    "location" character varying(50) COLLATE pg_catalog."default",
    PRIMARY KEY(scooter_id)
)

CREATE TABLE public.scooter_user
(
    "user_id" bigint GENERATED ALWAYS AS IDENTITY,
    "user_name" character varying(50) COLLATE pg_catalog."default",
    "allowed_to_use" boolean,
    "currently_using" bigint,
    PRIMARY KEY(user_id)
    CONSTRAINT fk_scooter_rent
        FOREIGN KEY(currently_using)
            REFERENCES scooter_rent(scooter_id)
)

TABLESPACE pg_default;

ALTER TABLE hw5
    OWNER to postgres;
	
	
--Add in info (you would need to change the file path)
-- copy hw5 FROM '/home/james/hw5/CSCI4710_6710_Group12/hw5/data/project5csv.csv' DELIMITER ',' CSV HEADER;
copy hw5 FROM '/Users/adunphy/Sites/CSCI4710/CSCI4710-group12/hw5-part2/data/project5csv.csv' DELIMITER ',' CSV HEADER;


