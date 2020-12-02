# Dependencies
import os
import sqlalchemy
import psycopg2
from flask import Flask
from flask import render_template  
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, jsonify

# Save Connection String
databaseURI = "postgresql://postgres:Bootcamp@cwrubootcamp.c6sjh58vwb2z.us-east-2.rds.amazonaws.com/postgres"

# Create Engine
engine = create_engine(databaseURI)

#Reflect into Model
Base = automap_base()
#Relfect tables too
Base.prepare(engine, reflect=True)

## Flask Route ##

app = Flask(__name__)

@app.route("/")
def home():
        print("Heading Home...")
        return "This is the Home Page for the Olympic Medal with Weather API"
        #this will have index for database home page

@app.route("/about")
def about():
        print("Heading to 'About'...")
        return "This is the Placeholder for the About Page"
        #This will have the index for database about page

if __name__ == "__main__":
    app.run(debug=True)
