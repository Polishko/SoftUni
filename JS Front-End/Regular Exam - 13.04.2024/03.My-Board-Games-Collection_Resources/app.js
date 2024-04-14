function attachEvents() {
    // Main variables
    const baseURL = 'http://localhost:3030/jsonstore/games';

    const nameInput = document.getElementById('g-name');
    const typeInput = document.getElementById('type');
    const playersInput = document.getElementById('players');

    const gamesList = document.getElementById('games-list');
    const formContainer = document.getElementById('form');

    const loadBtn = document.getElementById('load-games');
    const editBtn = document.getElementById('edit-game');
    const addBtn = document.getElementById('add-game');

    loadBtn.addEventListener('click', loadGames);
    addBtn.addEventListener('click', addGame);
    editBtn.addEventListener('click', sendChange);

    // Helper functions
    function enableEditBtn() {
        editBtn.disabled = false;
        addBtn.disabled = true;
    }

    function enableAddBtn() {
        editBtn.disabled = true;
        addBtn.disabled = false;
    }

    function getInputs() {
        if (nameInput.value !== '' && playersInput.value !== '' && typeInput.value !== '') {
            return {
                name: nameInput.value,
                players: playersInput.value,
                type: typeInput.value,
            };
        }
    }

    function clearInputs() {
        nameInput.value = '';
        playersInput.value = '';
        typeInput.value = '';
    }

    function createGame(game) {
        const boardDiv = document.createElement('div');
        boardDiv.className = 'board-game';
        boardDiv.setAttribute('data-id', game._id);

        const contentDiv = document.createElement('div');
        contentDiv.className = 'content';
        boardDiv.appendChild(contentDiv);

        const namePara = document.createElement('p');
        namePara.textContent = game.name;
        contentDiv.appendChild(namePara);

        const playersPara = document.createElement('p');
        playersPara.textContent = game.players;
        contentDiv.appendChild(playersPara);

        const typePara = document.createElement('p');
        typePara.textContent = game.type;
        contentDiv.appendChild(typePara);

        const buttonsDiv = document.createElement('div');
        buttonsDiv.className = 'buttons-container';
        boardDiv.appendChild(buttonsDiv);

        const changeBtn = document.createElement('button');
        changeBtn.className = 'change-btn';
        changeBtn.textContent = 'Change';
        buttonsDiv.appendChild(changeBtn);

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = 'Delete';
        buttonsDiv.appendChild(deleteBtn);

        changeBtn.addEventListener('click', (e) => modifyGame(game));
        deleteBtn.addEventListener('click', (e) => deleteGame(e));

        return boardDiv;
    }

    // Requests
    function loadGames() {
        gamesList.innerHTML = '';
        const gameFragment = document.createDocumentFragment();

        fetch(baseURL)
            .then(response => response.json())
            .then(data => {
                Object.values(data).forEach(game => gameFragment.appendChild(createGame(game)));
                gamesList.appendChild(gameFragment);
                enableAddBtn();
            })
    }

    function addGame() {
        const newGame = getInputs();

        if (newGame) {
            fetch(baseURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newGame)
            })
                .then(response => {
                    if (!response.ok) {
                        return;
                    }
                    clearInputs();
                    return loadGames();
                })
        }
    }

    function modifyGame(game) {
        nameInput.value = game.name;
        playersInput.value = game.players;
        typeInput.value = game.type;
        formContainer.setAttribute('data-id', game._id);

        enableEditBtn();
    }

    function sendChange() {
        const newGame = getInputs();
        const gameId = formContainer.getAttribute('data-id');
        formContainer.removeAttribute('data-id');

        if (newGame) {
            fetch(`${baseURL}/${gameId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ gameId, ...newGame })
            })
                .then(response => {
                    if (!response.ok) {
                        return;
                    }
                    clearInputs();
                    enableAddBtn();
                    return loadGames();
                })
        }
    }
    function deleteGame(e) {
        const currGame = e.target.parentElement.parentElement;
        const gameId = currGame.getAttribute('data-id');

        fetch(`${baseURL}/${gameId}`, {
            method: 'DELETE'
        })
            .then(response => {
                if (!response.ok) {
                    return;
                }
                return loadGames();
            })
    }
}

attachEvents();