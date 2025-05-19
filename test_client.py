import requests
import json

# load sample from sample_events.json
with open('sample_events.json', 'r') as f:
    sample_data = json.load(f)

# send a POST request to the microservice
response = requests.post("http://localhost:5001/sort-events", json=sample_data)

# print the response
if response.status_code == 200:
    sorted_events = response.json()
    print("Sorted Events:")
    for event in sorted_events:
        print(f"{event['name']} - {event['date']}")
else:
    print("Request failed:")
    print(response.status_code)
    print(response.text)
