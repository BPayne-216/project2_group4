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



# Save Connection String
databaseURI = "postgresql://postgres:Bootcamp@cwrubootcamp.c6sjh58vwb2z.us-east-2.rds.amazonaws.com/postgres"


app = Flask(__name__)
app.config['databaseURI'] = 'postgresql://postgres:Bootcamp@cwrubootcamp.c6sjh58vwb2z.us-east-2.rds.amazonaws.com/postgres'


# Create Engine
engine = create_engine(databaseURI)
session = Session(engine)

#Reflect into Model
Base = automap_base()

#Relfect tables too
Base.prepare(engine, reflect=True)


## Flask Route ##

@app.route("/")
def home():
        print("Heading Home...")
        return "This is the Home Page for the Olympic Medal with Weather API"
        #this will have index for database home page

@app.route('/base')
def main():
    return render_template('try2.html')
    

@app.route("/about")
def about():
        print("Heading to 'About'...")
        return (
        f"Available Routes:<br/>"
        f"/api/v1.0/noc_regions<br/>"
        f"/api/v1.0/country_medals<br/>"
        f"/api/v1.0/athlete_medals<br/>"
        f"/api/v1.0/city_average_temperature<br/>"
        f"/api/v1.0/country_average_temperature<br/>"
    )

#@app.route("/api/v1.0/noc_regions")

if  __name__ == "__main__":
    app.run(debug=True)
