window.addEventListener("load", solve);
function solve() {
    // Main variables
    const firstNameInput = document.getElementById('first-name');
    const lastNameInput = document.getElementById('last-name');
    const ageInput = document.getElementById('age');
    const titleInput = document.getElementById('story-title');
    const genreInput = document.getElementById('genre');
    const contentInput = document.getElementById('story');

    const previewList = document.getElementById('preview-list');
    const mainDiv = document.getElementById('main');

    const publishBtn = document.getElementById('form-btn');
    publishBtn.addEventListener('click', loadStory);

    // Check inputs
    function getInputs() {

        if (firstNameInput.value !== '' && lastNameInput.value !== ''
            && ageInput.value !== '' && titleInput.value !== ''
            && contentInput.value !== '') {
            return {
                firstName: firstNameInput.value,
                lastName: lastNameInput.value,
                age: ageInput.value,
                title: titleInput.value,
                genre: genreInput.value,
                content: contentInput.value,
            };
        }
    }

    // Create List Element
    function createListElement(story) {
        const liEle = document.createElement('li');
        liEle.className = 'story-info';
        previewList.appendChild(liEle);

        const article = document.createElement('article');
        liEle.appendChild(article);

        const nameEle = document.createElement('h4');
        nameEle.textContent = `Name: ${story.firstName} ${story.lastName}`;
        article.appendChild(nameEle);

        const ageEle = document.createElement('p');
        ageEle.textContent = `Age: ${story.age}`;
        article.appendChild(ageEle);

        const titleEle = document.createElement('p');
        titleEle.textContent = `Title: ${story.title}`;
        article.appendChild(titleEle);

        const genreEle = document.createElement('p');
        genreEle.textContent = `Genre: ${story.genre}`;
        article.appendChild(genreEle);

        const contentEle = document.createElement('p');
        contentEle.textContent = story.content;
        article.appendChild(contentEle);

        const saveBtn = document.createElement('button');
        saveBtn.className = 'save-btn';
        saveBtn.textContent = 'Save Story';
        liEle.appendChild(saveBtn);

        const editBtn = document.createElement('button');
        editBtn.className = 'edit-btn';
        editBtn.textContent = 'Edit Story';
        liEle.appendChild(editBtn);

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = 'Delete Story';
        liEle.appendChild(deleteBtn);

        editBtn.addEventListener('click', (e) => modifyInputs(e, story));
        saveBtn.addEventListener('click', saveStory);
        deleteBtn.addEventListener('click', (e) => deleteStory(e))
    }

    // Clear inputs
    function clearInputs() {
        firstNameInput.value = '';
        lastNameInput.value = '';
        ageInput.value = '';
        titleInput.value = '';
        genreInput.value = '';
        contentInput.value = '';
    }

    // Disable/Enable Publish Btn
    function togglePublishBtn() { // doesn't pass Judge test with setAttribute and removeAttribute disabled
        publishBtn.disabled === true
            ? publishBtn.disabled = false
            : publishBtn.disabled = true;
    }

    // Load story
    function loadStory() {
        const story = getInputs();

        if (getInputs()) {
            createListElement(story);
            clearInputs();
            togglePublishBtn();
        }
    }

    // Modify inputs
    function modifyInputs(e, story) {
        const currentStory = e.currentTarget.parentElement;

        firstNameInput.value = story.firstName;
        lastNameInput.value = story.lastName;
        ageInput.value = story.age;
        titleInput.value = story.title;
        genreInput.value = story.genre;
        contentInput.value = story.content;

        currentStory.remove();
        togglePublishBtn();
    }

    // Save story
    function saveStory() {
        mainDiv.innerHTML = '';
        const h1Tag = document.createElement('h1');
        h1Tag.textContent = 'Your scary story is saved!';
        mainDiv.appendChild(h1Tag);
    }

    // Delete story
    function deleteStory(e) {
        const targetLi = e.currentTarget.parentElement;
        targetLi.remove();
        togglePublishBtn();
    }
}