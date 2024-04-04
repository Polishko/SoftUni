// Main variables
const baseURL = 'http://localhost:3030/jsonstore/tasks';

const locationInput = document.getElementById('location');
const temperatureInput = document.getElementById('temperature');
const dateInput = document.getElementById('date');

const loadHistoryButton = document.getElementById('load-history');

const addWeatherButton = document.getElementById('add-weather');
const editWeatherButton = document.getElementById('edit-weather');

const recordsList = document.getElementById('list');

// Helper functions
function  clearRecords() {
    recordsList.innerHTML = '';
}

function clearInputFields() {
    locationInput.value = '';
    dateInput.value = '';
    temperatureInput.value ='';
}

function enableAddWeather() {
    addWeatherButton.disabled = false;
    editWeatherButton.disabled = true;
}

function enableEditWeather() {
    addWeatherButton.disabled = true;
    editWeatherButton.disabled = false;
}

function displayRecords(data) {
    clearRecords();

    for (const key in data) {
        const recordContainer = document.createElement('div');
        recordContainer.className = 'container';
        recordContainer.id = data[key]._id;
        recordsList.appendChild(recordContainer);

        const location = document.createElement('h2');
        location.textContent = data[key].location;
        recordContainer.appendChild(location);

        const date = document.createElement('h3');
        date.textContent = data[key].date;
        recordContainer.appendChild(date);

        const temperature = document.createElement('h3');
        temperature.textContent = data[key].temperature;
        temperature.id = 'celsius';
        recordContainer.appendChild(temperature);

        const buttonsDiv = document.createElement('div');
        buttonsDiv.className = 'buttons-container';
        recordContainer.appendChild(buttonsDiv);

        const changeButton = document.createElement('button');
        changeButton.className = 'change-btn';
        changeButton.textContent = 'Change';
        buttonsDiv.appendChild(changeButton);

        const deleteButton = document.createElement('button');
        deleteButton.className = 'delete-btn';
        deleteButton.textContent = 'Delete';
        buttonsDiv.appendChild(deleteButton);

        changeButton.addEventListener('click', updateRecord);
        deleteButton.addEventListener('click', deleteRecord);
    }
}

// DOM manipulation
function loadRecords() {
    fetch(baseURL)
    .then((response) => response.json())
    .then((data) => displayRecords(data))
    .catch((error) => console.log(error))
}

function addWeatherRecord(e) {
    e.preventDefault();
    if (locationInput.value !== '' && temperatureInput.value !== '' && dateInput.value !== '') {
        const recordObj = {
            location: locationInput.value,
            date: dateInput.value,
            temperature: temperatureInput.value,
        };

        fetch(baseURL, {
            method: 'POST',
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify(recordObj),
        })
        .then((data) => loadRecords())
        .catch((error) => console.log(error))
    }
    clearInputFields();
}

function updateRecord(event) {
    const currentRecord = event.target.parentNode.parentNode;
    enableEditWeather();

    locationInput.value = currentRecord.querySelector('h2').textContent;
    dateInput.value = currentRecord.querySelector('h3:nth-child(2)').textContent;
    temperatureInput.value = currentRecord.querySelector('h3:nth-child(3)').textContent;

    editWeatherButton.addEventListener('click', () => {
        sendUpdate(currentRecord.id);
    })
}

function sendUpdate(id) {
    if (locationInput.value !== '' && temperatureInput.value !== '' && dateInput.value !== '') {
        const editedObj = {
            location: locationInput.value,
            temperature: temperatureInput.value,
            date: dateInput.value,
        }

        fetch(`${baseURL}/${id}`, {
            method: 'PUT',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify(editedObj),
        })
            .then((data) => loadRecords())
            .catch((error) => console.log(error))
        clearInputFields();
        enableAddWeather();
    }
}

function deleteRecord(e) {
    const id = e.target.parentElement.parentElement.id;

    fetch(`${baseURL}/${id}`, {
        method: 'DELETE',
    })
    .then((data) => loadRecords())
    .catch((error) => console.log(error))
}

loadHistoryButton.addEventListener('click', (event) => {
    event.preventDefault();
    loadRecords();
});

addWeatherButton.addEventListener('click', addWeatherRecord);
