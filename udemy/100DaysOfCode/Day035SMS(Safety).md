# Day 035
```python 
# API list: https://apilist.fun/ ❤️
```

# Side Quest: API Authentication for not free services, Current Weather and Forecast
```python
# Source: https://openweathermap.org/api
# Documentation: https://openweathermap.org/api/one-call-3?collection=one_call_api_3.0

https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
import requests
API_KEY = "PLACEHOLDER"

parameters = {
    "q": "London,UK", 
    "appid": API_KEY
}

if __name__ == "__main__":
    response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
    response.raise_for_status()

    data = response.json()
    print(data)
```

# Side Quest: Will it rain within 12 hours
```python
import requests

API_KEY = "PLACEHOLDER"
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "cnt": 4,
    "appid": API_KEY
}

if __name__ == "__main__":
    response = requests.get(url=OWM_ENDPOINT, params=parameters)
    print(f"DEBUG: {response.status_code}")
    response.raise_for_status()

    data = response.json()
    # print(data)
    # Online JSON Viewer: https://jsonviewer.stack.hu/

    will_rain = False

    for item in data["list"]:
        if int(item["weather"][0]["id"]) < 700:
            will_rain = True
    
    if will_rain:
        print("Bring an umbrella")
```

# Side Quest: Send SMS via Twilio API or WhatsApp
```python
# API: https://www.twilio.com/en-us
# Documentation: https://www.twilio.com/docs/messaging/quickstart

# Get a Trail Number: +1 (123) 456-7890         11234567890
# Programmable SMS Quickstart

# Send an SMS Using Twilio
from twilio.rest import Client              # pip3 install twilio

account_sid = "fromtwiliodashboard"
auth_token = "fromtwiliodashboard"          
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body="Hi there",
        from_="+11234567890",
        to="15558675310"                    # Note: have to be verified numbers on twilio
    )

print(message.sid)
print(message.status)
```

# Side Quest: Rain app sending SMS via Twilio API
```python
import requests
from twilio.rest import Client              # pip3 install twilio
account_sid = "fromtwiliodashboard"
auth_token = "fromtwiliodashboard" 

API_KEY = "PLACEHOLDER"
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "cnt": 4,
    "appid": API_KEY
}

if __name__ == "__main__":
    response = requests.get(url=OWM_ENDPOINT, params=parameters)
    print(f"DEBUG: {response.status_code}")
    response.raise_for_status()

    data = response.json()
    # print(data)
    # Online JSON Viewer: https://jsonviewer.stack.hu/

    will_rain = False

    for item in data["list"]:
        if int(item["weather"][0]["id"]) < 700:
            will_rain = True
    
    if will_rain:
        # print("Bring an umbrella")
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body="Bring an umbrella",
                from_="+11234567890",
                to="15558675310"                    # Note: have to be verified numbers on twilio
            )

        print(message.sid)
        print(message.status)
```

# Side Quest: Environment Variables
```python
env             : Mac using Pycharm in bash
dir Env:        : Windows using Pycharm in Powershell

in terminal (temp)
export OWM_API_KEY=PLACEHOLDER              # IMPORTANT: No "" and no spaces 👀

main.py
import os

api_key = os.environ.get("OWM_API_KEY")      # ⭐⭐⭐⭐⭐

# Note in PythonAnywhere must run code
export OWM_API_KEY=PLACEHOLDER; export AUTH_TOKEN=PLACEHOLDER; python3 app.py ❤️❤️❤️❤️❤️
# This is problem if on github or bitbucket.org
```