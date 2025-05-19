import requests
import json

# read json file 
with open('sample_events.json', 'r') as f:
    sample_data = json.load(f)

# response url
response = requests.post("http://localhost:5001/sort-events", json=sample_data)

# events as dictionary
if response.status_code == 200:
    sorted_events = response.json()
    print("Sorted Events:")
    for event in sorted_events:
        print(f"{event['artist']} - {event['title']} - {event['date']}")
else:
    print("Request failed:")
    print(response.status_code)
    print(response.text)
