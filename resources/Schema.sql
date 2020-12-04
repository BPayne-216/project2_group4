-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "noc_regions" (
    "region" VARCHAR(100)   NOT NULL,
    "NOC" VARCHAR(10)   NOT NULL,
    CONSTRAINT "pk_noc_regions" PRIMARY KEY (
        "NOC"
     )
);

CREATE TABLE "country_medals" (
    "NOC" VARCHAR(10)   NOT NULL,
    "region" VARCHAR(100)   NOT NULL,
    "Bronze" INT   NOT NULL,
    "Silver" INT   NOT NULL,
    "Gold" INT   NOT NULL
);

CREATE TABLE "country_average_temperature" (
    "Country" VARCHAR(100)   NOT NULL,
    "Year" INT   NOT NULL,
    "NOC" VARCHAR(10)   NOT NULL,
    "AverageTemperature" INT   NOT NULL
);

CREATE TABLE "city_average_temperature" (
    "region" VARCHAR(100)   NOT NULL,
    "NOC" VARCHAR(10)   NOT NULL,
    "City" VARCHAR(100)   NOT NULL,
    "Year" INT   NOT NULL,
    "Latitude" INT   NOT NULL,
    "Longitude" INT   NOT NULL,
    "AverageTemperature" INT   NOT NULL
);

CREATE TABLE "athlete_medals" (
    "Sex" VARCHAR(2)   NOT NULL,
    "Team" VARCHAR(100)   NOT NULL,
    "NOC" VARCHAR(10)   NOT NULL,
    "Games" VARCHAR(100)   NOT NULL,
    "Year" INT   NOT NULL,
    "Season" VARCHAR(50)   NOT NULL,
    "City" VARCHAR(100)   NOT NULL,
    "Sport" VARCHAR(50)   NOT NULL,
    "Medal" VARCHAR(50)   NOT NULL
);

ALTER TABLE "country_medals" ADD CONSTRAINT "fk_country_medals_NOC" FOREIGN KEY("NOC")
REFERENCES "noc_regions" ("NOC");

ALTER TABLE "country_average_temperatue" ADD CONSTRAINT "fk_country_average_temperatue_NOC" FOREIGN KEY("NOC")
REFERENCES "noc_regions" ("NOC");

ALTER TABLE "city_average_temperature" ADD CONSTRAINT "fk_city_average_temperature_NOC" FOREIGN KEY("NOC")
REFERENCES "noc_regions" ("NOC");

ALTER TABLE "athlete_medals" ADD CONSTRAINT "fk_athlete_medals_NOC" FOREIGN KEY("NOC")
REFERENCES "noc_regions" ("NOC");

