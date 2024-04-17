window.addEventListener("load", solve);

function solve() {
    const playerInput = document.getElementById('player');
    const scoreInput = document.getElementById('score');
    const roundInput = document.getElementById('round');

    const sureList = document.getElementById('sure-list');
    const scoreBoardList = document.getElementById('scoreboard-list');

    const addButton = document.getElementById('add-btn');
    const clearButton = document.querySelector('.btn.clear');

    addButton.addEventListener('click', addItem);
    clearButton.addEventListener('click', function() {
      clearInputs();
      sureList.innerHTML = '';
      scoreBoardList.innerHTML = '';
    });

    function toggleAddButton() {
      addButton.disabled === true ? addButton.disabled = false : addButton.disabled = true;
    }

    function clearInputs() {
      playerInput.value = '';
      scoreInput.value = '';
      roundInput.value = '';
    }

    function attachButtonEvents() {
      const editButtons = document.querySelectorAll('.btn.edit');
      const okButtons = document.querySelectorAll('.btn.ok');

      Array.from(editButtons).forEach((button) => {
        button.addEventListener('click', function(event) {
          const targetArticle = event.target.previousElementSibling;
          const targetItem = targetArticle.parentElement;
          playerInput.value = targetArticle.querySelector('p:nth-child(1)').textContent;
          scoreInput.value = targetArticle.querySelector('p:nth-child(2)').textContent.replace('Score: ', '');
          roundInput.value = targetArticle.querySelector('p:nth-child(3)').textContent.replace('Round: ', '');
          targetItem.innerHTML = '';
          toggleAddButton();
        });
      })

      Array.from(okButtons).forEach((button) => {
        button.addEventListener('click', function (event) {
          const targetItem = event.target.previousElementSibling.parentElement;
          Array.from(targetItem.querySelectorAll('button')).forEach((button) => button.remove());
          const copyLiItem = targetItem.cloneNode(true);
          scoreBoardList.appendChild(copyLiItem);
          targetItem.innerHTML = '';
          toggleAddButton();
        });
      })
    }

    function addItem() {
      if (playerInput.value !== '' && scoreInput.value !== '' && roundInput.value !== '') {
        const dartItem = document.createElement('li');
        dartItem.className = 'dart-item';
        sureList.appendChild(dartItem);

        const article = document.createElement('article');
        dartItem.appendChild(article);

        const pName = document.createElement('p');
        pName.textContent = playerInput.value;
        article.appendChild(pName);

        const pScore = document.createElement('p');
        pScore.textContent = `Score: ${scoreInput.value}`;
        article.appendChild(pScore);

        const pRound = document.createElement('p');
        pRound.textContent = `Round: ${roundInput.value}`;
        article.appendChild(pRound);

        const editButton = document.createElement('button');
        editButton.className = 'btn edit';
        editButton.textContent = 'edit';
        dartItem.appendChild(editButton);

        const okButton = document.createElement('button');
        okButton.className = 'btn ok';
        okButton.textContent = 'ok';
        dartItem.appendChild(okButton);

        attachButtonEvents();

        toggleAddButton();
        clearInputs();
      }
    }
  }

