function attachEvents() {
    GET_POST_URL ='http://localhost:3030/jsonstore/phonebook';
    DELETE_BASE_URL = ' http://localhost:3030/jsonstore/phonebook/';

    const loadButton = document.getElementById('btnLoad');
    const createButton = document.getElementById('btnCreate');

    const loadInfo = function() {
        const ulElement = document.getElementById('phonebook');
        ulElement.innerHTML = '';

        fetch(GET_POST_URL)
        .then((response) => response.json())
        .then((data) => {
            // console.log(data);
            for (const record of Object.entries(data)) {
                const person = record[1].person;
                const phone = record[1].phone;
                const uniqueId = record[1]._id;

                const liElement = document.createElement('li');
                liElement.textContent = `${person}: ${phone}`;

                const deleteButton = document.createElement('button');
                deleteButton.id = uniqueId;
                deleteButton.textContent = 'Delete';

                deleteButton.addEventListener('click', deleteInfo);

                liElement.appendChild(deleteButton);
                ulElement.appendChild(liElement);
            }
        })
        .catch((error) => console.log(error.message))
    };

    const deleteInfo = function(event) {
        const targetButton = event.target;
        const key = targetButton.id;

        fetch(`${DELETE_BASE_URL}${key}`, {
            method: 'DELETE',
        })
        .then((response) => {
            if (response.ok) {
                targetButton.parentElement.remove();
            }
        })
        .catch((error) => console.log(error.message))
    };

    const createInfo = function() {
        const personInfo = document.getElementById('person');
        const phoneInfo = document.getElementById('phone');

        const newRecord = {
            'person': personInfo.value,
            'phone': phoneInfo.value,
        }

        fetch(GET_POST_URL, {
            method: 'POST',
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify(newRecord),
        })
        .then((response) => {
            if (response.ok) {
                loadInfo();
            }
        })
        .catch((error) => console.log(error.message))

        personInfo.value = '';
        phoneInfo.value = '';
    };

    loadButton.addEventListener('click', loadInfo);
    createButton.addEventListener('click', createInfo);

}

attachEvents();