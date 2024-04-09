window.addEventListener("load", solve);

function solve() {
  const titleInput = document.getElementById('task-title');
  const categoryInput = document.getElementById('task-category');
  const contentInput = document.getElementById('task-content');

  const reviewList = document.getElementById('review-list');
  const publishedList = document.getElementById('published-list');

  const publishButton = document.getElementById('publish-btn');
  publishButton.addEventListener('click', function(e) {
      if (allInputsProvided()) {
          createTask();
          clearInputs();
      }
  })

  function allInputsProvided() {
      return (titleInput.value !== '' & categoryInput.value !== '' && contentInput.value !== '');
  }
  function clearInputs() {
      titleInput.value = '';
      categoryInput.value = '';
      contentInput.value = '';
  }

  function createTask() {
      const liEle = document.createElement('li');
      liEle.className = 'rpost';
      reviewList.appendChild(liEle);

      const article = document.createElement('article');
      liEle.appendChild(article);

      const title = document.createElement('h4');
      title.textContent = titleInput.value;
      article.appendChild(title);

      const category = document.createElement('p');
      category.textContent = `Category: ${categoryInput.value}`;
      article.appendChild(category);

      const content = document.createElement('p');
      content.textContent = `Content: ${contentInput.value}`;
      article.appendChild(content);

      const editButton = document.createElement('button');
      editButton.className = 'action-btn edit';
      editButton.textContent = 'Edit';
      liEle.appendChild(editButton);

      const postButton = document.createElement('button');
      postButton.className = 'action-btn post';
      postButton.textContent = 'Post';
      liEle.appendChild(postButton);

      editButton.addEventListener('click', function(e) {
          const currentLi = e.target.parentElement;
          titleInput.value = currentLi.querySelector('h4').textContent;
          categoryInput.value = currentLi.querySelector('p:nth-child(2)').textContent.replace('Category: ', '');
          contentInput.value = currentLi.querySelector('p:nth-child(3)').textContent.replace('Content: ', '');
          reviewList.innerHTML = '';
      })

      postButton.addEventListener('click', function(e) {
          const currentLi = e.target.parentElement;
          const copyLi = currentLi.cloneNode(true);
          Array.from(copyLi.querySelectorAll('button')).forEach((ele) => ele.remove());
          publishedList.appendChild(copyLi);
          reviewList.innerHTML = '';
      })
  }
}