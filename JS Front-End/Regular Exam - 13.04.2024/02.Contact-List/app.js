window.addEventListener("load", solve);

function solve() {
    // Main variables
    const nameInput = document.getElementById('name');
    const phoneInput = document.getElementById('phone');
    const categoryInput = document.getElementById('category');

    const checkList = document.getElementById('check-list');
    const contactList = document.getElementById('contact-list');

    const addBtn = document.getElementById('add-btn');
    addBtn.addEventListener('click', () => {
      createLog();
      clearInputs();
    });

    // Helper functions
    function getInputs() {
      if (nameInput.value !== '' && phoneInput.value !== '' && categoryInput.value !== '') {
        return {
          name: nameInput.value,
          phone: phoneInput.value,
          category: categoryInput.value,
        };
      }
    }

    function clearInputs() {
      nameInput.value = '';
      phoneInput.value = '';
      categoryInput.value = '';
    }

    // DOM Modification
    function sendToEdit(e) {
      const currentLi = e.target.parentElement.parentElement;
      nameInput.value = currentLi.querySelector('p:nth-of-type(1)').textContent.replace('name:', '');
      phoneInput.value = currentLi.querySelector('p:nth-of-type(2)').textContent.replace('phone:', '');
      categoryInput.value = currentLi.querySelector('p:nth-of-type(3)').textContent.replace('category:', '');

      currentLi.remove();
    }

    function saveLog(e) {
      const currentLi = e.target.parentElement.parentElement;
      const copyLi = currentLi.cloneNode(true);
      contactList.appendChild(copyLi);
      currentLi.remove();

      copyLi.querySelector('.buttons').remove();

      const deleteBtn = document.createElement('button');
      deleteBtn.className = 'del-btn';
      copyLi.appendChild(deleteBtn);

      deleteBtn.addEventListener('click', (e) => deleteLog(e));
    }

    function deleteLog(e) {
      const currLi = e.target.parentElement;
      currLi.remove();
    }

    function createLog() {
      const newPerson = getInputs();

      if (newPerson) {
        const liEle = document.createElement('li');
        checkList.appendChild(liEle);

        const articleEle = document.createElement('article');
        liEle.appendChild(articleEle);

        const namePara = document.createElement('p');
        namePara.textContent = `name:${newPerson.name}`;
        articleEle.appendChild(namePara);

        const phonePara = document.createElement('p');
        phonePara.textContent = `phone:${newPerson.phone}`;
        articleEle.appendChild(phonePara);

        const categoryPara = document.createElement('p');
        categoryPara.textContent = `category:${newPerson.category}`;
        articleEle.appendChild(categoryPara);

        const buttonsDiv = document.createElement('div');
        buttonsDiv.className = 'buttons';
        liEle.appendChild(buttonsDiv);

        const editBtn = document.createElement('button');
        editBtn.className = 'edit-btn';
        buttonsDiv.appendChild(editBtn);

        const saveBtn = document.createElement('button');
        saveBtn.className = 'save-btn';
        buttonsDiv.appendChild(saveBtn);

        editBtn.addEventListener('click', (e) => sendToEdit(e));
        saveBtn.addEventListener('click', (e) => saveLog(e));
      }
    }
  }

