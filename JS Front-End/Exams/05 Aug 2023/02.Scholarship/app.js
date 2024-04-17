window.addEventListener("load", solve);

function solve() {
    const studentInput = document.getElementById('student');
    const universityInput = document.getElementById('university');
    const scoreInput = document.getElementById('score');

    const nextButton = document.getElementById('next-btn');
    nextButton.addEventListener('click', addInputs);

    const previewList = document.getElementById('preview-list');
    const candidatesList = document.getElementById('candidates-list');

  function toggleNextButton() {
    nextButton.disabled === true ? nextButton.disabled = false : nextButton.disabled = true;
  }

  function allInputsAdded () {
    return (studentInput.value !== '' && universityInput.value !== '' && scoreInput.value !== '')
  }

  function clearAllInputs() {
    studentInput.value = '';
    universityInput.value = '';
    scoreInput.value = '';
  }

  function createListItem() {
    const liElement = document.createElement('li');
    liElement.className = 'application';
    previewList.appendChild(liElement);

    const article = document.createElement('article');
    liElement.appendChild(article);

    const name = document.createElement('h4');
    name.textContent = studentInput.value;
    article.appendChild(name);

    const university = document.createElement('p');
    university.textContent = `University: ${universityInput.value}`;
    article.appendChild(university);

    const score = document.createElement('p');
    score.textContent = `Score: ${scoreInput.value}`;
    article.appendChild(score);

    const editButton = document.createElement('button');
    editButton.textContent = 'edit';
    editButton.className = 'action-btn edit';
    liElement.appendChild(editButton);

    const applyButton = document.createElement('button');
    applyButton.textContent = 'apply';
    applyButton.className = 'action-btn apply';
    liElement.appendChild(applyButton);

    editButton.addEventListener('click', editItem);
    applyButton.addEventListener('click', apply)

  }

  function addInputs() {
    if (allInputsAdded()) {
      createListItem();
      toggleNextButton();
      clearAllInputs();
    }
  }

  function editItem(e) {
    const targetLiItem = e.target.parentElement;
    studentInput.value = targetLiItem.querySelector('h4').textContent;
    universityInput.value = targetLiItem.querySelector('p:nth-child(2)').textContent.replace('University: ', '');
    scoreInput.value = targetLiItem.querySelector('p:nth-child(3)').textContent.replace('Score: ', '');

    previewList.innerHTML = '';
    toggleNextButton();
  }

  function apply(e) {
    const targetLiItem = e.target.parentElement;
    const newLiItem = document.createElement('li');
    newLiItem.className = 'application';
    candidatesList.appendChild(newLiItem);

    const articleCopy = targetLiItem.querySelector('article').cloneNode(true);
    newLiItem.appendChild(articleCopy);
    targetLiItem.remove();
    toggleNextButton();
  }
  }
  