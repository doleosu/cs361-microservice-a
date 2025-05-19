import time
from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return 'Sort microservice is listening for a request'

# **NEW** post (send back to concert.html)
@app.route('/sort-events', methods=['POST'])
def sort_events():
    print("Request received")
    data = request.get_json()  # get the data from the POST request
    
    events = data.get('events', [])
    order = data.get('order', 'asc')

    # sleep to show the received and the sent data
    time.sleep(5)
    
    # sort the dates
    sorted_events = sorted(events, key=lambda x: x['date'], reverse=(order == 'desc'))
    
    print("New sorted data has been sent back to concerts.html")
    return jsonify(sorted_events)  # return the sorted events as JSON

if __name__ == '__main__':
    app.run(port=5001)  # make sure it runs on port 5001
