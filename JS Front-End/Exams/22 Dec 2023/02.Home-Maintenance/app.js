window.addEventListener("load", solve);

function solve() {
    const addButton = document.getElementById('add-btn');
    const placeInput = document.getElementById('place');
    const actionInput = document.getElementById('action');
    const personInput = document.getElementById('person');
    const tasksList = document.getElementById('task-list');
    const doneList = document.getElementById('done-list');

    function clearInputFields() {
        placeInput.value = '';
        actionInput.value = '';
        personInput.value = '';
    }

    function handleEdit(event) {
        const targetArticle = event.target.parentElement.previousElementSibling;
        placeInput.value = targetArticle.querySelector('p:nth-child(1)').textContent.replace('Place:', '');
        actionInput.value = targetArticle.querySelector('p:nth-child(2)').textContent.replace('Action:', '');
        personInput.value = targetArticle.querySelector('p:nth-child(3)').textContent.replace('Person:', '');
        targetArticle.parentElement.remove();
    }

    function handleDone(event) {
        const liEleToMove = event.target.parentElement.parentElement;
        const newLiEle = liEleToMove.cloneNode(true);
        newLiEle.classList.remove('clean-task');
        newLiEle.querySelector('.buttons').remove();
        const deleteButton = document.createElement('button');
        deleteButton.className = 'delete';
        deleteButton.textContent = 'Delete';
        newLiEle.appendChild(deleteButton);
        
        doneList.appendChild(newLiEle);
        liEleToMove.remove();

        deleteButton.addEventListener('click', handleDelete);
    }

    function handleDelete(event) {
        event.target.parentElement.remove();
    }

    addButton.addEventListener('click', function() {
        if (placeInput.value !== '' && actionInput.value !== '' && personInput.value !== '') {
            const liEle = document.createElement('li');
            liEle.className = 'clean-task';
            tasksList.appendChild(liEle);
            const articleEle = document.createElement('article');
            liEle.appendChild(articleEle);

            const placePEle = document.createElement('p');
            placePEle.textContent = `Place:${placeInput.value}`;
            articleEle.appendChild(placePEle);

            const actionPEle = document.createElement('p');
            actionPEle.textContent = `Action:${actionInput.value}`;
            articleEle.appendChild(actionPEle);

            const personPEle = document.createElement('p');
            personPEle.textContent = `Person:${personInput.value}`;
            articleEle.appendChild(personPEle);

            const divButtons = document.createElement('div');
            divButtons.className = 'buttons';
            liEle.appendChild(divButtons);

            const editButton = document.createElement('button');
            editButton.className = 'edit';
            editButton.textContent = 'Edit';
            divButtons.appendChild(editButton);

            const doneButton = document.createElement('button');
            doneButton.className = 'done';
            doneButton.textContent = 'Done';
            divButtons.appendChild(doneButton);

            editButton.addEventListener('click', handleEdit);
            doneButton.addEventListener('click', handleDone);

            clearInputFields();
        }
    })
}