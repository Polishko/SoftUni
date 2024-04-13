window.addEventListener('load', solve);

function solve() {
    // Main variables
    let totalLikes = 0;

    const genreInput = document.getElementById('genre');
    const nameInput = document.getElementById('name');
    const authorInput = document.getElementById('author');
    const dateInput = document.getElementById('date');

    const hitsContainer = document.querySelector('.all-hits-container');
    const savedContainer = document.querySelector('.saved-container');

    const totalLikesElement = document.querySelector('#total-likes p');

    const addBtn = document.getElementById('add-btn');
    addBtn.addEventListener('click', (e) => {
        e.preventDefault();
        createHit();
        clearInputs();
    });

    function saveHit(e) {
        const currHit = e.target.parentElement;
        const copyHit = currHit.cloneNode(true);
        currHit.remove();

        copyHit.querySelector('button:nth-of-type(1)').remove();
        copyHit.querySelector('button:nth-of-type(1)').remove();
        const currDeleteBtn = copyHit.querySelector('button:nth-of-type(1)');
        currDeleteBtn.addEventListener('click', (e) => deleteHit(e));
        savedContainer.appendChild(copyHit);
    }

    function deleteHit(e) {
        const toDeleteHit = e.target.parentElement;
        toDeleteHit.remove();
    }

    function getInputs() {
        if (genreInput.value !== '' && nameInput. value !== '' && authorInput.value !== '' && dateInput.value !== '') {
            return {
                genre: genreInput.value,
                name: nameInput.value,
                author: authorInput.value,
                date: dateInput. value,
            };
        }
    }

    function clearInputs() {
        genreInput.value = '';
        nameInput.value = '';
        authorInput.value = '';
        dateInput.value = '';
    }

    function createHit() {
        const newHit = getInputs();

        if (newHit) {
            const hitDiv = document.createElement('div');
            hitDiv.className = 'hits-info';
            hitsContainer.appendChild(hitDiv);

            const hitImg = document.createElement('img');
            hitImg.src = './static/img/img.png';
            hitDiv.appendChild(hitImg);

            const hitGenre = document.createElement('h2');
            hitGenre.textContent = `Genre: ${newHit.genre}`;
            hitDiv.appendChild(hitGenre);

            const hitName = document.createElement('h2');
            hitName.textContent = `Name: ${newHit.name}`;
            hitDiv.appendChild(hitName);

            const hitAuthor = document.createElement('h2');
            hitAuthor.textContent = `Author: ${newHit.author}`;
            hitDiv.appendChild(hitAuthor);

            const hitDate = document.createElement('h3');
            hitDate.textContent = `Date: ${newHit.date}`;
            hitDiv.appendChild(hitDate);

            const saveBtn = document.createElement('button');
            saveBtn.className = 'save-btn';
            saveBtn.textContent = 'Save song';
            hitDiv.appendChild(saveBtn);

            const likeBtn = document.createElement('button');
            likeBtn.className = 'like-btn';
            likeBtn.textContent = 'Like song';
            hitDiv.appendChild(likeBtn);

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = 'Delete';
            hitDiv.appendChild(deleteBtn);

            likeBtn.addEventListener('click', (e) => {
                e.preventDefault();
                totalLikes += 1;
                totalLikesElement.textContent = `Total Likes: ${totalLikes}`;
                likeBtn.disabled = true;
            });

            saveBtn.addEventListener('click', (e) => {
                e.preventDefault();
                saveHit(e);
            });

            deleteBtn.addEventListener('click', (e) => deleteHit(e));
        }
    }
}