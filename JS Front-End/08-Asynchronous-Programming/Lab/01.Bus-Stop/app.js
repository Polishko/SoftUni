function getInfo() {
    const busStopInfo = document.querySelector('#stopId').value;
    const busList = document.querySelector('#buses');
    const stopNameDiv = document.querySelector('#stopName');
    busList.innerHTML = '';
    stopNameDiv.textContent = '';

    fetch(`http://localhost:3030/jsonstore/bus/businfo/${busStopInfo}`)
    .then((response) => {
        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }

        return response.json();
    })
    .then((data) => {
        // const stopName = data.stopID.name;
        const stopName = data.name;
        stopNameDiv.textContent = stopName;

        // const busesInfo = data.stopID.buses;
        const busesInfo = data.buses;
        Object.entries(busesInfo).forEach(([busID, time]) => {
               const liItem = document.createElement('li');
               liItem.textContent = `Bus ${busID} arrives in ${time} minutes`;
               busList.appendChild(liItem);
        });
    })
    .catch((error) => {
        stopNameDiv.textContent = 'Error';
    });
}
