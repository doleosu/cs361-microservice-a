Microservice A - Communication Contract

Required external packages: Flask



A. How to progammatically REQUEST Data:

To request sorted data from the microservice send a POST request to http://localhost:5001/sort-events with appropriate header and JSON body structure, shown in the example below.

Example of requesting data:

```js
// requesting data
fetch('http://localhost:5001/sort-events', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        events: [
            {
                date: '2025-05-20',
                artist: 'The Weeknd',
                description: 'Kissland',
                location: 'Chicago, IL'
            },
            {
                date: '2025-06-10',
                artist: 'BLACKPINK',
                description: '25 Tour',
                location: 'New York, NY'
            }
        ],
        order: 'asc'
    })
});
```
The microservice will then, sort the data and then send it back to your server, in order to receive the data, see the example below.

B. How to programmatically RECEIVE data

Use the following example to receivethe sorted data from the microservice:

```js
// receiving data
fetch('http://localhost:5001/sort-events')
    .then(response => response.json())  // parse JSON response
    .then(sortedEvents => {
        
        // update the display
        renderEvents(sortedEvents);
    });
```

C. UML Sequence Diagram

![UML Sequence Diagram](./UML%20Diagram.png)