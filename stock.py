import yfinance as yf
import pandas as pd
import json

# extract apple stock data
import requests
import json

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
response = requests.get(url)

if response.status_code == 200:
    with open("apple.json", "wb") as json_file:
        json_file.write(response.content)
    
    with open("apple.json", "r") as json_file:
        apple_info = json.load(json_file)
    
    print(apple_info)
else:
    print("File download failed.")
