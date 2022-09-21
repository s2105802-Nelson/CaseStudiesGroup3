
# Import Libraries
import pandas as pd
import os
from pathlib import Path

from flask import Flask, render_template, request, session, redirect

from utilities import errorlog_utility as errorlog
from utilities import data_basic_utility as databasic

# Flask
app = Flask(__name__)
app.secret_key = os.urandom(16) 

# logger is used to write log messages or error details to a file in the debug folder. In production, this would be turned off
# by setting this debug variable to False
debug = True
logger = errorlog.ErrorLog(debug, "milestone2") # can pass in a different relative folder path


#############
# START PAGE ROUTES
#############

# Route: Homepage
@app.route("/")
def home():    
    logger.write_log_line("Home page: start")
    return render_template("home.html")

# Route: Location
@app.route("/location", methods=["GET", "POST"])
def location():    
    logger.write_log_line("Location: start")
    
    locationId = request.form['ddlSearchLocation']

    locationObj = LocationData()
    if locationId == "bourke":
        locationObj.locationMapImg = "location1.jpg"
        locationObj.locationName = "Bourke Street Mall (North)"
        locationObj.locationAddress = "280 Bourke Str, Melbourne, VIC, 3000"
        locationObj.busynessImg = "busyness-5.png"
    elif locationId == "southbank":
        locationObj.locationMapImg = "location2.jpg"
        locationObj.locationName = "Southbank"
        locationObj.locationAddress = "7 Riverside Quay, Southbank, VIC, 3006"
        locationObj.busynessImg = "busyness-5.png"
    else:
        locationObj.locationMapImg = "location1.jpg"
        locationObj.locationName = "Bourke Street Mall (North)"
        locationObj.locationAddress = "280 Bourke Str, Melbourne, VIC, 3000"
        locationObj.busynessImg = "busyness-5.png"

    return render_template("location.html", location=locationObj)


#############
# END PAGE ROUTES
#############


class LocationData:    
    locationMapImg = ""
    locationName = ""
    locationAddress = ""
    busynessImg = ""