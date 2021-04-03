--create table script
CREATE TABLE public.hw5
(
    index bigint,
    "What country do you live in?" character varying(50) COLLATE pg_catalog."default",
    "How old are you?" bigint,
    "What is your gender?" character varying(50) COLLATE pg_catalog."default",
    "To what extent do you feel FEAR due to the coronavirus?" bigint,
    "To what extent do you feel ANXIOUS due to the coronavirus?" bigint,
    "To what extent do you feel ANGRY due to the coronavirus?" bigint,
    "To what extent do you feel HAPPY due to the coronavirus?" bigint,
    "To what extent do you feel SAD due to the coronavirus?" bigint,
    "Which emotion is having the biggest impact on you?" character varying(5000) COLLATE pg_catalog."default",
    "What makes you feel that way?" character varying(5000) COLLATE pg_catalog."default",
    "What brings you the most meaning during the coronavirus outbrea" character varying(5000) COLLATE pg_catalog."default",
    "What is your occupation?" character varying(5000) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.hw5
    OWNER to postgres;
	
	
--Add in info (you would need to change the file path)
copy hw5 FROM 'C:\Users\James\OneDrive\Desktop\Masters program\CSCI 6710\project5csv.csv' DELIMITER ',' CSV HEADER;