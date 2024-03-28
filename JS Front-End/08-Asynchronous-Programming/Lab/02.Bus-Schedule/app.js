function solve() {
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/schedule/';
    const departButton = document.getElementById('depart');
    const arriveButton = document.getElementById('arrive');
    const infoDiv = document.querySelector('.info');

    let stopId = 'depot';
    let stopName;

    function depart() {    
        fetch(`${BASE_URL}${stopId}`)
        .then((response) => response.json())
        .then((data) => {
            stopName = data.name;
            stopId = data.next;
            infoDiv.textContent = `Next Stop ${stopName}`;
            departButton.disabled = true;
            arriveButton.disabled = false;
            
        })
        .catch((error) => {
            infoDiv.textContent = 'Error';
            arriveButton.disabled = true;
        }) 
    }

    async function arrive() {
        infoDiv.textContent = `Arriving at ${stopName}`;
        departButton.disabled = false;
        arriveButton.disabled = true;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();