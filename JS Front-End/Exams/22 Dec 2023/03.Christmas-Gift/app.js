BASE_URL = 'http://localhost:3030/jsonstore/gifts/'
const giftList = document.getElementById('gift-list');

const giftInput = document.getElementById('gift');
const personInput = document.getElementById('for');
const priceInput = document.getElementById('price');

const loadPresentsButton = document.getElementById('load-presents');
const addPresentButton = document.getElementById('add-present');
const editPresentButton = document.getElementById('edit-present');

let giftId = null;

//Main button event listeners
function attachEvents() {
    loadPresentsButton.addEventListener('click', loadPresents);
    addPresentButton.addEventListener('click', addPresent);
    editPresentButton.addEventListener('click', editPresentEventHandler);
}

// Gift button event listeners
function attachGiftButtonEvents() {
    const changeButtons = document.querySelectorAll('.change-btn');
    const deleteButtons = document.querySelectorAll('.delete-btn');

    changeButtons.forEach((changeButton) => {
        changeButton.addEventListener('click', function (event) {
            const contentDiv = event.target.parentElement.previousElementSibling;
            const gift = contentDiv.querySelector('p:nth-child(1)').textContent;
            const person = contentDiv.querySelector('p:nth-child(2)').textContent;
            const price = contentDiv.querySelector('p:nth-child(3)').textContent;
            editPresent(gift, person, price);
            enableEditButton();
        })
    })

    deleteButtons.forEach((deleteButton) => {
        deleteButton.addEventListener('click', function (event) {
            const contentDiv = event.target.parentElement.previousElementSibling;
            const gift = contentDiv.querySelector('p:nth-child(1)').textContent;
            deletePresent(gift);
        })
    })
}

// Helper functions
function clearPresents() {
    giftList.innerHTML = '';
}

function  clearInputs() {
    giftInput.value = '';
    personInput.value = '';
    priceInput.value = '';
}
function enableAddButton() {
    editPresentButton.disabled = true;
    addPresentButton.disabled = false;
}

function enableEditButton() {
    editPresentButton.disabled = false;
    addPresentButton.disabled = true;
}

function getIdByPresent(gift) { // Unique gift names assumed
    return fetch(BASE_URL)
        .then(res => res.json())
        .then(res => Object.entries(res).find(e => e[1].gift === gift)[1]._id);
}

// DOM Manipulation functions
async function loadPresents() {
    clearPresents();
    try {
        const response = await fetch(BASE_URL);
        const data = await response.json();
        // console.log(data);
        for (const key in data) {
            const giftSock = document.createElement('div');
            giftSock.className = 'gift-sock';
            giftList.appendChild(giftSock);

            const contentDiv = document.createElement('div');
            contentDiv.className = 'content';
            giftSock.appendChild(contentDiv);

            const giftParaEle = document.createElement('p');
            giftParaEle.textContent = data[key].gift;
            contentDiv.appendChild(giftParaEle);

            const personParaEle = document.createElement('p');
            personParaEle.textContent = data[key].for;
            contentDiv.appendChild(personParaEle);

            const pricePraEle = document.createElement('p');
            pricePraEle.textContent = data[key].price;
            contentDiv.appendChild(pricePraEle);

            const buttonsContainer = document.createElement('div');
            buttonsContainer.className = 'buttons-container';
            giftSock.appendChild(buttonsContainer);

            const changeButton = document.createElement('button');
            changeButton.className = 'change-btn';
            changeButton.textContent = 'Change';
            buttonsContainer.appendChild(changeButton);

            const deleteButton = document.createElement('button');
            deleteButton.className = 'delete-btn';
            deleteButton.textContent = 'Delete';
            buttonsContainer.appendChild(deleteButton);

            attachGiftButtonEvents();
        }
    } catch (error) {
        console.log(error);
    }
}

function addPresent() {
    if (giftInput.value !== '' && personInput.value !== '' && priceInput.value !== '') {
        const giftObj = {
            gift: giftInput.value,
            for: personInput.value,
            price: priceInput.value,
        }

        fetch(BASE_URL, {
            method: 'POST',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify(giftObj),
        })
            .then(loadPresents)
            .catch((error) => console.log(error.message))

        clearInputs();
    }
}

async function editPresent(gift, person, price){
    giftId = await getIdByPresent(gift);
    giftInput.value = gift;
    personInput.value = person;
    priceInput.value = price;
}

function editPresentEventHandler() {
    const updatedGift = {
        gift: giftInput.value,
        for: personInput.value,
        price: priceInput.value,
        _id: giftId,
    }
    fetch(`${BASE_URL}${giftId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedGift),
    })
        .then(() => {
            clearInputs();
            loadPresents();
            giftId = null;
            enableAddButton();
        })
        .catch(console.error);
}

async function deletePresent(gift) {
    giftId = await getIdByPresent(gift)
    fetch(`${BASE_URL}${giftId}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
    })
        .then(() => {
        clearPresents();
        loadPresents();
        giftId = null;
        enableAddButton();
        }).catch(console.error);
}

attachEvents();
