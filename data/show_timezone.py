import requests
import json
import pytz
from datetime import datetime

def desktop_timezone():
     
# getting desktop IP address with ipify api
     
    my_ip = "https://api.ipify.org"
    response_ip = requests.get(my_ip)
    print("User's IP is {}".format(response_ip.text))
     
# getting json object including timezone for current desktop with ip-api
     
    url = "http://ip-api.com/json/{}".format(response_ip.text)
    response = requests.get(url)
    print("\nReceived JSON object : {} ".format(response.text))
    response_text = response.text
    response_json = json.JSONDecoder().decode(response_text)
#     print(type(response_json))
    current_timezone = response_json['timezone']
    print("\nUser's timezone is: {}".format(current_timezone))

# Provide a local time according to timezone
     
    desktop_loc_time = pytz.timezone(current_timezone)
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    
    loc_dt = desktop_loc_time.localize(datetime.now())
    print ("\nLocal time for desktop location is: {}".format(loc_dt.strftime(fmt)))

    
        
desktop_timezone()