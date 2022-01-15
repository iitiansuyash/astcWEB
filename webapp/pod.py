import requests
import json 
import datetime



def pod():
    API_KEY = "djeiZMw3HRcOep5vYg0rT1FmkYggtA3a8hixbuCA"
    API_URL = "https://api.nasa.gov/planetary/apod"
    parameter = {
        'hd':'true',
        'api_key':API_KEY
     }
    res = requests.get(API_URL,parameter)
    data= json_data = json.loads(res.text)
    return data

