# Dependencies
import os
import sqlalchemy
import psycopg2
from flask import Flask
from flask import render_template  
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from flask import jsonify
import json
import numpy as np

app = Flask(__name__)
con = psycopg2.connect("postgresql://postgres:Bootcamp@cwrubootcamp.c6sjh58vwb2z.us-east-2.rds.amazonaws.com/postgres")
cursor = con.cursor()


# Save Connection String
databaseURI = "postgresql://postgres:Bootcamp@cwrubootcamp.c6sjh58vwb2z.us-east-2.rds.amazonaws.com/postgres"

# Create Engine
engine = create_engine(databaseURI)
session = Session(engine)

#Reflect into Model
Base = automap_base()

#Relfect tables too
Base.prepare(engine, reflect=True)

# Flask Routes
@app.route("/")
def home():
        print("Heading Home...")
        return (
        f"Available Routes:<br/>"
        f"/api/v1.0/noc_regions<br/>"
        f"/api/v1.0/country_medals<br/>"
        f"/api/v1.0/athlete_medals<br/>"
        f"/api/v1.0/city_average_temperature<br/>"
        f"/api/v1.0/country_average_temperature<br/>"
    )

@app.route('/base')
def main():
    return render_template('')
    

@app.route("/about")
def about():
        print("Heading to 'About'...")
        return (
    )

@app.route("/api/v1.0/noc_regions")
def noc_regions():  
    cursor.execute('''SELECT * FROM noc_regions''')
    noc_regions_list = []
    results = cursor.fetchall()
    for result in results:
        row = {'region':'NOC'}
        row['region'] = result[0]
        row['NOC'] = result[1]
        noc_regions_list.append(row)
    return (
        jsonify(noc_regions_list)
    )

@app.route("/api/v1.0/country_medals")
def country_medals():  
    cursor.execute('''SELECT * FROM country_medals''')
    country_medals_list = []
    results = cursor.fetchall()
    for result in results:
        row = {'NOC':'region'}
        row['NOC'] = result[0]
        row['region'] = result[1]
        row['Bronze'] = result[2]
        row['Silver'] = result[3]
        row['Gold'] = result[4]
        country_medals_list.append(row)
    return(
        jsonify(country_medals_list)
    )

@app.route("/api/v1.0/athlete_medals")
def athlete_medals():  
    cursor.execute('''SELECT * FROM athlete_medals''')
    athlete_medals_list = []
    results = cursor.fetchall()
    for result in results:
        row = {'NOC':'Team'}
        row['Sex'] = result[0]
        row['Team'] = result[1]
        row['NOC'] = result[2]
        row['Games'] = result[3]
        row['Year'] = result[4]
        row['Season'] = result[5]
        row['City'] = result[6]
        row['Sport'] = result[7]
        row['Medal'] = result[8]
        athlete_medals_list.append(row)
    return(
        jsonify(athlete_medals_list)
    )

@app.route("/api/v1.0/city_average_temperature")
def city_average_temperature():  
    cursor.execute('''SELECT * FROM city_average_temperature''')
    city_average_temperature_list = []
    results = cursor.fetchall()
    for result in results:
        row = {'NOC':'region'}
        row['region'] = result[0]
        row['NOC'] = result[1]
        row['City'] = result[2]
        row['Year'] = result[3]
        row['Latitude'] = result[4]
        row['Longitude'] = result[5]
        row['AverageTemperature'] = result[6]
        city_average_temperature_list.append(row)
    return(
        jsonify(city_average_temperature_list)
    )

@app.route("/api/v1.0/country_average_temperature")
def country_average_temperature():  
    cursor.execute('''SELECT * FROM country_average_temperature''')
    country_average_temperature_list = []
    results = cursor.fetchall()
    for result in results:
        row = {'NOC':'Country'}
        row['Country'] = result[0]
        row['Year'] = result[1]
        row['NOC'] = result[2]
        row['AverageTemperature'] = result[3]
        country_average_temperature_list.append(row)
    return(
        jsonify(country_average_temperature_list)
    )

if  __name__ == "__main__":
    app.run(debug=True)