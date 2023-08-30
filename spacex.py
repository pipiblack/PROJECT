import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import json
import datetime
import traceback
pd.set_option("display.max_columns",None)
pd.set_option("display.max_colwidth",None)

def getBoosterVersion(data):
    for x in data:
        response = requests.get("https://api.spacexdata.com/v4/rockets/"+str(x))
        rocket_data = response.json()
        booster_version = rocket_data["boosters"]
        print(booster_version)
        BoosterVersion.append(response["name"])

def getLaunchSite(data):
    for x in data["launchpad"]:
        if x:
            response = requests.get("https://api.spacexdata.com/v4/launchpads/"+ str(x).json())
            Longitude.append(response["longitude"])
            Latitude.append(response["latitude"])
            Launchsite.append(response["name"])

def getPayLoadData(data):
    for load in data["payloads"]:
        if load:
            response = requests.get("https://api.spacexdata.com/v4/payloads/"+ load).json()
            PayLoadMass.append(response["mass_kg"])
            Orbit.append(response["orbit"])

def getCoreData(data):
    for core in data["cores"]:
        if core["core"] != None:
            response = requests.get("https://api.spacexdata.com/v4/cores/"+core["core"]).json()
            Block.append(response["block"])
            ReusedCount.append(response["reuse_count"])
            Serial.append(response["serial"])
        else:
            Block.append(None)
            ReusedCount.append(None)
            Serial.append(None)
        Outcome.append(str(core["landing_success"])+""+str(core["Landing_type"]))
        Flight.append(core["flight"])
        GridFins.append(core["gridfins"])
        ReusedCount.append(core["reused"])
        Legs.append(core["legs"])
        Landingpad.append(core["landinpad"])

url="https://api.spacexdata.com/v4/launches/past"
response = requests.get(url)

static_json_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'
response = requests.get(static_json_url)
print(response.status_code)

data = pd.json_normalize(response.json())

data = data[['rocket', 'payloads', 'launchpad', 'cores', 'flight_number', 'date_utc']]

data = data[data["cores"].map(len)==1]
data = data[data["payloads"].map(len)==1]

print(data.head())



data["cores"] = data["cores"].map(lambda x:x[0])
data["payloads"] = data["payloads"].map(lambda x:x[0])

data["date"] = pd.to_datetime(data["date_utc"]).dt.date



BoosterVersion = []
PayLoadMass = []
Orbit = []
Block = []
ReusedCount = []
Serial = []
Outcome = []
Flight = []
GridFins = []
Legs = []
Landingpad = []
Longitude = []
Latitude = []
Launchsite = []
Reused = []

getBoosterVersion(data)
getLaunchSite(data)
getPayLoadData(data)
getLaunchSite(data)

launch_dict = {'FlightNumber': list(data['flight_number']),
'Date': list(data['date']),
'BoosterVersion':BoosterVersion,
'PayloadMass':PayLoadMass,
'Orbit':Orbit,
'LaunchSite':Launchsite,
'Outcome':Outcome,
'Flights':Flight,
'GridFins':GridFins,
'Reused':Reused,
'Legs':Legs,
'LandingPad':Landingpad,
'Block':Block,
'ReusedCount':ReusedCount,
'Serial':Serial,
'Longitude': Longitude,
'Latitude': Latitude}


flight_numbers = list(data['flight_number'])
dates = list(data['date'])
booster_versions = BoosterVersion[:95]
PayLoadMass = PayLoadMass[:95]
Orbit = Orbit[:95]
Launchsite = Launchsite[:95]
Outcome = Outcome[:95]
Flight = Flight[:95]
GridFins = GridFins[:95]
Reused = Reused[:95]
Legs = Legs[:95]
Landingpad = Landingpad[:95]
Block = Block[:95]
ReusedCount = ReusedCount[:95]
Serial = Serial[:95]
Longitude = Longitude[:95]
Latitude = Latitude[:95]

if len(flight_numbers) == len(dates) == len(booster_versions) == len(Launchsite) == len(PayLoadMass) == len(Outcome) == len(Flight) == len(GridFins) == len(Reused) == len(Legs) == len(Landingpad) == len(Block) == len(ReusedCount) == len(Serial) == len(Longitude) == len(Latitude):
    flight_numbers_filtered = [0 if val is None else val for val in flight_numbers]
    dates_filtered = [0 if val is None else val for val in dates]
    booster_versions_filtered = [0 if val is None else val for val in booster_versions]
    PayLoadMass_filtered = [0 if val is None else val for val in PayLoadMass]
    Orbit_filtered = [0 if val is None else val for val in Orbit]
    Launchsite_filtered = [0 if val is None else val for val in Launchsite]
    Outcome_filtered = [0 if val is None else val for val in Outcome]
    Flight_filtered = [0 if val is None else val for val in Flight]
    GridFins_filtered = [0 if val is None else val for val in GridFins]
    Reused_filtered = [0 if val is None else val for val in Reused]
    Legs_filtered = [0 if val is None else val for val in Legs]
    Landingpad_filtered = [0 if val is None else val for val in Landingpad]
    Block_filtered = [0 if val is None else val for val in Block]
    ReusedCount_filtered = [0 if val is None else val for val in ReusedCount]
    Serial_filtered = [0 if val is None else val for val in Serial]
    Longitude_filtered = [0 if val is None else val for val in Longitude]
    Latitude_filtered = [0 if val is None else val for val in Latitude]

    launch_dict = {
        'FlightNumber': flight_numbers_filtered,
        'Date': dates_filtered,
        'BoosterVersion': booster_versions_filtered,
        'PayloadMass': PayLoadMass_filtered,
        'Orbit': Orbit_filtered,
        'LaunchSite': Launchsite_filtered,
        'Outcome': Outcome_filtered,
        'Flights': Flight_filtered,
        'GridFins': GridFins_filtered,
        'Reused': Reused_filtered,
        'Legs': Legs_filtered,
        'LandingPad': Landingpad_filtered,
        'Block': Block_filtered,
        'ReusedCount': ReusedCount_filtered,
        'Serial': Serial_filtered,
        'Longitude': Longitude_filtered,
        'Latitude': Latitude_filtered
        }

    df = pd.DataFrame(launch_dict)

    print(df)
else:
    print(traceback.format_exc())
    print("Arrays have different lengths. Please ensure all arrays have the same length.")
    








