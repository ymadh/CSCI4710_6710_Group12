/* Step 1: Split data based on age and gender */

CREATE TABLE YoungMen
AS (SELECT *
    FROM hw5
    WHERE "What is your gender?" = "Male"
    AND "How old are you?" <= 35);

CREATE TABLE MiddleOldMen
AS (SELECT *
    FROM hw5
    WHERE "What is your gender?" = "Male"
    AND "How old are you?" >= 36);

CREATE TABLE YoungWomen
AS (SELECT *
    FROM hw5
    WHERE "What is your gender?" = "Female"
    AND "How old are you?" <= 35);

CREATE TABLE MiddleOldWomen
AS (SELECT *
    FROM hw5
    WHERE "What is your gender?" = "Female"
    AND "How old are you?" >= 36);

