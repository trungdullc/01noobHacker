# Day 037
```python
# Advanced Authentication

# HTTP Requests ❤️
GET                     # requests.get()            Read
POST                    # requests.post()           Create
PUT                     # requests.put()            Update
DELETE Requests         # requests.delete()         Delete
```

# Side Quest: Habit Tracker using Post Request
```python
# pixela API: https://pixe.la/
import requests
import datetime as dt

# today = dt.datetime(year=2026, month=1, day=22)
today = dt.datetime.now()

# Japanese Color Translation
"""
green = shibafu
red = momiji
blue = sora
yelow  = ichou
purple = ajisai
black = kuro
"""

USERNAME = "hackerDu"
TOKEN = "thisissecret"

GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"         # change username
POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
UPDATE_ENDPOINT = f"{POST_ENDPOINT}/{today.strftime('%Y%m%d')}"

# Source: https://docs.pixe.la/entry/post-user
# Fill in required
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_parameters = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

update_parameters = {
    "quantity":"4.5"
}

# Don't want the date hardcoded
post_parameters = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"6.9"
}

# Note: This is safer than apikey
headers = {
    "X-USER-TOKEN":TOKEN
}

if __name__ == "__main__":
    # Create your User account (Method 1/2) via Python3
    # Note: post uses json while get uses params
    # response = requests.post(url=PIXELA_ENDPOINT, json=pixela_parameters)
    # print(response.text())

    # Create your User account via terminal (Method 2/2), Faster
    # curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"hackerDu", "agreeTermsOfService":"yes", "notMinor":"yes"}'

    # Create a graph definition via Python3 (Method 1/2)
    # Note: no username or token so auth via Request Header called X-USER-TOKEN ❤️
    # response = requests.post(url=GRAPH_ENDPOINT, json=graph_parameters, headers=headers)
    # print(response.text)

    # Create a graph definition via terminal (Method 2/2)
    #  curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'

    # Look at graph created (GET)
    # Browser:  https://pixe.la/v1/users/hackerDu/graphs/graph1.html ❤️

    # Post value to the graph via Python3 (Method 1/2)
    # response = requests.post(url=POST_ENDPOINT, json=post_parameters, headers=headers)    
    # print(response.text)

    # Post value to the graph via terminal (Method 2/2)
    # curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'

    # Look at graph created (GET)
    # Browser:  https://pixe.la/v1/users/hackerDu/graphs/graph1.html ❤️

    # Update value on graph via Python3
    # response = requests.put(url=UPDATE_ENDPOINT, json=update_parameters, headers=headers)
    # print(response.text)

    # Look at graph created (GET)
    # Browser:  https://pixe.la/v1/users/hackerDu/graphs/graph1.html ❤️

    # Delete value on graph via Python3
    response = requests.delete(url=UPDATE_ENDPOINT, headers=headers)

    # Look at graph created (GET)
    # Browser:  https://pixe.la/v1/users/hackerDu/graphs/graph1.html ❤️
```