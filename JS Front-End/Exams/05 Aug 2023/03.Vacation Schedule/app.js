// Main variables
const baseURL = 'http://localhost:3030/jsonstore/tasks';

const nameInput = document.getElementById('name');
const daysInput = document.getElementById('num-days');
const fromInput = document.getElementById('from-date');

const vacationList = document.getElementById('list');

const loadVacationsButton = document.getElementById('load-vacations');
const addVacationButton = document.getElementById('add-vacation');
const editVacationButton = document.getElementById('edit-vacation');

loadVacationsButton.addEventListener('click', loadVacations);
addVacationButton.addEventListener('click', addVacation);

// Helper functions
function displayVacations(data) {
    console.log(data);
    vacationList.innerHTML = '';
    for (const key in data) {
        const id = data[key]._id;
        const vacationContainer = document.createElement('div');
        vacationContainer.className = 'container';
        vacationContainer.id = id;
        vacationList.appendChild(vacationContainer);

        const name = document.createElement('h2');
        name.textContent = data[key].name;
        vacationContainer.appendChild(name);

        const from = document.createElement('h3');
        from.textContent = data[key].date;
        vacationContainer.appendChild(from);

        const days = document.createElement('h3');
        days.textContent = data[key].days;
        vacationContainer.appendChild(days);

        const changeButton = document.createElement('button');
        changeButton.textContent = 'Change';
        changeButton.className = 'change-btn';
        vacationContainer.appendChild(changeButton);

        const doneButton = document.createElement('button');
        doneButton.textContent = 'Done';
        doneButton.className = 'done-btn';
        vacationContainer.appendChild(doneButton);

        changeButton.addEventListener('click', updateVacation);
        doneButton.addEventListener('click', deleteVacation);
    }
}

function enableAddButton() {
    addVacationButton.disabled = false;
    editVacationButton.disabled = true;
}

function enableEditButton() {
    addVacationButton.disabled = true;
    editVacationButton.disabled = false;
}

function allInputsProvided() {
    return (nameInput.value !== '' && daysInput.value !== '' && fromInput.value !== '');
}

function clearAllInputs() {
    nameInput.value = '';
    daysInput.value = '';
    fromInput.value = '';
}

function updateVacation(ev) {
    const targetVacation = ev.target.parentElement;
    nameInput.value = targetVacation.querySelector('h2').textContent;
    fromInput.value = targetVacation.querySelector('h3:nth-child(2)').textContent;
    daysInput.value = targetVacation.querySelector('h3:nth-child(3)').textContent;
    enableEditButton();
    editVacationButton.addEventListener('click', () =>
        {sendUpdate(targetVacation.id)
    });
}

// Requests
function loadVacations() {
    fetch(baseURL)
    .then((response) => response.json())
    .then((data) => displayVacations(data))
    .catch((error) => console.log(error))
    enableAddButton();
}

function addVacation(ev) {
    ev.preventDefault();
    if (allInputsProvided()) {
        const newVacation = {
            name: nameInput.value,
            days: daysInput.value,
            date: fromInput.value,
        };

        fetch(baseURL, {
            method: 'POST',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify(newVacation)
        })
        .then((response) => {
            if (response.ok) {
                loadVacations();
            }
        })
        .catch((error) => console.log(error))

        clearAllInputs();
    }
}

function sendUpdate(id) {
    if (allInputsProvided()) {
        const updatedVacation = {
            name: nameInput.value,
            date: fromInput.value,
            days: daysInput.value,
        }

        fetch(`${baseURL}/${id}`, {
            method: 'PUT',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify(updatedVacation)
        })
        .then((response) => {
            if (response.ok) {
                loadVacations();
            }
        })
        .catch((error) => console.log(error))

        clearAllInputs();
        enableAddButton();
    }
}

function deleteVacation(ev) {
    ev.preventDefault();
    const id = ev.target.parentElement.id;

    fetch(`${baseURL}/${id}`, {
        method: 'DELETE'
    })
    .then((response) => {
        if (response.ok) {
            loadVacations();
        }
    })
    .catch((error) => console.log(error))

    enableAddButton();
}
