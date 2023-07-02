import requests
import json

# URL to send the POST request to
url = 'http://localhost:8000/manufactures'

# JSON data to send in the request
manufactures = (
    {'name': 'DarkSide'},
    {'name': 'Must Have'},
    {'name': 'Daily Hookah'},
    {'name': 'Bonch'},
    {'name': 'WTO'},
    {'name': 'Северный'}
)

for manufacture in manufactures:

    # Convert the data to JSON format
    json_data = json.dumps(manufacture)

    # Set the headers for the request
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the POST request
    response = requests.post(url, data=json_data, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print('Request successful!')
        print('Response:', response.json())
    else:
        print('Request failed. Status code:', response.status_code)
